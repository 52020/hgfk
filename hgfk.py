import sys
import os


root_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(root_dir, "Lib"))


import hashlib
import base64
import hmac
import time
import requests
import json
from PIL import Image
import numpy as np
import os
from ubpa.encrypt import decrypt
import cv2
from io import BytesIO
from PIL import Image

Str_Webhook_URL = r'https://lanxin.picc.com:10443/open/apigw/v1/bot/hook/messages/create?hook_token=12428032-yzhBCJYn7yEIjOV5RxfBJ3zDmtYn6KbKt7lYLGsGAY5G9T12obBAuKKp2SPz8A8Sog6KD'
Str_Countersign = r'83F10778D9863F98A985C23D78C4341F'
Str_Text = '各位好，附件为2026年“五个一"合规风控法治文化培训宣导情况记录本，请大家活动开展后及每月25日时在登记本上记录，每月25日定期发送到本群，每月月底合规部通报开展情况、登记活动台账。大家在年底时可根据台账撰写相关总结报告。'
Str_File_Path = r"./2026年度培训宣传会议记录本模板(后缀1去掉).zip1"
# 人保e办发送群消息
# 
# Str_Webhook_URL:Webhook机器人的链接
# Str_Countersign:Webhook机器人的加签
# Str_Text:文本信息
# Str_File_Path:文件绝对路径
# 
# 注：图片会压缩至1M左右，文件要在2M内否则报错


#获取token
def getAppToken():
    AppIdTxt='i01NjYwOTI2KiMIyoxMjQyODAzM='
    AppId = decrypt(AppIdTxt) 
    AppSecretTxt='MkMyOEUzQzhDQjYyODI3NiojIypDOThFNzJBNENGMzUzNTJE'
    AppSecret=decrypt(AppSecretTxt)
    url=f'https://lanxin.picc.com:10443/open/apigw/v1/apptoken/create?grant_type=client_credential&appid={AppId}&secret={AppSecret}'
    # "https://lanxintest.picc.com:10443/open/apigw"
    response = requests.get(url)
    if response.status_code == 200:
        # 解析响应
        data = json.loads(response.text)
        # 处理数据
    else:
        raise UserWarning('请求失败')
    print(data)
    #获取apptoken
    appToken=data['data']['appToken']
    print(appToken)
    return appToken
    
    
#压缩图片
def compress_image(path):
    file_size = os.path.getsize(path) / 1024.0 # 获取文件大小并转换为KB
    if file_size <= 819.2: # 如果文件大小小于等于819.2KB，直接返回
        return
    img = Image.open(path) # 打开图片
    quality = 95 # 初始压缩质量
    while file_size > 1024:
        img.save(path, optimize=True, quality=quality) # 保存压缩后的图片
        file_size = os.path.getsize(path) / 1024.0 # 获取压缩后的文件大小
        quality -= 5 # 降低压缩质量
    print('图片压缩')
#压缩图片更新2024-5-20   
def pic_compress(pic_path):
    # 读取图片bytes
#     out_path=pic_path
    outFile=os.path.basename(pic_path)
    outPath=os.path.dirname(pic_path)
    outFile=outFile.replace('.','-tmp.')
    out_path=os.path.join(outPath,outFile)
    target_size=819
    quality=90
    step=5
    pic_type='.jpg'
    with open(pic_path, 'rb') as f:
        pic_byte = f.read()
    img_np = np.frombuffer(pic_byte, np.uint8)
    img_cv = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    current_size = len(pic_byte) / 1024
    print("图片压缩前的大小为(KB)：", current_size)
    while current_size > target_size:
        pic_byte = cv2.imencode(pic_type, img_cv, [int(cv2.IMWRITE_JPEG_QUALITY), quality])[1]
        if quality - step < 0:
            break
        quality -= step
        current_size = len(pic_byte) / 1024
    # 保存图片
    with open(out_path, 'wb') as f:
        f.write(BytesIO(pic_byte).getvalue())
        time.sleep(1)
    os.replace(out_path, pic_path)
    print("图片压缩后的大小为(KB)：", current_size)
    return out_path

#获取图片id
def getPicture(appToken,Str_File_Path,sendType,size):
    headers = {
        "User-Agent": "Apifox/1.0.0 (https://www.apifox.cn)",
        "Accept": "*/*"
    }
    type=3
    url = f"https://lanxin.picc.com:10443/open/apigw/v2/medias/create?type={type}&app_token={appToken}"
    if sendType==2:
        pic_compress(Str_File_Path)
        type=2
        width=size[0]
        height=size[1]
        url = f"https://lanxin.picc.com:10443/open/apigw/v2/medias/create?type={type}&app_token={appToken}&width={width}&height={74}"
        
    
    # 设置请求体的数据
    files = {"media": (os.path.basename(Str_File_Path), open(Str_File_Path, "rb"), "image/png")}
    print(url)
    # 发起 POST 请求
    response = requests.post(url, headers=headers, files=files)
    # 输出响应结果
    print(response.text)
    if response.status_code == 200:
        # 解析响应
        data = json.loads(response.text)
        # 处理数据
    else:
        raise UserWarning('请求失败')
    print(data)
    #获取apptoken
    mediaId=data['data']['mediaId']
    return mediaId

#发送群文件消息
def sendSwarmBots(Str_Countersign,swarmBotsUrl,Str_Text,mediaIds,sendType):
    url=swarmBotsUrl
    Str_Countersign=Str_Countersign
    timestamp = int(round(time.time()))
    print(timestamp)
    string_to_sign = '{}@{}'.format(timestamp, Str_Countersign)
    print(string_to_sign)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    print(sign)
    headers={'Content-Type':'application/json'}
    mediaIds=mediaIds
    data={
        "sign":sign,
        "timestamp":str(timestamp),
        "msgType":"textMedia",
        "msgData":{
            "text":{
                "content":Str_Text,
                "mediaType":sendType,
                "mediaIds":mediaIds
           }
        }
    }
    print(url)
    jsonData=json.dumps(data)
    # jsonData = json.dumps(data)
    print(jsonData)
    route=requests.post(url,headers=headers,data=jsonData) 
    print(route.json()) 
#发送群文本消息
def sendTxtBots(Str_Countersign,swarmBotsUrl,Str_Text):
    url=swarmBotsUrl
    Str_Countersign=Str_Countersign
    timestamp = int(round(time.time()))
    print(timestamp)
    string_to_sign = '{}@{}'.format(timestamp, Str_Countersign)
    print(string_to_sign)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    print(sign)
    headers={'Content-Type':'application/json'}
    data={
        "sign":sign,
        "timestamp":str(timestamp),
        "msgType":"text",
        "msgData":{
            "text":{
                "content":Str_Text,
           }
        }
    }
    jsonData=json.dumps(data)
    # jsonData = json.dumps(data)
    print(jsonData)
    route=requests.post(url,headers=headers,data=jsonData) 
    print(route.json())

#自动校验文件是否是图片
sendType=3
width=0
height=0
size=[width,height]


if Str_File_Path:
    print('发送群文件')
    print(Str_Webhook_URL)
    print(Str_Countersign)
    print(Str_Text)
    print(Str_File_Path)
    #图文
    try:
        img = Image.open(Str_File_Path)
        width, height = img.size
        img.close()
        # 如果文件是图片，则不会抛出异常
        print("文件是图片")
        sendType=2
    except:
        print('文件不是图片')
        sendType=3
    #获取token
    appToken=getAppToken()
    mediaId=getPicture(appToken,Str_File_Path,sendType,size)
    sendSwarmBots(Str_Countersign,Str_Webhook_URL,Str_Text,[mediaId],sendType)
else:
    print('发送群文本')
    print(Str_Webhook_URL)
    print(Str_Countersign)
    print(Str_Text)
    #纯文字
    sendTxtBots(Str_Countersign,Str_Webhook_URL,Str_Text)


