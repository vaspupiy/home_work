class NotNumTypeError(Exception):
    def __init__(self, text):
        self.text = text


class OfficeEquipmentWarehouse:
    """Склад оргтехники, может помещать на склад: Ксерокс, Принтер и Сканер'"""

    def __init__(self, ):
        self.quantity_of_equipment = {'Ксерокс': {}, "Принтер": {}, "Сканер": {}, "Объем mm**3": [0, 200000000]}

    @staticmethod
    def valid_volume(equipment, quantity, quantity_of_equipment):
        if quantity_of_equipment["Объем mm**3"][0] + (equipment.width * equipment.height * equipment.depth * quantity)\
                <= quantity_of_equipment["Объем mm**3"][1]:
            return True
        print(f"{equipment.vendor} {equipment.model} в количестве {quantity} не помещается на склад")

    @staticmethod
    def check_office_equipment(equipment):
        """Проверяет класс объекта"""
        if not isinstance(equipment, OfficeEquipment):
            print(f'Внимание! {equipment} не принята на склад, так как не является оргтехникой')
        else:
            return True

    @staticmethod
    def valid_num(equipment, quantity):
        """Проверяет является ли тип данных числовым"""
        try:
            if isinstance(quantity, str):
                raise NotNumTypeError(f"Ошибка ввода! количество устройств {equipment.vendor} {equipment.model}, "
                                      f"указано строковым типом данных. Данная техника не была учтена.")
            if int(quantity) <= 0:
                raise NotNumTypeError(f"Ошибка ввода! количество устройств {equipment.vendor} {equipment.model}, "
                                      f"должно быть больше 0. Данная техника не была учтена.")
        except NotNumTypeError as err:
            print(err)
            return False
        except TypeError:
            print(f"Ошибка ввода! количество устройств {equipment.vendor} {equipment.model},"
                  f"указано не верным типом данных. Данная техника не была учтена")
            return False
        else:
            return True

    def reception_of_equipments(self, equipments):
        """передача техники на склад"""
        for equipment, quantity in equipments.items():
            if OfficeEquipmentWarehouse.check_office_equipment(equipment) and \
                    OfficeEquipmentWarehouse.valid_num(equipment, quantity):
                if isinstance(equipment, Printer) and \
                        OfficeEquipmentWarehouse.valid_volume(equipment, quantity, self.quantity_of_equipment):
                    self.changing_the_warehouse(equipment, quantity, "Принтер")
                elif isinstance(equipment, Scanner) and \
                        OfficeEquipmentWarehouse.valid_volume(equipment, quantity, self.quantity_of_equipment):
                    self.changing_the_warehouse(equipment, quantity, "Сканер")
                elif isinstance(equipment, Copier) and \
                        OfficeEquipmentWarehouse.valid_volume(equipment, quantity, self.quantity_of_equipment):
                    self.changing_the_warehouse(equipment, quantity, "Ксерокс")
                else:
                    print(f"{equipment.vendor} {equipment.model} в количестве {quantity} - не принят на склад!")

    def send_to_department(self, equipments):
        """передача техники со склада в отделы"""
        for equipment, quantity in equipments.items():
            if OfficeEquipmentWarehouse.check_office_equipment(equipment) and \
                    OfficeEquipmentWarehouse.valid_num(equipment, quantity):
                if isinstance(equipment, Printer):
                    self.changing_the_warehouse(equipment, -quantity, "Принтер")
                elif isinstance(equipment, Scanner):
                    self.changing_the_warehouse(equipment, -quantity, "Сканер")
                elif isinstance(equipment, Copier):
                    self.changing_the_warehouse(equipment, -quantity, "Ксерокс")
                else:
                    print(f"техника {equipment.vendor} {equipment.model} - на складе отсутствует")

    def changing_the_warehouse(self, equipment, quantity, type_equipment):
        """ Учет техники на складе, (сообщает, если кол-во на складе меньше запрошенного) """
        if (equipment.vendor, equipment.model) in self.quantity_of_equipment[type_equipment]:
            if self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] + quantity > 0:
                self.quantity_of_equipment["Объем mm**3"][0] += (
                            equipment.width * equipment.height * equipment.depth * quantity)
                self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] += quantity
            elif self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] + quantity == 0:
                self.quantity_of_equipment["Объем mm**3"][0] += (
                        equipment.width * equipment.height * equipment.depth * quantity)
                del self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]
            else:
                print(
                    f"{equipment.vendor} {equipment.model} - запрошено {-quantity},  на складе "
                    f"{self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]}. "
                    f"Выданно: {self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]}"
                    f" не хватило: "
                    f"{abs(self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] + quantity)}"
                )
                self.quantity_of_equipment["Объем mm**3"][0] += (
                        equipment.width * equipment.height * equipment.depth *
                        -self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model])
                del self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]
        else:
            if quantity > 0:
                self.quantity_of_equipment["Объем mm**3"][0] += (
                        equipment.width * equipment.height * equipment.depth * quantity)
                self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] = quantity
            else:
                print(f"{equipment.vendor} {equipment.model} - запрошено {-quantity} - отсутствует на складе")


class OfficeEquipment:
    """Оргтехника: vendor - Производитель; model - модель ,size_str - Габариты (ШхВхГ)"""

    def __init__(self, vendor, model, size_str):
        self.vendor = vendor
        self.model = model
        self.on_off = False
        self.width, self.height, self.depth = self.size(size_str)

    @classmethod
    def size(cls, size_str):
        return map(int, size_str.split('x'))

    def turn_power_grid(self, on_off=1):
        """Подключение к электросети"""
        if isinstance(on_off, int) and int(on_off) == 0 or int(on_off) == 1:
            self.on_off = on_off


class Printer(OfficeEquipment):
    """Принтер"""

    def print(self):
        if self.on_off:
            print(f"{self.vendor} {self.model} чепятает")
        else:
            print(f"{self.vendor} {self.model} не подключен к эл. сети")


class Scanner(OfficeEquipment):
    """Сканер"""

    def scan(self):
        if self.on_off:
            print(f"{self.vendor} {self.model} сканирует")
        else:
            print(f"{self.vendor} {self.model} не подключен к эл. сети")


class Copier(OfficeEquipment):
    """Ксерокс"""

    def copy(self):
        if self.on_off:
            print(f"{self.vendor} {self.model} копирует")
        else:
            print(f"{self.vendor} {self.model} не подключен к эл. сети")


cop_1 = Copier("Xerox", "Phaser 3020BI", "324x15x215")
cop_2 = Copier("Xerox", "Phaser 6020", "331x188x215")
sk_1 = Scanner("Epson", "Perfection V19", "431x388x215")
sk_2 = Scanner("Canon", "CanoScan LiDE 300", "231x188x215")
pr_1 = Printer("HP", "LaserJet Pro M15w", "331x188x345")
pr_2 = Printer("Epson", "L120", "51x118x215")
po_1 = "Кукуруза"
po_2 = OfficeEquipment('logitech', 'K 120', "331x18x15")
warehouse = OfficeEquipmentWarehouse()

print()
print("Первое поступление на склад")
warehouse.reception_of_equipments({cop_1: 1, cop_2: 3, sk_1: 2, sk_2: 1, pr_1: 4, po_2: 1})  # Передали на склад
print("Проверка свободного объема на складе")
print(warehouse.quantity_of_equipment["Объем mm**3"])
print()
print("Второе поступление на склад")
warehouse.reception_of_equipments({cop_1: 1, sk_2: 20, pr_1: -1, sk_1: "2", po_1: 45})  # Передали на склад
print("Проверка свободного объема на складе")
print(warehouse.quantity_of_equipment["Объем mm**3"])
print()
print("Проверка техники на складе")
print(warehouse.quantity_of_equipment)
print()
print("Первое поступление в подразделение")
warehouse.send_to_department({cop_1: 1, sk_2: 2, pr_1: 9, pr_2: 1, po_2: 1})  # Передали в подразделение
print("Проверка свободного объема на складе")
print(warehouse.quantity_of_equipment["Объем mm**3"])
print()
print("Второе поступление в подразделение")
warehouse.send_to_department({cop_1: 1, sk_2: "уук", pr_1: 10, pr_2: [1]})  # Передали в подразделение
print("Проверка свободного объема на складе")
print(warehouse.quantity_of_equipment["Объем mm**3"])
print()
print("Проверка техники на складе")
print(warehouse.quantity_of_equipment)
print()
print("Проверка Сканеров на складе")
print(warehouse.quantity_of_equipment['Сканер'])
