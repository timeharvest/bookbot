from stats import get_num_words, get_letter_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    filepath = sys.argv[1]
    num_words = get_num_words(filepath)
    letters = get_letter_count(filepath)
    
    bookbotline = "============ BOOKBOT ============" + "\n"
    bookline = f"Analyzing book found at {filepath}..." + "\n"
    countline = "----------- Word Count ----------" + "\n"
    count = f"Found {num_words} total words" + "\n"
    charcount = "--------- Character Count -------" + "\n"
    endline = "============= END ==============="

    char_list = ""
    header = bookbotline + bookline + countline + count + charcount

    for key,val in letters.items():
        char_list += f"{key}: {val}\n"
    print(header+char_list+endline)  

main()