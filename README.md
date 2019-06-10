# SpeechToSummary

This project is an integration of google speech api and nltk to create a speech to text summarizer.

This has two utilities:
1. Can record a speech/audio and convert it to text. Applicable for .wav files as well.
2. Can summarize any text file.

Real life usage:
Automated Minutes of Minute generator

Steps to set-up:
Best to use Python 3.6 version, since pyAudio has dependency. Though, for python 3.7, it can be installed using .whl file
Install speech_recognition library (for accessing speech api. https://realpython.com/python-speech-recognition/)
Install pyAudio library
While recording on micrphone, dictate punctuations - e.g. point for fullstop, comma for comma etc. This is not required if you use google cloud speech api since it has auto-punctuation feature.
For text summarizer: install nltk
Concept used: word frequency weightage is used to calculate weight of sentences.Next sentences are stored in has with their weightage values. top 40% of highest weighed sentences are selected as summary 
