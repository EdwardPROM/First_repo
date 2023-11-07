def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    text_f = (
        text.strip()
        .replace(".", "")
        .replace(",", ""))
    list_word = text_f.split(" ")

    x = 0

    for word in list_word:
        if not space_around:
            for spam in spam_words:
                if word.endswith(spam) or word.startswith(spam):
                    x += 1
                else:
                    continue
        else:  # випадок, коли слово окремо, перевіряємо слово.
            x = spam_words.count(word)

    # Перевірка чи знайдене хоч одне слово
    if x > 0:
        return True
    else:
        return False