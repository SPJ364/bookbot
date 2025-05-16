import sys
from stats import get_num_words, get_num_letters, get_report

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        contents = file.read()
        number = get_num_words(contents)
        letters = get_num_letters(contents)
        final_report = get_report(letters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file} ...")
        print("----------- Word Count ----------")
        print(f"Found {number} total words")
        print("--------- Character Count -------")

        for report in final_report:
            print(f"{report['char']}: {report['num']}")

        print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(sys.argv[1])

main()
