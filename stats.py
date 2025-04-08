#This function takes a string as words from a book
#then counts the individual words in the book and returns them
def count_words(book_text):  
    return f"{len(book_text.split())}"

#This function sorts a books text into individual characters only if they are alpha
#numeric and the returns a dictionary of how often those characters appeared in the text
#provided as parameter "book"
def num_char(book):
    characters = {}
    for char in book:         
        if char.isalpha(): # checks if char is alphanumeric
            c = char.lower() # if alphanumeric convert it to lower case     
            if c not in characters: #if the character is not in the list add it and set its value to 1
                characters[c] = 1
            else:
                characters[c]+=1 #if the character is already in the list increase its key count by one
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True)) #sort the characters in decending order based on key value highest values first
    result = ""
    for i, (k, v) in enumerate(sorted_characters.items()):# iterates of the sorted Dict and checks for last entry in order not to add a /n new line tag at the end which creates a space
        is_last = i == len(sorted_characters) - 1
        if is_last:
            result += f"{k}: {v}"   #if it is the last entry dont tack on a newline \n char
        else:  
            result += f"{k}: {v}\n" #if it is not the last entry create a new line for each entry          
    return result  #return the key value paris in a sorted decending order based on highest value count first      