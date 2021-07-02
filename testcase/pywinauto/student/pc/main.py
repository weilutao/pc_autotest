import pytest
import os
import shutil


def main():
    # 如果此路径下有temp文件夹，就删除
    path = os.getcwd() + '/temp'
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        pass

    pytest.main(['testStudentLogin.py'])
    pytest.main(['testEnterStudio.py'])


if __name__ == '__main__':
    main()
