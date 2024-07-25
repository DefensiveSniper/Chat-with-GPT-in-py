import os
import time
import pyautogui
import glob
import base64
from func.audio_play import play_mp3

# 手动截屏
def hand_capture_screenshot(screenshot_path):
    global screenshot_filename
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)

    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_filename = f'{screenshot_path}/{timestamp}.png'
    pyautogui.screenshot().save(screenshot_filename)
    print(f'截图保存至路径: {screenshot_filename}')
    
# 截图并返回Base64编码的图像
def capture_screenshot(screenshot_path):
    play_mp3('./audio/success.mp3')
    hand_capture_screenshot(screenshot_path)# 截图并保存
    files = glob.glob(os.path.join(screenshot_path, '*.png'))
    latest_file = max(files, key=os.path.getmtime)
    with open(latest_file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")