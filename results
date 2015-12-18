from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

with open('stem-testCase-11-24-15.txt', 'r') as f:
	for line in f:
		for word in line.split():
			print(stemmer.stem(word))
