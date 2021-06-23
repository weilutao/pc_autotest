import pytest
from time import sleep
import allure
from util.get_pid_auto import get_pid
from pywinauto import Application, WindowSpecification


class TestClose(object):
    @classmethod
    def setup_class(cls):
        process = get_pid('贝尔云课堂教师端.exe')
        process.append(0)
        # 选择正确的应用进程，并且进行连接
        for i in process:
            try:
                refresh_btn = cls.document_studio.child_window(title='授课模式', control_type='Text')
                WindowSpecification.print_control_identifiers(cls.dlg_studio)
            except:
                cls.app = Application(backend='uia').connect(process=i)
                # 直播间主窗口
                cls.dlg_studio = cls.app['贝尔云课堂']
                # 直播间子窗口
                cls.document_studio = cls.dlg_studio.window(control_type='Document')
                cls.titleBar_studio = cls.dlg_studio.window(control_type='TitleBar')
                continue
            else:
                break

    # 直播间内关闭客户端
    @allure.step('直播间内关闭客户端')
    @pytest.mark.run(order=-1)
    def test_close(self):
        # sleep(10)
        close_btn = self.titleBar_studio.child_window(title='关闭', control_type='Button')
        close_btn.click()

        # 确认退出
        affirm_btn = self.app['关闭']['确认']
        affirm_btn.wait('ready')
        affirm_btn.click()