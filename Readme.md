环境依赖：
python3
requests
urllib3
pyyml
pytest
allure-pytest
pytest-html



运行命令：pytest test_fnd_uc.py --alluredir=../result
收集测试结果：allure serve ../result


base
    base.py文件重构get请求，解决ssl：certificate_verify_failed问题
common
    env.yml 存放域名
    api_data.yml   存放接口
    my_observatory_api.py  组装数据发送请求，处理数据
result
    存放报告文件
testcase
    test_fnd_uc.py  测试接口返回的状态码以及获取后台的湿度
    log.log   存放日志
conftest.py  设置log格式
pytest.ini  一些日志的配置
