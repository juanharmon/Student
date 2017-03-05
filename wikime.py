import sys
import wikipedia as wiki

query = input("wiki wut\n")
result = wiki.page(title=query)

file = open(result.title + ".txt", 'w')
file.write(result.content.encode('utf-8'))
file.close()