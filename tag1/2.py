tiere = ["hase", "igel", "huhn", "ameise"]

def count_total_number_of_letters(list_with_words):
    num_letters = 0
    for word in list_with_words:
        for letter in word:
            num_letters += 1
    return num_letters

def return_number_of_letters(list_with_words):
    new_list=[]
    for word in list_with_words:
        num_letters = 0
        for letter in word:
            num_letters += 1
        new_list.append(num_letters)
    return new_list

print(count_total_number_of_letters(tiere))
print(return_number_of_letters(tiere))

def is_large_word(word):
    num_letters = len(word)
    print(f"num_letters = {num_letters}")
    if num_letters > 10:
        return True
    else:
        return False
    
print(is_large_word("Elefant"))
print(is_large_word("Donaudampfschiff"))
print(is_large_word("Obstkuchen"))
print(is_large_word("100"))