'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random


def ln(x):
	n = 10000.0
	return n * ((x ** (1/n)) - 1)
    

def logarithm(x, base):
	
	return (ln(x)/ln(base)) 	#changing the base
	
	
	
	
		

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
	
	entropy = 0.0
	
	p = 0
	n = 0
	
	target_value_1 = df[df.columns[len(df.columns)-1]][0]
	
	for i in df[df.columns[len(df.columns)-1]]: 	
		if(i == target_value_1):	# p and n are interchangeable, target value can take only 2 values
			p += 1
		else:
			n += 1
	
	entropy = -( p/(p+n) * logarithm((p/(p+n)), 2) + n/(n+p) * logarithm((n/(n+p)), 2)) 
	
	
	return entropy












# Entropy of an attribute is same as the average information

'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large






def get_entropy_of_attribute(df,attribute):
	entropy_of_attribute = 0.0
	
	p = 0
	n = 0
	

	target_value = df[df.columns[len(df.columns)-1]][0]
	
	for i in df[df.columns[len(df.columns)-1]]: 	
		if(i == target_value):	# p and n are interchangeable, target value can take only 2 values
			p += 1
		else:
			n += 1
	

	possible_values = []	# To get all the possible values the attribute can take
	
	for i in df[attribute]:
		if i not in possible_values:
			possible_values.append(i)

	to_add = []

	for value in possible_values:
		list_1 = []
				
		for ind in df.index:
			if (value == df[attribute][ind]):		
				list_1.append(df[df.columns[len(df.columns)-1]][ind])
				

				
		p_1 = 0
		n_1 = 0
	
		target_value_1 = list_1[0]
		
		
		for i in list_1: 	
			if(i == target_value_1):	# p and n are interchangeable, target value can take only 2 values
				p_1 += 1
			else:
				n_1 += 1
		
		entropy = -( p_1/(p_1+n_1) * logarithm((p_1/(p_1+n_1)), 2) + n_1/(n_1+p_1) * logarithm((n_1/(n_1+p_1)), 2)) 
		
		
		a = (p_1 + n_1) / (p + n) * entropy
		
		to_add.append(a)
		
	
	for i in to_add:
		entropy_of_attribute += i 				
		
	
	
	return abs(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
	#input:pandas_dataframe,str
	#output:int/float/double/large
def get_information_gain(df,attribute):
	
	information_gain = 0.0
	
	information_gain = get_entropy_of_dataset(df) - get_entropy_of_attribute(df,attribute)
	
	
	return information_gain



''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
   
	information_gains={}
	selected_column=''
	
	
	list_2 = []					
			
	for i in df:
		list_2.append(i)
	
	

	for i in range(len(list_2)-1):
		information_gains[list_2[i]] = get_information_gain(df, list_2[i])
		
	selected_column = max(information_gains, key=information_gains.get)
		
	
	

	'''
	Return a tuple with the first element as a dictionary which has IG of all columns 
	and the second element as a string with the name of the column selected

	example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
	'''

	return (information_gains,selected_column)



'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''
