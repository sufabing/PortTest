from faker.providers import BaseProvider


class CustomProvider(BaseProvider):
    def db_user_id(self):
        print(" ")
        return "数据库中关联的数据"