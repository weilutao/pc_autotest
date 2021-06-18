from pywinauto import Application
from config.operation_yaml import OperathionYAML
import pytest

student_login_data = OperathionYAML().read_yaml('student_login.yaml')
path = student_login_data['init']['path']


class TestStudentLogin(object):
    @classmethod
    def setup_class(cls):
        cls.app = Application(backend='uia').start(path)

    def exposed_test_login_success(self):
        print('login success')


if __name__ == '__main__':
    pytest.main(['testStudentLogin.py'])
