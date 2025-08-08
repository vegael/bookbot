import sys
from stats import count_words, count_chars, sorter

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def main():
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    file_contents = get_book_text(path)

    num_words = count_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_chars = count_chars(file_contents)
    sorted_num_chars = sorter(num_chars)

    print("--------- Character Count -------")
    for ch, count in sorted_num_chars:
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()