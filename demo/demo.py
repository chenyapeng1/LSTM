import os
# 处理yolo3生成的txt数据文件，将所有数据文件存储到字典中，字典的key为txt的文件名，value为值
def txt_handle(path):
    txt_total = []
    file = os.listdir(path)
    for filename in file:
        first,last = os.path.splitext(filename)
        txt_total.append(first)
    total_ = {}
    for img_ in txt_total:
        total_[img_] = []
        filename_txt = img_+".txt"
        with open(os.path.join(path,filename_txt),"r+",encoding="utf-8",errors="ignore") as f:
            for line in f:
                aa = line.split(" ")
                aa = [x.strip() for x in aa] # 删除列表中的换行符 \n
                total_[img_].append(aa)
    return total_

path = "./labels"
a = txt_handle(path)
print(a)

