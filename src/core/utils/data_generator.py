from faker.proxy import Faker


class DataGenerator:
    faker = Faker()

    @classmethod
    def name(cls):
        return cls.faker.user_name()

    @classmethod
    def password(cls):
        return cls.faker.password()
