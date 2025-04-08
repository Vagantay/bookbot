from stats import count_words, num_char

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

def get_book_text(filepath):
    with open(filepath) as f:         
        return f.read()   



main()

