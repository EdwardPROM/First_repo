articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

    
def find_articles(key, letter_case=False):
   
    found_articles = []

    for article in articles_dict:
        title = article['title']
        author = article['author']

        if not letter_case:
            key = key.lower()
            title = title.lower()
            author = author.lower()

        if key in title or key in author:
            found_articles.append(article)

    return found_articles

# message = "Hello my little friend!"

# print(message.find("li", 5, 15))  # 9
# print(message.find("li", 10, 15))  # -1
# print(message.find("li"))  # 9    
    
    