import requests
import logging

API_ENDPOINT = "https://api.remove.bg/v1.0/removebg"


class RemoveBg:

    def __init__(self, api_key, error_log_file):
        self.__api_key = api_key
        logging.basicConfig(filename=error_log_file)

    def remove_background_from_img_file(self, img_file_path, size="regular"):
        """
        Removes the background given an image file and outputs the file as the original file name with "no_bg.png"
        appended to it.
        :param img_file_path: the path to the image file
        :param size: the size of the output image (regular = 0.25 MP, hd = 4 MP, 4k = up to 10 MP)
        """
        # Open image file to send information post request and send the post request
        img_file = open(img_file_path, 'rb')
        response = requests.post(
            API_ENDPOINT,
            files={'image_file': img_file},
            data={'size': size},
            headers={'X-Api-Key': self.__api_key})

        self.__output_file__(response, img_file.name + "_no_bg.png")

        # Close original file
        img_file.close()



    def __output_file__(self, response, new_file_name):
        # If successful, write out the file
        if response.status_code == requests.codes.ok:
            with open(new_file_name, 'wb') as removed_bg_file:
                removed_bg_file.write(response.content)
        # Otherwise, print out the error
        else:
            error_reason = response.json()["errors"][0]["title"].lower()
            logging.error("Unable to save %s due to %s", new_file_name, error_reason)

my = RemoveBg(api_key="7MALffu9QgveasDU8mAj7Et8",  error_log_file="error.log")
my.remove_background_from_img_file(img_file_path='E:/Chrome下载/test1.jpg', size="regular")

from PIL import Image

#输入已经去除背景的图像
im = Image.open('E:/Chrome下载/test1.jpg_no_bg.png')
im.show()
x,y = im.size

print('please input a background color:')
color = str(input())

try:
    if color == 'r':
        #填充红色背景
        p = Image.new('RGBA',im.size,(255,0,0))
    elif color == 'g':
        # 填充绿色背景
        p = Image.new('RGBA', im.size, (0,255 ,0))
    elif color == 'b':
        #填充蓝色背景
        p = Image.new('RGBA',im.size,(0,0 ,255))
    p.paste(im,(0,0,x,y),im)
    #保存
    p.show()
    #p.save('e:/my_red_bg.png')
except:
    with open('./error.log', 'a') as f:
        f.write('background change fail')
