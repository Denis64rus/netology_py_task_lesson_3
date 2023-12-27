# boolean + if
name = input("Введите имя: ")
login = "Dima"

if name == login:
    print("Hello,", name)
elif name == "Yo":
    print("Yo, bro")
elif len(name) < 3:
    print("Недопустимое имя")
else:
    print("Неверный логин")

print("The end")

# while
x = 1
while x <= 10:
    print(x)
    x += 1