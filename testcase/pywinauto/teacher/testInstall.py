import pytest
from pywinauto import Application
from config.operation_yaml import OperathionYAML
from time import sleep
import allure

install_data = OperathionYAML().read_yaml('install.yaml')
t_package = install_data['init']['teacher']['package']
s_package = install_data['init']['student']['package']


@allure.feature('客户端安装')
class TestInstall(object):
    # @classmethod
    # def setup_class(cls):
    #     cls.package = Application(backend='uia').start(t_package)
    #
    #     cls.dlg = cls.package['贝尔云课堂教师端 安装 ']

    @allure.step('教师端安装')
    def test_teacher_install(self):
        self.package = Application(backend='uia').start(t_package)

        self.dlg = self.package['贝尔云课堂教师端 安装 ']

        next_btn = self.dlg.child_window(title='下一步(N) >', control_type='Button')
        next_btn.wait('ready')
        next_btn.click()

        install_btn = self.dlg.child_window(title='安装(I)', control_type='Button')
        install_btn.wait('ready')
        install_btn.click()
        sleep(10)

        # dlg.print_control_identifiers()
        # 取消运行勾选
        q_btn = self.dlg.child_window(title='运行 贝尔云课堂教师端(R)', control_type='CheckBox')
        q_btn.wait('ready')
        q_btn.click()

        # 完成
        finish_btn = self.dlg.child_window(title='完成(F)', control_type='Button')
        finish_btn.wait('ready')
        finish_btn.click()

    @allure.step('学生端安装')
    def test_student_install(self):
        self.package = Application(backend='uia').start(s_package)

        self.dlg = self.package['贝尔云课堂教 安装 ']

        next_btn = self.dlg.child_window(title='下一步(N) >', control_type='Button')
        next_btn.wait('ready')
        next_btn.click()

        install_btn = self.dlg.child_window(title='安装(I)', control_type='Button')
        install_btn.wait('ready')
        install_btn.click()
        sleep(10)

        # dlg.print_control_identifiers()
        # 取消运行勾选
        q_btn = self.dlg.child_window(title='运行 贝尔云课堂(R)', control_type='CheckBox')
        q_btn.wait('ready')
        q_btn.click()

        # 完成
        finish_btn = self.dlg.child_window(title='完成(F)', control_type='Button')
        finish_btn.wait('ready')
        finish_btn.click()


if __name__ == '__main__':
    pytest.main(['testInstall.py'])
