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
    print("create"+path)

    path=pname+"/"+"library"
    os.mkdir(path)
    print("create"+path)
    fname=path+"/__init__.py"
    f=os.open(fname,'w')
    f.write('#init labrary')
    f.close()

    path=pname+"/"+"docs"
    os.mkdir(path)
    print("create"+path)
    
    path=pname+"/"+"requirements.txt"
    f = open(path, "w")
    f.write( "#requirements.txt \n")
    f.close()
    print("create"+path)

    path=pname+"/"+"readme.txt"
    f = open(path, "w")
    f.write( "#readme.txt \n")
    f.close()
    print("create"+path)

    path=pname+"/"+"start.py"
    f = open(path, "w")
    f.write( 'print("hllo world!") \n')
    f.close()
    print("create"+path)


def help():
    a="""
    startproject    
        -create project name
        note:
            startproject name test
    library 
        -create library 
    """
    print(a)

def main(cmd):
    lcmd=len(cmd)
    print(str(sys.argv))
    print(len(sys.argv)) 
    if lcmd >1:  
        if cmd[1]=='startproject':
            if lcmd ==3:
                pname=cmd[2]
                project(pname)

            elif cmd[1]=='library':
                lib()

        elif cmd[1]=='h' or cmd[1] == 'help':
            help()
    else:
        help()

if __name__ == "__main__":
    cmd=sys.argv
    main(cmd)