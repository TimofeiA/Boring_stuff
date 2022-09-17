today = input('введите день: ')
if today == "holiday":
    print("Lucky you!")
else:
    print('Keep your chin up, then.')


print("It\'s a day now!" if sun else "It's a night for sure")


x = int(input("введите значение x=  "))
if x < 100:
    print('x < 100')
else:
    if x == 100:
        print('x = 100')
    else:
        print('x > 100')
    print('This will be printed only because x >= 100')

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
if word in dictionary:
    print('Correct')
else:
    print('Incorrect')


city = "..."
summer = "Barcelona, Rome, Istanbul, Lisbon, Paris"
winter = "Oslo, Helsinki, Sydney, Cape Town, Vienna"

if (city in summer) or (city in winter):
    if city in summer:
        print("You should visit it in the summer!")
    else:
        print("You should visit it in the winter!")
else:
    print("I don't know what the best season is :(")