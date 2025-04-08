#import stats functions from other file stats.py in same directory.
from stats import count_words, num_char

#present the output in a nice readable format and list the dic values decending based on key count.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
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

