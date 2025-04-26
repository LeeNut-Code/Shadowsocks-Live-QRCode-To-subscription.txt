import time
import pyautogui
from datetime import datetime, timedelta
import os

def capture_screenshots():
    # 获取脚本所在文件夹路径
    script_folder = os.path.dirname(os.path.abspath(__file__))
    # 创建一个保存截图的文件夹
    screenshots_folder = os.path.join(script_folder, "Screenshots")
    os.makedirs(screenshots_folder, exist_ok=True)

    # 记录开始时间
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=30)  # 60分钟后停止

    while datetime.now() < end_time:
        # 获取当前时间作为文件名
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_folder, f"screenshot_{timestamp}.png")
        
        # 截取屏幕并保存
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
        # 等待2分钟
        time.sleep(60)

if __name__ == "__main__":
    capture_screenshots()