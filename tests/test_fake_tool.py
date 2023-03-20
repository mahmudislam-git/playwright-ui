from utils.faker import generate_personal_info


def test_generate_fake_data():
    personal_info = generate_personal_info()
    print(personal_info['first_name'])
    print(personal_info['last_name'])
    print(personal_info['phone_number'])
