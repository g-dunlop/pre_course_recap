number_1 = 3
number_2 = 10
number_3 = 15
number_4 = "25"
string_1 = "hello"
string_2 = "there"

def addition (num1, num2):
    print(int(num1) + int(num2))
addition(number_1, number_4)

def what_type(thing):
    print(type(thing))
what_type("cat")
what_type(True)
what_type(0.5)

def make_sentence(item1, item2):
    print(item1.capitalize() + " " + item2 + ".")
make_sentence(string_1, string_2)

