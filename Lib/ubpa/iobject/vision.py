# coding: utf8
"""
视觉类，包含：ocr，image
"""

from ubpa import iimg, iocr
from ubpa.iobject.element import Action


class OCR:
    """OCR类"""

    class Engine:
        """OCR引擎"""
        Internet = 0  # 互联网公共服务
        Private = 1  # 私有化局域网服务

    def __init__(self, apikey="", secretkey="", engine: int = Engine.Internet):
        """
        实例化
        示例：
            # 互联网OCR服务，需要使用自己的apiKey和secretKey
            OCR(apikey="your_apiKey", secretkey="your_secretKey")

            # 私有OCR服务无需apikey和secretkey
            OCR(engine=Engine.Private）
        :param apikey: 艺赛旗控制台接口key
        :param secretkey: 艺赛旗控制台加密key
        :param engine: OCR识别引擎，默认可不设置（艺赛旗公共服务）
            0：互联网，1：私有化（无需apikey和secretkey）
        """
        self.apikey = apikey
        self.secretkey = secretkey
        self.engine = engine

    def verification_code(self, image_path="", code_type=8000) -> str:
        """
        验证码
        示例：
            # 指定滑动验证码的方式识别指定路径的验证码类图片
            OCR(engine=Engine.Private).vcode(
                "C:\\Users\\Administrator\\Desktop\\1.jpg", 8000)

            # 默认滑动验证码的方式识别指定路径的验证码类图片
            OCR(engine=Engine.Private).vcode(
                "C:\\Users\\Administrator\\Desktop\\1.jpg")
        :param image_path: 识别图片的路径
        :param code_type: 验证码类型，默认为8000 字母、数字、汉字验证。
            代号对应示意:
                6000/8000
                        不定长度英文数字汉字混合，字母验证、数字验证、数字+字母验证；
                7000    问答题，智能回答题验证；
                9000    滑动验证，点选一处验证；
                9001    点击1~4个位置（图标、字母）验证；
                9002    点击3~5个位置（汉字）验证；
                9003    点击两个相同的字验证；
        :return: 返回识别出的验证码，类型为str
        """
        return iocr.vcode_recognize(
            image_path=image_path,
            code_type=code_type,
            apiKey=self.apikey,
            secretKey=self.secretkey
        )

    def text(self, image_path: str = "") -> str:
        """
        OCR文本识别
        示例：
            OCR(engine=Engine.Private).text(
                "C:\\Users\\Administrator\\Desktop\\1.jpg")
        :param image_path: 需识别的图片路径
        :return: 通用文字识别，返回文本
        错误返回:
                1       服务器内部错误
                2       服务暂不可用
                100     无效的access_token参数，请检查后重新尝试
                110     access_token无效
                111     access_token过期
                216201  上传的图片格式错误，现阶段支持的图片格式为：
                        PNG、JPG、JPEG、BMP，请进行转码或更换图片
                216202  上传的图片大小错误，现阶段我们支持的图片
                        大小为：base64编码后小于4M，分辨率不高
                        于4096*4096。
                282810  图像识别错误
        """
        return iocr.general_recognize(
            image_path=image_path,
            apiKey=self.apikey,
            secretKey=self.secretkey,
            ocr_engine=self.engine
        )


class Image:
    """图片类"""

    def __init__(self, win_title="",
                 win_class: [str, None] = None,
                 win_text: [str, None] = None):
        """
        初始化
        示例：
            # 激活标题为"无标题 - 记事本"的窗口
            Image(win_title="无标题 - 记事本")

            # 不传入win_title，则在当前屏幕截取图片
            Image()
        :param win_class:
        :param win_title:
        """
        self.win_title = win_title
        self.win_class = win_class
        self.win_text = win_text

    def capture(self, path: [str, None] = None,
                name: [str, None] = None,
                position: (float, float) = (0, 0),
                size: (float, float) = (0, 0),
                wait_seconds: int = Action.WaitSeconds):
        """
        截图
        示例：
            # 从屏幕0,0的位置截取宽度50、高度50的图像
            Image().capture(position=(0,0), size=(0,0))

            # 从屏幕0,0的位置截取宽度50、高度50、名称为test_pic的图片，并保存在桌面
            Image().capture(
                path="C:\\Users\\Administrator\\Desktop",
                name="test_pic", position=(0,0), size=(50,50))
        :param path: 指定截图保存文件夹的路径
        :param name: 指定截图保存的名称,不需要加后缀，保存为.png格式
        :param position: 类型为元组 (与屏幕左侧距离, 与屏幕顶部距离)
        :param size: 类型为元组（宽, 高）
        :param wait_seconds: 等待时间秒数
        :return: 截图保存路径
        """
        x, y, *_ = position
        width, height, *_ = size
        return iimg.capture_image(
            win_title=self.win_title,
            win_class=self.win_class,
            win_text=self.win_text,
            in_img_path=path,
            in_img_name=name,
            left_indent=x,
            top_indent=y,
            width=width,
            height=height,
            waitfor=wait_seconds
        )
