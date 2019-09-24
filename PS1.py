#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
coder1 = 'hello world! python line' + '1' # Simar
print(coder1)

# second group member's error to fix
coder2 = ['apple','banana', 'orange', 'pear']  # Annie

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
coder3 = 1.2 + 3.4 # Moaz
print(coder3)

# etc. until all group members have fixed and made 1 error
coder4 = 1 + 1.2 + 20 + 1.2 # Lauren
print(coder4)


#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt[4]

# and then use missing_rt to remove the trial from rt
clean_rt = del(rt[missing_rt])


# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]


# try the same procedure. Does it work? 
# use a comment to explain why or why not below in comments

missing_rt = rt_trouble[4,6]
clean_rt = del(rt[missing_rt])

# did not work as you can't index more than one integer. TypeError: list indices must be integers or slices, not tuple.



# now write an if statement that you can use to remove the frist missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.   

for x in rt_trouble:
  if x < 0:
    rt_trouble.remove(x)
print(rt_trouble)


# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

for element in data[0]:
  if element < 0:
    to_delete = data[0].index(element)
    del(data[0][to_delete])
del(data[1][to_delete])
del(data[2][to_delete])
print(data)

# Final Submission
