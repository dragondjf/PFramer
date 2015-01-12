# Qt WebEngine 简介

+ 英文：(http://blog.qt.digia.com/blog/2013/09/12/introducing-the-qt-webengine/)
+ 中文：(http://blog.qt.digia.com/cn/2013/09/25/introducing-the-qt-webengine/)

自从2007年首次引入Qt WebKit以来，Web技术发生了翻天覆地的变化。依据市场份额，WebKit开源项目已经成为现在世界上最流行的浏览器引擎。WebKit的Qt移植基本上是第一个WebKit的非Apple移植，多年来，许多项目和公司都加入到追随的行列。

Chromium项目在WebKit中扮演了特殊的角色，成为WebKit的最大的贡献者（接下来两位是Apple和Qt）。但是同一开源项目中不同公司之间的合作从来问题多多，这直接导致Google决定离开WebKit项目，创建了其自己的WebKit分支——Blink。

从那时起，集成在Chromium中的Blink和WebKit分道扬镳。两个版本的代码快速分化。正因如此，Digia Qt R&D WebKit团队决定仔细对比Chromium和WebKit，来决定未来版本的Qt使用哪一个来提供最好的Web引擎。

在经过一段时间的研究和调查之后，我们得出了结论：我们将在Chromium基础之上建立未来的Web引擎——Qt WebEngine。很多原因促使我们做出这个决定：

+ Chromium关注于跨平台建设，其浏览器能够运行在所有主流桌面平台和Android上；与此同时，WebKit则不那么专注。我们自己的项目则必须支持所有的OS平台。
+ Chromium中对很多事情都提供了支持，在WebKit下同样支持这些东西则需要耗费大量精力。例如，我们可以简单地重用平台/OS的适配代码。多媒体以及如WebRTC这样的新HTML5特性，都是直接可用的，无需特别的Qt代码。
+ 使用Chromium可以简化OS集成工作，这使得我们可以有更多精力关注于更高层面，提供一个可以无缝集成于Qt之中并且简单而强大的API。
+ 我们注意到Chromium的开发处于代码质量的严格控制之中。这简化了我们的测试工作，有利于提供更稳定和高质量的Web引擎。
+ 比起WebKit，Chromium允许我们构建更好更高效的组件和Qt Quick scene graph。

最后，我们注意到Chromium是现在发展最快的浏览器。基于Chromium构建我们的下一代Web引擎是一个战略性的长期的决定。我们相信上面几点理由会让我们提供一个比现在的Qt WebKit更好的Web引擎。同时，将现在同类中最好的浏览器引擎与Qt整合为一个框架将为需要Web浏览器的嵌入式设备提供有力的支持。

Chromium的基础特性之一是出于安全和稳定原因，在不同进程渲染Web内容。但是这导致我们无法在Chromium中提供现有的Qt WebKit API中的某些方面内容。一个明显的部分就是QWebElement API。我们还得改变QObject嵌入的方式，因为所有QObject与网页的交互都要求必须是异步的。

**这些改变对Qt WebKit用户意味着什么？**
首先，没什么可怕的。对于大多数用例，Web内容都是嵌入到应用程序中的，Qt WebKit现在工作的很好，以后若干年也会工作的很好。Qt 5.2发布之后，我们将会集中精力开发新的Qt Web Engine。所以如果您需要让您的应用或设备支持所有最新最好的HTML5特性，在我们发布了您所需要的API特性时，您就应该考虑移植到Qt WebEngine。

对于从Qt WebKit到新的Qt WebEngine迁移工作，我们尽力使它变得简单无缝。对于Qt Quick WebView元素，我们基本上能提供一个接近100%兼容的API。对于那些使用基本的QWebView API的用户，我们也有好消息。新的Qt WebEngine将在源代码级兼容大部分API。如果您使用了QObject桥或者QWebElement API，我们建议您等一段时间再进行移植。因为这些内容的替换API不大可能会在Qt WebEngine的初版就提供。

尽管我们不再对Qt WebKit提供任何新特性的开发，已有版本仍将可用。Digia将继续为Qt Enterprise商业授权用户提供合同规定的Qt WebKit支持，并且我们还可以提供延长支持的选项。

#Qt 5.4 简介

Qt 5.4支持HTML5混合开发，引入了Windows Phone的支持和若干跨桌面、移动和嵌入式平台的增强功能

2014年12月10日 — The Qt Company今天发布了其领先的跨平台应用和用户界面(UI)开发框架的最新版本Qt 5.4。Qt 5.4使得创建具有原生C++性能的连接设备和精彩应用变得更加简单，企业可以执行面向未来的多屏幕适应和物联网战略，并延伸到所有主要的桌面、嵌入式和移动操作系统。此版本同样将LGPLv3作为授权协议方式之一，希望藉此保护自由软件基金会（The Free Software Foundation）所倡导的用户自由。

Qt 5.4延续了之前各个版本中所包含的先进技术（前一个版本Qt 5.3下载量已逾160万次），并进一步增加了功能，提升了性能，帮助开发者面向更加广泛的应用。其亮点包括：在商业授权和LGPLv3授权协议下，增加了新的基于Chromium浏览器引擎的Qt WebEngine，以支持面向未来、整合网络技术的Qt与HTML5的混合开发；完全支持Windows Store Apps，包括WinRT和Windows Phone 8.1；Qt Quick控件在商业和LGPLv3授权协议下可提供原生的Android风格；针对嵌入式系统开发增加了新的功能，特别是增加了Qt Quick Compiler 2.0和新的Qt Quick 2D Renderer；提供全新的“平滑”式Qt Quick控件，为应用和设备的用户界面带来更加精致的外观。为了满足可穿戴设备和物联网开发需求的增长，提供了蓝牙低能耗支持的技术预览版本。此外，Qt 5.4还将Qt Creator IDE更新到3.3版本，其提供了全新的Qt Quick Designer和许多其它提高工作效率的功能。

Qt将简单的开发与高效的性能相结合，即使在处理器能力受限的平台上，依然能开发出精彩、流畅和时尚的用户界面。该框架带来的这些优势不仅体现在最初的目标平台或设备上，也包括所有其它的支持平台。开发者可以放心工作，并清楚地知道，他们的投资在支持其它操作系统或部署到额外设备硬件时会得到回报。

**随着HTML5的重要性越来越高，Qt 5.4用新的基于Chromium的浏览器引擎Qt WebEngine支持面向未来的混合应用开发，并得到桌面和嵌入式平台上的完全支持。除了为Chromium提供方便的跨平台API，Qt WebEngine还完全集成了Qt的图形库，允许网页内容进行叠加，并与Qt用户界面或OpenGL图形效果混合。Qt近一年内已经没有对Webkit引入任何_新功能，Qt 5.4将是最后一个支持Webkit Suppot的版本。今后发布的版本将停止对Webkit的支持，因此建议所有需要浏览器能力的新项目采用Qt WebEngine开发。针对移动平台，在商业授权协议和LGPLv3授权协议下推出的Qt WebView，能够利用原生的操作系统浏览器引擎整合网页内容。**

Qt 5.4更加适用于最新的桌面操作系统版本，提升了在OS X 10.10 Yosemite上的体验，支持高清显示，并针对Windows 8.1进行了改进，还能够在Windows上的OpenGL和ANGLE之间进行动态GL切换。现在使用Qt 5.4提供的图形API，可以根据需要混搭Qt Quick、Qt Widgets和原生OpenGL。

针对移动应用开发，Qt 5.4引入了对Windows Store Apps的完全支持，并改进了对Android和iOS平台的支持。Qt Quick控件，即UI控件的集合，增加了对Android 原生应用程序风格的支持。Qt 5.3版本就开始支持Android 5。经过改进，Qt更加适用于iOS8和XCode 6。此外，Qt 5.4 the Indie Mobile包（专为个人移动开发者或移动应用开发屋而设计）现在包括了Qt Purchasing API。

Qt 5.4进一步增强了其应用于开发连接设备系统的能力，可以带来更加精彩的外观和更强大的性能。Qt 对开发嵌入式系统的现有支持包括强大的C++类库、完整的嵌入式工具链和即时原型设计用的预编译库。Qt 5.4推出了全新专业设计“平滑”风格的Qt Quick控件，覆盖了传统和工业企业的控件，为应用和设备的用户界面带来更靓丽的外观。它还引入了Qt Quick 2D Renderer插件，使Qt Quick的图形不用OpenGL也能运行，并允许Qt Quick在没有GPU的低端设备上运行，还纳入了Qt Quick Compiler 2.0，进一步缩短设备启动时间，并防止逆向工程。



#Porting from Qt WebKit to Qt WebEngine

This provides rough steps to follow when porting an application using Qt WebKit's QWebView API to use Qt WebEngine's QWebEngineView.
>下面提供了如何将一个基于Qt WebKit's QWebView API的应用程序升级到Qt WebEngine's QWebEngineView的基本步骤：

####1.类名/Class names

The Qt WebEngine equivalent of Qt WebKit C++ classes are prefixed by "QWebEngine" instead of "QWeb".
>  Qt WebEngine中前缀为QWebEngine的类等价于Qt WebKit 前缀为QWeb的类

Qt WebKit

        #include <QWebHistory>
        #include <QWebHistoryItem>
        #include <QWebPage>
        #include <QWebView>


Qt WebEngine

        #include <QWebEngineHistory>
        #include <QWebEngineHistoryItem>
        #include <QWebEnginePage>
        #include <QWebEngineView>


####2. Qt Module Name

In qmake Project Files
> 在qmake 工程文件中

Qt WebKit

    QT += webkitwidgets
Qt WebEngine

    QT += webenginewidgets

####3. Including the Module in Source Files

Qt WebKit

    #include <QtWebKit/QtWebKit>
    #include <QtWebKitWidgets/QtWebKitWidgets> // With Qt >= 4.8
Qt WebEngine

    #include <QtWebEngineWidgets/QtWebEngineWidgets>

####3.QWebFrame has been Merged into QWebEnginePage

It is not possible to access sub-frames. Methods of the main QWebFrame are now available directly through the QWebEnginePage itself.
> 不再需要访问QWebPage的子frames，QWebFrame的方法现在在QWebEnginePage中直接可以访问

Qt WebKit

    QWebPage page;
    connect(page.mainFrame(), SIGNAL(urlChanged(const QUrl&)), SLOT(mySlotName()));
    page.mainFrame()->load(url);
Qt WebEngine

    QWebEnginePage page;
    connect(&page, SIGNAL(urlChanged(const QUrl&)), SLOT(mySlotName()));
    page.load(url);

####4.Some methods now return their result asynchronously

Since Qt WebEngine uses a multi-process architecture, applications needs to return to the event loop where the result will be received asynchronously from Qt WebEngine's render process. A function pointer, a functor or a lambda expression must be provided to handle the result when it is available.
> 由于Qt WebEngine 采用多进程机制，应用程序需要返回Qt的事件循环当结果从Qt WebEngine's 的渲染进程异步返回时。必须提供一个函数指针或者一个lambda函数表达式当结果有效时。

Qt WebKit

        QWebPage *page = new QWebPage;
        QTextEdit *textEdit = new QTextEdit;
        // *textEdit is modified immediately.
        textEdit->setPlainText(page->toHtml());
        textEdit->setPlainText(page->toPlainText());

Qt WebEngine (with a lambda function in C++11)

    QWebEnginePage *page = new QWebEnginePage;
    QTextEdit *textEdit = new QTextEdit;
    // *textEdit must remain valid until the lambda function is called.
    page->toHtml([textEdit](const QString &result){ textEdit->setPlainText(result); });
    page->toPlainText([textEdit](const QString &result){ textEdit->setPlainText(result); });
Qt WebEngine (with a functor template wrapping a member function)

    template<typename Arg, typename R, typename C>
    struct InvokeWrapper {
        R *receiver;
        void (C::*memberFun)(Arg);
        void operator()(Arg result) {
            (receiver->*memberFun)(result);
        }
    };
    
    template<typename Arg, typename R, typename C>
    InvokeWrapper<Arg, R, C> invoke(R *receiver, void (C::*memberFun)(Arg))
    {
        InvokeWrapper<Arg, R, C> wrapper = {receiver, memberFun};
        return wrapper;
    }
    
    QWebEnginePage *page = new QWebEnginePage;
    QTextEdit *textEdit = new QTextEdit;
    // *textEdit must remain valid until the functor is called.
    page->toHtml(invoke(textEdit, &QTextEdit::setPlainText));
    page->toPlainText(invoke(textEdit, &QTextEdit::setPlainText));

Qt WebEngine (with a regular functor)
    
    struct SetPlainTextFunctor {
        QTextEdit *textEdit;
        SetPlainTextFunctor(QTextEdit *textEdit) : textEdit(textEdit) { }
        void operator()(const QString &result) {
            textEdit->setPlainText(result);
        }
    };
    
    QWebEnginePage *page = new QWebEnginePage;
    QTextEdit *textEdit = new QTextEdit;
    // *textEdit must remain valid until the functor is called.
    page->toHtml(SetPlainTextFunctor(textEdit));
    page->toPlainText(SetPlainTextFunctor(textEdit));

####5. Qt WebEngine does not Interact with QNetworkAccessManager

Some classes of Qt Network such as QAuthenticator were reused for their interface but, unlike Qt WebKit, Qt WebEngine has its own HTTP implementation and can't go through a QNetworkAccessManager.
> 一些Qt Network的类 例如QAuthenticator 的接口被重用，但是不像Qt WebKit, Qt WebEngine拥有自己的HTTP实现，无法通过QNetworkAccessManager访问
    
Signals and methods of QNetworkAccessManager that are still supported were moved to QWebEnginePage directly.

> QNetworkAccessManager 依然支持的 信号与槽 直接移植到 QWebEnginePage了


Qt WebKit

    QNetworkAccessManager qnam;
    QWebPage page;
    page.setNetworkAccessManager(&qnam);
    connect(&qnam, SIGNAL(authenticationRequired(QNetworkReply*,QAuthenticator*)), this, SLOT(authenticate(QNetworkReply*,QAuthenticator*)));
Qt WebEngine

    QWebEnginePage page;
    connect(&page, SIGNAL(authenticationRequired(QNetworkReply*,QAuthenticator*)), this, SLOT(authenticate(QNetworkReply*,QAuthenticator*)));

###Notes about individual methods

####6.runJavaScript (QWebEnginePage)

QWebFrame::evaluateJavaScript was renamed and moved as QWebEnginePage::runJavaScript. It is currently only possible to run JavaScript on the main frame of a page and the result is returned asynchronously to the provided functor.

Qt WebKit

    QWebPage *page = new QWebPage;
    qDebug() << page->mainFrame()->evaluateJavaScript("'Java' + 'Script'");

Qt WebEngine (with lambda expressions in C++11)

    QWebEnginePage *page = new QWebEnginePage;
    page->runJavaScript("'Java' + 'Script'", [](const QVariant &result){ qDebug() << result; });

####7.setHtml and setContent (QWebEnginePage)
Those methods now perform asynchronously the same way as a normal HTTP load would.

####8. Unavailable Qt WebKit APIs

Qt WebKit classes or methods in this list will not be available in Qt WebEngine.

####9.QGraphicsWebView
Qt WebEngine requires hardware acceleration. Since we couldn’t support a web view class in a QGraphicsView unless it is attached to a QGLWidget viewport, this feature is out of scope.

####10.QWebElement
Qt WebEngine uses a multi-process architecture and this means that any access to the internal structure of the page has to be done asynchronously, any query result must be returned through callbacks. The QWebElement API was designed for synchronous access and this would require a complete redesign.

####11.QWebDatabase
The Web SQL Database feature that this API was wrapping in QtWebKit was dropped from the HTML5 standard.

####12.QWebPluginDatabase, QWebPluginFactory, QWebPluginInfo, QWebPage::setPalette, QWebView::setRenderHints
Qt WebEngine renders web pages using Skia and isn’t using QPainter or Qt for this purpose. The HTML5 standard also now offers much better alternatives that were not available when native controls plugins were introduced in QtWebKit.

####13.QWebHistoryInterface
Visited links are persisted automatically by Qt WebEngine.

#####14.QWebPage::setContentEditable
In the latest HTML standard, any document element can be made editable through the contentEditable attribute. So runJavaScript is all that is needed.
    
    page->runJavascript("document.documentElement.contentEditable = true")


