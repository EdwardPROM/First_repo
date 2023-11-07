import re


def find_word(text, word):
    result = False
    start = None
    end = None
    if word in text:
        result = True
        search = re.search(word, text)
        start = search.start()
        end = search.end()
    return {
        'result': result,
        'first_index': start,
        'last_index': end,
        'search_string': word,
        'string': text
    }    
    