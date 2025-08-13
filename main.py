
# Sets a path for the frankenstein text file 
frankenstein_path = "books/frankenstein.txt"

# Prints content of get_book_text to console
def main():
    print(get_book_text(frankenstein_path))

# Returns the content of a file as a string
def get_book_text(filepath):
    
    with open(filepath) as f:
        return f.read()
    
main()