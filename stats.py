def get_num_words(string):
    words = string.split()
    return len(words)

def get_num_letters(string):
    letters = {}
    for char in string.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def get_report(char_dict):
    # First, create a list of dictionaries in the required format
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Then sort the list by count in descending order
    return sorted(chars_list, key=lambda x: x["num"], reverse=True)
