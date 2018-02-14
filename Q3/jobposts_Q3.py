# Owner: Ayman Salama
# Email: ayman3salama@gmail.com
# Q3. Jobposts Data Exploration and Analysis (code in python)


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import re
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import inflect
# Read the file
data = pd.read_csv("data job posts.csv", low_memory=False)
# Get the jobposts column.
jobpost=data.iloc[:,0]

########################################################################################################################
# Q3 b) Extract Title from the jobpost column:
id_counter=0
title_df = pd.DataFrame(columns=['JobpostID','Title'])
for eachjobpost in jobpost:
    for line in eachjobpost.splitlines():
        if "TITLE" in line:
             title_df.loc[id_counter] = [id_counter,line]
             id_counter+=1
title_df.to_csv(r'results/Q3_b_title.csv')
# print(title_df)

########################################################################################################################
# Q3 b) Extract Duration from the jobpost column:
id_counter=0
duration_df = pd.DataFrame(columns=['JobpostID','Duration'])
for eachjobpost in jobpost:
    for line in eachjobpost.splitlines():
        if "DURATION" in line:
             duration_df.loc[id_counter] = [id_counter,line]
    id_counter+=1
duration_df.to_csv(r'results/Q3_b_duration.csv')

########################################################################################################################
# Q3 b) Extract Location from the jobpost column:
id_counter=0
location_df = pd.DataFrame(columns=['JobpostID','Location'])
for eachjobpost in jobpost:
    for line in eachjobpost.splitlines():
        if "LOCATION" in line:
            location_df.loc[id_counter] = [id_counter, line]
    id_counter+=1
location_df.to_csv(r'results/Q3_b_location.csv')

########################################################################################################################
# Q3 b) Extract Description from the jobpost column:
id_counter=0
description_df = pd.DataFrame(columns=['JobpostID','description'])
flag=0
descr=''
for eachjobpost in jobpost:
    wordList = re.sub("[^\w]", " ",  eachjobpost).split()
    for words in wordList:
        if "DESCRIPTION" in words:
            flag=1
        if "RESPONSIBILITIES" in words:
            flag=0
        if "JOB" in words:
            flag=0
        if (flag == 1):
            descr+=words
            descr+=' '
    description_df.loc[id_counter] = [id_counter, descr]
    id_counter+=1
description_df.to_csv(r'results/Q3_b_description.csv')

########################################################################################################################
# Q3 b) Extract Responsibilities from the jobpost column:
id_counter=0
responsibilities_df = pd.DataFrame(columns=['JobpostID','responsibilities'])
flag=0
respons=''
for eachjobpost in jobpost:
    wordList = re.sub("[^\w]", " ",  eachjobpost).split()
    for words in wordList:
        if "RESPONSIBILITIES" in words:
            flag=1
        if "QUALIFICATIONS" in words:
            flag=0
        if (flag == 1):
            respons+=words
            respons+=' '
    responsibilities_df.loc[id_counter] = [id_counter, respons]
    id_counter+=1
responsibilities_df.to_csv(r'results/Q3_b_Responsibilities.csv')

########################################################################################################################
# Q3 b) Extract Qualifications from the jobpost column:
id_counter=0
qualifications_df = pd.DataFrame(columns=['JobpostID','qualifications'])
flag=0
qualifications=''
for eachjobpost in jobpost:
    wordList = re.sub("[^\w]", " ",  eachjobpost).split()
    for words in wordList:
        if "QUALIFICATIONS" in words:
            flag=1
        if "REMUNERATION" in words:
            flag=0
        if (flag == 1):
            qualifications+=words
            qualifications+=' '
    qualifications_df.loc[id_counter] = [id_counter, qualifications]
    id_counter+=1
qualifications_df.to_csv(r'results/Q3_b_qualifications.csv')

########################################################################################################################
# Q3 b) Extract Remuneration from the jobpost column:
id_counter=0
remuneration_df = pd.DataFrame(columns=['JobpostID','Remuneration'])
flag=0
remuneration=''
for eachjobpost in jobpost:
    wordList = re.sub("[^\w]", " ",  eachjobpost).split()
    for words in wordList:
        if "REMUNERATION" in words:
            flag=1
        if "APPLICATION" in words:
            flag=0
        if (flag == 1):
            remuneration+=words
            remuneration+=' '
    remuneration_df.loc[id_counter] = [id_counter, remuneration]
    id_counter+=1
remuneration_df.to_csv(r'results/Q3_b_Remuneration.csv')

########################################################################################################################
# Q3 b) Extract Application Deadline from the jobpost column:
id_counter=0
application_deadline_df = pd.DataFrame(columns=['JobpostID','ApplicationDeadLine'])
for eachjobpost in jobpost:
    for line in eachjobpost.splitlines():
        if "APPLICATION DEADLINE" in line:
             print ("Jobpost ID: ",id_counter,"Application Deadline: ",line)
             application_deadline_df.loc[id_counter] = [id_counter, line]
    id_counter+=1
application_deadline_df.to_csv(r'results/Q3_b_application_deadline.csv')

########################################################################################################################
# Q3 b) Extract About Company from the jobpost column:
id_counter=0
aboutcompany_df = pd.DataFrame(columns=['JobpostID','AboutCompany'])
flag=0
company=''
for eachjobpost in jobpost:
    wordList = re.sub("[^\w]", " ",  eachjobpost).split()
    flag1=flag2=0
    for words in wordList:
        if "ABOUT" in words:
            flag1=1
        if "COMPANY" in words:
            flag2=1
        if (flag1 == 1) and (flag2 == 1):
            company+=words
            company+=' '
    aboutcompany_df.loc[id_counter] = [id_counter, company]
    id_counter+=1
aboutcompany_df.to_csv(r'results/Q3_b_application_aboutcompany.csv')




########################################################################################################################
# Q3.c Identify the company with the most number of job ads in the past 2 years
# Get the company name and the year "Assuming past two year 2015,2014"
company_year=data.iloc[:, [3,21]]
df1 = pd.DataFrame(columns=['Company', 'Year'])
res=[]
for index, row in company_year.iterrows():
    # Get the records of 2014 and 2015
    if (row['Year'] == 2015) or (row['Year'] == 2014):
        res.append(row['Company'])
# Convert list to dataframe
d = {'Company':res}
df = pd.DataFrame(d)
# Count the frequency in which the company has jobs in 2014 & 2015
f = open('results/Q3_c_largest_company.txt','w')
# write the result to the file
job_count=df['Company'].value_counts()
print(job_count, file=f)
f.close()
job_count_df=pd.DataFrame({'company':job_count.index, 'jobCount':job_count.values})
# print(job_count_df)
# Result Mentor Graphics Development Services CJSC  83

########################################################################################################################
# Q3 d) Identify the month with the largest number of job ads over the years
# Get the opening date field as it looks like the most clean one and assuming other date should be relevant to this date
openingdate=data.iloc[:, [16]]
# Sum the the number of jobs in each Month.
jan=openingdate.OpeningDate.str.contains('Jan').sum()
feb=openingdate.OpeningDate.str.contains('Feb').sum()
mar=openingdate.OpeningDate.str.contains('Mar').sum()
apr=openingdate.OpeningDate.str.contains('Apr').sum()
may=openingdate.OpeningDate.str.contains('May').sum()
jun=openingdate.OpeningDate.str.contains('Jun').sum()
jul=openingdate.OpeningDate.str.contains('Jul').sum()
aug=openingdate.OpeningDate.str.contains('Aug').sum()
sep=openingdate.OpeningDate.str.contains('Sep').sum()
octo=openingdate.OpeningDate.str.contains('Oct').sum()
nov=openingdate.OpeningDate.str.contains('Nov').sum()
dec=openingdate.OpeningDate.str.contains('Dec').sum()
# Create a list with all Months
months= [['jan',jan],['feb',feb],['mar',mar],['apr',apr],['may',may],['jun',jun],['jul',jul],['aug',aug],['sep',sep],['oct',octo],['nov',nov],['dec',dec]]
f = open('results/Q3_d_best_month.txt','w')
# write the result to the file, Number of jobs in the highest month.
print(max(months), file=f)
f.close()
best_month_df=pd.DataFrame({'Month':months.index, 'jobCount':months})
# print(best_month_df)

########################################################################################################################
# Q3. e) Clean text and generate new text from Job Responsibilities column:
# The new text shall not contain any stop words, and the plural words shall be converted into singular words.

# Get all stop words
stop_words = set(stopwords.words('english'))
# Generate the dataframe from the jop Responsibilities.
responsabilities=data.iloc[:, [12]]
counter_id=0
p = inflect.engine()
f = open('results/Q3_e_filtertext.txt','w')
filtered_text_df = pd.DataFrame(columns=['JobpostID','filteredText'])
for eachjobpost in responsabilities.iterrows():
    # tokanize all words in each element
    words = word_tokenize(' '.join(str(v) for v in eachjobpost[1].values))
    # initialize the result list
    wordsFiltered = []
    # loop to remove all stop words.
    for w in words:
        wordsFiltered = [w for w in words if not w in stop_words]
    wordsFiltered2=[]
    # Loop to replace plural with singular
    for w in wordsFiltered:
        if p.singular_noun(w):
            wordsFiltered2.append( p.singular_noun(w))
        else:
            wordsFiltered2.append(w)
        # wordsFiltered2 = [p.singular_noun(w) for w in words if p.singular_noun(w)]
    #
    # for word in wordsFiltered:
    #     if p.singular_noun(w):

    print(words,file=f)
    print(wordsFiltered2,file=f)
    print('###############################',file=f)
    print('###############################',file=f)
    # filtered_text_df = pd.DataFrame({'id': counter_id, 'text': wordsFiltered2})
    filtered_text_df.loc[counter_id] = [counter_id, wordsFiltered2]

    counter_id+=1
f.close()
print(filtered_text_df)
# type(eachjobpost)

########################################################################################################################
# Q3 f) Write functions to identify null/NA values and to replace null/NA values with a custom message in “Duration” column
duration=data.iloc[:,9]
# fill the null values with custom messade
duration.fillna('customer_message', inplace=True)
print(duration)

########################################################################################################################
# Q3 g) Store the results in a new Dataframe/SQL table(s)
# # List of all dataframes as below
# title_df
# duration_df
# location_df
# description_df
# responsibilities_df
# qualifications_df
# remuneration_df
# application_deadline_df
# aboutcompany_df
# job_count_df
# best_month_df
# filtered_text_df
# duration

from sqlalchemy import create_engine
engine = create_engine('mysql://username:password@host:port/database') #change to connect your mysql
#if you want to create a new table

title_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
duration_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
location_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
description_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
responsibilities_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
qualifications_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
remuneration_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
application_deadline_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
aboutcompany_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
job_count_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
best_month_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
filtered_text_df.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)
duration.to_sql(name='New SQL Table name',con=engine,if_exists='fail',index=False)

