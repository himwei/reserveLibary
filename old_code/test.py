import datetime
import time


def countdown_to_2230():
    now = datetime.datetime.now()
    target_time = now.replace(hour=20, minute=26, second=0, microsecond=0)
    if now > target_time:
        target_time = target_time + datetime.timedelta(days=1)
    time_difference = target_time - now
    # 计算总秒数，这里包含了微秒部分转换为秒的结果
    total_seconds = time_difference.total_seconds()
    return total_seconds


remaining_seconds = countdown_to_2230()
print(f"距离 22:30 还有 {remaining_seconds} 秒。")
try:
    # 进行倒计时休眠
    time.sleep(remaining_seconds)
    print("已到达 22:30！")
except KeyboardInterrupt:
    print("倒计时被手动中断。")