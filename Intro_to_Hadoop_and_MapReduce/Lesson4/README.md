#### Solutions tasks from the Udacity Intro to MapReduce Lesson 4

##### 1. Inverted Index
Task: Count the number of occurrences of the word "fantastic" and print out the nodes
in which the word "fantastically" occurs in the provided forum data.

The actual lesson can be found here:

 https://www.udacity.com/course/viewer#!/c-ud617/l-713848763/m-719748756

1. Upload the provided forum data to hadoop using:
  * hadoop fs -mkdir forum
  * hadoop fs -put *.tsv forum/

2. Run the scripts in the provided virtual box using:
  * hs mapper_inverted_idx.py reducer_inverted_idx.py "forum/forum_node.tsv" count_words

3. Gather the output with
  * hadoop fs -cat count_words/part-00000


##### 2. Finding Mean
1. Upload the provided sales data (purchases.txt) to hadoop using:
  * hadoop fs -mkdir sales
  * hadoop fs -put purchases.txt sales/

2. Run the scripts in the provided virtual box using:
   hs mapper_mean_of_sales.py reducer_mean_of_sales.py  "input/purchases.txt" mean_of_sales

3. Output result
   hadoop fs -cat mean_of_sales/part-00000


##### 2. Finding Mean using combiner
1. Follow step 1 of 2. above

2. Add the bash function hsc as described in the lecture notes

3. Run the scripts in the provided virtual box using:
   hsc mapper_mean_of_sales.py reducer_combiner_mean_of_sales.py  "input/purchases.txt" mean_of_sales_combiner_hsc

4. Output result and look at the hadoop job webpage for the result
   hadoop fs -cat mean_of_sales_combiner_hsc/part-00000

