

import wikipedia
import random

wikipedia_page = wikipedia.page("snoop dogg")

# This next line gets the textual content of the page and splits it up
# based on the characters ". " which creates a list of strings. The
# idea is that this would create a list of sentences, but it is not
# perfect
sentences = wikipedia_page.content.split(". ")

# Now you can proceed with the patterns from the tutorials, looking at
# any example where you have a list of strings. Some examples:

# Prints the first sentence:
print(sentences[0])

# Chooses a random sentence:
random_number = random.randrange( len(sentences) )
print( sentences[random_number] )
