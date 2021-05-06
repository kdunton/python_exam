#!/usr/bin/env python3
  #this makes it so you don't have to type python3 before the script name when you go to run it

#usage: python3 exam4_clean.py


import pandas as pd
import argparse
#for error testing:
import re
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-filename', type = str)
args = parser.parse_args()


#### Question 1 ####
# function to count kmers of size k
def count_kmers_observed(read, k):
   '''
   Takes in sequence read and length of kmer, outputs number of observed kmers.
   '''
   counts = {}
      #create an empty dictionary to append counts for each kmer to
      #the kmer is the key, the count is the value
   num_kmers = len(read) - k + 1
      #the number of kmers you can have depends on this formula where you take the length of the read, then subtract k and add 1
   for i in range (num_kmers):
      #but since you might have some kmers with the same sequence, your observed kmers may be less than the actual
      #so this part is weeding out any duplicates
       kmer = read[i:i+k]
          #for each successive kmer, subset the read to that kmer based on the size of k
          #this is like a sliding window because you start at 1 and go to k, then start at 2 and go to k, etc.
       if kmer not in counts:
          #if the kmer is not already in the dictionary, assign it a value of 0 and add the kmer as the key
          counts[kmer] = 0
       else: continue
          #if the kmer is already in the dictionary, continue to the next i
   return counts
#print(len(count_kmers_observed(read, k)))


# function to count possible kmers
def count_kmers_possible(read, k):
   '''
   Takes in sequence read and length of kmer, outputs number of possible kmers.
   '''
   num_kmers1 = len(read) - k + 1
   num_kmers2 = 4**k
     #double asterick means to the power of
   num_kmers = min(num_kmers1,num_kmers2)
     #this takes the smallest value between these 2 variables
   return num_kmers
#print(len(count_kmers_observed(read,k)))



#### Question 2 - make a dataframe ####
# function for making df
def make_df(read):
   ''' 
   Takes in a sequence read, outputs a dataframe of the observed and possible number of kmers 
   for each kmer length.
   '''
   
   #first column
   k_values = []
     #make an empty list to append to
   for i in range(1,len(read)+1):
      #loop through the length of the read
      #since len() doesn't include the last number in the range, add 1
     k_values.append(i)
   
   #second column
   observed_kmers = []
   #loop through each value of k and get the observed kmers from the count_kmers_observed function
   for i in k_values:
     observed_kmers.append(len(count_kmers_observed(read, i)))
   
   #thid column
   possible_kmers = []
   #loop through each value of k and get the possible kmers from the count_kmers_possible function
   for i in k_values:
     possible_kmers.append(count_kmers_possible(read, i))
     
   #create the df
   df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
     #zip allows multiple lists to be combined into a dataframe 
     #the 'columns=' part sets the column names
   df.at['Total', 'observed kmers'] = df['observed kmers'].sum()
   df.at['Total', 'possible kmers'] = df['possible kmers'].sum()
     #make another row called 'Total' which is the sum of the two rows 'observed kmers' and 'possible kmers'
   df = df.astype({"observed kmers":'int', "possible kmers":'int'}) 
     #change columns to integer rather than float; can't change 'k' due to the NaN value in the totals row
   return(df)
  


#### Question 3 - calculate Linguistic Complexity ####
# function to calculate LC
def calculate_LC(read):
   '''
   Takes a sequence read, outputs the linguistic complexity.
   '''
   #run the df function to create the df, in order to get the sums
   df = make_df(read)
   #set x and y equal to the total of observed and possible kmers
   x = int(df.at['Total', 'observed kmers'])
   y = int(df.at['Total', 'possible kmers'])
   #calculate LC as x/y
   LC = (x/y)
   return(LC)
#print(calculate_LC(read))
 


#### Question 5- read in file and output results to files ####
# main function to run all above functions and output results to files
def main():
   '''
   Takes no arguments. It opens a file of sequences, loops through and generates output files stating
   linguistic complexity and a dataframe of the observed and expected kmers for each sequence in the file.
   '''
   #fn = open(args.filename)
     #open the file containing sequences
   fn = open("sequences.txt", "r")
   for i, sequence in enumerate(fn):
       #enumerate() allows you to iterate, and it returns both the index (i) and value (sequence) in the current iteration
       #so you iterate through each sequence in the file
       
     #throw an error if the read has other letters aside from ACTG
     if not re.match("^[c('A','C','T','G')]*$", sequence):
        print("Error: only letters A,C,T,G allowed")
        sys.exit()
     file_LC = open("sequence_%i_LC.txt" %i,"w")
       #open a file to write the LC to
       #%i means to substitute with the current value of the iteration into the filename
     LC = str(calculate_LC(sequence.rstrip()))
       #write() requires a string argument, can't have float
       #use rstrip to strip any whitespace to the right of the sequence
     file_LC.write(f"Sequence: {sequence}\n")
       #the f indicates that whatever is in the {} is a variable and not to be taken literally
       #this states which sequence corresponds to the LC value given on the next line
       #make a newline with \n
     file_LC.write(f"Linguistic complexity: {LC}") 
       #write the LC to the file
     df = make_df(sequence.rstrip()) 
       #create the df
     df.to_csv("sequence_%i_df.csv" %i, sep = '\t')
       #write the df to a tsv file
     file_LC.close()
   fn.close()


# call the function   
main()





