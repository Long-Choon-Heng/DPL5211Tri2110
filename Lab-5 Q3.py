

def get_bonus(unit,salary):
    if(unit > 1000):
        bonus = salary * 0.2
    elif(unit>=501 and unit <=1000):
        bonus = salary * 0.1
    return bonus

def get_nett_salary(salary,bonus):
    nett = salary + bonus
    return nett

def display(id,salary,unit,bonus,nett_salary):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("               SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID     :",id)
    print("Staff salary : RM {:.2f}".format(salary))
    print("Units sold   :",unit)
    print("Bonus        : RM {:.2f}".format(bonus))
    print("Nett Salary  : RM {:.2f}".format(nett_salary))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
id = int(input("Enter staff id         : "))
salary = float(input("Enter staff salary     : RM "))
unit = int(input("Enter total units sold : "))

bonus = get_bonus(unit,salary)

nett_salary = get_nett_salary(salary,bonus)

display(id,salary,unit,bonus,nett_salary)
