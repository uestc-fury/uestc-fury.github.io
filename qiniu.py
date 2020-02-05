# replace relative file links with qiniu temporary domain link

import sys
import os
import re

# qiniu temporary domain link
qiniuLink = 'http://q4v73d4us.bkt.clouddn.com'

# change path to path of script
os.chdir(sys.path[0])
# search md file in source/_posts/, add to a list
mdList = []
pathWalk = os.walk('./source/_posts/')
for path, dir_list, file_list in pathWalk:
    for file_name in file_list:
        filePath = os.path.join(path, file_name)
        if filePath[-3:] == '.md':
            mdList.append(filePath)
# for every md file, search for @qiniu, replace with qiniu temporary domain link
for filePath in mdList:
    with open(filePath) as mdCache:
        lines = mdCache.readlines()
    with open(filePath, "w") as md:
        for line in lines:
            # search for @qiniu start for ](, end with / and @qiniu start with src=", end with /
            if re.search(r']\(@qiniu/', line):
                # replace
                line = re.sub(r'(?<=]\()@qiniu(?=/)', qiniuLink, line)
            if re.search(r'src="@qiniu/', line):
                # replace
                line = re.sub(r'(?<=src=")@qiniu(?=/)', qiniuLink, line)
            md.write(line)
