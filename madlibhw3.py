# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk
import random
from nltk import word_tokenize,sent_tokenize
from nltk.book import * 

print('\n')
print('ORIGINAL TEXT')
list_first_150 = text2[:150]
#print(first_150)
string_first_150 = ' '.join(list_first_150)
print(string_first_150)
print('\n')
tokens = nltk.word_tokenize(string_first_150)
print("TOKENS")
print(tokens)
print('\n')
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)
print('\n')

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print('\n')
print("NEW TEXT")
print ("".join(final_words))


print("\n\nEND*******")
