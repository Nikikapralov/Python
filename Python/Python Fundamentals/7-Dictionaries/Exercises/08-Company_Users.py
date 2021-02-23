class CompaniesDatabase:
    def __init__(self):
        self.dict_companies_employees = {}
        self.filling_the_dict()

    def filling_the_dict(self):
        while True:
            command = input()
            if command == 'End':
                print(self.print_output())
                break
            company_name, employee_id = command.split(' -> ')
            if company_name not in self.dict_companies_employees:
                self.dict_companies_employees[company_name] = [employee_id]
            else:
                if employee_id in self.dict_companies_employees[company_name]:
                    continue
                else:
                    self.dict_companies_employees[company_name].append(employee_id)
        return

    def print_output(self):
        result = ''
        for name, employees in sorted(self.dict_companies_employees.items(), key=lambda x: x[0]):
            result += f'{name}\n'
            for employee in employees:
                result += f'-- {employee}\n'
        return result


database_1 = CompaniesDatabase()
