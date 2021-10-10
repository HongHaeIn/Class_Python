import os
data = os.listdir('.') #현재디렉터리
print(data)

for d in data:
    print(d)
    print(f'is directory? : {os.path.isdir(d)}')