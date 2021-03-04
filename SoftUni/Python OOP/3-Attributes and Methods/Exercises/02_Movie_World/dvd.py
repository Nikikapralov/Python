import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month: str, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) ' \
               f'has age restriction {self.age_restriction}. ' \
               f'Status: {"rented" if self.is_rented else "not rented"}'

    @staticmethod
    def get_date_string(date):
        day, month, year = date.split('.')
        format = datetime.date(int(year), int(month), int(day))
        return format.strftime("%B"), year

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        creation_month, creation_year = cls.get_date_string(date)
        return cls(name, id, creation_year, creation_month, age_restriction)










