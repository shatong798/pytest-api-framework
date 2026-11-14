import requests

base_url = "http://localhost:1234"

# ==========================================
# 测试 1：查询接口 (GET)
# ==========================================
print("--- 开始查询 ---")
res1 = requests.get(f"{base_url}/area/listarea")
print("状态码:", res1.status_code)
# 用 .json() 可以直接把后端返回的 JSON 字符串变成 Python 字典
print("返回数据:", res1.json())


# ==========================================
# 测试 2：新增接口 (POST)
# ==========================================
print("\n--- 开始新增 ---")
# 我们把数据放在 json 里面发过去
new_data = {
    "areaName": "发财",
    "priority": "999"
}
res2 = requests.post(f"{base_url}/area/addarea", json=new_data)
print("状态码:", res2.status_code)
print("返回数据:", res2.json())


# ==========================================
# 测试 3：再次查询验证
# ==========================================
print("\n--- 再次查询，看看数据加进去没 ---")
res3 = requests.get(f"{base_url}/area/listarea")
print("当前所有数据:", res3.json())