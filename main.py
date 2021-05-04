# bot

# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')

# your_name = input('пиши тут >')
# print('What a great name you have,', your_name + '!')


# n = int(input())
# a = n + n
# print(a)
# a = a * n
# print(a)
# a = a - n
# print(a)
# a = a // n
# print(a)
# days = int(input())
# total_food = int(input())
# one_way_flight = int(input())
# cost_of_one_night = int(input())
# sum_vacation_food = total_food * days
# sum_flight = 2 * one_way_flight
# hotel = (days - 1) * cost_of_one_night
# print(sum_vacation_food + sum_flight + hotel)

# first, second, third = int(input()), int(input()), int(input())
# print((first // 2 + first % 2) + (second // 2 + second % 2) + (third // 2 + third % 2))
# three_digit_integer = int(input())
# a = three_digit_integer // 100
# b = three_digit_integer // 10 % 10
# c = three_digit_integer % 10
# print(a + b + c)
# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')
#
# name = input('>')
#
# print('What a great name you have, ' + name + '!')
# print('Let me guess your age.')
# print('Enter remainders of dividing your age by 3, 5 and 7.')
# remainder3 = int(input('>'))
# remainder5 = int(input('>'))
# remainder7 = int(input('>'))
# age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
#
# print("Your age is " + str(age) + "; that's a good time to start programming!")

# print(2 ** 3 % 20)

# truthy_integer = False or False and True
# print(truthy_integer)
# tricky = not 10
# print(tricky)
# a = int(input('>'))
# b = int(input('>'))
# c = int(input('>'))
# r = a < b < c
# print(r)
# number_of_halls = int(input())
# capacity = int(input())
# number_of_viewers = int(input())
# visit = (number_of_halls * capacity) >= number_of_viewers
# print(visit)
# a = int(input())
# b = int(input())
# if (a / b) % 2 == 1:
#     print(True)
# else:
#     print(False)
# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"
# ingri = input()
# if ingri in pasta:
#     print("pasta time!")
# if ingri in apple_pie:
#     print("apple pie time!")
# if ingri in ratatouille:
#     print("ratatouille time!")
# if ingri in chocolate_cake:
#     print("chocolate cake time!")
# if ingri in omelette:
#     print("omelette time!")
# amount = 1000
# interest_rate = 5
# years = 1
# a = (1000 / 100 ) * 5
# income = a
# print(income)
# counter = 0
# step = 0
# while counter <= 25:
#     counter += 3
#     step += 1
# print(counter)
# print(step)
# initial_quantity_of_atoms = int(input())
# final_quantity = int(input())
# periods = 0
# while initial_quantity_of_atoms > final_quantity:
#     initial_quantity_of_atoms //= 2     #initial_quantity_of_atoms = initial_quantity_of_atoms // 2
#     periods += 1
# print(periods * 12)
# sum_d = int(input())
# years = 0
# while sum_d < 700000:
#     sum_d = ((sum_d / 100 * 7.1) + sum_d)
#     years += 1
# print(years)
# i = 1
# while i <= 20:
#     if i == 1:
#         print(i)
#     else:
#         j = i * i
#         print(j)
#     i += 1
# i = 0
# a = 'a'
# while i < 8:
#     a *= 2
#     i += 1
# print (len (a))
# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')
#
# name = input()
#
# print('What a great name you have, ' + name + '!')
# print('Let me guess your age.')
# print('Enter remainders of dividing your age by 3, 5 and 7.')
#
# rem3 = int(input())
# rem5 = int(input())
# rem7 = int(input())
#
# age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
#
# print("Your age is " + str(age) + "; that's a good time to start programming!")
# print('Now I will prove to you that I can count to any number you want.')
# number = int(input('>'))
# s = 0
# while s <= number:
#    print(str(s) + "!")
#    s += 1
# print('Completed, have a nice day!')
# hidden = list(input())
# print(len(hidden))
# name = ['Helen']
# print(name)
# a = int(input())
# b = int(input())
# c = int(input())
# s = 4 * (a + b + c)
# Ss = 2 * (a * b + b * c + a * c)
# V = a * b * c
# print(s)
# print(Ss)
# print(V)
# a = int(input())
# if a > 0:
#     print(True)
# else:
#     print(False)
# jack_age = int(input())
# alex_age = int(input())
# lana_age = int(input())
# print(min(jack_age, alex_age, lana_age))
# string = input()
# print(len(string))
# x = int(input())
# y = int(input())
# print(sum((x, y)))
# name = input()
# print("Hello, world! Hello, " + name)
# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return round(celsius, 3)
#
#
# c = fahrenheit_to_celsius(120)
#
# print(c)
#
#
# def closest_higher_mod_5(x):
#     step = 0
#     remainder = x % 5
#     if remainder == 0:
#         return x
#     else:
#         while remainder % 5 != 0:
#             remainder += 1
#             step += 1
#     return x + step
#
#
# def closest_higher_mod_5(x):
#     remainder = x % 5
#     if remainder == 0:
#         return x
#     return x + (5 - remainder)


# print(closest_higher_mod_5(4))
n = int(input())
value = ((n + 1) * n + 2) * n + 3
print(value)


