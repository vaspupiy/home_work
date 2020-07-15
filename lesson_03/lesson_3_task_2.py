def user_data(**kwargs):
    """Функция принимает несколько имнованных параметров и возвращает данные о пользователе одной строкой """
    r_name = {
        "name": "имя",
        "last_name": "фамилия",
        "years_of_birth": "год рождения",
        "city_of_residence": "город проживания",
        "email": "email",
        "phone_number": "телефон"
    }
    print(
        f'\nДанные о пользователе:  {r_name["name"]}: {kwargs["name"]}; '
        f'{r_name["last_name"]}: {kwargs["last_name"]}; '
        f'{r_name["years_of_birth"]}: {kwargs["years_of_birth"]}; '
        f'{r_name["city_of_residence"]}: {kwargs["city_of_residence"]}; '
        f'{r_name["email"]}: {kwargs["email"]}; '
        f'{r_name["phone_number"]}: {kwargs["phone_number"]}.'
    )
#   print(kwargs) #вместо всего этого огорода, но смущают нижние подчеркивания и {}... ну не нравится мне,почему-то...
#   return kwargs # если этот словарь был бы нужен где-то далее


user_data(name=input("Введите имя: "),
          last_name=input("Введите фамилию: "),
          years_of_birth=input("Введите год рождения: "),
          city_of_residence=input("Введите город проживания: "),
          email=input("Введите email: "),
          phone_number=input("Введите телефон: "))
