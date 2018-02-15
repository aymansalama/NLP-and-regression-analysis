
# coding: utf-8

# In[13]:


# Q4. String similarity (code in python):
import re, math
import pandas as pd

from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
    
f = open('results/Q4.txt','w')
########################################################################################################################
# b) Load the data to a Spark/Pandas data frame
data = pd.read_csv("test.csv", low_memory=False)
########################################################################################################################
# b) Calculate similarity between description_x and description_y and store resultant
# scores in a new column

counter=0
for id,item in data.iterrows():
    text1=item['description_x']
    text2=item['description_y']
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    print ('ID : ', counter , 'Cosine:', cosine, file=f)
    counter+=1

f.close()
