def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_text_count(text)
    char_count = get_char_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print("")
    get_report(char_count)
    print("--- End report ---")

def get_report(char_count):
    dic = sorted(char_count.items(), key = lambda item: item[1], reverse=True)
    for key, value in dic:
        print(f"The '{key}' character was found {value} times")

def get_char_count(text):
    lower_text = text.lower()
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char_dic = dict()
    for t in lower_text:
        if t in abc:
            if t in char_dic:
                char_dic[t] += 1
            else:
                char_dic[t] = 1
    return char_dic

def get_text_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read() 
        return file_contents

main()