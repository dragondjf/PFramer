#!/bin/bash

echo "Start to build..."
sleep 1
rm -rf dist
rm -rf distmac
rm -rf build
python setupmac.py py2app build

mkdir -p dist/AppClient.app/Contents/Resources/gui
mkdir -p dist/AppClient.app/Contents/Resources/log
cp -rf DBFILE dist/AppClient.app/Contents/Resources/
cp -rf config dist/AppClient.app/Contents/Resources/
mv dist/AppClient.app/Contents/Resources/skin dist/AppClient.app/Contents/Resources/gui/

mv dist distmac
rm -rf build
echo "Build over"
