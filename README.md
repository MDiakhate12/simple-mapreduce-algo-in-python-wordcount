# simple-mapreduce-algo-in-python-wordcount

This is a simple MapReduce algorithm written in python. 
This program splits the MapReduce algorithm into 4 parts:
 1. map.py: runs through the file taken as input and splits it into <K,V> pairs where each key is a word and each value is 1.
 2. sort.py: takes a <K,V> as input and sorts alphabetically by key
 3. groupByKey: takes a sorted <K,V> and produces a <K, list<V>> pairs grouped by keys with correponding values appended into a list
 4. reduceByKey: takes as input <K, list<V>> returns a <K, V> where each value is the sum of list elements
  
 To run the MapReduce job:
  ```shell  
  $ sudo chmod +x ./start_job.sh
  $ ./start_job.sh -f PATH/TO/YOUR/INPUT/FILE
  ```
