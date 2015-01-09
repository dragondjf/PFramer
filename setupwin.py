#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
利用Python脚本从获取最新版本信息，然后利用py2exe进行打包，最新进行相应的清理操作
"""

import os
import time
from datetime import datetime
import glob
import shutil
import subprocess
import sys
import stat
import zipfile
import json
from settings import __version__
from cx_Freeze import setup, Executable


def change_package_fromLib(rootpath, package_name):
    '''
        根据包名从python Lib中获取到包，替换library.zip中名字相同的包
    '''
    library_zippath = os.sep.join([rootpath, 'library.zip'])
    library_path = os.sep.join([rootpath, 'library'])
    with zipfile.ZipFile(library_zippath, 'r') as zip_file:
        zip_file.extractall(path=library_path)
    shutil.rmtree(library_path + os.sep + package_name)
    for item in [package_name]:
        package = __import__(item)
        package_path = os.path.dirname(package.__file__)
        shutil.copytree(package_path, library_path + os.sep + package_name)

    os.remove(library_zippath)
    addFolderToZip(library_path, library_zippath)
    shutil.rmtree(library_path)


def change_package_fromLocal(rootpath, package_name):
    '''
        根据包名从当前项目中获取到包，替换library.zip中名字相同的包
    '''
    library_zippath = os.sep.join([rootpath, 'library.zip'])
    library_path = os.sep.join([rootpath, 'library'])
    with zipfile.ZipFile(library_zippath, 'r') as zip_file:
        zip_file.extractall(path=library_path)

    package_dir = os.sep.join([library_path, package_name])
    if os.path.isdir(package_dir):
        delete_file_folder(package_dir)
    for item in [package_name]:
        package_path = os.sep.join([os.getcwd(), package_name])
        shutil.copytree(package_path, package_dir)

    os.remove(library_zippath)
    addFolderToZip(library_path, library_zippath)
    delete_file_folder(library_path)


def addFolderToZip(folder, zip_filename):
    '''
        将文件夹foldler添加到名字为zip_filename的zip中去
    '''
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        def addhandle(folder, zip_file):
            for f in os.listdir(folder):
                full_path = os.path.join(folder, f)
                if os.path.isfile(full_path):
                    zip_file.write(full_path, full_path.split('library\\')[1])
                elif os.path.isdir(full_path):
                    addhandle(full_path, zip_file)
        addhandle(folder, zip_file)


def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


def get_py2exe_datafiles(datapath, relativehead):
    head, tail = os.path.split(datapath)
    d = {}
    for root, dirs, files in os.walk(datapath):
        files = [os.path.join(root, filename) for filename in files]
        root = root.replace(tail, relativehead)
        root = root[root.index(relativehead):]
        d[root] = files
    return d.items()


def write_file(filename, content):
    '''
        将相应的content写入filename中去
    '''
    fd = open(filename, "w")
    fd.write(content)
    fd.close()


def get_sw_distributedname(sw_name, sw_version, project_svnpath):
    '''
    输入：
        sw_name : 软件名称
        sw_version: 软件版本号
        project_svnpath: 项目在svn中的路径
    输出：
        project_localpath： 项目在本地的路径
        distributedname：软件发行版本号
    作用：
        从svn仓库将项目checkout到本地，获取svn版本号，构建软件发行版本号distributedname
    '''
    project_localpath = os.sep.join([os.getcwd(), sw_name])
    subprocess.call('svn co %s %s' % (project_svnpath, project_localpath))
    svn_info = subprocess.check_output(['svn', 'info'])
    svn_infolines = svn_info.split(os.linesep)
    svn_version = svn_infolines[6][6:]
    buildtime = time.strftime(
        "%Y%m%d", time.localtime(int(time.time()))).decode('UTF8')
    distributedname = '%s-v%s-r%s-b%s' % (sw_name,
                                          sw_version, svn_version, buildtime)
    info = [svn_version, buildtime]
    return project_localpath, distributedname, info


def clearsvn(sw_path):
    '''
    输入：
        sw_path: 项目软件路径
    输出：
        空
    作用：
        调用shutil.rmtree进行整个文件夹删除
    '''
    for (p, d, f) in os.walk(sw_path):
        if p.find('.svn') > 0:
            shutil.rmtree(p)


def getfiles(path):
    '''
        获取指定path下的所有文件列表
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.sep.join([dirpath, filename]))
    return files


def gitLastCommitID():
    p = subprocess.Popen(
        ['git', 'log', '--pretty=oneline', '-1'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True,
    )
    lastCommitId = p.stdout.readlines()[0][:40][-6:]
    return lastCommitId


def getCurrentBranchName():
    p = subprocess.Popen(
        ['git', 'branch'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True,
    )
    branch = p.stdout.readlines()[0][2:-1]
    return branch


def getCurrentTime():
    buildtime = datetime.today().strftime("%y%m%d")
    return buildtime


def getBuildInfo():
    return dict(
        sw_name="AppClient",
        sw_version=__version__,
        lastCommitId=gitLastCommitID(),
        branch=getCurrentBranchName(),
        buildtime=getCurrentTime(),
    )


if __name__ == '__main__':

    for key in ['build']:
        path = os.sep.join([os.getcwd(), key])
        delete_file_folder(path)

    # 从config中获取软件的基本信息
    import gui.uiconfig as config
    sw_name = config.__softwarename__
    sw_version = __version__
    sw_publisher = config.__author__
    sw_url = config.__url__
    sw_description = config.__description__
    sw_logoico = config.__logoico__

    buildOptions = dict(
        packages=[],
        excludes=[],
        includes=['atexit'],
        icon=sw_logoico,
    )

    if sys.platform == 'win32':
        base = 'Win32GUI'
    else:
        base = None

    executables = [
        Executable(
            'main.py',
            base=base,
            icon=sw_logoico,
            targetName="%s.exe" % sw_name,
            appendScriptToExe=False,
            appendScriptToLibrary=True,
        )
    ]

    for key in ['build', 'dist']:
        path = os.sep.join([os.getcwd(), key])
        delete_file_folder(path)

    pyversion = 'exe.%s.%s.%s' % (sys.platform,
                                  sys.version_info.major,
                                  sys.version_info.minor)

    build_path = os.sep.join([os.getcwd(), 'build', pyversion])

    sys.argv.append("build")
    setup(
        name=sw_name,
        version='1.0',
        description=sw_description,
        options=dict(build_exe=buildOptions),
        executables=executables
    )

    '''
        拷贝响应的图片皮肤和与项目有关的资源文件到打包目录
    '''

    for item in ['log']:
        os.mkdir(os.sep.join([build_path, item]))

    for item in ['skin']:
        shutil.copytree(
            os.sep.join([os.getcwd(), 'gui', item]),
            os.sep.join([build_path, 'gui', item])
        )
