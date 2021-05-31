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
#         if b != 0.0:
#             print('%.2f / %.2f = %.2f' % (a, b, a / b))
#         else:
#             print("Division by 0!")
#     elif operations == 'mod':
#         print('%.2f mod %.2f = %.2f' % (a, b, a % b))
#     elif operations == 'pow':
#         if b != 0.0:
#             print('%.2f pow %.2f = %.2f' % (a, b, a ** b))
#         else:
#             print("Division by 0!")
#     elif operations == 'div':
#         if b != 0.0:
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
# n = input()
# n_int = [int(x) for x in n]
#
# result = []
# number = 0
#
# for i in n_int:
#     number += i
#     result.append(number)
# else:
#     print(result)
# ##
# numbers = [int(x) for x in input()]
# for index in range(1, len(numbers)):
#     numbers[index] += numbers[index - 1]
#
# print(numbers)
# ##
# n = [int(x) for x in input()]
# print([sum(n[0:x + 1]) if x >= 1 else n[0] for x in range(len(n))])
# ###################################
#
# print([int(num) for num in str(input()) if int(num) % 2])
# ###########
# user_input = input()
#
# odd_numbers = [int(i) for i in user_input if int(i) % 2 != 0]
#
# print(odd_numbers)
# ##########################
# text = ["function", "is", "a", "synonym", "of", "occupation"]
# words_tion = [word for word in text if word.endswith("tion")]
# print(words_tion)  # ["function", "occupation"]
#########
# words = ["apple", "pear", "banana", "Ananas"]
# word_a = [word for word in words if word.startswith(("a", "A"))]
# print(word_a)
###############################################
# my_numbers = [int(x) for x in input().split(" ")]
# odd_numbers = [i for i in my_numbers if i % 2 == 0]
# print(odd_numbers)
############################################
# old_list = [int(num) for num in input().split()]
# binary_list = [1 if num > 0 else 0 for num in old_list]
# print(binary_list)
###############################################
# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# days = [i // (60 * 60 * 24) for i in seconds]
# print(days)
#############################################
# digits_list = [float(x) for x in input()]
# print(sum(digits_list) / len(digits_list))
# Учитывая числовую последовательность на входе, создайте список, в котором каждое число будет цифрой из этой
# входной строки. Затем используйте этот список для вычисления среднего арифметического, то есть суммы всех
# цифр, деленной на их общее количество
##################################################
# nums = [x for x in range(1, 1001) if x % 3 == 0]
# print(nums)
###########################################
# vowels = 'aeiou'
# string = input()
# new_list = [each for each in string if each in vowels]
# print(new_list)
# Прочтите строку из ввода и распечатайте список гласных, принадлежащих этой строке.
########################################################
# a = input()
# print(a[0])
#####################################
# a = int(input())
# print(a * [[1, 2]])
#######################################
# str_1 = input()
# str_2 = input()
# str_3 = input()
# print([str_1, [str_2], [[str_3]]])
############################################
# numbers = [int(x) for x in input()]
# out = []
# for index in range(0, len(numbers) - 1):
#     out.append((numbers[index] + numbers[index + 1]) / 2)
# print(out)
#################################################
# els = [el for a in x for el in a if el > 0]
# тоже внизу
# for a in x:
#     for el in a:
#         if el > 0:
#             els.append(el)
################################################
# move = input()
# exec("game_matrix" + move)
# for row in game_matrix:
#     print(row)
#
# reference_matrix = [
#     game_matrix[0],
#     game_matrix[1],
#     game_matrix[2],
#     [i[0] for i in game_matrix],
#     [i[1] for i in game_matrix],
#     [i[2] for i in game_matrix],
#     [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
#     [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
# ]
# for item in reference_matrix:
#     result = list(set(item))
#     if len(result) == 1 and result[0] != None:
#         print("Game over!")
#         game_is_on = False
#         brea
#
# ##############
# incells = input('Enter cells: ')
#
# print("---------" + '\n' +
#       '|' + ' ' + incells[0] + ' ' + incells[1] + ' ' + incells[2] + ' ' + '|' + '\n'
#                                                                                  '|' + ' ' + incells[3] + ' ' + incells[
#           4] + ' ' + incells[5] + ' ' + '|' + '\n'
#                                               '|' + ' ' + incells[6] + ' ' + incells[7] + ' ' + incells[
#           8] + ' ' + '|' + '\n'
#       + "---------")
# if incells == "XXXOO__O_" or incells == "XOXOXOXXO":
#     print("X wins")
#
# elif incells == "XOOOXOXXO":
#     print("O wins")
#
#
# elif incells == "XOXOOXXXO":
#     print("Draw")
#
# elif incells == "XO_OOX_X_":
#     print("Game not finished")
#
# else:
#     print("Impossible")
# #########
# incells = input('Enter cells: ')
#
# print("---------" + '\n' +
#       '|' + ' ' + incells[0] + ' ' + incells[1] + ' ' + incells[2] + ' ' + '|' + '\n'
#                                                                                  '|' + ' ' + incells[3] + ' ' + incells[
#           4] + ' ' + incells[5] + ' ' + '|' + '\n'
#                                               '|' + ' ' + incells[6] + ' ' + incells[7] + ' ' + incells[
#           8] + ' ' + '|' + '\n'
#       + "---------")
# if incells == "XXXOO__O_" or incells == "XOXOXOXXO":
#     print("X wins")
#
# elif incells == "XOOOXOXXO":
#     print("O wins")
#
#
# elif incells == "XOXOOXXXO":
#     print("Draw")
#
# elif incells == "XO_OOX_X_":
#     print("Game not finished")
#
# else:
#     print("Impossible")
# ##########
# user_input = input()
# user_input = list(user_input)
# print("---------")
# print("| " + user_input[0] + " " + user_input[1] + " " + user_input[2] + " |")
# print("| " + user_input[3] + " " + user_input[4] + " " + user_input[5] + " |")
# print("| " + user_input[6] + " " + user_input[7] + " " + user_input[8] + " |")
# print("---------")
#
# input_matrix = [[user_input[0], user_input[1], user_input[2]],
#                [user_input[3], user_input[4], user_input[5]],
#                [user_input[6], user_input[7], user_input[8]]]
#
# only_x = [_ for _ in user_input if _ == "X"]
# only_o = [_ for _ in user_input if _ == "O"]
# only_empty = [x for x in user_input if x == "_"]
# x_wins = 0
# o_wins = 0
# total_wins = 0
#
# for i in range(3):
#     if input_matrix[0][i] == input_matrix[1][i] == input_matrix[2][i]:
#         total_wins += 1
#         if input_matrix[0][i] == "X":
#             x_wins += 1
#         else:
#             o_wins += 1
#     if input_matrix[i][0] == input_matrix[i][1] == input_matrix[i][2]:
#         total_wins += 1
#         if input_matrix[i][0] == "X":
#             x_wins += 1
#         else:
#             o_wins += 1
# if input_matrix[0][0] == input_matrix[1][1] == input_matrix[2][2]:
#     total_wins += 1
#     if input_matrix[1][1] == "X":
#         x_wins += 1
#     else:
#         o_wins += 1
#
# if input_matrix[0][2] == input_matrix[1][1] == input_matrix[2][0]:
#     total_wins += 1
#     if input_matrix[1][1] == "X":
#         x_wins += 1
#     else:
#         o_wins += 1
# if abs(len(only_x) - len(only_o)) >= 2:
#     print("Impossible")
# elif total_wins > 1:
#     print("Impossible")
# elif total_wins == 0 and len(only_empty) == 0:
#     print("Draw")
# elif x_wins == 1:
#     print("X wins")
# elif o_wins == 1:
#     print("O wins")
# elif total_wins == 0 and len(only_empty) > 0:
#     print("Game not finished")
# ###############################################################
# print('''
# '
# '"'
# '"'"'
# '"'"'"'
# ''')
#############################################
# n = int(input())
# k = int(input())
# it = k % n
# print(it)
# #####################################################
# print('You\nare\nthe\nbest\nprogrammer!')
##################################################
# print(len(repr('That is \n mine')))
# Напишите программу, которая будет печатать длину печатаемого представления строки 'That is \n mine'.
#################################################
# x = "global"
# def outer():
#     x = "outer local"
#     def inner():
#         x = "inner local"
#         def func():
#             x = "func local"
#             print(x)
#         func()
#     inner()
#
# outer()  # "func local"
# x = "global"
# def outer():
#     x = "outer local"
#     def inner():
#         x = "inner local"
#         def func():
#             print(x)
#         func()
#     inner()
#
# outer()  # "inner local"
# x, y = 1, 2
#
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
#
# foo()
# print(x)
# if y == 1:
#     x = 3
# print(x)
###############################
# message = "bonjour and welcome to Paris!"
# print(message.replace("Paris", "Lyon"))
# replaced_message = message.replace("o", "!", 2)
# print(replaced_message)
##########################
# import re
#
# inp_str = input()
# opt = re.sub(r"[^\w\s]", '', inp_str)
#
# s = re.sub(r"\s"{2,},' ', opt)
# #Help! Help! I’m being repressed!
# print(str.lower(s))
# # re.sub(r"[^a-zA-Z0-9]","",s)
###########
# a = input()
# a1 = a.replace("!", " ")
# a2 = a1.replace("?", " ")
# a3 = a2.replace(",", " ")
# a4 = a3.replace(".", " ")
# while a4.find('  ') != -1:
#     a4 = a4.replace('  ', ' ')
#
# print(str.lower(a4))
###################################
# text = input()
# text = text.replace("o", " ")
# text = text.split()
# text = " o".join(text)
# print(text)
####
# # b = "-".join(a) обеденить все части массива через знак
# a = input().split('-')
#
# for val in a:
#     print(val)
###
# a = input().split()
# print(" ".join([i for i in reversed(a)]))
####
# a = int(input())
# point = "#"
# b = a * 2
# for i in range(0, a):
#     print(point.center(b))
#     point += "##"
##########
# import string
# a = input()
# a1 = string.capwords(a, sep='_')
# import re
# a2 = re.sub('_', '', a1)
# print(a2)
# другое решение
# s = input().split("_")
# for word in s:
#     word = word.capitalize()
#     print("".join(word), end="")
###
# print(''.join(input().title().split('_')))
########################################################
# for word in input().split():
#     if word.lower().startswith(('https://', 'http://', 'www.')):
#         print(word)
# #######
# data = input().split()
# addr = 'https://', 'http://', 'www.'
#
# for word in data:
#     if word.lower().startswith(addr):
#         print(word)
#######
# print("\n".join([word for word in input().split() if word.lower().startswith(('https://', 'http://', 'www.'))]))
#######################################################
# a = int(input())
# if a < 2:
#     print("That's rare nowadays!")
# elif 2 <= a < 4:
#     print("This seems reasonable")
# else:
#     print("Don't forget to take breaks!")
#############
input_x, input_y = int(input('enter x')),int(input('enter y'))

# input_x = input('enter val')

user_input = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
print("---------")
print("| " + user_input[0] + " " + user_input[1] + " " + user_input[2] + " |")
print("| " + user_input[3] + " " + user_input[4] + " " + user_input[5] + " |")
print("| " + user_input[6] + " " + user_input[7] + " " + user_input[8] + " |")
print("---------")

input_matrix = [[user_input[0], user_input[1], user_input[2]],
                [user_input[3], user_input[4], user_input[5]],
                [user_input[6], user_input[7], user_input[8]]]

only_x = [_ for _ in user_input if _ == "X"]
only_o = [_ for _ in user_input if _ == "O"]
only_empty = [x for x in user_input if x == "_"]
x_wins = 0
o_wins = 0
total_wins = 0

for i in range(3):
    if input_matrix[0][i] == input_matrix[1][i] == input_matrix[2][i]:
        total_wins += 1
        if input_matrix[0][i] == "X":
            x_wins += 1
        else:
            o_wins += 1
    if input_matrix[i][0] == input_matrix[i][1] == input_matrix[i][2]:
        total_wins += 1
        if input_matrix[i][0] == "X":
            x_wins += 1
        else:
            o_wins += 1
if input_matrix[0][0] == input_matrix[1][1] == input_matrix[2][2]:
    total_wins += 1
    if input_matrix[1][1] == "X":
        x_wins += 1
    else:
        o_wins += 1

if input_matrix[0][2] == input_matrix[1][1] == input_matrix[2][0]:
    total_wins += 1
    if input_matrix[1][1] == "X":
        x_wins += 1
    else:
        o_wins += 1
if abs(len(only_x) - len(only_o)) >= 2:
    print("Impossible")
elif total_wins > 1:
    print("Impossible")
elif total_wins == 0 and len(only_empty) == 0:
    print("Draw")
elif x_wins == 1:
    print("X wins")
elif o_wins == 1:
    print("O wins")
elif total_wins == 0 and len(only_empty) > 0:
    print("Game not finished")


def turn_set(x, y, val, matrix):
    matrix[x][y] = val


def turn_get(x, y, matrix):
    return matrix[x][y]
