def dedupe(items):
    """去除列表中的重复元素，保持顺序"""
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

def add(a, b):
    """新增的加法功能"""
    return a + b

if __name__ == "__main__":
    # 测试去重功能
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    result = list(dedupe(sample_list))
    print(f"Original: {sample_list}")
    print(f"Deduped: {result}")
    
    # 测试加法功能
    print(f"Addition: 2 + 3 = {add(2, 3)}")