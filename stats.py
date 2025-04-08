def count_words(book_text):  
    return f"{len(book_text.split())}"

def num_char(book):
    characters = {}
    for char in book:         
        if char.isalpha():
            c = char.lower()      
            if c not in characters:
                characters[c] = 1
            else:
                characters[c]+=1
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    result = ""
    for i, (k, v) in enumerate(sorted_characters.items()):
        is_last = i == len(sorted_characters) - 1
        if is_last:
            result += f"{k}: {v}"   
        else:  
            result += f"{k}: {v}\n"           
    return result        