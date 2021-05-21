import json
import numpy as np
import pandas as pd
#importing the redo_sequences or observationn sequences from data.json
# with open('data.json', 'r') as fp:            //we are taking sequences of all students
#     data = json.load(fp)

with open('low_scorers.json', 'r') as fp:               #Here we take sequences of only top scorers
    data = json.load(fp)
seq_list=[[]*len(data) for i in range(len(data))]
i=0
for student in data:
    seq_list[i]=data[student]
    i+=1

def create_bigrams():
    bigrams=[]
    for seq in seq_list:
        for i in range(len(seq)-1):
            bigrams.append((seq[i],seq[i+1]))
        
    return bigrams

labels=["UP", "FG", "GS", "CR", "EV", "RA","REDO","RADO"]

def calc_prob(state_prev,state_current):
    bigrams=create_bigrams()
    numerator=bigrams.count((state_prev,state_current))
    denominator=0
    for seq in seq_list:
        denominator+=seq.count(state_prev)
    # print(denominator)
    # print(denominator)

    # if(seq_list.count(state_prev)==0):
    #     return 0
    # else:
    return (round(numerator/denominator,2))
   
def trans_matrix():
    trans_mat={}
    trans_array=np.array([])
    for key in labels:
        trans_mat[key]={}
    for key in trans_mat:
        trans_mat[key]={"UP": calc_prob(key,'UP'), "FG": calc_prob(key,'FG'), "GS": calc_prob(key,'GS'), "CR": calc_prob(key,'CR'), "EV":calc_prob(key,'EV'), "RA":calc_prob(key,'RA'),"REDO": calc_prob(key,'REDO'),"RADO": calc_prob(key,'RADO')}
    
    return trans_mat

def obs_prob(obs_seq,trans_mat):
    prob=1
    for i in range(1,len(obs_seq)):
        prob=prob*trans_mat[obs_seq[i-1]][obs_seq[i]]
    return prob

A=trans_matrix()
# print((obs_prob(data['117A1009'],A)))
# print(A)
with open('A_lowscorers.json', 'w') as fp:
        json.dump(A,fp)
# print(seq_list[0].count('UP'))



###############################   Finding Parameters for Top Scorer dataset ################################

