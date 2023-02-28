import os
dir_str = './labels'
dir_list = os.listdir(dir_str)
long = len(dir_list)
data = [0]*long
j=0
for file in dir_list:
    fb = open(file=r"./labels/"+file,mode="r",encoding="utf-8")
    ct = fb.read()
    sp = ct.split('\n')
    data[j] = sp
    j+=1
    fb.close()
for dg in data:
    for dh in dg:
        sd = dh.split()
        print(sd)
print(data)