import json
import numpy as np
import pandas as pd
#importing the redo_sequences or observationn sequences from data.json
with open('data.json', 'r') as fp:
    data = json.load(fp)

row1=data['117A1004']
labels=["UP", "FG", "GS", "CR", "EV", "RA","REDO","RADO"]
bigrams=[]
for i in range(len(row1)-1):
    bigrams.append((row1[i],row1[i+1]))

def calc_prob(state_prev,state_current):
    numerator=bigrams.count((state_prev,state_current))
    if(row1.count(state_prev)!=0):
        
        return (round(numerator/row1.count(state_prev),2))
    else:
        return 0
    
# def calc_stationary_prob(trans_mat):
#     l = [ []*8 for i in range(8)]
#     i=0
#     for k1,v1 in trans_mat.items():
#         for k2,v2 in v1.items():
#             l[i].append(v2)
#         i+=1
#     a=np.array(l)
#     b=a.dot(a)
#     while(not(np.array_equal(a,b))):
#         a=b.copy()
#         b=np.dot(b,a)
#     i=0
#     print(a)
#     for key in trans_mat:
#         trans_mat[key]={"UP": b[i][0], "FG": b[i][1], "GS":b[i][2], "CR": b[i][3], "EV": b[i][4], "RA": b[i][5],"REDO": b[i][6],"RADO": b[i][7]}
#         i+=1
#     return trans_mat

def trans_matrix(seq):
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
    return round(prob,12)

labels=["UP", "FG", "GS", "CR", "EV", "RA","REDO","RADO"]

# for key in trans_mat:
#     trans_mat[key]={"UP": 0, "FG": 0.1, "GS": 0.1, "CR": 0.1, "EV": 0.1, "RA":0.1,"REDO": 0.1,"RADO": 0.1}
# for key in trans_mat:
#     print(key,": ",trans_mat[key])

trans_mat=trans_matrix(row1)
# print(trans_matrix(row1))

# print(trans_mat)
with open('A.json', 'w') as fp:
    json.dump(trans_mat,fp)

print(obs_prob(row1,trans_mat))