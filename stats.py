def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read().split()
        num_words = len(file_contents)
        return num_words

def get_letter_count(filepath):
    with open(filepath) as f:
        letter_string = "".join(f.read().split())
        char_dict = {}
        for char in letter_string.lower():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        sorted_dict = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse = True)}
        new_dict = {key: value for key, value in sorted_dict.items() if key.isalpha()}  
        return new_dict     


        

filepath = "books/frankenstein.txt"

#print(letters)