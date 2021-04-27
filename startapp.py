from pywinauto import application

app = application.Application(backend='uia').start('C:/Users/User/AppData/Local/Programs/bell-chocloud-live-teacher/贝尔云课堂教师端.exe')

app.