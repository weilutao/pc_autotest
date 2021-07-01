from pywinauto import Application
from config.operation_yaml import OperathionYAML
import pytest
import allure
from time import sleep

student_login_data = OperathionYAML().read_yaml('student_login.yaml')
path = student_login_data['init']['path']


@allure.feature('学生pc客户端登录')
class TestStudentLogin(object):
    @classmethod
    def setup_class(cls):
        cls.app = Application(backend='uia').start(path)
        cls.dlg = cls.app['学生端 - 贝尔云课堂']
        cls.document = cls.dlg.window(control_type='Document')

    @pytest.mark.run(order=1)
    @allure.step('学生pc客户端登录成功')
    def test_login_success(self):
        input_phone = self.document.child_window(title="请输入手机号码", control_type="Edit")
        input_phone.wait('ready')
        input_phone.set_text('18312840013')

        input_captcha = self.document.child_window(title="请输入验证码", control_type="Edit")
        input_captcha.wait('ready')
        input_captcha.set_text('205481')

        login_btn = self.document.child_window(title="登录", control_type="Button")
        login_btn.click()

        # 等待插件安装成功
        sleep(40)


if __name__ == '__main__':
    pytest.main(['testStudentLogin.py'])
