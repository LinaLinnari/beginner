# sentence = input()
# print(sentence[-1])
##################
# times = int(input('How many times should I say "Hello"?'))
# for i in range(times):
#     print('Hello!')
##############################
# string = ""
# for i in range(1, 58, 4):
#     string += "&" * i
# 
# print(len(string))
################################
# total = 0
# for _ in range(n):
#     total += int(input())
# print(total / n)
#############################

# string = "red yellow fox bite orange goose beeeeeeeeeeep"
# vowels = 'aeiou'
# counter = 0
# for i in vowels:
#     counter += string.count(i)
# print(counter)
################
# string = "red yellow fox bite orange goose beeeeeeeeeeep"
# vowels = 'aeiou'
# a = 0
# for char in string:
#     if char in vowels:
#         a += 1
# print(a)
#############################
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
###############################
#
# a = int(input())
# b = int(input())
# counter = 0
# summ = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         summ += i
#         counter += 1
# print(summ / counter)
##################################
# numbers = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
# tele = input()
#
# for char in tele:
#     print(numbers[char])
######################
# number = input()
# words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#
# for n in number:
#     print(words[int(n)])
########################

# def romrob(num):
#     if num % 7 == 0:
#         print(num * num)
#
#
# inputs = int(input())
#
# for _ in range(0, inputs):
#     n = int(input())
#     romrob(n)
#######################
# a = float(input())
# b = float(input())
# operations = input()
#
# if operations in ('+', '-', '*', '/', "mod", "pow", "div"):
#
#     if operations == '+':
#         print('%.2f + %.2f = %.2f' % (a, b, a + b))
#
#     elif operations == '-':
#         print('%.2f - %.2f = %.2f' % (a, b, a - b))
#
#     elif operations == '*':
#         print('%.2f * %.2f = %.2f' % (a, b, a * b))
#
#     elif operations == '/':
#         if b != 0:
#             print('%.2f / %.2f = %.2f' % (a, b, a / b))
#         else:
#             print("Division by 0!")
#     elif operations == 'mod':
#         if b != 0:
#             print('%.2f mod %.2f = %.2f' % (a, b, a % b))
#         else:
#             print("Division by 0!")
#     elif operations == 'pow':
#         if b != 0:
#             print('%.2f pow %.2f = %.2f' % (a, b, a ** b))
#         else:
#             print("Division by 0!")
#     elif operations == 'div':
#         if b != 0:
#             print('%.2f div %.2f = %.2f' % (a, b, a // b))
#         else:
#             print("Division by 0!")
####################################

# def snake_case(j):
#     out = []
#     step = 0
#     for i in j:
#         if i.isupper() and step == 0:
#             out.append(i.lower())
#         elif i.isupper():
#             out.append('_')
#             out.append(i.lower())
#         else:
#             out.append(i)
#         step += 1
#     return ''.join(out)
#
#
# s = input()
# print(snake_case(s))
########################################################
# nums = [x * 2 for x in range(11) if x % 2 == 1]
# print(nums)
# work with a list from this variable
##########################
# numbers = [int(n) for n in input()]
# less_than_5 = [x for x in numbers if x < 5]
# greater_than_5 = [x for x in numbers if x > 5]
# print(less_than_5)
# print(greater_than_5)
#################################
# words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
#          "apothecary"]
#
# wordslen = [len(word) for word in words]
#
# print(wordslen)
###########################
# list_of_strings =['10', '100', '1000', '10000']
# list_of_stringsn = [int(num) + 1 for num in list_of_strings]
# print(list_of_stringsn)
########################
# sm: int = 0
#
#
# def my_summ(n):
#     sm += n
#     return sm


a = [1, 2, 3]
b = [a[0] + (a[1] + item) for num, item in enumerate(a)]


print(b)