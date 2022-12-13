import wikipedia

choice = input("Choice: ")
# while choice != "":
#     try:
#         wiki_summary = wikipedia.summary(f"{choice}")
#         print(wiki_summary)
#     except wikipedia.exceptions.DisambiguationError as e:
#         print(e.options)
#
#     choice = input("Choice: ")
try:
    wiki_page = wikipedia.page(f"{choice}", auto_suggest=False)  # Python (programming language) as input
    print(wiki_page.title)
    print(wiki_page.summary)
    print(wiki_page.url)
except wikipedia.exceptions.DisambiguationError as error:
    print(error.options)

