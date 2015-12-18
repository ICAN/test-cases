import nltk

with open('adj-test.txt', 'r') as f:
	count = 0
	for line in f:
		count += 1
		#print(line)
		if count % 2 == 0:
			for word in line.split():
				print(nltk.pos_tag(nltk.word_tokenize(word.decode('utf-8'))))

