import requests
import pytest
import unittest
import os,sys
import logging
import allure
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jlkjinterfce_mster.Common import handldconfig
url_test = 'https://gatewaytest.jinlingkeji.cn/v9'
date = {
    "phone":"17677355052",
    "code":"8888"
}
get_code_path = handldconfig.hand_config().read_config(section_name='App',key_name='get_code',filename="requestpath.ini")
login_path = handldconfig.hand_config().read_config(section_name='App',key_name='login',filename="requestpath.ini")
class TestCase():
    def setup_class(self):
        print("开始进行登录")
        self.res = requests.get(url=url_test + login_path, params=date)
        handldconfig.hand_config().set_config(section_name='App', key_name='token',filename=os.getcwd()+"\jlkjinterfce_mster\Common\config.ini",update_value=self.res.json()['data'])
        if self.res.json()['status'] == 200:
            print("登录成功")
    def teardown_class(self):
        print("teardown_class：所有用例执行之前，测试完成")

    log = logging.getLogger('test_class')
    log.info("aaa")
    def test_one(self):
        assert 1 == 1
        print("用例1是否成功")
    def test_two(self):
        assert 2 == 2
        print("用例2是否成功")










