import json
with open('low_scorers.json', 'r') as fp:
    data = json.load(fp)
# del(data['117A1047'])
print(len(data))
with open('low_scorers.json', 'r') as fp:               #Here we take sequences of only top scorers
    low_scorers_data = json.load(fp)
##################Counting how many times each state was visited by all students######################

# This can help us decide which states we can choose for hidden states


count_UP=0
count_FG=0
count_GS=0
count_CR=0
count_RA=0
count_EV=0
count_REDO=0
count_RADO=0
count={"UP": 0, "FG": 0, "GS": 0, "CR": 0, "EV": 0, "RA": 0, "REDO": 0, "RADO": 0}
for student in data:
    count['UP']+=data[student].count('UP')
    count['FG']+=data[student].count('FG')
    count['GS']+=data[student].count('GS')
    count['CR']+=data[student].count('CR')
    count['RA']+=data[student].count('RA')
    count['EV']+=data[student].count('EV')
    count['REDO']+=data[student].count('REDO')
    count['RADO']+=data[student].count('RADO')



    count_UP+=data[student].count('UP')
    count_FG+=data[student].count('FG')
    count_GS+=data[student].count('GS')
    count_CR+=data[student].count('CR')
    count_RA+=data[student].count('RA')
    count_EV+=data[student].count('EV')
    count_REDO+=data[student].count('REDO')
    count_RADO+=data[student].count('RADO')

total_count=count_UP+count_FG+count_GS+count_RA+count_CR+count_RADO+count_REDO+count_EV
# print("UP: ",count_UP,"FG: ",count_FG, "GS: ",count_GS, "CR: ",count_CR,"EV: ",count_EV,"RA: ",count_RA,"REDO: ",count_REDO,"RADO: ",count_RADO)
# print(len(data))
# print(sum(count))
def prob_state(state):
    return count[state]/total_count
    
# print(prob_state("UP"))
# print(count)







########################################################################################################################
# This is the output:

# UP:  88 FG:  116 GS:  56 CR:  50 EV:  24 RA:  72 REDO:  13 RADO:  118

#Clearly UP, RADO, FG and RA had most visits. We may choose 3 or all 4 of them for hidden states(1...K) 



from first_layer_whole import create_bigrams
from first_layer_whole import trans_matrix

from first_layer_whole import obs_prob

bigram=create_bigrams()

# state_prev='FG'
# state_current='RADO'
# numerator=bigram.count((state_prev,state_current))
# denominator=count_FG
# # print("Hidden to Hidden: ",numerator/denominator)
def calc_hidden_state_prob(state_prev,state_current):
    numerator=bigram.count((state_prev,state_current))
    denominator=count[state_prev]
    return numerator/denominator
#We calculate P(O/Model) for each student
A1=trans_matrix()
# print(A1)
hidden_states=['UP','FG','GS','RADO']
prob_hmm={}
for student in low_scorers_data:
    prob_hmm[student]=1
for student in prob_hmm:
    for j in range(len(hidden_states)-1):
        prob_hmm[student]=prob_hmm[student]*(calc_hidden_state_prob(hidden_states[j],hidden_states[j+1]) * obs_prob(low_scorers_data[student],A1)) 


# for student in prob_hmm:
#     print(student, prob_hmm[student]*pow(10,21))



# print(max(prob_hmm.values()))


##############################    Emission Probability ######################
def calc_hidden_state_prob(state_prev,state_current):
    numerator=bigram.count((state_prev,state_current))
    denominator=count[state_prev]
    return round(numerator/denominator,2)

def emission_matrix():
    emission_mat={}
    for key in hidden_states:
        emission_mat[key]={}
    for key in emission_mat:
        emission_mat[key]={"UP": calc_hidden_state_prob(key,'UP'), "FG": calc_hidden_state_prob(key,'FG'), "GS": calc_hidden_state_prob(key,'GS'), "RADO": calc_hidden_state_prob(key,'RADO')}
    return emission_mat
B=emission_matrix()
with open('B_lowscorers.json', 'w') as fp:
    json.dump(B,fp)

