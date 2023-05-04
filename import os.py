import os
os.system('cls' if os.name=="nt" else 'clear')


def print_type(data_list):
    for data in data_list:
        print(f"{data} is {type(data)}")
        
class Person:
 def say_hello(name, username):
        return f"Hello {name} {username}"
    
def say_age(age):
        return f"I am {age} years old"


print_type([
    1,
    1.1,
    "1",
    True,
    None,
    [1, 2, 3],
])
class Person:
    name = 'Selim'
    surname = 'Has'

    def test(self):
        print(self.name + ' ' + self.surname)
   

# __x = 'x'

# def call_x(self):
#         return self.__x
        