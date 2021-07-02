from util.oa_test_course_scheduling import TestOATestCourse
from time import sleep
from testcase.pywinauto.teacher.testTeacherLogin import TestTeacherLogin
import pytest
import rpyc
import os
import shutil


if __name__ == '__main__':
    path = os.getcwd() + '/temp'
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        pass

    # OA正式服排课
    pytest.main(['E:/pc_autotest/util/oa_pro_course_scheduling.py'])

    # OA测试服排课
    pytest.main(['E:/pc_autotest/util/oa_test_course_scheduling.py'])
    sleep(300)

    # 执行本地教师端的用例
    pytest.main()

    # 远程控制，执行pc学生端的用例
    conn = rpyc.classic.connect('192.168.20.76', 9999)
    t = conn.modules['testcase.pywinauto.student.pc.main']
    t.main()

