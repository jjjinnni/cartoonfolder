import os
import re
import sys
##---------------------------如果原始文件名为纯数字，直接用这一部分就行,把这一部分注释取消
path = '/Users/jinzhenyi/PycharmProjects/icartoon/cartoon_ims'  #图片路径
for file in os.listdir(path):
   if os.path.isfile(os.path.join(path,file))==  True:
       fname,ext=os.path.splitext(file)
       on=os.path.join(path,file)
       nn=os.path.join(path,str(fname).zfill(6)+ext)   # 数字6是定义为6位数，可随意修改需要的
       os.rename(on,nn)
##---------------------------如果原始文件为纯数字，直接用这一部分就行


# ###-------------------如果原始文件名不为纯数字，用下面一部分,把上面部分注释
# path = '/Users/jinzhenyi/PycharmProjects/icartoon/cartoon_ims'
# for i,file in enumerate(os.listdir(path)):
#     if os.path.isfile(os.path.join(path,file))==  True:
#         fname,ext=os.path.splitext(file)
#         on=os.path.join(path,file)
#         nn=os.path.join(path,str(i+1)+ext)
#         os.rename(on,nn)
# path = r"/Users/jinzhenyi/PycharmProjects/icartoon/cartoon_ims"
# filelist = os.listdir(path)
# filetype = '.jpg'
# for file in filelist:
#     print(file)
# for file in filelist:
#     Olddir = os.path.join(path, file)
#     print(Olddir)
#     if os.path.isdir(Olddir):
#         continue
#
#     # os.path.splitext("path")：分离文件名与扩展名
#     filename = os.path.splitext(file)[0]
#     filetype = os.path.splitext(file)[1]
#
#     # zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
#     Newdir = os.path.join(path, filename.zfill(6) + filetype)  # 数字6是定义为6位数，可随意修改需要的
#     os.rename(Olddir, Newdir)

