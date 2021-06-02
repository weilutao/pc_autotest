import yaml
import os


# 获取目录的绝对路径
config_path = os.path.split(os.path.realpath(__file__))[0]
# print(config_path)

class OperathionYAML:
    def read_yaml(self, sign):
        '''

        :param sign: yaml文件名称
        :return:
        '''
        file_path = os.path.abspath(os.path.join(config_path, sign))
        # print(file_path)
        with open(file_path, 'rb') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':
    o = OperathionYAML()
    print(o.read_yaml('oa_test_course_scheduling.yaml')['loading']['phone'])
