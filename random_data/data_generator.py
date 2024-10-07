import json
from faker import Faker

from CustomFaker import CustomProvider

fake = Faker(locale='zh-CN')
fake.add_provider(CustomProvider)

result = {
    "name": fake.name(),  # 生成名字，每次运行 生成不同的名字
    "contact": fake.address(),  # 生成随机地址
    "age": fake.random_int(18, 48),   # 生成随机年龄
    "gender": fake.random_element(elements=('男', '女')),  # 生成指定范围内随机的数据
    "推荐人ID": fake.db_user_id()
}

print(json.dumps(result,ensure_ascii=False))