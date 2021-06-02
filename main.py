from util.oa_test_course_scheduling import OATestCourse
from testcase.pywinauto.testTeacherLogin import TestTeacherLogin
from time import sleep
from testcase.pywinauto.testEnterStudio import TestEnterStudio


if __name__ == '__main__':
    # OA排课
    oa_ready_course = OATestCourse()
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
