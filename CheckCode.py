from captcha.image import ImageCaptcha
import os
import sys
import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
char_set = ['0','1','2','3','4','5','6','7','8','9']
char_set_len = len(char_set)
captcha_len = 4

captcha_image_path = 'checkcode'

test_image_path = 'test'

test_image_number = 100

def generate_captcha_image(charSet=char_set,
                           charSetLen=char_set_len,captchaImagePath=captcha_image_path):

    captcha_text = ''
    for i in range(captcha_len):
        c = random.choice(char_set)
        captcha_text+=c
    print(captcha_text)
    image = ImageCaptcha()
    #生成并显示验证码
    # img = image.generate(captcha_text)
    # captcha_image = Image.open(img)
    # captcha_image = np.array(captcha_image)
    # plt.imshow(captcha_image)
    # plt.show()

    if not os.path.exists(captchaImagePath):
        os.mkdir(captchaImagePath)
    image.write(captcha_text,captchaImagePath+"/"+captcha_text+".png")


    #读取图片
    # pic = mpimg.imread(captchaImagePath+"/"+captcha_text+".png")
    # print(pic.shape)
    # print(pic)



if __name__ == '__main__':
    generate_captcha_image()