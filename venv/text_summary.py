import nltk
import re
import heapq

article_text = open("OriginalText.txt", "r").read()
formatted_article_text= re.sub('[\\t\\n\\r\\f]',' ',article_text)
formatted_article_text = re.sub('[^a-zA-Z0-9]', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(article_text)
summary_length = int(len(sentence_list)/0.25)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] +=1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)


sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

summary_sentences = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get) # summary contains 40% of the sentences in Original text

summary = ' '.join(summary_sentences)
print(summary)
f = open("SummarizedText.txt", "w+")
f.write(r.recognize_google(audio))
f.close()