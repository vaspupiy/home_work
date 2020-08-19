class NotNumTypeError(Exception):
    def __init__(self, text):
        self.text = text


def valid_num(equipment, quantity):
    try:
        if isinstance(quantity, str):
            raise NotNumTypeError(f"Ошибка ввода! количество устройств , "
                                  f"указано строковым типом данных. Данная техника не была учтена.")
        float(quantity)
    except NotNumTypeError as err:
        print(err)
        return False
    except TypeError:
        print(f"Ошибка ввода! количество устройств ,"
              f"указано не верным типом данных. Данная техника не была учтена")
        return False
    else:
        return True


equipment = [1, 3]
print(valid_num(equipment, ["quantity"]))


class MyClass:
   def __init__(self, param_1, param_2):
       self.param_1 = param_1
       self.param_2 = param_2

   def __str__(self):
       return f"Объект с параметрами ({self.param_1}, {self.param_2})"


mc = MyClass("text_1", "text_2")
print(mc)