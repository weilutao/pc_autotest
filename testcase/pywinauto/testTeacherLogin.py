from pywinauto import Application, WindowSpecification
from time import sleep


class TestTeacherLogin:
    def __init__(self, path=None, process=None):
        if path:
            # 启动未打开的客户端
            # path='C:/Users/User/AppData/Local/Programs/bell-chocloud-live-teacher/贝尔云课堂教师端.exe'
            self.app = Application(backend='uia').start(path)
        else:
            # 连接已打开的客户端
            self.app = Application(backend='uia').connect(process=process)
            # self.app = Application(backend='uia').connect(path)
        # 选择主窗口
        self.dlg = self.app['员工登录 - 贝尔云课堂']
        # 子窗口
        self.document = self.dlg.window(control_type='Document')
        self.titleBar = self.dlg.window(control_type='TitleBar')
        # self.document.print_control_identifiers()

    # 登录准确
    def login_success(self, phone_num, captcha):

        # 输入账号密码，点击登录
        input_phone = self.document.child_window(title="请输入手机号", control_type="Edit")
        input_phone.wait('ready')
        # WindowSpecification.print_control_identifiers(input_phone)
        input_phone.type_keys(phone_num)
        # 验证码
        input_captcha = self.document.child_window(control_type='Table').child_window(title="请输入验证码", control_type="Edit")
        input_captcha.wait('ready')
        input_captcha.type_keys(captcha)
        # 登录按钮
        login_btn = self.document.child_window(title="登 录", control_type="Button")
        login_btn.click()

        sleep(5)

    def close(self):
        # 关闭客户端
        close_btn = self.titleBar.child_window(title='关闭', control_type='Button')
        # WindowSpecification.print_control_identifiers(min_btn)
        close_btn.click()


if __name__ == '__main__':
    login = TestTeacherLogin()
    login.login_success()
    login.close()
