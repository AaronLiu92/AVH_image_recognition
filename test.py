# -*- Coding=utf-8
import paddlehub as hub #install paddlehub, paddlepaddle
#树莓派安装paddlelite;x86电脑上安装paddlehub，并将paddlehub中的预训练模型转换为paddlelite格式，使之能在树莓派上运行。
import cv2

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDf9OO9etteAQRCj38xXsxmMgla9TXMvEI'  # 替换为用户的 secretId
secret_key = 'rSntmumPnvnPnvnPmtlQs53mGUUFk00k'  # 替换为用户的 secretKey
region = 'ap-shanghai'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

classifier = hub.Module(name="mobilenet_v2_animals")

# 上传一个照片，生成list，对list里的文件下载，做一次识别，显示结果。删除bucket里的图片。显示“please take another photo”。
# 这时候程序进行下一次循环（如果不另外拍照片，list应该是空的），看list里没有东西，就继续循环

print("----please take a photo----")
while True:  # 一直循环
    allcontent = client.list_objects(Bucket='avh-1312691646')
    all_list = []

    if str('Contents' in allcontent) == 'False':  # 如果有图片，这个dict里会有key：content
        pass

    else:
        for i in allcontent['Contents']:
            all_list.append(i.get('Key'))  # 得到list

        # 下载all_list[-1]图片
        #识别
        file1 = client.get_object(Bucket='avh-1312691646',Key=str(all_list[0]))
        fp = file1.get_stream_to_file(str(all_list[0])+'.png')
        result = classifier.classification(images=[cv2.imread(fp)])  #要找到文件本身
        print(result)

        #response = client.delete_object(Bucket='avh-1312691646', Key=str(all_list[-1]))  # 云端删除图片
        print('----please take another photo----')
