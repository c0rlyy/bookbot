def main():
    book_path = "./book.txt"
    text = get_book_text(book_path)

    #print(text)
    num_of_words = get_words(text)
    #print(num_of_words)

    chars = get_chars(text)
    #print(chars)

    get_report(num_of_words,chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    words = text.split()
    num_of_unique_letters = {}
    for word in words:
        for letter in word:
            char = letter.lower()
            if char in num_of_unique_letters:
                num_of_unique_letters[char] +=1
            else:
                num_of_unique_letters[char] =1
    return num_of_unique_letters

def get_report(get_words,get_chars):
    list_of_chars = []
    print("begining the report")

    print(f"There is {get_words} words in the document")

    for key in get_chars:
        if key.isalpha():
            items = [key,get_chars[key]]
            list_of_chars.append(items)
    list_of_chars.sort()
    for char in list_of_chars:
        print(f"The charachter {char[0]} was found {char[1]} times")
    
    print("--- End report ---") 


main()