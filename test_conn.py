import requests
import json
from datetime import datetime, timedelta
import time
import random

cookie = "UNI_AUTH_JSESSIONID=D36A79C6372FFBE6DA748F0EE70FE77F; ic-cookie=9f63ee7f-7490-4f69-b58b-3c08957bc862"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "cookie": "ic-cookie=9f63ee7f-7490-4f69-b58b-3c08957bc862",
    "host": "oneseat.zjhzu.edu.cn",
    "lan": "1",
    "pragma": "no-cache",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}

getAppAccNoUrl = "https://oneseat.zjhzu.edu.cn/ic-web/reserve/resvInfo"
getAppAccNoUrlParams = {
    "beginDate": "2025-10-13",
    "endDate": "2025-10-19",
    "needStatus": 8582,
    "page": 1,
    "pageNum": 10,
    "orderKey": "gmt_create",
    "orderModel": "desc"
}
response = requests.get(url=getAppAccNoUrl,  params=getAppAccNoUrlParams, headers=headers)
print(response.text)