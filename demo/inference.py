# 使用yolo3检测作为people的检测结果
# yolo3 的输出结果结构：1.classes，每个类别的数据量，2.labels，标签，3、center xy，中心点的位置，4、labels 标签的长和宽。
import torch
import numpy as np

# 利用3与4，划定people位于图片中的准确位置。针对单张图片
'''def people_position(center_x,center_y,labels_width,labels_length):
    people_top_left = [center_x-labels_length//2,center_y-labels_width//2]
    people_top_right = [center_x-labels_length//2,center_y+labels_width//2]
    people_bottom_left = [center_x+labels_length//2,center_y-labels_width//2]
    people_bottom_right = [center_x+labels_length//2,center_y+labels_width//2]
    people_p = [labels_width,labels_length,people_top_left,people_top_right,people_bottom_left,people_bottom_right]
    return people_p

# 使用people_position的结果，在图片中所有人中计算遮挡度，取所有人所处位置的topmax，bottommix，leftmix，rightmax，获得一张包括所有人在内的最小图片。
# 由yolo获得的所有人中，计算每个人所占面积相加为所有所占总面积。
# 由所有人所占总面积除以包括所有人在内的最小图片，视为遮挡度。

# 返回图片中所有的“人”，输入为yolo的所有检测的输出
def all_people(body):
    people = []
    for one in body:
        if one.id == 'person':
            people.append(one)
    return people

# 返回包括所有人在内的最小图片的面积，输入为yolo所有人的输出，即all_people的输出
def mix_picture(people):
    top = []
    bottom = []
    left = []
    right = []
    for one in people:
        people_p = people_position(one.center_x,one.cener_y,one.labels_width,one.labels_length)
        top.append(people_p[2][0])
        bottom.append(people_p[4][1])
        left.append(people_p[2][1])
        right.append(people_p[3][0])
    topmax = max(top)
    bottommix = min(bottom)
    leftmix = min(left)
    rightmax = max(right)
    all_people_area = (topmax-bottommix) * (rightmax-leftmix)
    return all_people_area

# 返回所有人面积之和，输入为yolo所有人的输出，即all_people的输出
def peoples_area(people):
    peoples_areas = 0 # 总面积
    for one in people:
        people_area = one.labels_width * one.labels_length # 某个人的面积
        peoples_areas += people_area
    return peoples_areas

# 遮挡度
def people_occlusion_degree(all_people_area,peoples_areas):
    return peoples_areas/all_people_area'''


