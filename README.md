

## 安装依赖
```bash
pip install -r requirements.txt
```


# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_users.py

# 并行运行测试
pytest -n 4

# 生成HTML报告
pytest --html=report.html


使用多线程运行测试（4个线程）：
```bash
pytest -n 4
```

生成 Allure 报告：
```bash
pytest --alluredir=./allure-results
allure serve ./allure-results
```

pytest --fixtures 查看可用fixtures

## 测试标记
- `@pytest.mark.skip`: 跳过测试
- `@pytest.mark.parametrize`: 参数化测试


项目结构要点
模块化设计：分离了测试逻辑、API客户端和工具函数

可重用性：通过fixture和工具类减少代码重复

参数化测试：使用pytest的parametrize进行多场景测试

日志记录：API请求和响应都有详细日志

灵活的配置：支持环境变量配置

多种报告格式：支持HTML、Allure等报告格式

并行测试：支持使用pytest-xdist并行运行测试