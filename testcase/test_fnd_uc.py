import logging

import allure

from common.my_observatory_api import MyObservatoryApi
logger=logging.getLogger()
@allure.feature("测试九天预报接口")
class TestFndUc:
    def setup(self):
        self.api=MyObservatoryApi()
    @allure.title("测试九天预报状态码及打印后天相对湿度")
    def test_fnc_uc(self):
        res=self.api.fnd_uc()
        logger.info(r"响应状态码： %s",res[0])
        assert res[0]==200
        logger.info(r"后天的相对湿度: %s"%(res[1],))

