from pywinauto import Application, WindowSpecification
from time import sleep
from config.operation_yaml import OperathionYAML
import allure
import pytest
import os

# 参数
teacher_login_data = OperathionYAML().read_yaml('teacher_login.yaml')
path = teacher_login_data['init']['path']
phone_num = teacher_login_data['login_success']['phone_num']
captcha = teacher_login_data['login_success']['captcha']


@allure.feature('教师端登录')
class TestTeacherLogin:
    @classmethod
    def setup_class(cls):
        # 启动未打开的客户端
        cls.app = Application(backend='uia').start(path)

        # 选择首页主窗口
        cls.dlg = cls.app['员工登录 - 贝尔云课堂']
        # 首页子窗口
        cls.document = cls.dlg.window(control_type='Document')
        cls.titleBar = cls.dlg.window(control_type='TitleBar')
        print('---------------11111111111------------------')
        # self.document.print_control_identifiers()

        # # 直播间主窗口
        # cls.dlg_studio = cls.app['贝尔云课堂']
        # # 直播间子窗口
        # cls.document_studio = cls.dlg_studio.window(control_type='Document')
        # cls.titleBar_studio = cls.dlg_studio.window(control_type='TitleBar')

    # 登录成功
    @allure.step('登录成功')
    def test_login_success(self):
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

    # 直播间内关闭客户端
    def close(self):
        sleep(5)
        close_btn = self.titleBar_studio.child_window(title='关闭', control_type='Button')
        # WindowSpecification.print_control_identifiers(min_btn)
        close_btn.click()

        # 确认退出
        affirm_btn = self.app['关闭']['确认']
        affirm_btn.wait('ready')
        affirm_btn.click()


if __name__ == '__main__':
    pytest.main(['testTeacherLogin.py'])


