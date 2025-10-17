# -*- coding:utf-8 -*-
import requests
import json
from datetime import datetime, timedelta
import time
import random

cookie_prefix = 'ic-cookie='

token = "f33d5a89-aea3-4985-afe9-1dbcfe2c57e6"
    # token = ""

cookie = cookie_prefix + token
def handler():
    # cookie_prefix = 'ic-cookie='

    # token = "f33d5a89-aea3-4985-afe9-1dbcfe2c57e6"
    # # token = ""

    # cookie = cookie_prefix + token

    appAccNo = 116379

    headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
      # "Token": token,
      "Cookie": cookie,
      "Referer": "http://icspace.lib.zjhu.edu.cn/",
      "Host": "icspace.lib.zjhu.edu.cn",
    }

    resvDateNumber = int((datetime.now() + timedelta(days=2)).strftime('%Y%m%d'))
    resvDateStr = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    # print(resvDateNumber)
    startTime = "08:00:00"



    current_time = datetime.now()
    # 默认为0 表示当前时间不处于22点
    seconds_difference = 0
    # 判断是否处于22点
    print("当前时间:", current_time)
    target_time_22_00 = current_time.replace(hour=22, minute=0, second=0, microsecond=0)
    target_time_22_30 = current_time.replace(hour=22, minute=30, second=0, microsecond=0)

    # if target_time_22_00 <= current_time < target_time_22_00 + timedelta(minutes=1):
    if target_time_22_00 <= current_time < target_time_22_30:
        print("当前时间处于22点。")

        # 进一步判断是否小于22:30
        if current_time <= target_time_22_30:
            print("且当前时间小于22:30。")

            # 计算离22:30:01还差多少秒
            seconds_difference = (target_time_22_30 - current_time).total_seconds()
            print(f"离22:30还差{seconds_difference}秒。")
            # return seconds_difference
            # reserveFun(inputCookie,dateChoose,seconds_difference,resTime,'5')
            print("且当前时间大于等于22:30。")
            return seconds_difference

    else:
    #    print("执行keep_alive")
       if(not keep_alive(headers,resvDateNumber)):
          print("需要报告")
          report("SNzG-6sPDyiEOdLh77YayJfALlakTIMi4Ll09g828lo")


    return True


    # return "yes"
    

    # return {
    #     "statusCode": 200,
    #     "isBase64Encoded": False,
    #     "body": json.dumps(event),
    #     "headers": {
    #         "Content-Type": "application/json"
    #     }
    # }





# 用来保活的函数 即当未处于22:30时的
def keep_alive(headers,resvDateNumber):
    current_date = datetime.now().strftime("%Y-%m-%d")
    # 就是访问一下是否有预定信息 如果有那么就试试签到
    url = "http://icspace.lib.zjhu.edu.cn/ic-web/reserve/resvInfo?beginDate="+current_date+"&endDate="+current_date+"&needStatus=6&page=1&pageNum=10&orderKey=gmt_create&orderModel=desc"


    # url="http://icspace.lib.zjhu.edu.cn/ic-web/reserve"
    # params = {
    #   # 4F 100455478
    #   # 5F 100457789
    #   "roomIds": 100457789,
    #   # "resvDates": 20241126,
    #   "resvDates": resvDateNumber,
    #   "sysKind": 8
    # }
    try:
      response = requests.get(url=url, headers=headers)
      # # 获取响应的文本内容
      response_text = response.text
      response_text_dump = json.loads(response_text)
      message = response_text_dump['message']
      returnText = ""
      if message =="用户未登录，请重新登录":
        returnText = "token过期"
        return False
      elif message =="查询成功":
        if len(response_text_dump['data'])>0:
            resvId = response_text_dump['data'][0]['resvId']
            devSn = response_text_dump['data'][0]['resvDevInfoList'][0]['devSn']
            labId = response_text_dump['data'][0]['resvDevInfoList'][0]['labId']
            if int(time.time() * 1000) >= response_text_dump['data'][0]['resvBeginTime']:
                print("resvId: "+str(resvId))
                print("需要进行签到")
                reserve_sign(headers=headers,resvId=resvId,dev=devSn,lab=labId)
        returnText = "成功保活"
        return True

      print(returnText)
    
    #   return returnText
    except Exception as e:
    #    return e
        print(e)
        return False

def reserve_sign(headers,resvId,lab,dev):
    url = "http://icspace.lib.zjhu.edu.cn/ic-web/phoneSeatReserve/sign"

    # 定义请求的数据
    data = {"resvId": resvId}

    # 将数据转换为 JSON 字符串
    json_data = json.dumps(data)
    
    # params = json.dumps({'resvId':resvId})
    # params = {"resvId": resvId}
    # params = {'resvId': resvId}

    # headers['origin'] = "http://icspace.lib.zjhu.edu.cn"
    # headers['referer'] = "http://icspace.lib.zjhu.edu.cn/scancode.html"


    headers1 = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "connection": "keep-alive",
        "content-length": "18",
        "content-type": "application/json;charset=UTF-8",
        "cookie": cookie,
        "host": "icspace.lib.zjhu.edu.cn",
        "origin": "http://icspace.lib.zjhu.edu.cn",
        "referer": "http://icspace.lib.zjhu.edu.cn/scancode.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }


    # headers['content-type'] = "application/json;charset=UTF-8"

    try:
    #   session = requests.Session()
    #   codeurl = "http://icspace.lib.zjhu.edu.cn/scancode.html#/login?sta=1&sysid=1BC&lab="+str(lab)+"&dev="+str(dev)
    #   session.get(url=codeurl, headers=headers)

      response = requests.post(url=url,data=json_data, headers=headers1)
      request_obj = response.request
      print("请求 URL:", request_obj.url)
      print("请求方法:", request_obj.method)
      print("请求 Headers:", dict(request_obj.headers))  # 转为字典格式
      print("请求 Body:", request_obj.body)  # 查看请求体（字节数据）
      # # 获取响应的文本内容
      response_text = response.text
      response_text_dump = json.loads(response_text)
      message = response_text_dump['message']
      print(response_text_dump)
      returnText = ""
      if message == "操作成功":
        print("签到成功")
        returnText = "成功保活"
        report("fj3IM6bN7JY0Z1wlVK6m77j6NiF9cqF0EgAFAAsctf4")
        return True
      else:
         return False
      print(returnText)
    
    #   return returnText
    except Exception as e:
    #    return e
        return False

def reserve_action(headers,appAccNo,resvDateStr,startTime):

    
    whiteList_5F_need_random1_1 = ['东5F088', '东5F080', '东5F072']
    whiteList_5F_need_random1_2 = ['东5F084', '东5F076', '东5F068']
    whiteList_5F_need_random2 = ['东5F087', '东5F086', '东5F083', '东5F082', '东5F079', '东5F078', '东5F075', '东5F074', '东5F071', '东5F067']
    random.shuffle(whiteList_5F_need_random1_1)
    random.shuffle(whiteList_5F_need_random1_2)
    whiteList_5F_need_random1 = whiteList_5F_need_random1_1 + whiteList_5F_need_random1_2
    # random.shuffle(whiteList_5F_need_random1)
    random.shuffle(whiteList_5F_need_random2)
    whiteList_5F_need_random = whiteList_5F_need_random1+whiteList_5F_need_random2
    whiteList_5F_backup = [ '东5F081', '东5F085', '东5F077', '东5F073', '东5F069', '东5F065',  '东5F070','东5F066''东5F030', '东5F029', '东5F028', '东5F027', '东5F026', '东5F025', '东5F024', '东5F023', '东5F022', '东5F021', '东5F020', '东5F019', '东5F018', '东5F017', '东5F016', '东5F015', '东5F014', '东5F013', '东5F012', '东5F011', '东5F010', '东5F009', '东5F008', '东5F007', '东5F006', '东5F005', '东5F004', '东5F003', '东5F001']
    whiteList_5F = whiteList_5F_need_random+whiteList_5F_backup



    resvRequestObject = {
        "sysKind": 8,
        "appAccNo": int(appAccNo),
        "memberKind": 1,
        "resvMember": [
        int(appAccNo)
        ],
        # "resvBeginTime": "2024-11-26 08:00:00",
        # "resvEndTime": "2024-11-26 22:00:00",
        # "resvBeginTime": resvDateStr+" 08:00:00",
        "resvBeginTime": resvDateStr+" "+startTime+":00",
        "resvEndTime": resvDateStr+" 22:00:00",
        "testName": "",
        "captcha": "",
        "resvProperty": 0,
        "resvDev": [
        # int(resvDev)
        ],
        "memo": ""
    }

def report(templateId):
    appID = "wx07f9ed5063cf0d64"
    appSecret = "36f9a2d7393e30bd0b889d62c7f45c75"
    openId1 = "oyGj47AlRHsRPNjTKGZ4QyqL2NuI"
    openId2 = "oyGj47AM_23xtvJftqW8A4oNdWSA"
    # templateId = "SNzG-6sPDyiEOdLh77YayJfALlakTIMi4Ll09g828lo"
    
    
    def get_access_token():
        # 获取access token的url
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}' \
            .format(appID.strip(), appSecret.strip())
        response = requests.get(url).json()
        # print(response)
        access_token = response.get('access_token')
        return access_token
    def send_weather(access_token):
        # touser 就是 openID
        # template_id 就是模板ID
        # url 就是点击模板跳转的url
        # data就按这种格式写，time和text就是之前{{time.DATA}}中的那个time，value就是你要替换DATA的值

        try:
            # body1 = {
            #     "touser": openId1.strip(),
            #     "template_id": templateId.strip(),
            #     "url": "https://weixin.qq.com",
            #     "data": {
            #     }
            # }
            # url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
            # print(requests.post(url, json.dumps(body1)).text)


            body2 = {
                "touser": openId2.strip(),
                "template_id": templateId.strip(),
                "url": "https://weixin.qq.com",
                "data": {
                }
            }
            url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
            print(requests.post(url, json.dumps(body2)).text)
            return "success"
        except Exception as e:
           return "fail" 

    send_weather(get_access_token())


if __name__ == "__main__":
  print(handler())
