## Files:
- exam4_clean.py: this is the script that reads in a file of sequences and outputs separate files for each sequence, one for the linguistic complexity and one for a table of kmer values.
  - usage: python3 exam4_clean.py
  - output:
    - sequence_index_LC.txt: lists the linguistic complexity for a sequence at index 0 or 1 in the file
    - sequence_index_df.csv: lists the table of kmer counts for a sequence at index 0 or 1 in the file
- test_exam4_clean.py: this is the test script for exam4_clean.py. It tests the functions in exam4_clean.py, using a read of ATTTGGATT and k of 2.
  - usage: py.test
- sequences.txt: file containing read sequences.
