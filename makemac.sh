#!/bin/bash

echo "Start to build..."
sleep 1
rm -rf dist
rm -rf distmac
rm -rf build
python setupmac.py py2app build

mkdir -p dist/ALE.app/Contents/Resources/gui
mkdir -p dist/ALE.app/Contents/Resources/log
mv dist/ALE.app/Contents/Resources/skin dist/ALE.app/Contents/Resources/gui/

mkdir dist/ALE.app/Contents/Resources/report
cp -rf report/sample  dist/ALE.app/Contents/Resources/report/
cp -rf drivingsimulator  dist/ALE.app/Contents/Resources/

cp -rf mac_release dist/ALE.app/Contents/Resources
chmod +x dist/ALE.app/Contents/Resources/mac_release/ManageSDL
chmod +x dist/ALE.app/Contents/Resources/mac_release/smartDeviceLinkCore

mv dist distmac
cp Readme_Mac.rtf distmac/Readme.rtf
rm -rf build
echo "Build over"
