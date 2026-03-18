from faker.proxy import Faker


class DataGenerator:
    faker = Faker()

    @classmethod
    def name(cls):
        return cls.faker.user_name()

    @classmethod
    def password(cls):
        return cls.faker.password()

    @classmethod
    def job_title(cls):
        return cls.faker.job()

    @classmethod
    def rand_text(cls):
        return cls.faker.text(50)