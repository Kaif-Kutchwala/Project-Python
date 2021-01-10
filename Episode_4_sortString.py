
def sort_string(txt):
    words = txt.split()
    dictionary = {}
    for word in words:
        dictionary[word.lower()] = word
    output = ' '.join(dictionary[key] for key in sorted(dictionary))
    return output

print(sort_string('grape, Orange, apple, Watermelon'))
print(sort_string('Hello my name is John'))
print(sort_string('Can you believe That'))

    