def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result