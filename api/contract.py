# URL： http://kdtx-test.itheima.net/api/common/upload
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  " multipart/form-data ",  "Authorization":  "xxx " }
# 请求体：{" file " : 合同文件"}
import requests
import config

# 接口信息：
# 新增合同：
# 地址：http://kdtx-test.itheima.net/api/contract
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  "application/json ",  "Authorization":  "xxx " }
# 请求体：{ "name": "测试888", "phone": "13612345678", "contractNo": "HT10012003", "subject": "6", "courseId": " 99", "channel": "0", "activityId": 77, "fileName": "xxx"}


# 导包

# 创建接口类
class ContractAPI:
    # 初始化
    def __init__(self):
        self.url_upload = config.BASE_URL + '/api/common/upload'
        self.url_add_contract = config.BASE_URL + '/api/contract'
    # 合同上传接口
    def upload_contract(self, test_data,token):
        return requests.post(url=self.url_upload,files={"file": test_data},headers={'Authorization': token})

    # 新增合同
    def add_contract(self, test_data,token):
        return requests.post(url=self.url_add_contract,json=test_data,headers={'Authorization': token})