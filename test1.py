# -*- Coding=utf-8
#pip install -U cos-python-sdk-v5
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import time

secret_id = 'AKIDf9OO9etteAQRCj38xXsxmMgla9TXMvEI'  # 替换为用户的 secretId
secret_key = 'rSntmumPnvnPnvnPmtlQs53mGUUFk00k'  # 替换为用户的 secretKey
region = 'ap-shanghai'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

print("----please take a photo----")
while True:#一直循环
    allcontent = client.list_objects(Bucket='avh-1312691646')
    all_list = []

    if str('Contents' in allcontent) == 'False': #如果有图片，这个dict里会有key：content
        pass 
    
    else:
        for i in allcontent['Contents']:
            all_list.append(i.get('Key')) #得到list
            print(all_list)
            #下载all_list[-1]图片到本地pics文件夹
            download_pic = client.get_object(Bucket='avh-1312691646',Key=str(all_list[-1]))
            download_pic['Body'].get_stream_to_file('/home/pi/Desktop/pics/'+ str(all_list[-1]))                                                                                        
                                                                                                                      
        #文件夹里删除图片
        time.sleep(10)                                                                                                            
        os.remove('/home/pi/Desktop/pics/'+ str(all_list[-1]))    
        
        #识别，显示结果
        
        #腾讯云COS删除文件
        response = client.delete_object(Bucket='avh-1312691646',Key=str(all_list[-1]))  # 云端删除图片
                                                                                                                  
        print('----please take another photo----')
        
