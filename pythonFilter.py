import numpy as np

def colorize_blue(ins, outs):
    # 读取'Classification'维度的值
    classification = ins['Classification']

    # 找到'Classification'值为1的所有点的索引
    blue_indices = np.where(classification == 1)

    # 将这些点的'Red'和'Green'维度值设为0，'Blue'维度值设为255（即蓝色）
    ins['Red'][blue_indices] = 0
    ins['Green'][blue_indices] = 0
    ins['Blue'][blue_indices] = 255

    # 将处理过的数据返回
    outs['Classification'] = ins['Classification']
    outs['Red'] = ins['Red']
    outs['Green'] = ins['Green']
    outs['Blue'] = ins['Blue']

    return True
