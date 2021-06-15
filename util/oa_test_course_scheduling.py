from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from config.operation_yaml import OperathionYAML
import allure
import os
import pytest



# 参数
oa_test_course_scheduling_data = OperathionYAML().read_yaml('oa_test_course_scheduling.yaml')
url = oa_test_course_scheduling_data['init']['get_url']
phone = oa_test_course_scheduling_data['loading']['phone']
password = oa_test_course_scheduling_data['loading']['password']
class_name = oa_test_course_scheduling_data['select_class']['class_name']
class_types = oa_test_course_scheduling_data['course_scheduling']['class_types']
class_time = oa_test_course_scheduling_data['course_scheduling']['class_time']


@allure.feature('排课')
class TestOATestCourse(object):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        sleep(5)
        cls.driver.close()

    @allure.step('登录OA')
    def test_loading(self):
        '''登录'''
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/input').send_keys(phone)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div[2]/button').click()

    @allure.step('选择班级')
    def test_select_class(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/ul[1]/li[4]/div/div[1]"))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '中心班级列表'))).click()

        while True:
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(),'%s')]" % class_name))).click()
            except Exception as e:
                # 此处有个死循环，如果没有找到班级时，一直点击下一页操作
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[3]/div/button[2]"))).click()
            else:
                return True

    @allure.step('给选中班级排课')
    def test_course_scheduling(self):
        '''排课'''
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[5]/button[3]/span[contains(text(), "单节排课")]'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="foobar"]/div/div/input'))).click()
        # 选择上课日期
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "今天")]'))).click()
        # 选择上课时间
        H_time = time.strftime("%H", time.localtime())
        M_time1 = time.strftime("%M", time.localtime())
        if int(M_time1) < 10 and int(M_time1) >= 5:
            M_time = '05'
        elif int(M_time1) < 5:
            M_time = '00'
        else:
            M_time = str(int(M_time1) // 5 * 5)
        current_time = "{0}:{1}".format(H_time, M_time)
        print(type(current_time), current_time)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div/input'))).click()
        # 定位下拉框
        # x_path = "//div[contains(text(), '%s')]" % current_time
        # print(type(x_path), x_path)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '%s')]" %current_time))).click()
        # 选择课时类型
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div/div/div[2]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' %class_types))).click()
        # 选择上课时长
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '%s')]" %class_time))).click()
        # 选择课程种类
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div[1]/ul/li[1]'))).click()
        # 选择课程小类
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[1]'))).click()
        try:
            # 选择课程
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/label/span[2]'))).click()
            # 点击保存
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[3]/button[1]'))).click()
        except Exception as e:
            print("错误的原因：", repr(e))


if __name__ == '__main__':
    pytest.main(['oa_test_course_scheduling.py'])
    # os.system('allure generate ./temp -o E:/pc_autotest/reports --clean')
    # os.system('allure open E:/pc_autotest/reports')
