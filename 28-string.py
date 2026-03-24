#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the" +item)

#print("The {} jumped over the {}".format(animal,item)) #positional argument
#print("The {1} jumped over the {0}".format(animal,item))
#print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))#keyword argument
#print("The {1} jumped over the {1}".format(animal,item))

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#name = "Bro"
#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:>10}. Nice to meet you".format(name)) #right
#print("Hello, my name is {:<10}. Nice to meet you".format(name)) #left
#print("Hello, my name is {:^10}. Nice to meet you".format(name)) #middle

number = 1000

print("The nunber pi is {:.3f}".format(number))
print("The nunber pi is {:,}".format(number))
print("The nunber pi is {:b}".format(number))
print("The nunber pi is {:o}".format(number))
print("The nunber pi is {:X}".format(number))
print("The nunber pi is {:E}".format(number))
