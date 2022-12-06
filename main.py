

class RCCheck:
    def __init__(self, id_number):
        self.id_number = id_number
        self.validity_info = {
            "Contains slash": None,
            "Pre-1954": None,
            "Valid length": None,
            "Is all digits": None,
            "Valid month": None,
            "Real month": None,
            "Valid day": None,
            "Gender": None,
            "Valid checksum": None
        }
        self.check_all()

    def check_all(self):
        self.check_slash()
        if self.validity_info["Contains slash"] is None:
            print("Rodné číslo má špatně napsané lomítko.")
            return
        self.check_len()
        self.check_digits()
        self.check_month()
        self.check_day()
        self.checksum()
        self.print_info()

    def print_info(self):
        for key, item in self.validity_info.items():
            print(f"{key}: {item}")

    def check_slash(self):
        for char_num in range(len(id_number)):
            if char_num != 6 and id_number[char_num] == "/":
                return
            elif char_num == 6 and id_number[char_num] == "/":
                self.validity_info["Contains slash"] = True
        if not self.validity_info["Contains slash"]:
            self.validity_info["Contains slash"] = False

    def check_len(self):
        if self.validity_info["Contains slash"]:
            if len(id_number) == 10:
                print(f"Rodné číslo {id_number} má správnou délku před rokem 1954.")
                self.validity_info["Pre-1954"] = True
                self.validity_info["Valid length"] = True
            elif len(id_number) == 11:
                print(f"Rodné číslo {id_number} má správnou délku po roce 1954.")
                self.validity_info["Pre-1954"] = False
                self.validity_info["Valid length"] = True
            else:
                print(f"Rodné číslo {id_number} nemá správnou délku.")
                self.validity_info["Valid length"] = False
        else:
            if len(id_number) == 9:
                print(f"Rodné číslo {id_number} má správnou délku před rokem 1954.")
                self.validity_info["Pre-1954"] = True
                self.validity_info["Valid length"] = True
            elif len(id_number) == 10:
                print(f"Rodné číslo {id_number} má správnou délku po roce 1954.")
                self.validity_info["Pre-1954"] = False
                self.validity_info["Valid length"] = True
            else:
                print(f"Rodné číslo {id_number} nemá správnou délku.")
                self.validity_info["Valid length"] = False

    def check_digits(self):
        self.validity_info["Is all digits"] = True
        for char_num in range(len(self.id_number)):
            if not id_number[char_num].isdigit():
                if not (self.validity_info["Contains slash"] and char_num == 6):
                    self.validity_info["Is all digits"] = False

    def check_month(self):
        month = int(self.id_number[2:4])
        if month in range(1, 13):
            self.validity_info["Valid month"] = True
            self.validity_info["Gender"] = "Male"
            self.validity_info["Real month"] = month
        elif month in range(21, 33):
            self.validity_info["Valid month"] = True
            self.validity_info["Gender"] = "Male"
            self.validity_info["Real month"] = month - 20
        elif month in range(51, 63):
            self.validity_info["Valid month"] = True
            self.validity_info["Gender"] = "Female"
            self.validity_info["Real month"] = month - 50
        elif month in range(71, 83):
            self.validity_info["Valid month"] = True
            self.validity_info["Gender"] = "Female"
            self.validity_info["Real month"] = month - 70
        else:
            self.validity_info["Valid month"] = False

    def check_day(self):
        year = int(self.id_number[:2])
        day = int(self.id_number[4:6])
        long_months = {1, 3, 5, 7, 8, 10, 12}
        short_months = {4, 6, 9, 11}
        if self.validity_info["Real month"] in long_months:
            if day in range(1, 32):
                self.validity_info["Valid day"] = True
            else:
                self.validity_info["Valid day"] = False
        elif self.validity_info["Real month"] in short_months:
            if day in range(1, 31):
                self.validity_info["Valid day"] = True
            else:
                self.validity_info["Valid day"] = False
        else:
            if day in range(1, 29):
                self.validity_info["Valid day"] = True
            elif day == 29 and year % 4 == 0:
                self.validity_info["Valid day"] = True
            else:
                self.validity_info["Valid day"] = False

    def checksum(self):
        if self.validity_info["Pre-1954"]:
            print("Rodná čísla před rokem 1954 nemají kontrolní číslici")
            return
        if self.validity_info["Contains slash"]:
            id_num = self.id_number.replace("/", "")
        else:
            id_num = self.id_number

        odds, evens = [], []
        for i in range(len(id_num)-1):
            if i % 2 == 0:
                evens.append(int(id_num[i]))
            else:
                odds.append(int(id_num[i]))
        if (sum(odds) - sum(evens) + int(id_num[9])) % 11 == 0:
            print("Kontrolní číslice je správná, rodné číslo je validní")
            self.validity_info["Valid checksum"] = True
        else:
            self.validity_info["Valid checksum"] = False
            print("Rodné číslo není validní")


id_number = "736028/5163"
r = RCCheck(id_number)
