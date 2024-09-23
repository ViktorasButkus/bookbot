def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_of_chars = character_calculator(text)
    num_of_chars = character_calculator(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in num_of_chars.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_calculator(text):
    lower_case_count = {}
    words = text.split()
    for word in words:
        lower_word = word.lower()
        for char in lower_word:
            if char.isalpha():  
                if char in lower_case_count:
                    lower_case_count[char] += 1
                else:
                    lower_case_count[char] = 1 
    return lower_case_count


main()
