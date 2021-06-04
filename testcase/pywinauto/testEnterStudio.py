from testcase.pywinauto.testTeacherLogin import TestTeacherLogin
import os
from pywinauto import WindowSpecification,keyboard
import allure
import pytest


@allure.feature('教师端进入直播间')
class TestEnterStudio:
    '''
        进入直播间
    '''
    @allure.step('进入直播间')
    @pytest.mark.dependency(depends=['teacher_login'], scope='module')
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
    # 登录教师端
    # enterstudio = TestEnterStudio()
    # enterstudio.login_success()
    # enterstudio.teacher_enter_studio()
    # enterstudio.close()
    pytest.main('testEnterStudio.py')

