import datetime

class Tests:
    def __init__(self):
        self.pc = datetime.date(year=2024, month=4, day=10)
        self.ac = datetime.date(year=2024, month=4, day=11)

    def all_tests(self):
        next_texts = f"Prova de PC no dia {self.pc.strftime('%d/%m')} e de AC no dia {self.ac.strftime('%d/%m')}"
        return next_texts
