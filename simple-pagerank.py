from collections import Counter

in_nodes_map, out_nodes_count = {}, {}

with open("test_data.txt") as file:
    for index, line in enumerate(file):
        if index == 0:
            nodes_num = int(line[:-1]) #read first line which is the number of nodes in data 
        elif index <= nodes_num: 
            in_nodes_map[line[:-1]] = [] 
            out_nodes_count[line[:-1]] = 0    
        elif index > nodes_num+1:
            edges = line[:-1].split(" ") #split edges eg ABC->DEG
            in_nodes_map[edges[1]].append(edges[0]) #nodes as keys, nodes pointing at node as values
            out_nodes_count[edges[0]] += 1 #nodes as keys, count number of arrows pointing out from that node

scores = {} #set all scores to 100 
for node in in_nodes_map.keys():
    scores[node] = 100.00

converge = False 
while not converge: 
    new_scores = {}
    for node, in_nodes in in_nodes_map.items():
        new_scores[node] = sum(scores[in_node]/ out_nodes_count[in_node] for in_node in in_nodes)
        #set convergence - conditions made up by me 
        if 0 < abs(scores[node] - new_scores[node]) < 0.0001:  
            converge = True 
    scores, new_scores = new_scores, scores

print("\nPage Rank: ") 
for node, score in scores.items(): 
    print node, score  

print("\nTop 3 pages are: ")
print dict(Counter(scores).most_common(3)) #largest 5 values 