import tweepy

from authorization_tokens import *

import random

# consumer_key = 'gO4uS9FcgbwiFR6rKUtjrRi83'
# consumer_secret = '1yoN1hz30tetGHb9ofXf9c2fwLkcF9N7OmNaIfCmG5VotYVanJ'
consumer_key = 'FnRl0EJ2IXyM8IytDrskiuuzt'
consumer_secret = '8UkiysHXuzcQZY6f4VPuoxwat1L8LhGSYdf1RlaWSuqMVyhbkr'


access_token = '1301523490365997057-qYya5kNen2pobQUyD8yBnwotvhzRMu'
access_token_secret = 'L4eLhi1cwPnMGPsRJ5BWambMdyARFg2LBlw2qfmK6EUgI'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#import pronouncing
# op:1

# pick a phrase randomly from a list

# phrase_list =  [ "Hi, my name is Groucho",
#                     "I like python",
#                     "I am a twitter bot"]
# random_number = random.randrange(len(phrase_list) )
# message = phrase_list[random_number]

# op:2

# create a sentence template with some blanks, and
# randomly pick a word from a list to fill in each blank

# word_list = [ "apricots", "blueberries", "celery", "dragonfruit"]
#
# string_template = "some people think {} tastes bad but enjoy the taste of {}?"
#
# random_number = random.randrange(len(word_list) )
# word1 = word_list [ random_number ]
# random_number = random.randrange(len(word_list) )
# word2 = word_list [ random_number ]
#
# message = string_template.format(word1,word2)

# op:3

# Randomly pick template from list, then randomly fill in template
# word_list = [ "templars", "swordsmen", "archers", "kings"]
# template_list = [ "If you dislike {}, I think you'll love {}.",
#                     "Some people assume I like {} but I actually like {} more.",
#                     "Sometimes I prefer {} over {}."]
# random_number = random.randrange(len(template_list) )
# template = template_list[random_number]
#
# random_number = random.randrange(len(word_list) )
# word1 = word_list [ random_number ]
#
# random_number = random.randrange(len(word_list) )
# word2 = word_list [ random_number ]
#
# message = template.format(word1,word2)



# option 4 basic search

# search_results = api.search( q="hate filter:safe", lang="en", tweet_mode="extended" )
# random_number = random.randrange( len(search_results) )
# random_tweet = search_results[random_number]
# message = random_tweet.full_text.replace( "hate","love" )
# api.update_status(message)


# option 5 reply to random mention

# mentions = api.mentions_timeline()
# random_number = random.randrange( len(mentions) )
# # random_mention = mentions[random_number]
# latest_mention = mentions[0]
#
# message = "@" + random_mention.user.screen_name + " I promise im not a bot!"
#
#
# api.update_status(message, in_reply_to_status_id=random_mention.id)

#option 5b reply to recent mention with rhyme

# mentions = api.mentions_timeline(count=1)
# mention = mentions[0]
#
# mention_word_list = mention.text.split()
# random_number = random.randrange( len(mention_word_list))
# word = mention_word_list[random_number]
#
# rhyming_word_list = pronouncing.rhymes(word)
# random_number = random.randrange( len(rhyming_word_list))
# rhyme = rhyming_word_list[random_number]
#
# template = "some people like {} but I like {} "
# message = template.format(word, rhyme)
#
# api.update_status(message, in_reply_to_status_id=mention.id)
#
# print("Done.")


# #wiki
#
import wikipedia
import random


mentions = api.mentions_timeline(count=1)
mention = mentions[0]
search = " ".join(mention.text.split()[1:])
wikipedia_page = wikipedia.page(search)
sentences = wikipedia_page.content.split(". ")
random_number = random.randrange( len(sentences) )
fact = sentences[random_number]
api.update_status(fact[:280])
print(fact)


exit()
# api.update_status(message, mentions[random.randrange(len(mentions))

# # wikipedia_page = wikipedia.page("'"+things[random.randrange(len(things))]+"'")
#clean up mention text, strip screen name, no white space
# topic = mentions[random.randrange(len(things))]
# wikipedia_page = wikipedia.page(topic)
# #
# # # This next line gets the textual content of the page and splits it up
# # # based on the characters ". " which creates a list of strings. The
# # # idea is that this would create a list of sentences, but it is not
# # # perfect
# sentences = wikipedia_page.content.split(". ")
# #
# # # Now you can proceed with the patterns from the tutorials, looking at
# # # any example where you have a list of strings. Some examples:
# #
# # # Prints the first sentence:
# print(sentences[0])
# #
# # # Chooses a random sentence:
# random_number = random.randrange( len(sentences) )
# print( sentences[random_number] )
#
# # api.update_status(sentences[0])
# api.update_status("An interesting fact about " + topic + " is: "+ sentences[random.randrange(len(sentences))])
#
# mentions = api.mentions_timeline()
# random_number = random.randrange( len(mentions) )
# # random_mention = mentions[random_number]
# latest_mention = mentions[0]
#
# # message = "@" + random_mention.user.screen_name + " I promise im not a bot!"
#
#
#
#
# # api.update_status(message, in_reply_to_status_id=random_mention.id)





# #wiki
#
# import wikipedia
# import random
#
# things = ["Vietnam","Syria","Afghanistan","The United States","Canada","Mexico","Turkmenistan","Sweden","Pakistan","Iran","Walmart","Mercedes-AMG","Python","Iphone","Samsung","Microsoft","Nvidia","Socialism","Capitalism","Amazon Rainforest","Amazon","Coding","Milk","Cereal",]
# #
# # wikipedia_page = wikipedia.page("'"+things[random.randrange(len(things))]+"'")
# topic = things[random.randrange(len(things))]
# wikipedia_page = wikipedia.page(topic)
# #
# # # This next line gets the textual content of the page and splits it up
# # # based on the characters ". " which creates a list of strings. The
# # # idea is that this would create a list of sentences, but it is not
# # # perfect
# sentences = wikipedia_page.content.split(". ")
# #
# # # Now you can proceed with the patterns from the tutorials, looking at
# # # any example where you have a list of strings. Some examples:
# #
# # # Prints the first sentence:
# print(sentences[0])
# #
# # # Chooses a random sentence:
# random_number = random.randrange( len(sentences) )
# print( sentences[random_number] )
#
# # api.update_status(sentences[0])
# api.update_status("An interesting fact about " + topic + " is: "+ sentences[random.randrange(len(sentences))])
