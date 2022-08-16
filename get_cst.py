#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:42:02 2022
Modified in Aug 2022
@author: ahmed elsherbini
"""
import pandas as pd 
import seaborn as sns_plot
import seaborn as sns
import matplotlib.pyplot as plt
#from matplotlib.pyplot import  bar_label
import argparse

##################################################################
my_parser = argparse.ArgumentParser(description='Make sure your files exsit in the same data folder!')
my_parser.add_argument('-i','--input',
                       action='store',
                       metavar='input',
                       type=str,
                       help='the path to your file')
##################################################################
args = my_parser.parse_args()
f_name = args.input

abundances = pd.read_csv(f_name, sep='\t',skiprows=0,index_col=0)

mylist =  []
##################################################################
for i in abundances:
     max_index = abundances[i].idxmax()
     if "aureus" in max_index:
         mylist.append([i,"CST1"])
     elif "Enterobacteriaceae"  in max_index:
          mylist.append([i,"CST2"])
     elif "epidermidis"  in max_index:
          mylist.append([i,"CST3"])
     elif "Cutibacterium"  in max_index:
          mylist.append([i,"CST4"])
     elif "Corynebacterium"  in max_index:
          mylist.append([i,"CST5"])
     elif "Moraxella"  in max_index:
          mylist.append([i,"CST6"])
     elif "Dolosigranulum"  in max_index:
          mylist.append([i,"CST_7"])
     else:
          mylist.append([i,"Unclassified"])
##################################################################

df = pd.DataFrame(mylist)

df = df.rename(columns={'Community state type (CST)': 'Count'})
df = df.rename(columns={0:"Sample_name", 1: "CST"})

rel_df = pd.DataFrame(df["CST"].value_counts(normalize=True))

rel_df.plot(kind = 'bar',legend=False,rot=0)
#plt.xticks(rotation=30, horizontalalignment="center")
plt.title("CST types")
plt.ylabel("Relative abundace")

df.to_csv('Samples_CST.csv', index=False)
rel_df.to_csv('CST_comp.csv', index=True)
plt.savefig('CST_barplot.png')   
