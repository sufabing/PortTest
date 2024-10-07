# 课程模块接口封装：核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用
import requests
import config

# 导包

#创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        self.url_add_course = config.BASE_URL + '/api/clues/course'

    # 课程添加
    def add_course(self,test_data,token):
        return requests.post(self.url_add_course, json=test_data,headers={"Authorization": token})

    # 查询课程列表
    def select_course(self, test_data, token):
        return requests.get(url=self.url_select_course + f"/{test_data}", headers={"Authorization": token})

    # 修改课程
    def update_course(self, test_data, token):
        return requests.put(url=self.url_add_course, json=test_data, headers={"Authorization": token})

    # 删除课程
    def delete_course(self, course_id, token):
        return requests.delete(url=self.url_add_course + f"/{course_id}", headers={"Authorization": token})