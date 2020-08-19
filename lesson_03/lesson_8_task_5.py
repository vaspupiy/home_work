class OfficeEquipmentWarehouse:
    """Склад оргтехники, может помещать на склад: Ксерокс, Принтер и Сканер'"""

    def __init__(self,):
        self.quantity_of_equipment = {'Ксерокс': {}, "Принтер": {}, "Сканер": {}}

    def reception_of_equipments(self, equipments):
        """передача техники на склад"""
        for equipment, quantity in equipments.items():
            if isinstance(equipment, Printer):
                self.changing_the_warehouse(equipment, quantity, "Принтер")
            elif isinstance(equipment, Scanner):
                self.changing_the_warehouse(equipment, quantity, "Сканер")
            elif isinstance(equipment, Copier):
                self.changing_the_warehouse(equipment, quantity, "Ксерокс")
            else:
                print(f"{equipment} - неизвестный  тип техники, не принят на склад!")

    def send_to_department(self, equipments):
        """передача техники со склада в отделы"""
        for equipment, quantity in equipments.items():
            if isinstance(equipment, Printer):
                self.changing_the_warehouse(equipment, -quantity, "Принтер")
            elif isinstance(equipment, Scanner):
                self.changing_the_warehouse(equipment, -quantity, "Сканер")
            elif isinstance(equipment, Copier):
                self.changing_the_warehouse(equipment, -quantity, "Ксерокс")
            else:
                print(f"техника {equipment} - на складе отсутствует")

    def changing_the_warehouse(self, equipment, quantity, type_equipment):
        """ Учет техники на складе, (сообщает, если кол-во на складе меньше запрошенного) """
        if (equipment.vendor, equipment.model) in self.quantity_of_equipment[type_equipment]:
            if self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] + quantity > 0:
                self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] += quantity
            elif self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] + quantity == 0:
                del self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]
            else:
                print(f"{equipment.vendor} {equipment.model} - запрошено {-quantity},  на складе "
                      f"{self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model]}. "
                      f"Техника не выдана")
        else:
            if quantity > 0:
                self.quantity_of_equipment[type_equipment][equipment.vendor, equipment.model] = quantity
            else:
                print(f"{equipment.vendor} {equipment.model} - запрошено {-quantity} - отсутствует на складе")


class OfficeEquipment:
    """Оргтехника"""

    def __init__(self, vendor, model):
        self.vendor = vendor
        self.model = model
        self.on_off = False

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


cop_1 = Copier("Xerox", "Phaser 3020BI")
cop_2 = Copier("Xerox", "Phaser 6020")
sk_1 = Scanner("Epson", "Perfection V19")
sk_2 = Scanner("Canon", "CanoScan LiDE 300")
pr_1 = Printer("HP", "LaserJet Pro M15w")
pr_2 = Printer("Epson", "L120")
po_1 = "Кукуруза"
warehouse = OfficeEquipmentWarehouse()
warehouse.reception_of_equipments({cop_1: 1, cop_2: 3, sk_1: 2, sk_2: 1, pr_1: 4})  # Передали на склад
warehouse.reception_of_equipments({cop_1: 1, sk_2: 2, pr_1: 1})  # Передали на склад
warehouse.send_to_department({cop_1: 1, sk_2: 2, pr_1: 10, pr_2: 1, po_1: 3})  # Передали в подразделение
print(warehouse.quantity_of_equipment)
print(warehouse.quantity_of_equipment['Сканер'])
