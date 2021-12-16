import json
import logging
import os
import yaml
from base.base import Base
logger=logging.getLogger()

dir_path=os.path.dirname(os.path.abspath(__file__))
env_file=os.path.join(dir_path,r"env.yml")
api_file=os.path.join(dir_path,r"api_data.yml")
class MyObservatoryApi:
    get_env=yaml.safe_load(open(env_file))
    host=get_env[get_env['default']]
    request=Base()
    def fnd_uc(self):
        get_fnduc = yaml.safe_load(open(api_file))['fnd_uc']
        url=f'{self.host}{get_fnduc}'
        respose=self.request.Get(url)       #发送请求
        respose_data=json.loads(respose.content.decode('utf-8'))
        logger.info(r"处理后的响应: %s",respose_data)
        relative_humidity=(respose_data['forecast_detail'][1]['min_rh'],respose_data['forecast_detail'][1]['max_rh'])   #获取相对湿度数据
        return respose.status_code,relative_humidity


# MyObservatoryApi().fnd_uc()