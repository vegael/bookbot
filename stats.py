def count_words(book_string):
    word_list = book_string.split()
    num_words = len(word_list)
    return num_words

def count_chars(book_string):
    num_chars = {}
    for word in book_string:
        lowered_word = word.lower()
        for char in lowered_word:
            num_chars[char] = num_chars.get(char, 0) + 1
    return num_chars

def sorter(num_chars):
    sorted_num_chars = sorted(num_chars.items(), key=lambda item: item[1])
    return sorted_num_chars