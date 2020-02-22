import os

os.system("vim test.txt")

with open('./test.txt','r')as fp:
    print(fp.read())