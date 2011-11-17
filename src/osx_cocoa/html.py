# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

"""
Classes for embedding a full web browser rendering engine in a window.
"""

import _html
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import _core
wx = _core 
__docfilter__ = wx.__DocFilter(globals()) 
#---------------------------------------------------------------------------

WEB_VIEW_ZOOM_TINY = _html.WEB_VIEW_ZOOM_TINY
WEB_VIEW_ZOOM_SMALL = _html.WEB_VIEW_ZOOM_SMALL
WEB_VIEW_ZOOM_MEDIUM = _html.WEB_VIEW_ZOOM_MEDIUM
WEB_VIEW_ZOOM_LARGE = _html.WEB_VIEW_ZOOM_LARGE
WEB_VIEW_ZOOM_LARGEST = _html.WEB_VIEW_ZOOM_LARGEST
WEB_VIEW_ZOOM_TYPE_LAYOUT = _html.WEB_VIEW_ZOOM_TYPE_LAYOUT
WEB_VIEW_ZOOM_TYPE_TEXT = _html.WEB_VIEW_ZOOM_TYPE_TEXT
WEB_NAV_ERR_CONNECTION = _html.WEB_NAV_ERR_CONNECTION
WEB_NAV_ERR_CERTIFICATE = _html.WEB_NAV_ERR_CERTIFICATE
WEB_NAV_ERR_AUTH = _html.WEB_NAV_ERR_AUTH
WEB_NAV_ERR_SECURITY = _html.WEB_NAV_ERR_SECURITY
WEB_NAV_ERR_NOT_FOUND = _html.WEB_NAV_ERR_NOT_FOUND
WEB_NAV_ERR_REQUEST = _html.WEB_NAV_ERR_REQUEST
WEB_NAV_ERR_USER_CANCELLED = _html.WEB_NAV_ERR_USER_CANCELLED
WEB_NAV_ERR_OTHER = _html.WEB_NAV_ERR_OTHER
WEB_VIEW_RELOAD_DEFAULT = _html.WEB_VIEW_RELOAD_DEFAULT
WEB_VIEW_RELOAD_NO_CACHE = _html.WEB_VIEW_RELOAD_NO_CACHE
WEB_VIEW_BACKEND_DEFAULT = _html.WEB_VIEW_BACKEND_DEFAULT
WEB_VIEW_BACKEND_WEBKIT = _html.WEB_VIEW_BACKEND_WEBKIT
WEB_VIEW_BACKEND_IE = _html.WEB_VIEW_BACKEND_IE
class WebViewHistoryItem(object):
    """Proxy of C++ WebViewHistoryItem class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String url, String title) -> WebViewHistoryItem"""
        _html.WebViewHistoryItem_swiginit(self,_html.new_WebViewHistoryItem(*args, **kwargs))
    def GetUrl(*args, **kwargs):
        """GetUrl(self) -> String"""
        return _html.WebViewHistoryItem_GetUrl(*args, **kwargs)

    def GetTitle(*args, **kwargs):
        """GetTitle(self) -> String"""
        return _html.WebViewHistoryItem_GetTitle(*args, **kwargs)

_html.WebViewHistoryItem_swigregister(WebViewHistoryItem)

class WebView(_core.Control):
    """Proxy of C++ WebView class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id, String url=wxWebViewDefaultURLStr, 
            Point pos=DefaultPosition, Size size=DefaultSize, 
            long style=0, String name=wxWebViewNameStr) -> bool
        """
        return _html.WebView_Create(*args, **kwargs)

    def New(*args):
        """
        New(int backend=WEB_VIEW_BACKEND_DEFAULT) -> WebView
        New(Window parent, int id, String url=wxWebViewDefaultURLStr, 
            Point pos=DefaultPosition, Size size=DefaultSize, 
            int backend=WEB_VIEW_BACKEND_DEFAULT, 
            long style=0, String name=wxWebViewNameStr) -> WebView
        """
        val = _html.WebView_New(*args)
        val._setOORInfo(val)
        return val

    New = staticmethod(New)
    def GetCurrentTitle(*args, **kwargs):
        """GetCurrentTitle(self) -> String"""
        return _html.WebView_GetCurrentTitle(*args, **kwargs)

    def GetCurrentURL(*args, **kwargs):
        """GetCurrentURL(self) -> String"""
        return _html.WebView_GetCurrentURL(*args, **kwargs)

    def GetPageSource(*args, **kwargs):
        """GetPageSource(self) -> String"""
        return _html.WebView_GetPageSource(*args, **kwargs)

    def GetPageText(*args, **kwargs):
        """GetPageText(self) -> String"""
        return _html.WebView_GetPageText(*args, **kwargs)

    def IsBusy(*args, **kwargs):
        """IsBusy(self) -> bool"""
        return _html.WebView_IsBusy(*args, **kwargs)

    def IsEditable(*args, **kwargs):
        """IsEditable(self) -> bool"""
        return _html.WebView_IsEditable(*args, **kwargs)

    def LoadURL(*args, **kwargs):
        """LoadURL(self, String url)"""
        return _html.WebView_LoadURL(*args, **kwargs)

    def Print(*args, **kwargs):
        """Print(self)"""
        return _html.WebView_Print(*args, **kwargs)

    def RegisterHandler(*args, **kwargs):
        """RegisterHandler(self, wxSharedPtr<(wxWebViewHandler)> handler)"""
        return _html.WebView_RegisterHandler(*args, **kwargs)

    def Reload(*args, **kwargs):
        """Reload(self, int flags=WEB_VIEW_RELOAD_DEFAULT)"""
        return _html.WebView_Reload(*args, **kwargs)

    def RunScript(*args, **kwargs):
        """RunScript(self, String javascript)"""
        return _html.WebView_RunScript(*args, **kwargs)

    def SetEditable(*args, **kwargs):
        """SetEditable(self, bool enable=True)"""
        return _html.WebView_SetEditable(*args, **kwargs)

    def SetPage(*args):
        """
        SetPage(self, String html, String baseUrl)
        SetPage(self, InputStream html, String baseUrl)
        """
        return _html.WebView_SetPage(*args)

    def Stop(*args, **kwargs):
        """Stop(self)"""
        return _html.WebView_Stop(*args, **kwargs)

    def CanCopy(*args, **kwargs):
        """CanCopy(self) -> bool"""
        return _html.WebView_CanCopy(*args, **kwargs)

    def CanCut(*args, **kwargs):
        """CanCut(self) -> bool"""
        return _html.WebView_CanCut(*args, **kwargs)

    def CanPaste(*args, **kwargs):
        """CanPaste(self) -> bool"""
        return _html.WebView_CanPaste(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self)"""
        return _html.WebView_Copy(*args, **kwargs)

    def Cut(*args, **kwargs):
        """Cut(self)"""
        return _html.WebView_Cut(*args, **kwargs)

    def Paste(*args, **kwargs):
        """Paste(self)"""
        return _html.WebView_Paste(*args, **kwargs)

    def CanGoBack(*args, **kwargs):
        """CanGoBack(self) -> bool"""
        return _html.WebView_CanGoBack(*args, **kwargs)

    def CanGoForward(*args, **kwargs):
        """CanGoForward(self) -> bool"""
        return _html.WebView_CanGoForward(*args, **kwargs)

    def ClearHistory(*args, **kwargs):
        """ClearHistory(self)"""
        return _html.WebView_ClearHistory(*args, **kwargs)

    def EnableHistory(*args, **kwargs):
        """EnableHistory(self, bool enable=True)"""
        return _html.WebView_EnableHistory(*args, **kwargs)

    def GetBackwardHistory(*args, **kwargs):
        """GetBackwardHistory(self) -> wxVector<(wxSharedPtr<(wxWebViewHistoryItem)>)>"""
        return _html.WebView_GetBackwardHistory(*args, **kwargs)

    def GetForwardHistory(*args, **kwargs):
        """GetForwardHistory(self) -> wxVector<(wxSharedPtr<(wxWebViewHistoryItem)>)>"""
        return _html.WebView_GetForwardHistory(*args, **kwargs)

    def GoBack(*args, **kwargs):
        """GoBack(self)"""
        return _html.WebView_GoBack(*args, **kwargs)

    def GoForward(*args, **kwargs):
        """GoForward(self)"""
        return _html.WebView_GoForward(*args, **kwargs)

    def LoadHistoryItem(*args, **kwargs):
        """LoadHistoryItem(self, wxSharedPtr<(wxWebViewHistoryItem)> item)"""
        return _html.WebView_LoadHistoryItem(*args, **kwargs)

    def ClearSelection(*args, **kwargs):
        """ClearSelection(self)"""
        return _html.WebView_ClearSelection(*args, **kwargs)

    def DeleteSelection(*args, **kwargs):
        """DeleteSelection(self)"""
        return _html.WebView_DeleteSelection(*args, **kwargs)

    def GetSelectedSource(*args, **kwargs):
        """GetSelectedSource(self) -> String"""
        return _html.WebView_GetSelectedSource(*args, **kwargs)

    def GetSelectedText(*args, **kwargs):
        """GetSelectedText(self) -> String"""
        return _html.WebView_GetSelectedText(*args, **kwargs)

    def HasSelection(*args, **kwargs):
        """HasSelection(self) -> bool"""
        return _html.WebView_HasSelection(*args, **kwargs)

    def SelectAll(*args, **kwargs):
        """SelectAll(self)"""
        return _html.WebView_SelectAll(*args, **kwargs)

    def CanRedo(*args, **kwargs):
        """CanRedo(self) -> bool"""
        return _html.WebView_CanRedo(*args, **kwargs)

    def CanUndo(*args, **kwargs):
        """CanUndo(self) -> bool"""
        return _html.WebView_CanUndo(*args, **kwargs)

    def Redo(*args, **kwargs):
        """Redo(self)"""
        return _html.WebView_Redo(*args, **kwargs)

    def Undo(*args, **kwargs):
        """Undo(self)"""
        return _html.WebView_Undo(*args, **kwargs)

    def CanSetZoomType(*args, **kwargs):
        """CanSetZoomType(self, int type) -> bool"""
        return _html.WebView_CanSetZoomType(*args, **kwargs)

    def GetZoom(*args, **kwargs):
        """GetZoom(self) -> int"""
        return _html.WebView_GetZoom(*args, **kwargs)

    def GetZoomType(*args, **kwargs):
        """GetZoomType(self) -> int"""
        return _html.WebView_GetZoomType(*args, **kwargs)

    def SetZoom(*args, **kwargs):
        """SetZoom(self, int zoom)"""
        return _html.WebView_SetZoom(*args, **kwargs)

    def SetZoomType(*args, **kwargs):
        """SetZoomType(self, int zoomType)"""
        return _html.WebView_SetZoomType(*args, **kwargs)

_html.WebView_swigregister(WebView)

def WebView_New(*args):
  """
    New(int backend=WEB_VIEW_BACKEND_DEFAULT) -> WebView
    WebView_New(Window parent, int id, String url=wxWebViewDefaultURLStr, 
        Point pos=DefaultPosition, Size size=DefaultSize, 
        int backend=WEB_VIEW_BACKEND_DEFAULT, 
        long style=0, String name=wxWebViewNameStr) -> WebView
    """
  val = _html.WebView_New(*args)
  val._setOORInfo(val)
  return val

class WebViewEvent(_core.NotifyEvent):
    """Proxy of C++ WebViewEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType type, int id, String href, String target) -> WebViewEvent"""
        _html.WebViewEvent_swiginit(self,_html.new_WebViewEvent(*args, **kwargs))
    def GetTarget(*args, **kwargs):
        """GetTarget(self) -> String"""
        return _html.WebViewEvent_GetTarget(*args, **kwargs)

    def GetURL(*args, **kwargs):
        """GetURL(self) -> String"""
        return _html.WebViewEvent_GetURL(*args, **kwargs)

_html.WebViewEvent_swigregister(WebViewEvent)

wxEVT_COMMAND_WEB_VIEW_NAVIGATING = _html.wxEVT_COMMAND_WEB_VIEW_NAVIGATING
wxEVT_COMMAND_WEB_VIEW_NAVIGATED = _html.wxEVT_COMMAND_WEB_VIEW_NAVIGATED
wxEVT_COMMAND_WEB_VIEW_LOADED = _html.wxEVT_COMMAND_WEB_VIEW_LOADED
wxEVT_COMMAND_WEB_VIEW_ERROR = _html.wxEVT_COMMAND_WEB_VIEW_ERROR
wxEVT_COMMAND_WEB_VIEW_NEWWINDOW = _html.wxEVT_COMMAND_WEB_VIEW_NEWWINDOW
wxEVT_COMMAND_WEB_VIEW_TITLE_CHANGED = _html.wxEVT_COMMAND_WEB_VIEW_TITLE_CHANGED
EVT_WEB_VIEW_NAVIGATING = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_NAVIGATING, 1 )
EVT_WEB_VIEW_NAVIGATED = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_NAVIGATED, 1 )
EVT_WEB_VIEW_LOADED = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_LOADED, 1 )
EVT_WEB_VIEW_ERROR = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_ERROR, 1 )
EVT_WEB_VIEW_NEWWINDOW = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_NEWWINDOW, 1 )
EVT_WEB_VIEW_TITLE_CHANGED = wx.PyEventBinder( wxEVT_COMMAND_WEB_VIEW_TITLE_CHANGED, 1 )

class WebViewHandler(object):
    """Proxy of C++ WebViewHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetFile(*args, **kwargs):
        """GetFile(self, String uri) -> FSFile"""
        return _html.WebViewHandler_GetFile(*args, **kwargs)

    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return _html.WebViewHandler_GetName(*args, **kwargs)

_html.WebViewHandler_swigregister(WebViewHandler)

class PyWebViewHandler(WebViewHandler):
    """Proxy of C++ PyWebViewHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String scheme) -> PyWebViewHandler"""
        _html.PyWebViewHandler_swiginit(self,_html.new_PyWebViewHandler(*args, **kwargs))
        PyWebViewHandler._setCallbackInfo(self, self, PyWebViewHandler)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _html.PyWebViewHandler__setCallbackInfo(*args, **kwargs)

_html.PyWebViewHandler_swigregister(PyWebViewHandler)

class WebViewArchiveHandler(WebViewHandler):
    """Proxy of C++ WebViewArchiveHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
_html.WebViewArchiveHandler_swigregister(WebViewArchiveHandler)



