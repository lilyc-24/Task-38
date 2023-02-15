#import spacy and dowload the web library
import spacy
nlp = spacy.load('en_core_web_md')

#comparing similarity of words - code from task 38 doc
words = nlp('cat apple monkey banana mango domestic zoo')

for word1 in words:
    for word2 in words:
        print(word1.text, word2.text, word1.similarity(word2))
        
#comparing sentence similarities - code from taskk 38 doc
sentence_to_compare = 'Why is my cat on the car'

sentences = ['where did my dog go',
'Hello, there is my car',
'I\'ve lost my car in my car',
'I\'d like my boat back',
'I will name my dog Diana']

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f'{sentence} - {similarity}')

#upon running the above code with both 'en_core_web_sm' and 'en_core_web_md' there was a large difference in the similarities found.
#this difference was larger with the comparison of sentences than words
#for example the comparion of monkey and zoo differed between the two versions with md finding a higher similarity
#with the sentences, the last sentence in the list had a large difference between the sm and md libraries, with them being found more similar with the md library as they both are about pets 
#however, some of the similarity observed such as 0.8 for 'hello, there is my car' to 'why is my cat on the car' seems quite high for the sentences


