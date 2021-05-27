# CocCoc_hometest
Environment Specs:
Python 3, Pandas install.
First argument is path to the sample file (eg. ../../hash_catid_count.csv).


1. Problem 1 and 2:
Run this command:
`/Users/baduy9x/opt/anaconda3/bin/python /Users/baduy9x/Desktop/projects/CocCoc_hometest/problem_1.py ../../hash_catid_count.csv`

The result would be: 
15276 is the most frequent category
6 is the largest total counter category

For analyzing and visualize the data, we can create a pandas data frame such that contain 3 columns:
1: category
2: freq
3: total

From this data frame, we can analyze and visualize most of characteristics and features of our data.


For problem 2, freq for each category already calculated in freq_counter variable or can be accessed through df_stat.

About the data sample, we have 529 categories, which minimum freq is 1, maximum
frequent is 85467, and appear 1835 times for average. Most of category (80%) appear less then 1000 times but some categories appear frequently.
We can see that our data has some outlier, also for the total count. You can see
more when running the script.


2. Problem 3
This problem appears in database store engine when dealing with indexes.
Run the following command:
`/Users/baduy9x/opt/anaconda3/bin/python /Users/baduy9x/Desktop/projects/CocCoc_hometest/problem_3.py ../../hash_catid_count.csv`

Algo: Break data into small chunks, sort these small chunks, dump these sorted chunks to temp files.
After have temp files that contain sorted chunks. We use the algo like in merge sort to merge these chunks but use a priority queue for faster select best candidate.

The algorithm uses memory just enough and does not load all data from input file.
The final output is output.temp, you can open the file to see the result.
You can try to run this on larger file.







