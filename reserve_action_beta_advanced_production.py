import requests
import json
from datetime import datetime, timedelta
import time
import random




#预定函数
def reserveFun(inputCookie,dateChoose,sleepSec,resTime,roomChoose = 0):
  # roomChoose = 0
  while True and (roomChoose != '4' and roomChoose != '5'):
        print("预定楼层 目前仅支持 东4F 和 东5F 请输入4或5")
        roomChoose = input("")
        if roomChoose in ["4", "5"]:
            # print("输入正确！")
            break
        else:
            print("输入不符合要求，请重新输入4或5。")


  # print("本程序默认预定的是东校区4楼 暂时无法进行更改 请须知")
  # print("本程序默认预定的是西校区5楼 暂时无法进行更改 请须知")
#   print("本程序的预定规则是找出未被预定的座位 然后直接订一天 如果没有未被预定的座位 那么就无法进行预定")
  # 可以不使用cookie
  # token = "5760a13519854b9c8b88770baa44af2c"
  cookie = inputCookie
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
  resvDateNumber = 0
  resvDateStr = ''
  if dateChoose == "0":
    resvDateNumber = int(datetime.now().strftime('%Y%m%d'))
    resvDateStr = datetime.now().strftime('%Y-%m-%d')
  elif dateChoose == "1":
    resvDateNumber = int((datetime.now() + timedelta(days=1)).strftime('%Y%m%d'))
    resvDateStr = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
  elif dateChoose == "2":
    resvDateNumber = int((datetime.now() + timedelta(days=2)).strftime('%Y%m%d'))
    resvDateStr = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    # 要进行等待 直到22:30:01
    sleepSecCount = int(sleepSec)
    while sleepSecCount > 0:
      print("距离预定时间还有" + str(sleepSecCount) + "秒")
      sleepSecCount -= 1
      time.sleep(1)
    # time.sleep(int(sleepSec))




  whiteList_4F = ["东4F140","东4F038","东4F048","东4F056","东4F148","东4F132","东4F130"]
  # whiteList_5F = ["东5F001", "东5F003", "东5F004", "东5F005", "东5F006",
  #                "东5F007", "东5F008", "东5F009", "东5F010", "东5F011", "东5F012",
  #                "东5F013", "东5F014", "东5F015", "东5F016", "东5F017", "东5F018",
  #                "东5F019", "东5F020", "东5F021", "东5F022", "东5F023", "东5F024",
  #                "东5F025", "东5F026", "东5F027", "东5F028", "东5F029", "东5F030",
  #                "东5F065", "东5F066", "东5F067", "东5F068", "东5F069", "东5F070",
  #                "东5F071", "东5F072", "东5F073", "东5F074", "东5F075", "东5F076",
  #                "东5F077", "东5F078", "东5F079", "东5F080", "东5F081", "东5F082",
  #                "东5F083", "东5F084", "东5F085", "东5F086", "东5F087", "东5F088"]

  whiteList_5F = ['东5F088', '东5F087', '东5F086', '东5F085', '东5F084', '东5F083', '东5F082', '东5F081', '东5F080', '东5F079', '东5F078', '东5F077', '东5F076', '东5F075', '东5F074', '东5F073', '东5F072', '东5F071', '东5F070', '东5F069', '东5F068', '东5F067', '东5F066', '东5F065', '东5F030', '东5F029', '东5F028', '东5F027', '东5F026', '东5F025', '东5F024', '东5F023', '东5F022', '东5F021', '东5F020', '东5F019', '东5F018', '东5F017', '东5F016', '东5F015', '东5F014', '东5F013', '东5F012', '东5F011', '东5F010', '东5F009', '东5F008', '东5F007', '东5F006', '东5F005', '东5F004', '东5F003', '东5F001']
  
  whiteList = whiteList_4F if roomChoose=='4' else whiteList_5F

  # # 黑名单机制 优先使用黑名单 根据 座位名称 进行判断 如果黑名单中的座位名称在resvInfo数组为空 则跳过该座位 否则继续遍历 直到找到一个resvInfo数组为空的座位
  blackList_4F = ["东4F139","东4F032","东4F055"]
  blackList_5F = ["东5F033", "东5F034", "东5F035", "东5F036", "东5F037", "东5F038",
                  "东5F039", "东5F040", "东5F041", "东5F042", "东5F043", "东5F044",
                  "东5F045", "东5F046", "东5F047", "东5F048", "东5F049", "东5F050",
                  "东5F051", "东5F052", "东5F053", "东5F054", "东5F055", "东5F056",
                  "东5F057", "东5F058", "东5F059", "东5F060"]
  blackList = blackList_4F if roomChoose=='4' else blackList_5F

  #默认开始时间
  # startTime = find_closest_time()if(dateChoose=='0')else"13:00"
  startTime = find_closest_time()if(dateChoose=='0')else resTime
  print("预定开始时间")
  print(resvDateStr+" "+startTime+":00")


  # 是否已预定成功
  isReserve = 0



  # 要传递的参数，以字典形式组织
  # 默认为东4楼
  roomId_4F = 100455478
  roomId_5F = 100457789
  params = {
      # 4F 100455478
      # 5F 100457789
      "roomIds": roomId_4F if roomChoose=='4' else roomId_5F,
      # "resvDates": 20241126,
      "resvDates": resvDateNumber,
      "sysKind": 8
  }
  # # http://icspace.lib.zjhu.edu.cn/ic-web/reserve?roomIds=100455478&resvDates=20241126&sysKind=8
  url="http://icspace.lib.zjhu.edu.cn/ic-web/reserve"
  try:
      response = requests.get(url=url,  params=params, headers=headers)
      # # 获取原始的字节数据
      # content_bytes = response.content
      # # 获取响应的文本内容
      response_text = response.text
  except Exception as e:
      print(e)
      #只要有异常就进行4楼保守模式进行预定 因为4楼预定成功的概率会比较大
      print()
      print('程序出错 进入保守4楼模式进行预定------------------')
      print()
      reserveFun(inputCookie,dateChoose,0,resTime,'4')

  # print(response_text)
  # response_text = content_bytes.decode('UTF-8')

  # # 将响应文本内容保存到文件
  # with open('response_data.json', 'w',  encoding='UTF-8') as f:
  #     f.write(response_text)

  # 解析json内容 获取还未被预定的座位 即 resvInfo 数组为空的座位


  # 使用json.load()方法读取并解析文件中的JSON数据
  # with open('response_data.json', 'r',  encoding='UTF-8') as f:
  #     python_obj = json.load(f)

  resvDev = 0
  try:
    python_obj = json.loads(response_text)
    pass
  except Exception as e:
    #只要有异常就进行4楼保守模式进行预定 因为4楼预定成功的概率会比较大
    print()
    print('程序出错 进入保守4楼模式进行预定------------------')
    print()
    reserveFun(inputCookie,dateChoose,0,resTime,'4')
  # 此时python_obj就是解析后的Python对象，可以进行后续操作了
  # print(type(python_obj))
  # print(python_obj['data'])
  # 白名单机制 优先使用白名单 根据 座位名称 进行判断 如果白名单中的座位名称在resvInfo数组为空 则预定该座位 否则继续遍历 直到找到一个resvInfo数组为空的座位
  # 白名单可以优先进行对完整空列表进行判断 如果白名单中的座位名称在resvInfo数组为空 则预定该座位 否则继续遍历 直到找到一个resvInfo数组为空的座位
  


  #白名单的预定
  for i in python_obj['data']:
      if i['resvInfo'] == []:
          if i['devName'] in whiteList:
              # resvDev = i['devId']
              # print("预定座位id:" + str(i['devId']))
              resvDev = i['devSn']
              print("预定座位id:" + str(i['devSn']))
              print("预定座位名称:" + str(i['devName']))
              break

  
  # blackList = []
  
  # 先从中间往后进行循环 如果没有找到 那么就从中间往前循环
  middle_index = len(python_obj['data']) // 2
  if resvDev == 0:
    for i in range(middle_index, len(python_obj['data'])):
        # print(i)
        if python_obj['data'][i]['resvInfo'] == []:
            # print(i['devName'])
            if python_obj['data'][i]['devName'] not in blackList:
                resvDev = python_obj['data'][i]['devId']
                print("预定座位id:" + str(python_obj['data'][i]['devId']))
                print("预定座位名称:" + str(python_obj['data'][i]['devName']))
                break
  if resvDev == 0:
    for i in range(middle_index, -1, -1):
       if python_obj['data'][i]['resvInfo'] == []:
          # print(i['devName'])
          if python_obj['data'][i]['devName'] not in blackList:
              resvDev = python_obj['data'][i]['devId']
              print("预定座位id:" + str(python_obj['data'][i]['devId']))
              print("预定座位名称:" + str(python_obj['data'][i]['devName']))
              break
  
  if resvDev == 0:
    # print("未找到未被预定的座位 程序终止")
    # return
    print("")
    print("")
    print("----------------未能找到未被预定的座位 正在尝试重新进行预定 进行4楼保守模式--------------------")
    # print("正在尝试重新进行预定")
    print("")
    print("")
    reserveFun(inputCookie,dateChoose,0,resTime,'4')


  # 预定座位
  # 首先获取当前用户的 appAccNo 然后将该appAccNo 作为resvRequestObject的appAccNo 然后将resvRequestObject作为请求参数 发送请求 预定座位

  # 获得当前用户的 appAccNo 
  getAppAccNoUrl = "http://icspace.lib.zjhu.edu.cn/ic-web/reserve/resvInfo"
  getAppAccNoUrlParams = {
      "beginDate": "2024-10-25",
      "endDate": "2025-01-30",
      "needStatus": "8454",
      "page": "1",
      "pageNum": "10",
      "orderKey": "gmt_create",
      "orderModel": "desc"
  }
  # response = requests.get(url=getAppAccNoUrl,  params=getAppAccNoUrlParams, headers=headers)
  # 获取原始的字节数据
  # 获取响应的文本内容
  # response_text = response.text
  # resvHistoryInfoObject = json.loads(response_text)
#   print(resvHistoryInfoObject)

  # 关于用户标识id 在22点后可能这个请求的结果会为空 导致无法正常获取id 建议自己使用时直接手动设置 例如appAccNo = 116379
  # appAccNo = resvHistoryInfoObject['data'][0]['appAccNo']
  appAccNo = 116379
  # print("用户标识id: "+str(appAccNo))


  # startTime = find_closest_time()if(dateChoose=='0')else"08:00"
  # print("预定开始时间")
  # print(resvDateStr+" "+startTime+":00")
#   return

  #预定Object
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
      int(resvDev)
    ],
    "memo": ""
  }
  # print(resvRequestObject)
  resvHeader = {
      "Content-Type": "application/json;charset=UTF-8"
  }
  resvHeader.update(headers)

  resvRequestObjectJson_str = json.dumps(resvRequestObject)
  resvUrl = "http://icspace.lib.zjhu.edu.cn/ic-web/reserve"

  print("开始预定---------------------->")


  # random_seconds = random.randint(3, 8)
  # print(f"即将休眠 {random_seconds} 秒")
  # time.sleep(random_seconds)
  # print("休眠结束")

  response = requests.post(url=resvUrl,  data=resvRequestObjectJson_str, headers=resvHeader)

  response_text = response.text
  # print(response_text)
  response_text_dump = json.loads(response_text)
  if response_text_dump['message']=="新增成功":
      print("预定成功")
  else:
      print("")
      print("预定失败，原因可能如下:")
      print("")
      print(response_text_dump['message'])
      print("--------------正在尝试重新进行预定-------------------")
      reserveFun(inputCookie,dateChoose,0,resTime,'4')
      print("")
      print("")
  time.sleep(5)

# 预定动作
def reserve_action(appAccNo,resvDateStr,startTime,resvDev,headers):
  try:
      #预定Object
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
        int(resvDev)
      ],
      "memo": ""
    }
    # print(resvRequestObject)
    resvHeader = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    resvHeader.update(headers)

    resvRequestObjectJson_str = json.dumps(resvRequestObject)
    resvUrl = "http://icspace.lib.zjhu.edu.cn/ic-web/reserve"

    print("开始预定---------------------->")


    # random_seconds = random.randint(3, 8)
    # print(f"即将休眠 {random_seconds} 秒")
    # time.sleep(random_seconds)
    # print("休眠结束")

    response = requests.post(url=resvUrl,  data=resvRequestObjectJson_str, headers=resvHeader)

    response_text = response.text
    # print(response_text)
    response_text_dump = json.loads(response_text)
    if response_text_dump['message']=="新增成功":
        print("预定成功")
        return 1
    else:
        print("预定失败，原因可能如下:")
        print(response_text_dump['message'])
        # print("正在尝试重新进行预定")
        return 0
  except Exception as e:
    print("出错 正在尝试重新进行预定")
    print(e)
    # return 0
    reserve_action(appAccNo,resvDateStr,startTime,resvDev,headers)



# 后天预定判断是否离22:30比较近
def check_time_and_calculate(inputCookie,dateChoose,resTime):
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
        if current_time < target_time_22_30:
            print("且当前时间小于22:30。")

            # 计算离22:30:01还差多少秒
            target_time_22_30_01 = current_time.replace(hour=22, minute=30, second=0, microsecond=0)
            seconds_difference = (target_time_22_30_01 - current_time).total_seconds()
            print(f"离22:30:01还差{seconds_difference}秒。")
            # return seconds_difference
            reserveFun(inputCookie,dateChoose,seconds_difference,resTime)
        else:
            print("且当前时间大于等于22:30。")
            return seconds_difference

    else:
        target_time_22_30 = current_time.replace(hour=22, minute=30, second=0, microsecond=0)
        if current_time > target_time_22_30:
            
                # print("当前时间大于22:30。")
            reserveFun(inputCookie,dateChoose,seconds_difference,resTime)
        else:
            print("当前时间既不处于22点也不大于22:30。")
            return seconds_difference



# 今天预定时匹配对应预定时间
def find_closest_time():
    current_time = datetime.now()

    # 获取当前时间的分钟数
    current_minute = current_time.minute

    # if current_minute <= 7:
    #     closest_time = current_time.replace(minute=0)
    if current_minute <= 13:
        closest_time = current_time.replace(minute=15)
    elif current_minute <= 27:
        closest_time = current_time.replace(minute=30)
    elif current_minute <= 43:
        closest_time = current_time.replace(minute=45)
    else:
        closest_time = current_time + timedelta(hours=1)
        closest_time = closest_time.replace(minute=0)

    return closest_time.strftime('%H:%M')

# 预定小时时间
def res_start_time():
  input_text = input("请输入预定开始小时数（默认值为 8点）：")
  if input_text == "":
      input_text = "8"

  if len(input_text) == 1:
      result = "0" + input_text + ":00"
  else:
      result = input_text + ":00"
  return result

def inputCookieFun():
    cookie_prefix = 'ic-cookie='
    while True:
        print("请输入cookie(直接输入ic-cookie=的后面值即可 前面不用输入 会自动进行补齐):(输入quit结束程序)")
        user_input = input()

        if not user_input:
            print("输入不能为空，请重新输入。")
            continue

        if user_input == "quit":
            print("程序即将结束。")
            break
        if len(user_input) < 30 or len(user_input) > 80:
            print("输入长度有误，请重新输入。")
            continue
        else:
          inputDateFun(cookie_prefix+user_input)
          break
        # print(f"你输入的是: {user_input}")
def inputDateFun(cookie):
  while True:
        print("预定日期 今天为0 明天为1 后天为2 ")
        user_input = input("")
        if user_input in ["0", "1"]:
            # print("输入正确！")
            res_time = res_start_time()
            reserveFun(cookie,user_input,0,res_time)
            break
        elif user_input == "2":
            # reserveFun(cookie,user_input,check_time_and_calculate())
            res_time = res_start_time()
            check_time_and_calculate(cookie,user_input,res_time)
            break
        else:
            print("输入不符合要求，请重新输入0或1或2。")
if __name__ == "__main__":
  inputCookieFun()