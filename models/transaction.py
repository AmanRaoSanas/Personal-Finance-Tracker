class Transaction:
    def __init__(self,ammount, category, date, note=""):
        self.ammount = ammount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return(f"{self.ammount} {self.category} {self.date} {self.note}")