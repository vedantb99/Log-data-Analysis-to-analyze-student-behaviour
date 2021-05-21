import json

with open('A_topscorers.json', 'r') as fp:
    A_topscorers_data = json.load(fp)
import networkx as nx
G=nx.Graph()
i=0
for state in A_topscorers_data:
    G.add_node(state,pos=(i,i))
    i+=1
edge_list=[]
weights=[]
# for state in A_topscorers_data:
#     if(state=='RADO' or state=='REDO' or state=='RA'):
#         continue
#     j=0

#     for value in A_topscorers_data[state]:
#         if(A_topscorers_data[state][value]!=0):
# #             print((round(A_topscorers_data[state][value]*100,2)))
#             if(round(A_topscorers_data[state][value]*100,2)<15.0):
# #                 edge_list.remove()
# #                 print(state,value,": ",A_topscorers_data[state][value])
#                 continue
#             else:
# #                 print(state,value,": ",A_topscorers_data[state][value])

#                 edge_list.append((i,j))
#                 weights.append(str(round(A_topscorers_data[state][value]*100,2))+"%")
#                 G.add_edge(state,value)
#             j+=1
#         i+=1



state_list=[state for state in A_topscorers_data]
edge_l=[]
for i in state_list[:5]:
    # print(A_topscorers_data[i]['REDO'])
    for j in state_list:
        if(A_topscorers_data[i][j]!=0):
            wt=round(A_topscorers_data[i][j]*100,2)
#             print((round(A_topscorers_data[state][value]*100,2)))
            if(round(A_topscorers_data[i][j]*100,2)>5.0 or j=='REDO'):
                G.add_edge(i,j,weight=wt)
                edge_l.append((i,j))


val_map = {'RA': 1.0,
           'RADO': 0.5714285714285714,
           'REDO': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

# print(len(G.edges()))
import matplotlib.pyplot as plt
# nx.draw(G,with_labels = True)
# pos = nx.spring_layout(G)
# nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)


# plt.show()


pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=edge_l, edge_color='r', arrows=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()