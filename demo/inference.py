# 使用yolo3检测作为people的检测结果
# yolo3 的输出结果结构：1.classes，每个类别的数据量，2.labels，标签，3、center xy，中心点的位置，4、labels 标签的长和宽。
import demo

path = '../yolov3/runs/detect/exp/labels'
txt_document = demo.txt_handle(path)
# print('txt:',txt_document)

# 利用3与4，划定people位于图片中的准确位置。针对单张图片 宽，高，左上，右上，左下，右下
def people_position(center_x,center_y,labels_width,labels_length):
    people_top_left = [center_x-labels_length//2,center_y-labels_width//2]
    people_bottom_left = [center_x-labels_length//2,center_y+labels_width//2]
    people_top_right = [center_x+labels_length//2,center_y-labels_width//2]
    people_bottom_right = [center_x+labels_length//2,center_y+labels_width//2]
    people_p = [labels_width,labels_length,people_top_left,people_top_right,people_bottom_left,people_bottom_right]
    return people_p

# 使用people_position的结果，在图片中所有人中计算遮挡度，取所有人所处位置的topmax，bottommix，leftmix，rightmax，获得一张包括所有人在内的最小图片。
# 由yolo获得的所有人中，计算每个人所占面积相加为所有所占总面积。
# 由所有人所占总面积除以包括所有人在内的最小图片，视为遮挡度。

# 返回包括所有人在内的最小图片的面积，输入为yolo所有人的输出
def mix_picture(people):
    top = []
    bottom = []
    left = []
    right = []
    if people != []:
        for one in people:
            top.append(one[2][1])
            bottom.append(one[4][1])
            left.append(one[2][0])
            right.append(one[3][0])
        topmin = min(top)
        bottommax = max(bottom)
        leftmix = min(left)
        rightmax = max(right)
    else:
        topmin = 0
        bottommax = 0
        leftmix = 0
        rightmax = 0
    all_people_area = (bottommax-topmin) * (rightmax-leftmix)
    return all_people_area

# 返回所有人面积之和，输入为yolo所有人的输出
def peoples_area(people):
    peoples_areas = 0 # 总面积
    for one in people:
        people_area = int(one[3]) * int(one[4]) # 某个人的面积
        peoples_areas += people_area
    return peoples_areas

# 处理yolo3 获得的数据，处理成字典格式，图片名：列表
def p_p(txt_document):
    d_ = {}
    for t_ in txt_document:
        f_ = []
        for i_ in txt_document[t_]:
            p_ = people_position(float(i_[1]),float(i_[2]),float(i_[3]),float(i_[4]))
            f_.append(p_)
        d_[t_] = f_
    return d_

# 使用mix_picture函数，处理p_p获得的数据，得到每张图片的最小面积
def mix_ps(pictures):
    d_ = {}
    for i_ in pictures:
        a_ = mix_picture(pictures[i_])
        d_[i_] = a_
    return d_

# 使用peoples_area函数获得所有人在内的 面积之和
def p_areas(picture):
    d_ = {}
    for i_ in picture:
        a_ = peoples_area(picture[i_])
        d_[i_] = a_
    return d_

# 每张图片的人数
def people_num(txt_document):
    d_ = {}
    for i_ in txt_document:
        long = len(txt_document[i_])
        d_[i_] = long
    return d_

# 遮挡度
def people_occlusion_degree(all_people_area,peoples_areas):
    d_ = {}
    for i_ in all_people_area:
        if all_people_area[i_] != 0:
            d_[i_] = int(all_people_area[i_]) / int(peoples_areas[i_])
    return d_

# 将图片，人数，遮挡度进行混合
def total(p_num,p_degree):
    d_ = {}
    for i_ in p_num:
        j = []
        j.append(p_num[i_])
        if i_ in p_degree:
            j.append(p_degree[i_])
        else:
            j.append(0)
        d_[i_] = j
    return d_

l = p_p(txt_document)
# print(l)
# print("所有人总面积：",mix_ps(l))
# print("所有人面积之和：",p_areas(txt_document))
# print('人数：',people_num(txt_document))
degree = people_occlusion_degree(p_areas(txt_document),mix_ps(l))
t_ = total(people_num(txt_document),people_occlusion_degree(p_areas(txt_document),mix_ps(l)))
print(t_)
