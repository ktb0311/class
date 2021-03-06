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

class Manager: #Применяем делегирование
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus = 10):
        self.person.giveRaise(percent + bonus)
    
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    
    def __repr__(self):
        return str(self.person)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMembers(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)        

if __name__ == '__main__': 
    
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    tom = Manager('Tom Jones', pay = 150000)
    
    development = Department(bob, sue)
    development.addMembers(tom)
    development.giveRaises(10)
    development.showAll()