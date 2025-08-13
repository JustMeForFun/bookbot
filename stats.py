# Counts the amount of words in a given string    
def word_count(text):
    
    word_list = text.split()
    return len(word_list)

# count each unique character in a give string
def count_characters(text):

    characters = {}

    for c in text.lower():
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

def sort_on(items):
    return items["num"]

def character_sorter(character_count):
    
    sorting_list = []

    for k in character_count:
        temp = {}
        temp["char"] = k
        temp["num"] = character_count[k]
        sorting_list.append(temp)
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list