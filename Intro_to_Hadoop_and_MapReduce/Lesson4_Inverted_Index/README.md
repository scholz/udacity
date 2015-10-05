#### Solution to the Inverted Index task from the Udacity Intro to MapReduce Lesson 4

Task: Count the number of occurrences of the word "fantastic" and print out the nodes
in which the word "fantastically" occurs in the provided forum data.

The actual lesson can be found here:

 https://www.udacity.com/course/viewer#!/c-ud617/l-713848763/m-719748756

1. Upload the provided forum data to hadoop using:
  * hadoop fs -mkdir forum
  * hadoop fs -put *.tsv forum/

2. Run the scripts in the provided virtualbox using:
  * hs mapper_count_words.py reducer_count_words.py "forum/forum_node.tsv" count_words

3. Gather the output with
  * hadoop fs -cat count_words/part-00000
