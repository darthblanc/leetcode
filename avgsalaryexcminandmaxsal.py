def average(salary):
    maximum = max(salary)
    minimum = min(salary)
    salary = list(filter(lambda x: x != maximum, salary))
    salary = list(filter(lambda x: x != minimum, salary))
    size = len(salary)
    sumtotal = sum(salary)
    avg = sumtotal/size
    return avg


# n = [4000, 3000, 1000, 2000]
n = [48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000, 93000, 77000, 33000, 28000, 4000, 54000,
     67000, 6000, 1000, 11000]
print(average(n))
