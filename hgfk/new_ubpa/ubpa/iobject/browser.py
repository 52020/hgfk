# coding: utf8
"""
浏览器类对象，打开网站、打开网址、打开浏览器等
"""

from ubpa import iie
from ubpa.ibrowse import Browser as _Browser, BrowserType
from ubpa.ilog import ILoger
from ubpa.iobject.element import Action


class Browser(_Browser):
    """浏览器"""

    class AppName:
        """浏览器应用程序名称"""
        none = None
        ie = BrowserType.AppIe
        chrome = BrowserType.AppChrome
        firefox = BrowserType.AppFirefox
        edge = BrowserType.AppEdge
        qihoo = BrowserType.AppQihoo  # 360浏览器

    def __init__(self, app: [str, None] = AppName.none):
        """
        初始化
        示例：
            Browser(AppName.chrome)     # 实例化谷歌浏览器对象
        :param app: 浏览器应用名称，ie、chrome、firefox、edge、qihoo，默认none
        """
        super(Browser, self).__init__(browser_type=app)
        self.browser_dll = self.get_browser_dll()

    @classmethod
    def run(cls,
            exe=r"C:/Program Files (x86)/Internet Explorer/iexplore.exe",
            url=""):
        """
        运行浏览器exe可执行程序
        示例：
            Browser.run()   # 打开ie浏览器的一个空页面
        :param exe: 应用程序可执行文件路径，默认ie浏览器
        :param url: 浏览器运行打开的网址，空则空页面
        :return:
        """
        return iie.open_url(ie_path=exe, url=url)

    def open(self, url="", path="", param="", timeout=30):
        """
        打开浏览器
        示例：
            # 打开谷歌浏览器，并访问艺赛旗官网
            Browser(AppName.chrome).open(url="i-search.com.cn")
        :param url: 打开浏览器时加载的地址，空则打开浏览器默认空白页
        :param path: 指定浏览器exe可执行程序路径，空则自动搜索
        :param param: 指定浏览器打开命令行（如安全模式运行）
        :param timeout: 启动超时时长，单位秒
        """
        self.iopen_browser(url=url, path=path, param=param, timeout=timeout)
        return self

    def close(self, wait_seconds: int = Action.WaitSeconds):
        """
        关闭浏览器
        示例：
            # 实例化谷歌浏览器，并打开页面，最后关闭当前浏览器
            browser = Browser(AppName.chrome)
            browser.open()
            browser.close()
        :param wait_seconds: 等待时间秒数，默认3秒
        """
        if self.tab_id is None:
            ILoger.warning("当前浏览器对象实例未打开任何标签页")
            return None
        return self.iclose_web_browser(wait_for=wait_seconds)

    def navigate(self, url="", wait_seconds: int = Action.WaitSeconds):
        """
        导航到网址
        :param url: 网址，空则为空页面
        :param wait_seconds: 等待时间秒数，默认3秒
        """
        if self.tab_id is None:
            self.open()
        self.inavigate_url(url=url, wait_for=wait_seconds)
        return self

    # 重定向跳转到网址
    redirect = navigate
