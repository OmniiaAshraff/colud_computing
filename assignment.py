#Read the two books By Download the books from links into files.txt

book1 = open('HP Lovecraft’s Beyond the Wall of Sleep.txt' , encoding='utf-8').read()
book2 = open('Jane Austin’s Pride and Prejudice.txt' , encoding='utf-8').read()

#Convert all words to lower case to can do compare well

lower_case1 = book1.lower()
lower_case2 = book2.lower()

#Delete punctuations and spaces .. and so on

import string 
cleaned_book1 = lower_case1.translate(str.maketrans('','',string.punctuation))
words1 = cleaned_book1.split()
cleaned_book2 = lower_case2.translate(str.maketrans('','',string.punctuation))
words2 = cleaned_book2.split()

#Set of stop words

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

#Find common words between the two books and Remove the stop words from it

common = set(words1).intersection( set(words2) )
final = common.difference(stop_words)

#Finally display this common words and their number 

print(final)
print('Number of common words is',len(final))