from pycrawlers import huggingface

# 实例化类
hg = huggingface()

url = "https://huggingface.co/openai-community/gpt2/tree/main"
# 单一位置
path = 'E:/qian/ai/fastApi/models'
bl = hg.get_data(url, path)
print(bl)