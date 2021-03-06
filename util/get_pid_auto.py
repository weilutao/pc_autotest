import psutil


def get_pid(name):
    """根据进程名获取pid，当然一个程序可能打开多个进程。前提条件是只打开一个进程"""
    pids = psutil.process_iter()
    pids_list =[]
    for pid in pids:
        # print(pid)
        if pid.name() == name:
            pids_list.append(pid.pid)
    return pids_list


if __name__ == '__main__':
    print(get_pid('贝尔云课堂教师端.exe'))
