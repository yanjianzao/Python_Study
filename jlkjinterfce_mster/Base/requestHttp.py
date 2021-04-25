import requests
import os,sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jlkjinterfce_mster.Common import handldconfig
url_test = 'https://gatewaytest.jinlingkeji.cn/v9'
get_code_path = handldconfig.hand_config().read_config(section_name='App',key_name='get_code',filename="requestpath.ini")
login_path = handldconfig.hand_config().read_config(section_name='App',key_name='login',filename="requestpath.ini")
# res = requests.get(url=url_test+get_code_path,params={'phone': '17677355052'})
# print(res.text)
app_token = handldconfig.hand_config().read_config(section_name="App",key_name="token",filename="../Common/config.ini")
handleapp = {
    "Host":"gatewaytest.jinlingkeji.cn",
    "Connection": "keep-alive",
    "Content type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-cn",
    "User-Agent":"%E7%BD%91%E4%B8%8A%E8%80%81%E5%B9%B4%E5%A4%A7%E5%AD%A6/2.8 CFNetwork/1128.0.1 Darwin/19.6.0",
    "app-version":"2.3.0",
    "source-type": "IOS",
    "Authorization":app_token
}
date = {
    "phone":"17677355052",
    "code":"8888"
}
# res = requests.get(url=url_test+login_path,params=date,headers=handleapp)
# handldconfig.hand_config().set_config(section_name='App',key_name='token',filename="../Common/config.ini",update_value=res.json()['data'])
# print(handleapp)
res2 = requests.post(url='https://gatewaytest.jinlingkeji.cn/v9/message/live/hot/list',json={"pageSize": "8","pageNum": "1","type": "1"},headers=handleapp)
print(res2.text)
