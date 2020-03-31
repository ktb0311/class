class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent/100))
    
    def __repr__(self): #Вывод на экран
        return '[Person: %s, %s, %s]' % (self.name, self.job, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus = 10):
        Person.giveRaise(self, percent + bonus)

bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
tom = Manager('Tom Jones', pay = 150000)

if __name__ == '__main__': 
    print('--All there--')
    for obj in (bob, sue, tom):
        obj.giveRaise(10)
        print(obj)