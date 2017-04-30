from os import *
from glob import glob
import re

basePath='C:/Users/welcome/Videos/'
chdir(basePath)
dirs=[]

for x,y,z in walk(basePath):
    ans=re.search(r'\w+$',x)
    if ans:
        dirs.append(ans.group())


for i,item in enumerate(dirs):
    print(i+1,'). ',item,sep='')
choice=int(input())

newPath=path.join(basePath,dirs[choice-1])    
chdir(newPath)

videos=glob('*.mp4')

for i,item in enumerate(videos):
    print(i+1,'). ',item,sep='')
choice=int(input())

startfile(path.join(newPath,videos[choice-1]))
