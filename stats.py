# Counts the amount of words in a given string    
def word_count(text):
    
    word_list = text.split()
    return len(word_list)

def count_characters(text):

    characters = {}

    for c in text.lower():
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters