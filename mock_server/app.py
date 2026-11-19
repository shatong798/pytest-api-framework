from flask import Flask, request, jsonify

# 1. 实例化一个 Flask 应用（这就是你的后端服务器）
app = Flask(__name__)

# 2. 模拟数据库（真实情况是存在 MySQL 里，这里为了方便你用列表模拟）
# 这是初始数据，相当于数据库里只有一条数据
fake_database = [
    {"areaId": 1, "areaName": "中发白", "priority": "700"}
]


# ==========================================
# 接口 1：查询所有区域信息 (对应笔记的 1.1)
# 请求方法：GET，URL：/area/listarea
# ==========================================app
@app.route('/area/listarea', methods=['GET'])
def list_area():
    # 直接将模拟的数据库数据转换成 JSON 格式返回给前端
    return jsonify({
        "code": 200,
        "msg": "查询成功",
        "data": fake_database
    })


# ==========================================
# 接口 2：新增区域信息 (对应笔记的 2.1)
# 请求方法：POST，URL：/area/addarea
# ==========================================
@app.route('/area/addarea', methods=['POST'])
def add_area():
    # 接收前端传过来的数据
    # 之前讲过，如果前端用 "data" 传，后端就用 request.form 接
    # 如果前端用 "json" 传，后端就用 request.json 接
    # 为了兼容，我们两个都写一下
    data = request.json if request.is_json else request.form

    areaName = data.get("areaName")
    priority = data.get("priority")

    # 简单的参数校验
    if not areaName or not priority:
        return jsonify({"success": False, "msg": "参数不能为空"}), 400

    # 模拟插入数据库
    new_area = {
        "areaId": len(fake_database) + 1,  # 自动生成 ID
        "areaName": areaName,
        "priority": priority
    }
    fake_database.append(new_area)

    # 返回成功报文 (完全按照笔记里写的返回)
    return jsonify({"success": True})


# 3. 启动服务器
if __name__ == '__main__':
    # 我们故意用 1234 端口，完美复现你视频里的场景
    print("后端服务器正在启动，监听端口 1234...")
    app.run(host='0.0.0.0', port=1234, debug=True)