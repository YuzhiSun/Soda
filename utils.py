# 该文件为各种方法函数 用于前期数据处理
import os
import pandas as pd
import numpy as np
wrong_path = []
def changeFileName(file_path = 'D:\\project\\soda\\Soda\\data\\busData\\July\\辽A·70008.xlsx'):
    try:
        data = pd.read_excel(file_path)
    except:
        print(file_path,' is wrong!!!')
        wrong_path.append(file_path)
    lineIds = list(set(data['线路']))
    newPathList = file_path.split('\\')
    month = newPathList[-2]
    lines = ''
    for namePiece in lineIds:
        lines += str(namePiece) + '_'
    path_ ='D:\\project\\soda\\Soda\\data\\line\\'+ lines + month +'_'+ newPathList[-1].split('.')[0] + '.csv'
    data.to_csv(path_,index=False)

    print(path_,'is OK! \n')

# changeFileName()
def traverse_dir(current_dir='D:\\project\\soda\\Soda\\data\\busData'):
    # 该方法用来 遍历文件夹下所有文件 并执行需要进行的操作
    file_list = os.listdir(current_dir)
    for file in file_list:
        path = os.path.join(current_dir, file)
        if os.path.isdir(path):
            # do something to this directory
            traverse_dir(path)
        if os.path.isfile(path):
             # do something to this file
            changeFileName(path)


traverse_dir()
