"""
01 - 调用大模型 API（Ollama 本地 / DeepSeek 云端）
对应课程：第 89-91 集
生成时间: 2026-07-28
"""

import requests
import json
import time

# ===== 1. 测试 Ollama 本地部署是否可用 =====
print("=== 1. 检查 Ollama 本地服务 ===")

OLLAMA_URL = "http://localhost:11434/api/generate"


def check_ollama():
    """检查本地的 Ollama 服务是否运行"""
    try:
        response = requests.get("http://localhost:11434", timeout=3)
        if response.status_code == 200:
            print("✅ Ollama 服务正在运行！")
            return True
    except requests.exceptions.ConnectionError:
        print("❌ Ollama 服务未启动")
        print("   请运行: ollama serve")
    return False


check_ollama()


# ===== 2. 调用本地 Ollama 模型 =====
def call_ollama(prompt, model="deepseek-v4-pro"):
    """调用本地的 Ollama 模型"""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"错误: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "无法连接 Ollama，请确保已运行 ollama serve"
    except Exception as e:
        return f"调用出错: {e}"


print("\n=== 2. 调用本地 Ollama ===")
print("(需先启动 ollama serve 并拉取了模型)")

# 注释掉的示例，取消注释即可运行（前提是 Ollama 已启动）
# result = call_ollama("用一句话介绍 Python")
# print(f"Ollama: {result}")


# ===== 3. 调用 DeepSeek 云端 API =====
print("\n=== 3. DeepSeek API 调用 ===")

# 从环境变量读取 API Key（更安全）
import os

API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
ENDPOINT = "https://api.deepseek.com/v1/chat/completions"


def call_deepseek(prompt, system_prompt="你是一个有用的助手"):
    """调用 DeepSeek API"""
    if not API_KEY or API_KEY == "":
        return "请设置 API Key: export DEEPSEEK_API_KEY='sk-xxx'"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1024,
        "stream": False
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        elif response.status_code == 401:
            return "认证失败: API Key 无效"
        elif response.status_code == 429:
            return "请求过于频繁, 请稍后重试"
        else:
            return f"服务器错误: {response.status_code}"
    except requests.exceptions.Timeout:
        return "请求超时, 请检查网络"
    except requests.exceptions.ConnectionError:
        return "网络连接失败, 请检查网络"
    except Exception as e:
        return f"未知错误: {e}"


# 注释掉的示例，取消注释即可运行（前提是设置了 API Key）
# result = call_deepseek("你好，用一句话介绍 Python")
# print(f"DeepSeek: {result}")


# ===== 4. 多轮对话演示（会话记忆）=====
print("\n=== 4. 多轮对话 ===")


class ChatSession:
    """带会话记忆的对话类"""

    def __init__(self, api_key="", system_prompt="你是一个有用的助手"):
        self.api_key = api_key or API_KEY
        self.messages = [{"role": "system", "content": system_prompt}]
        self.endpoint = ENDPOINT

    def send(self, user_input):
        """发送消息，自动记忆上下文"""
        if not self.api_key:
            return "请设置 API Key"

        # 追加用户消息
        self.messages.append({"role": "user", "content": user_input})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "deepseek-chat",
            "messages": self.messages,
            "temperature": 0.7,
            "max_tokens": 1024,
            "stream": False
        }

        try:
            response = requests.post(self.endpoint, headers=headers,
                                     json=data, timeout=30)
            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
                # 追加 AI 回复到历史
                self.messages.append({"role": "assistant", "content": reply})
                return reply
            return f"错误: {response.status_code}"
        except Exception as e:
            return f"错误: {e}"

    def clear(self):
        """清空对话历史"""
        system = self.messages[0]
        self.messages = [system]


if API_KEY and API_KEY != "":
    print("设置 API Key 后，可运行多轮对话示例：")
    chat = ChatSession(API_KEY)

    # 取消注释测试多轮对话
    # r1 = chat.send("1+1等于几？")
    # print(f"第1轮: {r1}")
    # r2 = chat.send("再加1呢？")
    # print(f"第2轮: {r2}")
    # r3 = chat.send("刚才我们聊了什么？")
    # print(f"第3轮: {r3}")
    # print(f"消息历史数: {len(chat.messages)}")
else:
    print("未设置 DEEPSEEK_API_KEY，跳过 API 调用演示")

# ===== 5. 模拟 API 响应结构 =====
print("\n=== 5. API 响应结构 ===")

# DeepSeek API 返回的 JSON 结构示例
example_response = {
    "id": "chatcmpl-xxx",
    "object": "chat.completion",
    "created": 1234567890,
    "model": "deepseek-chat",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "你好！我是 DeepSeek AI 助手，有什么可以帮你的吗？"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 15,
        "total_tokens": 25
    }
}

print("API 返回 JSON 结构:")
print(f"  id: {example_response['id']}")
print(f"  model: {example_response['model']}")
print(f"  reply: {example_response['choices'][0]['message']['content']}")
print(f"  tokens: {example_response['usage']['total_tokens']}")

# 提取回复的标准方式：
result = example_response
reply = result["choices"][0]["message"]["content"]
print(f"\n标准提取: result['choices'][0]['message']['content']")
print(f"=> '{reply}'")

# ===== 6. 环境变量设置说明 =====
print("\n=== 6. 使用说明 ===")
print("1. 安装 requests: pip install requests")
print("2. 设置 API Key:")
print("   Windows: set DEEPSEEK_API_KEY=sk-xxx")
print("   Linux/Mac: export DEEPSEEK_API_KEY='sk-xxx'")
print("3. 本地 Ollama:")
print("   ollama serve    # 启动服务")
print("   ollama pull deepseek-v4-pro  # 拉取模型")
print("4. 取消注释示例代码后运行本文件")
