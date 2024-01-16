from openai import OpenAI
from func.switch_model import switch_model
from func.read_file import read_file
from func.chat_with_gpt import chat_with_gpt
from func.generate_image import generate_image
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

model_list = ["gpt-4-1106-preview","gpt-4-vision-preview","gpt-4","gpt-4-32k","gpt-4-0613","gpt-4-32k-0613"]

client = OpenAI()
current_model = "gpt-4-vision-preview"
current_model_name = current_model

print(current_model_name + "：您好，有什么需要帮助的吗？")

while True:
    user_input = input("Me：")
    if user_input.lower() == "!exit":
        break
    elif user_input.lower() == "!read":
        user_input = read_file(current_model_name) + ",请对以上内容进行深度解析并总结。"
    elif user_input.lower() == "!switch":
        current_model_name = switch_model(model_list, current_model_name)
        continue
    elif user_input.lower() == "!draw":
        print("请输入图片生成的prompt：")
        prompt = input()
        generate_image(prompt, client)
        continue
    
    chat_with_gpt(user_input, current_model_name, client)