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

def bigramIdentify(content,n,ON):
	i = 0;
	sen = [];
	sixgrams = ngrams(content.split(), n);
	for grams in sixgrams:
  		m = list(grams);
		t =nltk.pos_tag(m);
		k = t[1];
		l = t[0];
		if k[1] == "JJ":
			if l[1] == "RB":
				print(l[0]+" "+k[0]);

n = 2;
filename = "neg/Rev34.txt";
f = open(filename);
content = f.read();
bigramIdentify(content,n,False);
