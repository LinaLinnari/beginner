
score = int(input())
maximum = int(input())
percentages_are_as_follows = (score * 100) / maximum
if percentages_are_as_follows < 60:
    print("F")
elif 60 <= percentages_are_as_follows < 70:
    print('D')
elif 70 <= percentages_are_as_follows < 80:
    print('C')
elif 80 <= percentages_are_as_follows < 90:
    print('B')
elif 90 <= percentages_are_as_follows < 100:
    print('A')