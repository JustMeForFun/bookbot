# Imports functions from stats.py
from stats import word_count
from stats import count_characters
from stats import character_sorter

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# Prints content of get_book_text to console
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(book_path))} total words")
    print("--------- Character Count -------")
        
    for c in character_sorter(count_characters(get_book_text(book_path))):
        if c["char"].isalpha() == True:
            print(f"{c["char"]}: {c["num"]}")

    print("============= END ===============")

# Returns the content of a file as a string
def get_book_text(filepath):
    
    with open(filepath) as f:
        return f.read()
    
main()