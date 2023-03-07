import json
import os
# 处理openpose生成的output_jsons文件
def json_handle(path):
    # 将所有json文件放入字典中
    json_total = [0]
    file = os.listdir(path)
    for filename in file:
        first,last = os.path.splitext(filename)
        json_total.append(first)
    json_total = json_total[1:]
    total_ = {}
    # 处理所有json文件
    for json_ in json_total:
        i = 1
        total_[json_] = {}
        filename_json = json_+".json"
        # 处理每一个json文件
        with open(os.path.join(path,filename_json),'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            if json_data['people'] != []:
                for i_ in json_data['people']:
                    j_ = 'people_'+str(i)
                    total_[json_][j_] = i_['pose_keypoints_2d']
                    # print(total_[json_][j_])
                    i+=1
    return total_

road = 'output_jsons/'
fx = json_handle(road)
print(fx)