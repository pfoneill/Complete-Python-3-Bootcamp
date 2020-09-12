import sys
import file1
num = int(sys.argv[1])
print(file1.myfunc(num))
print(f'argv[0] = {sys.argv[0]}\nargv[1] = {sys.argv[1]}')
