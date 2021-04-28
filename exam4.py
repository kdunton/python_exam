#!/usr/bin/env python3

#usage: python3 exam4.py -read ATTTGGATT -k 3

import pandas as pd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-read')
parser.add_argument('-k')
args = parser.parse_args()

#read = input("Enter read: ")
#print(read)
#k= int(input("Enter k: "))

read = args.read
k = int(args.k)



#### question 1 ####
# function to count kmers of size k
def count_kmers_observed(read, k):
    counts = {}
    num_kmers = len(read) - k + 1
    for i in range (num_kmers):
        kmer= read[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] +=1
    return counts
 
#print(len(count_kmers_observed(read, k)))
  


#### question 2 ####
# function to count possible kmers
#num_kmers = []
def count_kmers_possible(read, k):
  num_kmers = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
  #num_kmers.append(min(num_kmers1,num_kmers2))
  num_kmers = min(num_kmers1,num_kmers2)
  return(num_kmers)
#print(len(count_kmers_observed(read,k)))


def count_kmers_possible(read, k):
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
  num_kmers = min(num_kmers1,num_kmers2)
  return num_kmers


## function to create pandas df of possible and observed kmers ##
#get first column
k_values = []
 #make an empty list to append to
for i in range(1,len(read)+1):
  #loop through the length of the read
  #since len() doesn't include the last number in the range, add 1
  k_values.append(i)
   #append those into the list
#print(k_values)
 #check it works


#get second column
observed_kmers = []
#loop through each value of k and get the observed kmers from the count_kmers_observed function
#this time you use i as the input so you can get each iteration of k from k_values, rather than using the variable k which comes from command line
for i in k_values:
  observed_kmers.append(len(count_kmers_observed(read, i)))
#print(observed_kmers)


#get third column
possible_kmers = []
for i in k_values:
  possible_kmers.append(count_kmers_possible(read, i))
print(possible_kmers)
  
#create df
df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible_kmers'])
print(df)

