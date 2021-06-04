from util.oa_test_course_scheduling import TestOATestCourse
from time import sleep
from testcase.pywinauto.teacher.testEnterStudio import TestEnterStudio


if __name__ == '__main__':
    # OA测试服排课
    oa_ready_course = TestOATestCourse()
    oa_ready_course.loading()
    oa_ready_course.select_class()
    oa_ready_course.course_scheduling()
    oa_ready_course.close_driver()
    sleep(300)

    # 登录教师端,进入直播间
    enterstudio = TestEnterStudio()
    enterstudio.login_success()
    enterstudio.teacher_enter_studio()
    sleep(200)
    enterstudio.close()
