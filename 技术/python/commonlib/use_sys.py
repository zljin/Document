import sys

def test():
    # 命令行参数List，第一个元素是程序本身路径
    args = sys.argv
    print(args[1],args[2],args[3])
    print("",sys.path,"",sys.platform)


# d:/Codes/gitrepo/corePython/venv/Scripts/python.exe d:/Codes/gitrepo/corePython/commonlib/use_sys.py 1 2 3
if __name__=='__main__':
    test()