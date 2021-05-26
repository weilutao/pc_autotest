from pywinauto import Application

app = Application(backend='uia').start('C:/Users/User/AppData/Local/Programs/bell-c'
                                       'hocloud-live-teacher/贝尔云课堂教师端.exe')
# app = Application(backend='uia').connect(path='C:/Users/User/AppData/Local/Programs/bell-chocloud-live-teacher/贝尔云课堂教师端.exe')
# path='C:/Users/User/AppData/Local/Programs/bell-chocloud-live-teacher/贝尔云课堂教师端.exe'
# process=13616

# 输入账号密码，点击登录
app[u'员工登录 - 贝尔云课堂'][u'请输入手机号'].click()
# app['员工登录 - 贝尔云课堂']['验证码'].click().set_text('205481')
# app['员工登录 - 贝尔云课堂']['登 录'].click()
# pylnspect.wrapper_object()
