import os
from spacy.en import English

nlp = English()

str = ""

with open('text-in.txt', 'r') as f:
	str=f.read().replace('\n', ' ')
	#str = parser(data)

tokens = nlp(unicode(str,encoding="utf-8"))

#for i, token in enumerate(parsedData):
	#print(token, token.lemma_)

#for i, token in enumerate(tokens):
	#print("original", token.orth, token.orth_)

sents = []
#sents property returns spans
#spans have indices into original string
#where each index value returns a token
for span in tokens.sents:
	#go from the start to the end of the span, returning each token in the sentence
	#combine each token using join()
	sent = ''.join(tokens[i].string for i in range(span.start, span.end)).strip()
	sents.append(sent)

#print("... PRINTING SENTENCES...")
#for sentence in sents:
	#print(sentence)

for span in tokens.sents:
	sent = [tokens[i] for i in range(span.start, span.end)).strip()
	print("... PRINTING POS TAGS ...")
	for token in sent:
		print(token.orth, token.pos_)


