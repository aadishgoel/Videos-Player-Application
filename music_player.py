from os import *
from glob import glob
import re

base_path= r'C:\Users\hp\Videos\Playlists'
chdir(base_path)


files  = listdir(base_path)

print('''                Welcome To Aadish's Music Company

Choose What you want to listen:                                                
''')
    
for i,item in enumerate(files):
    print(i+1,'). ',item.split('.')[0],sep='')
choice=int(input('\n'))


startfile(files[choice-1])
