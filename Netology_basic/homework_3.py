def count_letter(list, letter):
    number_of_words = 0
    for word in list:
        if letter in word:
            number_of_words += 1
    return number_of_words

list = ['python', 'c++', 'c', 'scala', 'java']

result = count_letter(list, "c")
print(result)