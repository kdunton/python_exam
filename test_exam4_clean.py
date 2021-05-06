from exam4_clean import *
  #import all code in exam4_clean.py

#usage: py.test

  
#testing with these input data:  
read = "ATTTGGATT"
k = 2


## for testing wrong input
import re
import sys
if not re.match("^[c('A','C','T','G')]*$", read):
      #if the read doesn't match these characters, throw an error
    print("Error: only letters A,C,T,G allowed")
    sys.exit()
      #exit the script and don't continue
    
if k > len(read):
  #give error if k is longer than the read length
    print("Error: k must be shorter than the read length")
    sys.exit()
if k <= 0:
    print("Error: k must be greater than 0")
    sys.exit()


#test the function for counting observed kmers; just add "test_" to the start of the normal function name
def test_count_kmers_observed():
  actual_result = len(count_kmers_observed(read, k)) #
  expected_result = 5 #get the expected result from the exam pdf file 
  assert actual_result == expected_result #assert tells you whether the actual and expected results match
 
  
#test the function for counting possible kmers
def test_count_kmers_possible():
  actual_result = count_kmers_possible(read,k) 
  expected_result = 8 #get this from exam pdf file 
  assert actual_result == expected_result


#test function for making df
def test_make_df():
  expected_result = pd.DataFrame(list(zip([1,2,3,4,5,6,7,8,9], [3,5,6,6,5,4,3,2,1], [4,8,7,6,5,4,3,2,1])), columns = ['k','observed kmers','possible kmers'])
     #manually make the table with the numbers you expect from the exam pdf file; this is your expected df
  expected_result.at['Total', 'observed kmers'] = expected_result['observed kmers'].sum() 
  expected_result.at['Total', 'possible kmers'] = expected_result['possible kmers'].sum() 
  
  make_df(read).eq(expected_result) #instead of assert, use .eq to see if two df are the same 


#test function for calculating LC
def test_calculate_LC():
  actual_result = calculate_LC(read) 
  expected_result = 0.875
  assert actual_result == expected_result 
