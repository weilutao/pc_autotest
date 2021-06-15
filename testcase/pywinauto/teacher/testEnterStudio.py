import allure
import pytest
from pywinauto import Application
from config.operation_yaml import OperathionYAML


# 参数
teacher_login_data = OperathionYAML().read_yaml('teacher_login.yaml')
path = teacher_login_data['init']['path']

# @allure.feature('教师端进入直播间')
class TestEnterStudio():
    '''
        进入直播间
    '''
    @classmethod
    def setup_class(cls):
        # 启动未打开的客户端
        cls.app = Application(backend='uia').start(path)
        # 选择首页主窗口
        cls.dlg = cls.app['员工登录 - 贝尔云课堂']
        # 首页子窗口
        cls.document = cls.dlg.window(control_type='Document')
        cls.titleBar = cls.dlg.window(control_type='TitleBar')

    @allure.step('进入直播间')
    # @pytest.mark.dependency(depends=['teacher_login'], scope='package')
    def test_teacher_enter_studio(self):
        self.document.print_control_identifiers()
        # 刷新课表
        refresh_btn = self.document.Static11
        refresh_btn.wait('ready')
        refresh_btn.click_input()

        # 进入直播间
        enter_studio_btn = self.document.child_window(title="进入直播课堂", control_type="Text")
        enter_studio_btn.wait('ready')
        enter_studio_btn.click_input()


if __name__ == '__main__':
    # 登录教师端
    # enterstudio = TestEnterStudio()
    # enterstudio.login_success()
    # enterstudio.teacher_enter_studio()
    # enterstudio.close()
    pytest.main('testEnterStudio.py')

