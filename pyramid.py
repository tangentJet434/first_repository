def pyd():
    num = input("pyramid height :")
    n = int(num)
    for i in range(n):
        for j in range(i + 1):
            print("# ", end="")
        print("")

def pyd2():
    num = input("pyramid height :")
    n = int(num)
    for i in range(n):
        print("# " * (i + 1), end="")
        print("")




pyd()
pyd2()
