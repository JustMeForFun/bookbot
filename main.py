
# Sets a path for the frankenstein text file 
frankenstein_path = "books/frankenstein.txt"

# Prints content of get_book_text to console
def main():
    print(f"{word_count(get_book_text(frankenstein_path))} words found in the document")

# Returns the content of a file as a string
def get_book_text(filepath):
    
    with open(filepath) as f:
        return f.read()

# Counts the amount of words in a given string    
def word_count(text):
    
    word_list = text.split()
    return len(word_list)
    
main()