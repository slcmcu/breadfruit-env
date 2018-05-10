import sys
def lib():
    print("create lib")

def project():
    print("create project")

def help():
    print("hello world!")

def main(cmd):
    lcmd=len(cmd)
    print(str(sys.argv))
    print(len(sys.argv))
    if lcmd==2:    
        if cmd[1]=='startproject':
            project()
        if cmd[1]=='lib':
            lib()
        if cmd[1]=='h' or cmd[1] == 'help':
            help()
    else:
        help()

if __name__ == "__main__":
    cmd=sys.argv
    main(cmd)