from util.get_pid_auto import get_pid
from pywinauto import Application, WindowSpecification
import allure
import pytest


@allure.feature('pc学生端进入教室')
class TestStudentLogin(object):
    @classmethod
    def setup_class(cls):
        process = get_pid('贝尔云课堂.exe')
        print(process)
        process.append(0)
        for i in process:
            try:
                groupbox = cls.document.GroupBox
                WindowSpecification.print_control_identifiers(cls.document)
            except:
                cls.app = Application(backend='uia').connect(process=i)
                cls.dlg = cls.app['学生端 - 贝尔云课堂']
                cls.document = cls.dlg.window(control_type='Document')
                continue
            else:
                break

    @pytest.mark.run(order=2)
    @allure.step('进入直播间')
    def test_student_enter_studio(self):
        groupbox = self.document.GroupBox

        enter_btn = groupbox.child_window(title="进入课堂", control_type="Button")
        enter_btn.wait('ready')
        enter_btn.click()

        # 设备检测,有就完成自动检测，没有就跳过
        try:
            self.dlg1 = self.app['设备检测 - 贝尔云课堂']
            self.document1 = self.dlg1.window(control_type='Document')

            # 开始检测
            start_btn = self.document1.child_window(title='开始检测', control_type='Text')
            start_btn.wait('ready')
            start_btn.click_input()

            camera_btn = self.document1.child_window(title='能看到', control_type='Text')
            camera_btn.wait('ready')
            camera_btn.click_input()

            loudspeaker_btn = self.document1.child_window(title='能听到', control_type='Text')
            loudspeaker_btn.wait('ready')
            loudspeaker_btn.click_input()

            microphone_btn = self.document1.child_window(title='能看到', control_type='Text')
            microphone_btn.wait('ready')
            microphone_btn.click_input()

            net_btn = self.document1.child_window(title='下一步', control_type='Text')
            net_btn.wait('ready')
            net_btn.click_input()

            webGL_btn = self.document1.child_window(title='下一步', control_type='Text')
            webGL_btn.wait('ready')
            webGL_btn.click_input()

            finish_btn = self.document1.child_window(title='进入课堂', control_type='Text')
            finish_btn.wait('ready')
            finish_btn.click_input()
        except:
            pass


if __name__ == '__main__':
    pytest.main(['testEnterStudio.py'])
