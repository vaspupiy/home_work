class OfficeEquipmentWarehouse:
    """Склад оргтехники"""


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
cop_1.turn_power_grid(1)
cop_1.copy()
cop_2 = Copier("Xerox", "Phaser 6020")
cop_2.copy()
print()
sk_1 = Scanner("Epson", "Perfection V19")
sk_1.turn_power_grid(1)
sk_1.scan()
sk_2 = Scanner("Canon", "CanoScan LiDE 300")
sk_2.scan()
print()
pr_1 = Printer("HP", "LaserJet Pro M15w")
pr_1.turn_power_grid(1)
pr_1.print()
pr_2 = Printer("Epson", "L120")
pr_2.print()

