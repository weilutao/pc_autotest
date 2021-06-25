from util.get_pid_auto import get_pid


class TestStudentLogin(object):
    @classmethod
    def setup_class(cls):
        process = get_pid('贝尔云课堂.exe')
        print(process)