# Примитивы

# вывод
hello = "Hello, world!"
print(hello)

x = 1
print(x)

# ввод
name = input("Введите имя: ")
print("Привет,", name)

# простые мат операции
print(2 + 2)
print(15 - 2)
print( 3 * 7)
print(7 / 2) # 3.5
print(2 ** 8) # 256
print(7 % 2) # 1

# строки
s1 = "hello"
s2 = 'hello'
s3 = """hello"""

print(s1)
print(s2)
print(s3)

# конкатенация + длина строки
greeting = "Hello, " + "world!"
print(greeting)

l = len(greeting)
print(l)
print(len(s1))

# Составные Сложные Типы

# список
strings = ["Hello", "world"]
numbers = [1, 2, 3, 4, 5]
data = ["hello", 1]

print(strings)
print(numbers)
print(data)

summa = numbers + data
print(summa)

numbers.append(6)
print(numbers)

first = strings[0]
second = strings[1]
print(first)
print(second)

strings_length = len(strings)
print(strings_length)

s = sum(numbers)
print(s)

# словарь - "ключ" : "значение"
dictionary = {
    "cat": "кошка",
    "bat": "летучая мышь"
}

print(dictionary)
cat = dictionary["cat"]
print(cat)

countries = {
    "Африка": ["Египет", "Конго", "ЮАР"],
    "Азия": ["Китай", "Таиланд", "Индонезия"]
}

africa = countries["Африка"]
print(africa)

africa_key = "Африка"
print(countries[africa_key])

countries["Европа"] = ["Австрия", "Испания", "Италия"]
print(countries)
print(countries["Европа"])
# countries[0] = "Hello"
# print(countries)
africa.append("Эфиопия")
print(africa)
print(countries)
print(len(countries["Африка"]))