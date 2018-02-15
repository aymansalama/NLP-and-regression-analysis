# Owner: Ayman Salama
# Email: ayman3salama@gmail.com
# Q2. Sales Data Exploration and Analysis (code in python)

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Upload the csv file from the directory
sales = pd.read_csv('Sales_Transactions_Dataset_Weekly.csv')

# Get the product data for all weeks W0 - W51
product_sales = sales.iloc[:, 0:53] 
########################################################################################################################
# a) Write code to download the following Kaggle dataset:
# Weekly Sales Transaction Data: https://www.kaggle.com/crawford/weekly-sales-transactions
# From Linux command line
# Get kaggle API KEY from the account
# Install the file in ~/.kaggle/kaggle.json
# kaggle datasets download -d crawford -f weekly-sales-transactions.csv
# Note: the command download work with other repository
# but didn't work with this particular file, May be I am missing something

########################################################################################################################
# Q2.b Get the Median of each product, Megre the Median result with the product ID
product_median_tmp = pd.concat([sales.iloc[:, 0] , product_sales.median(axis=1)], axis=1)
product_median = pd.DataFrame(product_median_tmp).reset_index()
product_median.columns = ['ID','Product_Code', 'Median']
# Save the product Median to CSV
product_median.to_csv('results/Q2_b_product_median.csv')

########################################################################################################################
# Q2.b Get the Mean of each product, Megre the Mean result with the product ID
product_mean_tmp = pd.concat([sales.iloc[:, 0] , product_sales.mean(axis=1)], axis=1)
product_mean = pd.DataFrame(product_mean_tmp).reset_index()
product_mean.columns = ['ID','Product_Code', 'Mean']
# Save the product Mean to CSV
product_mean.to_csv('results/Q2_b_product_mean.csv')

########################################################################################################################
# Q2.b Get the Min of each product, Megre the Min result with the product ID
product_min_tmp = pd.concat([sales.iloc[:, 0] , product_sales.min(axis=1)], axis=1)
product_min = pd.DataFrame(product_min_tmp).reset_index()
product_min.columns = ['ID','Product_Code', 'Min']
# Save the product Min to CSV
product_min.to_csv('results/Q2_b_product_min.csv')

########################################################################################################################
# Q2.b Get the Max of each product, Megre the Max result with the product ID
product_max_tmp = pd.concat([sales.iloc[:, 0] , product_sales.max(axis=1)], axis=1)
product_max = pd.DataFrame(product_max_tmp).reset_index()
product_max.columns = ['ID','Product_Code', 'Max']
# Save the product Max to CSV
product_max.to_csv('results/Q2_b_product_max.csv')

########################################################################################################################
# Q2.c Get the Best Performing Peoduct (Based on volume)
# Get the dataframe of the mean of each product and get the highest value in mean.
# Open file to store the results
f = open('results/Q2_c_best_perform.txt','w')
# calculate the highest mean of all products from the mean dataframe
best=product_mean.loc[product_mean['Mean'].idxmax()]
# write the result to the file
f.write(best.to_string())
f.close()
# Result Product_Code       P409
# Mean            42.6923

########################################################################################################################
# Q2.d Identify the most promising product
# We will use regression analysis slope to determine the promising product
# Upload the csv to dataframe
sales = pd.DataFrame(np.genfromtxt('Sales_Transactions_Dataset_Weekly.csv',  dtype=None, delimiter=',', names=True) )
# Get the 51 weeks data
product_sales = sales.iloc[:, 0:53] 
# create a numeric weekely counter will be used in slop calculation
y =np.array(list(range (0 , 52)))
# Create a counter from the number of product by counting the rows, as some product IDs are missing
count=product_sales.count(axis=0, numeric_only=True)
counter=count.iloc[0]
# initialize the array
slope_result=[]
# For loop in the array of product.
for i in range(counter):
    # construct weekly data for each product
    x=product_sales.iloc[i].tolist()
    # delete the name of the product from the array
    del x[0]
    # conver X to array to be used in linear regression
    x = np.asarray(x)
    # Calculate the slop
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    # Append the result of the slop and the product id to an array
    slope_result.append([product_sales.iloc[i].tolist()[0],slope])
# sorting the slope of products
sorted_slop_result = sorted(slope_result, key=lambda x: x[1])
# get the most emerging prodcut 
emerging=sorted_slop_result[-1]
# Open file to store the results
f = open('results/Q2_d_best_emerging.txt','w')
# write the result to the file
for item in emerging:
  f.write("%s  " % item)
f.close()
# Result [b'P251', 22.941176470588236]

########################################################################################################################
# Q2.e Identify the top 5 worst performing products on a biweekly basis
# Upload the csv to dataframe
sales = pd.DataFrame(np.genfromtxt('Sales_Transactions_Dataset_Weekly.csv',  dtype=None, delimiter=',', names=True) )
# Get the 51 weeks data
product_sales = sales.iloc[:, 1:53] 
# Get the product code only to be used to create a dataframe of biweekly analysis
product_code=sales.iloc[:,0:1]

# Create counters for each week
count1=0
count2=2
array=[]
# Loop in 26 biweeks, which is 52 weeks
for i in range(26):
    # Get the mean value of every two weeks and create an array
    biweekly_value = product_sales.iloc[:, count1:count2].mean(axis=1)
    # join the resulted array from previous step of the mean of two weeks to the product code, and keep looping to fill all weeks
    product_code = pd.concat([product_code, biweekly_value.to_frame(i+1)], axis=1, join='inner')
    # increment the counters
    count1+=2
    count2+=2

# intial weeks
f = open('results/Q2_e_biweekly.txt','w')
# write the result to the file
f.write("\nWeek 1,2")
# loop in all weeoks (biweekly)
for i in range(1,27):
    # sort the extracted biweekly value and get the least five product IDs
    print(product_code.sort_values(by=[i]).iloc[:5, 0:1], file=f)
    # print(product_code.sort_values(by=[i]).iloc[:5, 0:1])
    if (i != 26):
        # Print the weeks number like 1,2 3,4 5,6 etc and stop at the last step in the loop
        print("\nWeek", (i*2)+1,",",(i*2)+2, file=f)
f.close()

########################################################################################################################
#Q2. f) Identify outliers from the data and output the corresponding week numbers
# We will identify Outliers Using Normal Distribution and Standard Deviation
# This is done by extracting points that were above (Mean + 3*SD) and any points below (Mean - 3*SD) 
weekcounter=0
f = open('results/Q2_f_outliers.txt','w')
for column in product_sales:
    # Print Week number
    print ("\n Week No.", weekcounter, file=f)
    # Intilize daaframe with product code only to be merged every loop with on week data
    product_code2 = sales.iloc[:,0:1]
    # Get the weekly data for each loop
    eachweek=product_sales[column]
    # Concatenate the product code with each week data
    product_code2 = pd.concat([product_code2, eachweek.to_frame(weekcounter)], axis=1, join='inner')
    # Get the mean and Standard Deviation for each week
    mean = np.mean(eachweek, axis=0)
    sd = np.std(eachweek, axis=0)
    # Loop in the weekly data with its product code
    for index, row in product_code2.iterrows():
        # This is done by extracting points that were above (Mean + 3*SD) and any points below (Mean - 3*SD) 
        if (row[weekcounter] < (mean - 3 * sd)) or (row[weekcounter] > (mean + 3 * sd)) :
            # Print the product code and the weekly data associated to it.
            print (row['Product_Code'], row[weekcounter],file=f)
    # Counter increment. 
    weekcounter+=1
f.close()


