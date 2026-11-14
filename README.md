# 基于 Pytest + Requests 的接口自动化测试框架

## 📖 项目简介
本项目是一个基于 Python 的接口自动化测试框架，用于测试公开 API 接口及本地 Mock 服务。框架采用了数据驱动、Session 连接复用、API 封装（API Object）以及 Allure 可视化报告等企业级设计理念，旨在快速验证接口的稳定性和正确性。

## 🛠️ 技术栈
- **语言**：Python 3.15.1
- **测试框架**：pytest
- **网络请求**：requests
- **Mock 后端**：Flask
- **测试报告**：allure-pytest

## 🚀 核心亮点
1. **Session 连接复用**：基于 `scope="session"` 封装全局 `api_client`，减少重复建立 TCP 连接的开销。
2. **API 对象封装（解耦）**：将底层请求与测试用例分离，提升代码可维护性。
3. **自研 Mock 服务**：内置 Flask 后端，实现了从模拟后端数据流转到自动化测试的闭环。
4. **Allure 结构化报告**：使用 `@allure.step` 标记测试步骤，报告极具可读性。

## 📸 测试报告展示
*(这里留空，稍后放截图)*

## 💻 本地运行指南

**1. 克隆项目到本地:**
```bash
git clone 你的新仓库链接.git
```