PFramer
=======

###### 1. PFramer 兼容 PySide/PyQt4/PyQt5 同时兼容python27 与 python34

###### 2. 在利用pyrcc 生成资源py文件后将相应的导入 更正为 

	from qframer.qt import QtCore

###### 3. 写程序注意python27与python34的兼容性问题

###### 4. 同目录导入模块时使用【.a】
	
	from .a import b
而不是
	from a import b
