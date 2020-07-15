def user_data(**kwargs):
    """Функция принимает несколько имнованных параметров и возвращает словарь """

    return kwargs


user_data = user_data(имя=input("Введите имя: "),
                      last_name=input("Введите фамилию: "),
                      years_of_birth=input("Введите год рождения: "),
                      city_of_residence=input("Введите город проживания: "),
                      email=input("Введите email: "),
                      phone_number=input("Введите телефон: "))

print(list(user_data))
