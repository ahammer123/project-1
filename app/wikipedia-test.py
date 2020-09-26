"""

    1. Add the following line to your requirements.txt file:
       wikipedia==1.4.0

    2. Modify your Dockerfile to change the last line to this:
        CMD ["python3", "wikipedia-test.py"]

    3. Run the docker build command again:
        docker build . --tag project1:1.0

    4. Now run the docker run command to run this file:
        docker run --rm -it -v "$(pwd)/app:/app" project1:1.0

    Hopefully you can see how to integrate some of the code below into
    the main.py that you have been working on. If you have any
    questions, let me know.

    When you want to go back to working on main.py, change the last
    line of your Dockerfile back to what it was before:
        CMD ["python3", "wikipedia-test.py"]

    and then run the docker build command again, and docker run as you
    wish.

"""

import wikipedia
import random

wikipedia_page = wikipedia.page("New York City")

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
