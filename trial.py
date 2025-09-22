class Employee:
    def __init__(self, name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
    
    def calculate_salary(self):
        self.salary = self.salary
        return self.salary

class PartTime(Employee):
    hourly_rate = 20  # Assuming $20 per hour for part-time employees
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.salary = self.hours_worked * self.hourly_rate
        return self.salary

class FullTime(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def calculate_salary(self):
        # Assuming full-time employees have a fixed salary
        return self.salary

class ContractEmployee(Employee):
    def __init__(self, name, age, salary, contract_duration,contract_fee):
        super().__init__(name, age, salary)
        self.contract_duration = contract_duration  # in months
        self.contract_fee = contract_fee  # Assuming a fixed fee for the contract

        def calculate_salary(self):
            self.salary = self.contract_fee / self.contract_duration
            return self.salary
        
# Example usage:
employee1 = PartTime("John Doe", 30, 1000, 40)
employee2 = FullTime("Jane Smith", 25, 5000)
employee3 = ContractEmployee("Alice Johnson", 35, 2000, 6, 500)

employee1.display_details()
employee2.display_details()
employee3.display_details()
    
