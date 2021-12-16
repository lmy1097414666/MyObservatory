import logging

import requests
import urllib3

logger=logging.getLogger()
class Base:
    #重构get方法，解决ssl：certificate_verify_failed

    def __init__(self,disable_ssl_verify=False, timeout=60):

        self.timeout = timeout
        self.disable_ssl_verify = disable_ssl_verify
        if self.disable_ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def Get(self, url, headers=None, data=None, json=None, params=None,*args, **kwargs):
        logger.info("请求方式：Get")
        logger.info(r"请求的url: %s",url)
        if headers is None:
            headers = {}
        if self.disable_ssl_verify:
            response = requests.get(url, headers=headers, data=data, json=json, params=params
                                       , verify=False, timeout=self.timeout, *args, **kwargs)
        else:
            response = requests.get(url, headers=headers, data=data, json=json, params=params
                                    ,  timeout=self.timeout, *args, **kwargs)
        logger.info(r"未处理的响应：%s",response.text)

        return response