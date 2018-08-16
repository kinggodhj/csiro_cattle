import numpy as np
import csv
import glob
import itertools
import os
import shutil

def getFilenames(exts):
    fnames = [glob.glob(ext) for ext in exts]
    fnames = list(itertools.chain.from_iterable(fnames))

    return fnames

def read_file(path):
    f = open(path,'r',encoding='utf-8')
    reader = csv.reader(f)
    included_cols = [0,1]
    l = []
    for row in reader:
        content = list(row[i] for i in included_cols)
        l.append(content)
    
    f.close()    
    l = np.array(l)
    return l

filePath = '/home/heejin_king/workspace/cattleProject/cattleImage/Images'
filePath_0 = '/home/heejin_king/workspace/cattleProject/cattleImage/0'
filePath_1 = '/home/heejin_king/workspace/cattleProject/cattleImage/1'
filePath_2 = '/home/heejin_king/workspace/cattleProject/cattleImage/2'
filePath_3 = '/home/heejin_king/workspace/cattleProject/cattleImage/3'
filePath_4 = '/home/heejin_king/workspace/cattleProject/cattleImage/4'
filePath_5 = '/home/heejin_king/workspace/cattleProject/cattleImage/5'
filePath_6 = '/home/heejin_king/workspace/cattleProject/cattleImage/6'
filePath_7 = '/home/heejin_king/workspace/cattleProject/cattleImage/7'
filePath_8 = '/home/heejin_king/workspace/cattleProject/cattleImage/8'
filePath_9 = '/home/heejin_king/workspace/cattleProject/cattleImage/9'
filePath_10 = '/home/heejin_king/workspace/cattleProject/cattleImage/10'
filePath_11 = '/home/heejin_king/workspace/cattleProject/cattleImage/11'
filePath_12 = '/home/heejin_king/workspace/cattleProject/cattleImage/12'
filePath_13 = '/home/heejin_king/workspace/cattleProject/cattleImage/13'
filePath_14 = '/home/heejin_king/workspace/cattleProject/cattleImage/14'
filePath_15 = '/home/heejin_king/workspace/cattleProject/cattleImage/15'
filePath_16 = '/home/heejin_king/workspace/cattleProject/cattleImage/16'
filePath_17 = '/home/heejin_king/workspace/cattleProject/cattleImage/17'

file2dic = {}
fileName = []

info = read_file("/Users/heejin/workspace/cattle/cattle_image.csv")

for name in info:
    file2dic[name[0]] = name[1]
 
for f in glob.glob(filePath+'*.JPG'):
    fileName.append(f[38:])
    
    if file2dic[f[38:]] == '0':
        shutil.move(f,filePath_0)
    elif file2dic[f[38:]] == '1':
        shutil.move(f,filePath_1)
    elif file2dic[f[38:]] == '2':
        shutil.move(f,filePath_2)
    elif file2dic[f[38:]] == '3':
        shutil.move(f,filePath_3)
    elif file2dic[f[38:]] == '4':
        shutil.move(f,filePath_4)
    elif file2dic[f[38:]] == '5':
        shutil.move(f,filePath_5)
    elif file2dic[f[38:]] == '6':
        shutil.move(f,filePath_6)
    elif file2dic[f[38:]] == '7':
        shutil.move(f,filePath_7)        
    elif file2dic[f[38:]] == '8':
        shutil.move(f,filePath_8)
    elif file2dic[f[38:]] == '9':
        shutil.move(f,filePath_9)
    elif file2dic[f[38:]] == '10':
        shutil.move(f,filePath_10)
    elif file2dic[f[38:]] == '11':
        shutil.move(f,filePath_11)
    elif file2dic[f[38:]] == '12':
        shutil.move(f,filePath_12)
    elif file2dic[f[38:]] == '13':
        shutil.move(f,filePath_13)
    elif file2dic[f[38:]] == '14':
        shutil.move(f,filePath_14)
    elif file2dic[f[38:]] == '15':
        shutil.move(f,filePath_15)
    elif file2dic[f[38:]] == '16':
        shutil.move(f,filePath_16)
    elif file2dic[f[38:]] == '17':
        shutil.move(f,filePath_17)
