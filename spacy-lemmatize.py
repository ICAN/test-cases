import os
from spacy.en import English, LOCAL_DATA_DIR

data_dir = os.environ.get('SPACY_DATA', LOCAL_DATA_DIR)
nlp = English(data_dir=data_dir)

with open('lemma-testCase.txt', 'r') as f:
	data=f.read().replace('\n', ' ')

parsedData = parser(data)
for i, token in enumerate(parsedData):
	print(token, token.lemma_)
	if i > 1:
		break
