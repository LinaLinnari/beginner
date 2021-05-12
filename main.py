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

a = int(input())
b = int(input())
counter = 0
summ = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        summ += i
        counter += 1
print(summ / counter)




