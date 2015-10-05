The mapper and reduce scripts for Udacity Intro to MapReduce Lesson 4
Task: Inverted Index

On the forum data count the number of occurrences
of the word "fantastic" and print out the nodes for the
word "fantastically".

The actual lesson can be found here:

 https://www.udacity.com/course/viewer#!/c-ud617/l-713848763/m-719748756

- Uploading the forum data to hadoop using:
hadoop fs -mkdir forum
hadoop fs -put *.tsv forum/

Run the scripts in the provided virtualbox using:
hs mapper_count_words.py reducer_count_words.py "forum/forum_node.tsv" count_words

And gather the output with
hadoop fs -cat count_words/part-00000
