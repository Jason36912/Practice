from removebg import RemoveBg
import os
import cv2 as cv

# 参数填入 api-key, 错误日志路径
rmbg = RemoveBg("7MALffu9QgveasDU8mAj7Et8", "error.log")



# 处理后的图片存放位置
path = os.path.join(os.getcwd(), "pic")

# for pic in os.listdir(path):
#     rmbg.remove_background_from_img_file(os.path.join(path, pic))

bg_remove = rmbg.remove_background_from_img_file('D:/DSC.jpg')
cv.imshow('br',bg_remove)
# 给去除了背景添加背景颜色
from PIL import Image

#输入已经去除背景的图像
im = Image.open('D:/DSC.jpg')
x,y = im.size

try:
    #填充红色背景
    p = Image.new('RGBA',im.size,(255,0,0))
    p.paste(im,(0,0,x,y),im)
    #保存
    p.save('e:/my_red_bg.png')
except:
    with open('./error.log', 'a') as f:
        f.write('background change fail')
