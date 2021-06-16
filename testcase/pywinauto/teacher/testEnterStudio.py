import allure
import pytest
from pywinauto import Application
from util.get_pid_auto import get_pid

process = get_pid('贝尔云课堂教师端.exe')


@allure.feature('教师端进入直播间')
class TestEnterStudio():
    '''
        进入直播间
    '''
    @classmethod
    def setup_class(cls):
        # 启动未打开的客户端
        cls.app = Application(backend='uia').connect(process=process)
        # 选择首页主窗口
        cls.dlg = cls.app['员工登录 - 贝尔云课堂']
        # 首页子窗口
        cls.document = cls.dlg.window(control_type='Document')
        cls.titleBar = cls.dlg.window(control_type='TitleBar')

    @allure.step('进入直播间')
    # @pytest.mark.dependency(depends=['teacher_login'], scope='module')
    def test_teacher_enter_studio(self):
        # self.document.print_control_identifiers()
        # 刷新课表
        refresh_btn = self.document.Static11
        refresh_btn.wait('ready')
        refresh_btn.click_input()

        # 进入直播间
        enter_studio_btn = self.document.child_window(title="进入直播课堂", control_type="Text")
        enter_studio_btn.wait('ready')
        enter_studio_btn.click_input()


if __name__ == '__main__':
    pytest.main('testEnterStudio.py')

