import nltk;
from nltk.util import ngrams;
def tokenizeContent(content,ON):
	tokens = nltk.word_tokenize(content);
	if ON:
		print(tokens);
	#print("Content Tokenized");
	return tokens;

def part_of_speach_tagging(tokens,ON):
	tagged = nltk.pos_tag(tokens);
	if ON:
		print(tagged);
	#print("Parts Of Speech Tagging Done");
	return tagged;

def select_adjectives(tagged,ON):
	adjectives = [];
	for i in tagged:
		if str(i[1]) == "JJ":
			adjectives.append(i[0]);
	if ON:
		print(adjectives);
	return adjectives;

def count_adjectives(adjectives,ON):
	adj_count = {};
	for i in adjectives:
		if i in adj_count:
			adj_count[i] = adj_count[i]+1;
		else:
			adj_count[i] = 1;
	if ON:
		print(adj_count);
	return adj_count;

def bigramIdentify(content, ON):
	sen = [];
	bi_grams = ngrams(content.split(), 2);
	for grams in bi_grams:
  		list_grams = list(grams);
		tagged_bigrams =nltk.pos_tag(list_grams);
		possible_adjective = tagged_bigrams[1];
		possible_adverb = tagged_bigrams[0];
		if possible_adjective[1] == "JJ":
			if possible_adverb[1] == "RB" and ON:
				print(possible_adverb[0]+" "+possible_adjective[0]);

def trigramIdentify(content):
	sen = [];
	trigrams = ngrams(content.split(), 3);
	for igrams in trigrams:
  		list_grams = list(igrams);
		tagged_trigrams =nltk.pos_tag(list_grams);
		possible_adjective = tagged_trigrams[2];
		possible_adverb2 = tagged_trigrams[1];
		possible_adverb1 = tagged_trigrams[0];
		if possible_adjective[1] == "JJ":
			if possible_adverb1[1] == "RB":
				if possible_adverb1[1] == "RB" and ON:
					print(possible_adverb1[0]+" "+possible_adverb2[0]+" "+possible_adjective[0]);

