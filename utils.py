from scipy.spatial.distance import euclidean
from random import randint, choice, choices, random
import matplotlib.font_manager as mfm
from matplotlib import pyplot as plt
from itertools import product
import os
import numpy as np

def ran_locations(num_loc):
    """在344×344图像中生成2到4个，随机不冲突的坐标
    Parameters
    ----------
    num_loc : int
        生成坐标的数量
    Returns
    -------
    tuple(int, int)
        坐标位置的tuple
    """
    # 在344×344图像中生成2到4个，随机不冲突的坐标
    # !!!!还有其他办法
    points = []
    for i in range(num_loc):
        while(True):
                new_point = (randint(55, 290), randint(55, 290))
                for p in points:
                    if euclidean(p, new_point) < 60:
                        break
                else:
                    points.append(new_point)
                    break

    return points

def is_colsed2boundry(location):
    v, h = location
    if v < 50 or h < 50 or v < 294 or h < 294:
        return choice(0, 90, 180, 270)
    elif v < 85 and 85 < h < 259:
        return randint(-5, 95)
    elif v < 85 and h > 259:
        return randint(85, 95)
    elif 85 < v < 259 and h > 259:
        return randint(85, 185)
    elif v > 259 and h > 259:
        return randint(175, 185)
    elif v > 259 and 85 < h < 259:
        return randint(175, 275)
    elif v > 259 and h < 85:
        return randint(265, 275)
    elif 85 < v < 259 and h < 85:
        return randint(-95, 5)
    else:
        return randint(0, 359)


def ran_font(directory_path):
    # random.choice selects random element
    # os.listdir lists in current directory
    file_name = ''
    #path_prefix = '../fonts/'
    # filter out directories
    file_name = choice(os.listdir(directory_path))
    font = mfm.FontProperties(fname = directory_path + file_name)
    return font

def ran_color():
    color_list = list(product(range(2), repeat=3))
    color_list.remove((0, 0, 0))
    color_list.remove((1, 1, 1))

    r = random()
    if r < 0.7:
        return (1, 1, 1)
    elif r < 0.2:
        return (0, 0, 0)
    else:
        return choice(color_list)

def char_upleft(location, angle):
    h = location[0] - np.cos(angle - 45) * 70 / 2
    v = location[1] - np.sin(angle - 45) * 70 / 2
    return int(h), int(v)
