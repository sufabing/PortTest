# 需求：登录成功

# 导包
import requests

# 发送请求
url = 'https://kdtx-test.itheima.net/api/login'
header_data={'Content-Type': 'application/json'}
login_data = {'username': 'admin', 'password': 'HM_2023_test',"code":2,"uuid":"7e36e31806904dab81bbda64ac29aa01"}
response = requests.post(url=url,
                         headers=header_data,
                         json=login_data)

# 查看响应
print(response.status_code)
print(response.json())
