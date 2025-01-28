def book_word_count(contents):
    words = contents.split()
    word_count = 0
    for word in words:
        word_count += 1

    # alternative solution as inline function
    # return len(contents.split())
    return word_count

def book_char_count(contents):
    result = {}
    for char in contents_lowered:
        l_char = char.lower() # lower the contents in the same pass that they're being counted in
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def book_report(path, contents):
    word_count = book_word_count(contents)
    char_dict  = book_char_count(contents)
    alpha_list = [char for char in "abcdefghijklmnopqrstuvwxyz"]

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char in char_dict:
        if char in alpha_list:
            print(f"The \'{char}\' character was found {char_dict[char]} times")
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_contents = f.read()
        #print(book_contents)

        '''
        Improvements that can be done, based on bootdev solution
        * Reverse sort the char counts (via the .sort(reverse, key) List method) by creating a list of dictionaries with
        * individual key-val entries for the char and num values, respectively. Then use this for the for loop, checking for
        * alpha characters with the string method .isalpha (as opposed to my clunky hack).
        ''' 
        book_report(book_path, book_contents)
        


main()