import allure
import pytest
from pywinauto import Application
from util.get_pid_auto import get_pid
from time import sleep


@allure.feature('教师端进入直播间')
class TestEnterStudio():
    '''
        进入直播间
    '''
    @classmethod
    def setup_class(cls):
        process = get_pid('贝尔云课堂教师端.exe')
        # print(process)
        # 选择正确的应用进程，并且进行连接
        for i in process:
            try:
                refresh_btn = cls.document
            except:
                print(i)
                cls.app = Application(backend='uia').connect(process=i)
                # 选择首页主窗口
                cls.dlg = cls.app['员工登录 - 贝尔云课堂']
                # 首页子窗口
                cls.document = cls.dlg.window(control_type='Document')
                cls.titleBar = cls.dlg.window(control_type='TitleBar')

                # 直播间主窗口
                cls.dlg_studio = cls.app['贝尔云课堂']
                # 直播间子窗口
                cls.document_studio = cls.dlg_studio.window(control_type='Document')
                cls.titleBar_studio = cls.dlg_studio.window(control_type='TitleBar')
                continue
            else:
                break

    @allure.step('进入直播间')
    # @pytest.mark.dependency(depends=['teacher_login'], scope='module')
    @pytest.mark.run(order=2)
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

    # 直播间内关闭客户端
    @allure.step('直播间内关闭客户端')
    @pytest.mark.run(order=-1)
    def test_close(self):
        sleep(10)
        close_btn = self.titleBar_studio.child_window(title='关闭', control_type='Button')
        # WindowSpecification.print_control_identifiers(min_btn)
        close_btn.click()

        # 确认退出
        affirm_btn = self.app['关闭']['确认']
        affirm_btn.wait('ready')
        affirm_btn.click()


if __name__ == '__main__':
    pytest.main('testEnterStudio.py')

