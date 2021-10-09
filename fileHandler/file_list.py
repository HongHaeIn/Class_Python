
import os
data = os.listdir('.') #현재디렉터리
p
rint(data)

for d in data:
    print(d)
    print(f'is directory? : {os.path.isdir(d)}')