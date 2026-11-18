"""
测试模块中的 03_test_titoken 模块，负责承载对应场景的具体实现逻辑。
"""
# uv add dashscope
import dashscope  # 百炼

def count_qwen_tokens_sdk(text: str) -> int:
    # 新版用法 ↓↓↓
    return len(dashscope.tokenizers.get_tokenizer("qwen-flash").encode(text))

# 测试
test_str = "测试Qwen token计算"
print(count_qwen_tokens_sdk(test_str))



import tiktoken  # openai
# uv add tiktoken
def count_qwen_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")  #openai分词器
    return len(encoding.encode(text))

# 测试
test_str = "测试Qwen token计算"
print(count_qwen_tokens(test_str))