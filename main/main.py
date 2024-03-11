def return_book_contents(path_to_file: str):
    with open(path_to_file) as f:
        book_contents = f.read()

    return book_contents

def count_words(book_contents) -> str:
    """Returns how many words are within supplied book"""
    all_words = len(book_contents.split())

    print(f"The book has: {all_words} words.")

def count_vowels(book_contents) -> dict:
    """Returns a dictionary with frequencies of all vowels"""
    total_letters = 0
    vowel_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    book_string = str(book_contents).lower()
    for vowel in book_string:
        total_letters += 1
        if vowel in vowel_dict:
            vowel_dict[vowel] += 1

    for vowel, vowel_count in vowel_dict.items():
        vowel_pct = round((vowel_count / total_letters) * 100, 2)
        print(f"Vowel: {vowel} pct is {vowel_pct}% ({vowel_count})")
    
    return vowel_dict

def print_report(book) -> str:
    """Returns report statistics for provided book"""
    print(f"---- Begin Report of Book ----")
    print(f"Total words:")
    vowel_dict = count_vowels(book)
    for vowel, vowel_count in vowel_dict.items():
        print(f"Vowel: {vowel} Was Used {vowel_count} times")

def main(book_path: str) -> None:
    """Returns all statistics for book"""
    book = return_book_contents(book_path)
    count_words(book)
    count_vowels(book)
    print_report(book)

main('/Users/jmunizbecerra/workspace/github.com/jmunizbecerra/bookbot/books/frankenstein.txt')