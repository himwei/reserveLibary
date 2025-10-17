import requests
import json
from datetime import datetime, timedelta
import time
import random

# 目前两种预定方法 先是打乱预定北区 再是走顺序匹配字典预定data_north_2th_json_array的

whiteList_north_2F_need_random = ['2F-N055', '2F-N056', '2F-N057', '2F-N058', '2F-N059', '2F-N060', '2F-N061', '2F-N062', '2F-N063', '2F-N064', '2F-N065', '2F-N066', '2F-N067', '2F-N068', '2F-N069', '2F-N070', '2F-N071', '2F-N072', '2F-N073', '2F-N074', '2F-N075', '2F-N076']
whiteList_north_2F = whiteList_north_2F_need_random
#北区
with open('2th_north_reserve_one_seat_clear_sorted_rev.json', 'r', encoding='utf - 8') as file:
    data_north_2th_json_array = json.load(file)
dev_name_to_sn_mapping_north_2th = {item["devName"]: item["devSn"] for item in data_north_2th_json_array}
#环廊
with open('2th_round_reserve_one_seat_clear_sorted_rev.json', 'r', encoding='utf - 8') as file:
    data_round_2th_json_array = json.load(file)
dev_name_to_sn_mapping_round_2th = {item["devName"]: item["devSn"] for item in data_round_2th_json_array}

#预定函数
def reserveFun(inputCookie,dateChoose,sleepSec,resTime,roomChoose = 0):
  # while True and (roomChoose != '4' and roomChoose != '5'):
  #       print("预定楼层 目前仅支持 东4F 和 东5F 请输入4或5")
  #       roomChoose = input("")
  #       if roomChoose in ["4", "5"]:
  #           # print("输入正确！")
  #           break
  #       else:
  #           print("输入不符合要求，请重新输入4或5。")


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
      "Referer": "https://oneseat.zjhzu.edu.cn/",
      "Host": "oneseat.zjhzu.edu.cn",
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
    # 要进行等待 直到22:30
    # sleepSecCount = int(sleepSec)
    # while sleepSecCount > 0:
    #   print("距离预定时间还有" + str(sleepSecCount) + "秒")
    #   sleepSecCount -= 1
    #   time.sleep(1)
    print("距离预定时间还有" + str(sleepSec) + "秒")
    time.sleep(sleepSec)
    # time.sleep(int(sleepSec))




  whiteList_4F = ["东4F140","东4F038","东4F048","东4F056","东4F148","东4F132","东4F130"]

  # whiteList = whiteList_4F if roomChoose=='4' else whiteList_north_2F
  whiteList = whiteList_north_2F

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

  #撞车匹配 根据白名单直接进行预定 撞车匹配纯属前瞻测试 
  # 5楼经过实践 不好撞车 所以暂时不进行撞车匹配
  print("正在进行撞车匹配 请稍等...")
  print("优先5楼")
  # with open('filtered_East_2th_reserve_batch_sorted_rev.json', 'r', encoding='utf - 8') as file:
  #   data_north_2th_json_array = json.load(file)
  # dev_name_to_sn_mapping_north_2th = {item["devName"]: item["devSn"] for item in data_north_2th_json_array}
    # # 遍历列表中的字典
    # for item in data:
    #     if item['devName'] in whiteList_north_2F:
    #           print("")
    #           print("正在尝试预定"+item['devName']+"     " + "其id号为"+str(item['devSn']))
    #           print("")
    #           reserveResult = reserve_action(39689,resvDateStr,startTime,item['devSn'],headers)
    #           if reserveResult==1:
    #               print("预定成功")
    #               time.sleep(5)
    #               return
  #新增功能 打乱预定座位顺序 玄学增加成功几率
  for item in whiteList_north_2F:
      if item in dev_name_to_sn_mapping_north_2th:
          print("")
          print("正在尝试预定"+item+"     " + "其id号为"+str(dev_name_to_sn_mapping_north_2th[item]))
          print("")
          reserveResult = reserve_action(39689,resvDateStr,startTime,dev_name_to_sn_mapping_north_2th[item],headers)
          if reserveResult==1:
              print("预定成功")
              time.sleep(5)
              return
          

  print("北区预定失败------------正在进行2楼环廊预定匹配 请稍等...")

  for item in data_round_2th_json_array:
    print("正在尝试预定"+item['devName']+"     " + "其id号为"+str(item['devSn']))
    print("")
    reserveResult = reserve_action(39689,resvDateStr,startTime,item['devSn'],headers)
    if reserveResult==1:
        print("预定成功")
        time.sleep(5)
        return
  

  # 获得当前用户的 appAccNo 
  getAppAccNoUrl = "https://oneseat.zjhzu.edu.cn/ic-web/reserve/resvInfo"
  getAppAccNoUrlParams = {
      "beginDate": "2024-10-25",
      "endDate": "2025-01-30",
      "needStatus": "8454",
      "page": "1",
      "pageNum": "10",
      "orderKey": "gmt_create",
      "orderModel": "desc"
  }
  
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
    resvUrl = "https://oneseat.zjhzu.edu.cn/ic-web/reserve"

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
    # reserve_action(appAccNo,resvDateStr,startTime,resvDev,headers)



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
            print(f"离22:30还差{seconds_difference}秒。")
            # return seconds_difference
            reserveFun(inputCookie,dateChoose,seconds_difference,resTime,'5')
        else:
            print("且当前时间大于等于22:30。")
            return seconds_difference

    else:
        target_time_22_30 = current_time.replace(hour=22, minute=30, second=0, microsecond=0)
        if current_time > target_time_22_30:
            
                # print("当前时间大于22:30。")
            reserveFun(inputCookie,dateChoose,seconds_difference,resTime,'5')
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