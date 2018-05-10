import sys
import os
def lib():
    print("create lib")

def project(pname):
    path=pname
    os.mkdir(pname)
    print("create project "+pname)

    path=pname+"/"+"tools"
    os.mkdir(path)
    print("create tools")

    path=pname+"/"+"library"
    os.mkdir(path)
    print("create library")

    path=pname+"/"+"docs"
    os.mkdir(path)
    print("create docs")
    
    path=pname+"/"+"requirements.txt"
    f = open(path, "w")
    f.write( "#requirements.txt \n")
    f.close()
    print("requirements.txt")

    path=pname+"/"+"readme.txt"
    f = open(path, "w")
    f.write( "#readme.txt \n")
    f.close()
    print("readme.md")

def help():
    print("hello world!")

def main(cmd):
    #lcmd=len(cmd)
    #print(str(sys.argv))
    #print(len(sys.argv))   
    if cmd[1]=='startproject':
        pname=cmd[2]
        project(pname)
    if cmd[1]=='lib':
        lib()
    if cmd[1]=='h' or cmd[1] == 'help':
        help()
    else:
        help()

if __name__ == "__main__":
    cmd=sys.argv
    main(cmd)