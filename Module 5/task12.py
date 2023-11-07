import re


def replace_spam_words(text, spam_words):
    for spam in spam_words:
        clear_words = '*' * len(spam)
        result = re.sub(spam, clear_words, text, flags=re.IGNORECASE)
        text = result
    return text 