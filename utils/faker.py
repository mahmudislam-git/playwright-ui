from faker import Faker


def generate_personal_info():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    return {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number}


