Qt webkit 和 webengine 技术调研

#### 1. Qt5.3
1. Qt5.3 Widgets

	+ QtWebkit
	+ QtWebkitWidgets

2. Qt5.3 qml WebView

	+  **import QtWebKit 3.0**
	+  **import QtWebKit.experimental 1.0**
> WebView is a component for displaying web content which is implemented using native APIs on the platforms where this is available, thus it does not necessarily require including a full web browser stack as part of the application.
> 
> WebView is currently supported on the following platforms: Android.
> 
> Note: Due to platform limitations overlapping the WebView and other QML components is not supported.

qml的webview只提供了展示html的的基本功能，拓展功能通过QtWebKit.experimental实验模块（可能存在bug,　未来将会移除）引入．

####2. Qt5.4
除了提供Qt5.3 webkit 模块来渲染html这种解决方案外, Qt5.4引入了基于chroium 的WebEngine 模块，用来替换webkit.

+ QtWebEngine
+  QtWebEngineWidgets

QtWebEngineWidgets为Qt widgets嵌入浏览器提供支持，PyQt5.4支持

+ import QtWebEngine 1.0
+ import QtWebEngine.experimental  1.0

QtWebEngine 1.0 为qml嵌入浏览器提供支持提供支持，PyQt5.4 目前不支持

[QtWebEngine使用简介](http://elproxy.github.io/devdays-2014/#1)

[PyQt5.4 qml webengine ](https://github.com/rodrigogolive/WebEngineWrapper)
