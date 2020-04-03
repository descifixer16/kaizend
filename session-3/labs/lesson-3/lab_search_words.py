# 3.5 Advanced Iteration (using List Comprehension)

# Filter out items in a list
# Modify every item in the list

import argparse

parser = argparse.ArgumentParser(description="Search for words including partial word")
parser.add_argument("snippet", help="Partial (or complete) string to search for in words")

args = parser.parse_args()
snippet = args.snippet.lower()


# orig
# with open('/usr/share/dict/words') as f:
#     words = f.readlines()
# matches = []
# for word in words:
#     if snippet in word.lower():
#         matches.append(word)
# print(matches)


# list comprehension

words = open("/usr/share/dict/words").readlines()

print([word for word in words if snippet in word.lower()])
