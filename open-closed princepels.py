# فئة الأساس (Base Class)
class Employee:
    def calculate_salary(self):
            pass

# فئة الموظف بدوام كامل
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

# فئة الموظف بدوام جزئي
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# فئة الموظف بعقد
class ContractEmployee(Employee):
    def __init__(self, name, daily_rate, days_worked):
        self.name = name
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked
class freelancer(Employee) :
    def __init__(self,name,daily_rated,hour_worked):
        self.name = name
        self.daily_rated = daily_rated
        self.hour_worked = hour_worked 
    def calculate_salary(self):
        return  self.daily_rated*self.hour_worked 
    
# اختبار الفئات المختلفة
full_time_emp = FullTimeEmployee("Ahmed", 5000)
part_time_emp = PartTimeEmployee("Sara", 20, 100)
contract_emp = ContractEmployee("Ali", 150, 20)
freelancer_emp = freelancer("Laila", 30, 120)

print(f"Full-Time Employee Salary: {full_time_emp.calculate_salary()}")
print(f"Part-Time Employee Salary: {part_time_emp.calculate_salary()}")
print(f"Contract Employee Salary: {contract_emp.calculate_salary()}")
print(f"Freelancer Salary: {freelancer_emp.calculate_salary()}")
        
    