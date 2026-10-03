from zhipuai import ZhipuAI

# 1. 初始化客户端，替换成你的真实 Key
client = ZhipuAI(api_key="7e73cf1638db439aaeaf375f4778f495.QlJIMaDdsXgk9QIO")

# 2. 发起对话请求
response = client.chat.completions.create(
    model="glm-4-flash",  # 指定模型
    messages=[
        {"role": "user", "content": "你好,1+2等于多少?"}
    ]
)

# 3. 打印模型回复
print(response.choices[0].message.content)