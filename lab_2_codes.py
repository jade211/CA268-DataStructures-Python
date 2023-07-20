# QUESTION 1 -> Worked on by Jade Hudson and Sruthi Santhosh


class Email(object):
    def __init__(self, fname, lname, salary=0):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def get_email(self):
        self.email = self.fname + "." + self.lname + "@dcu.ie"
        return self.email




# QUESTION 2 -> Worked on by Jade Hudson and Sruthi Santhosh


class Person(object):
    def __init__(self, name, age=0, height=0, weight=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    
    def get_height(self):
        return f"{self.name} is {self.height}cm tall"
    
    def get_weight(self):
        return f"{self.name} is {self.weight}kg"




# QUESTION 3 -> Worked on by Jade Hudson and Sruthi Santhosh


class Class4(object):
    def __init__(self, fname, lname, age=0):
        self.fname = fname
        self.lname = lname
        self.age = age


def sort_class4(lst, info):
    info_lst = []
    for person in lst:
        if info == "fname":
            info_lst.append(person.fname)
        elif info == "lname":
            info_lst.append(person.lname)
        else:
            info_lst.append(person.age)
    return sorted(info_lst)


p1 = Class4('Barack', 'Obama', 40)
p2 = Class4('Abraham', 'Lincoln', 21)
p3 = Class4('Donald', 'Trump', 14)

print(sort_class4([p1, p2, p3], 'fname'))










# QUESTION 4 -> Worked on by Jade Hudson and Sruthi Santhosh


class Smoothie(object):
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.ingredient_d = {
            'Banana': 0.50,
            'Strawberries': 1.50,
            'Mango': 2.50,
            'Blueberries': 1.00,
            'Raspberries': 1.00,
            'Apple': 1.75,
            'Pineapple': 3.50
        }

    def get_cost(self):
        cost = 0
        for i in self.ingredient:
            if i in self.ingredient_d:
                cost = cost + self.ingredient_d[i]
        return "€{:.2f}".format(cost)

    def get_price(self):
        cost_pre = float(Smoothie.get_cost(self)[1:]) + 2.5
        return "€{:.2f}".format(cost_pre)
    
    def get_name(self):
        if len(self.ingredient) > 1:
            return" ".join(self.ingredient) + " Fushion"
        else:
            return " ".join(self.ingredient) + " Smoothie"


drink = Smoothie(['Banana', 'Mango'])
print(drink.get_cost())
print(drink.get_price())
print(drink.get_name() )




# QUESTION 5


class Pizza(object):
    order_num = []
    def __init__(self, ingredients=[], order_number=1):
        self.order_number = (order_number)
        self.ingredients = ingredients
        self.ingredient_d = {
            'Margherita': ("Red Tomatoes", "White Mozzarella", "Green Basil"),
            'Serrano': ("Black olives", "Red onion", "Cooked picadillo"),
            'Diavola': ("Mozzarella", "Spicy sausage", "Pomodorino tomatoes")
        }
        Pizza.order_num.append(self.ingredients)
        self.order_number = len(Pizza.order_num)

    def diavola():
        return Pizza(["Mozzarella", "Spicy sausage", "Pomodorino tomatoes"])
    
    def margherita():
        return Pizza(["Red Tomatoes", "White Mozzarella", "Green Basil"])
    
    def serrano():
        return Pizza(["Black olives", "Red onion", "Cooked picadillo"])


p1 = Pizza(['Black olives', 'Red onion', 'Meatballs'])
p2 = Pizza.diavola()

print(p1.order_number)
print(p2.ingredients)
print(p2.order_number)




# QUESTION 6


class Employee(object):
    def __init__(self, full_name, **extra_info):
        self.fullname = full_name
        self.firstname = (self.fullname.split(" "))[0]
        self.lastname = (self.fullname.split(" "))[1]
        for key, value in extra_info.items():
            self.__dict__[key] = value


tom = Employee('Tom Ford')
john = Employee('John Travolta', nationality='American')
jack = Employee('Jack Nicholson', nationality='American', age=84)

print(jack.age)
print(tom.firstname)
print(john.lastname)
