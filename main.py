import sys
#import stats functions from other file stats.py in same directory.
from stats import count_words, num_char

#present the output in a nice readable format and list the dic values decending based on key count.
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    #book_path = input("Please enter a book is this format \n(directory/bookname.txt): books/frankenstein.txt: \n")
    text = get_book_text(f"{book}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")    
    print(num_char(text))
    print("============= END ===============")  

#define the get_book_text function ready to be fed a new book which returns a string "f"
def get_book_text(filepath):
    with open(filepath) as f:         
        return f.read()   



main()

