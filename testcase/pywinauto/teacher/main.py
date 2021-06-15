from util.oa_test_course_scheduling import TestOATestCourse
from time import sleep
from testcase.pywinauto.teacher.testEnterStudio import TestEnterStudio
import pytest


if __name__ == '__main__':
    # OA测试服排课
    pytest.main(['E:/pc_autotest/util/oa_test_course_scheduling.py'])
    sleep(300)

    # 登录教师端,进入直播间
    pytest.main()
    enterstudio = TestEnterStudio()
    sleep(100)
    enterstudio.close()
