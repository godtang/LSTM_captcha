#-*- coding:utf-8 -*


import os
import re
from PIL import Image
import random
import shutil

#rootdir = os.getcwd()
rootdir = 'D:/work/20180830/images'
image_path = rootdir + '/train_data_tmj'
new_image_path = 'D:/VSTEMP/captcha_image/55X120/train_data'

def process_iamge(file):
    try:
        if 8 == len(file):
            return
        filePath = os.path.join(image_path,file)
        size = os.path.getsize(filePath)
        if size > 3074:
            print('文件过大，删除文件|', filePath)
            os.remove(filePath)
            return
        newfile = filenameSplit(file)
        if '' == newfile:
            print('文件名不符合规则删除文件|', filePath)
            os.remove(filePath)
            return
        else:
            newfilepath = os.path.join(image_path,newfile+'.jpg')
            #print('重命名文件|', filePath,'为',newfilepath)
            #os.rename(filePath, newfilepath)
            print('重名文件，只能删除|', filePath)
            os.remove(filePath)
            return
    except Exception as err:
        print(err)

def process_iamge_cp(file):
    try:
        if 20 >= len(file):
            return
        oldfilePath = os.path.join(rootdir,file)
        size = os.path.getsize(oldfilePath)
        if size > 3074:
            return
        newfile = filenameSplit(file)
        if '' == newfile:
            return
        else:
            newfilepath = os.path.join(new_image_path,newfile+'.png')
            shutil.copyfile(oldfilePath,newfilepath)
            return
    except Exception as err:
        print(err)




def process_iamge_error(file):
    try:
        oldfilePath = os.path.join(new_image_path,file)
        img1 = Image.open(oldfilePath)
        img = np.array(img1)
        img1.close()
        batch_x = np.zeros([batch, time_steps, n_input])
        if len(img.shape) > 2:
            img = np.mean(img, -1)  #转换成灰度图像:(26,80,3) =>(26,80)
            img = img / 255   #标准化，为了防止训练集的方差过大而导致的收敛过慢问题。
    except Exception as err:
        print(err)

def filenameSplit(filename):
    try:
        u=r'^(.*?)_(.*?)_(.*?)\.png$'
        result = re.findall(u,filename) 
        if 1 == len(result):
            if 3 == len(result[0]):
                if 4 == len(result[0][2]):
                    return result[0][2]
        return ''
    except Exception as err:
        print(err)

def img_resize(filename, width, height):
    im = Image.open(image_path+'/'+filename)
    im= im.convert('RGB')
    out = im.resize((width, height), Image.ANTIALIAS)
    out.save(new_image_path+'/'+filename)



def prepare():
    image_file_list = os.listdir(rootdir)   #获取测试集路径下的所有文件
    print("验证码文件个数:",len(image_file_list))
    for i in range(0,len(image_file_list)):
        #print("验证码文件:",image_file_list[i])
        process_iamge_cp(image_file_list[i])
        #filename = random.choice(image_file_list)
        #img_resize(filename, 80, 26)


if __name__ == '__main__':
    prepare()
    # get_test_set()
