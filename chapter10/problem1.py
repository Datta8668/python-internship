class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

d = Programmer("Datta", 3600000, 412105)
print(d.name, d.salary, d.pin, d.company)

r = Programmer("Raj", 2100000, 411034)
print(r.name, r.salary, r.pin, r.company)