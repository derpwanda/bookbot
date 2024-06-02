def main():
    book_location = 'books/frankenstein.txt'
    book_text = get_book_text(book_location)
    word_count = get_word_count(book_text)
    character_dict = character_counter(book_text)
    dict_list = dictionary_list(character_dict)
    final_report = print_report(book_location, word_count, dict_list)


def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def character_counter(book_text):
    character_dict = {}
    lower_book_text = book_text.lower()

    for i in lower_book_text:
        if not i in character_dict:
            character_dict[i] = 1
        else:
            character_dict[i] += 1
    return character_dict


def dictionary_list(character_dict):
    dict_list=[]
    for i in character_dict:
        if i.isalpha() == True:
            dict_list.append({"character": i, "count" : character_dict[i]})
    return dict_list

def sort_by_count(dict_list):
    return dict_list['count']



def print_report(book_location, word_count, dict_list):
    print(f'--- Begin report of {book_location} ---')
    print(f'{word_count} words found in the document\n')

    new_list = sorted(dict_list, key=sort_by_count, reverse=True)

    for entry in new_list:
        print(f"The '{entry['character']}' character was found {entry['count']} times")   
    
    print('--- End report ---')



main()