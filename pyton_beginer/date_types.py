# 8 основных типы данных

# 1) int - целый число тип данных :
#   a ) float - числа с плавающей запятой
#   b ) complex - числа с буквенным выражением (12345123n)
# 2) str - строковый тип данных - Строка
# 3) bool - булевый тип данных / логический (True/false)
# 4) list - список []
# 5) tuple - кортеж / неизменяемый список ()
# 6) set - множество {}
# 7) dist - словарь {}
# 8) NoneType - тип данных для обозначения отсуствие значения (None)

# Изменяемые (mutable) :
# list
# dist
# set

# print("") - функция для вывода терминала
""" print('Hello World')
name = input('Введите ваше имя: ')

print("Helo" ,name)


print("Привет")

str1 = 'Hello'
str2 = 'World'
print(str1 + str2)

frog = 'Quag'
print(frog * 3) # QuagQuagQuag 

Функции и методы строк  
greeting = "Good Evening"

print(len(greeting))
len(x) - возвращяет кол-во элементов """

# greeting = "Good Evening"
# print(dir(greeting)) 
# dir(x) - возвращяет список методов предонного объекта

# Метод - функция, принадлежащая определенному типу данных, и может быть вызвана только через объект 

""" my_str = 'Hello#World'
print(my_str.lower()) # hello#world
print(my_str.upper()) # HELLO#WORLD
print(my_str.replace('#', ' ')) # Hello World

my_str2 = '      hello world       '

my_str2.title() #Hello World
my_str2.capitalize() # Helo World
my_str2.count("l") # 3
print(my_str2.strip()) # Удаляет лишние пробелы
my_str2.lstrip()
my_str2.rstrip() 

my_str2 = '      hello world       '

print(my_str2.strip('!'))"""

my_str3 = "my new String"

""" my_str3.isalpha() # True
my_str3.isdigit() # False
my_str3.isalnum() # False
my_str3.startswith('M') # True
my_str3.endswith('M') # False


# in 
my_str4 = "Hello World"

print('Hello' in my_str4)

# 'Hello' in my_str4 #True

name = input('Имя: ')
party = input('Вечернинка: ')

invitel = 'Дорогой %s, приглашаем  тебя на %s' % (name,party)
print(invitel)
invite2 = 'Дорогой {a1}, приглашаем тебя на {b2}'.format(a1=name,b2=party)
print(invite2)
 """

name = input('Имя: ')
party = input('Вечернинка: ')
invine3 = f'Дорогой {name}, Приглашаем тебя на {party}'
print(invine3)

