import os

def main():
    lines = []
    fileList = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            fileList.append(os.path.join(root, name))
    fileList = [i for i in fileList if i.rfind(".c") == (len(i) - 2) or i.rfind(".h") == (len(i) - 2)]
    for i in fileList:
        with open(i, "r") as fp:
            fileLines = fp.readlines()
            [lines.append(i) for i in fileLines]

    lines = [i.strip() for i in lines if i.strip()]
    print("length of project:",len(lines))

if __name__ == "__main__":
    main()