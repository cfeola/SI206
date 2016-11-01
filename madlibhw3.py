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
from nltk import word_tokenize,sent_tokenize
from nltk.book import * 

list_first_150 = text2[:150]
#print(first_150)
string_first_150 = ' '.join(list_first_150)
tokens = nltk.word_tokenize(string_first_150)
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1}

word_list = []

noun = input("Enter a noun: ")
word_list.append(noun)

plural_noun = input("Enter a plural noun: ")
word_list.append(plural_noun)

verb1 = input("Enter a verb: ")
word_list.append(verb1)

verb2 = input("Enter another verb: ")
word_list.append(verb2)

adj = input("Enter an adjective: ")
word_list.append(adj)


print("\n\nEND*******")
