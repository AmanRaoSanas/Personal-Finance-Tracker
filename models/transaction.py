class Transaction:
    def __init__(self,amount, category, date, note=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return(f"{self.amount} {self.category} {self.date} {self.note}")