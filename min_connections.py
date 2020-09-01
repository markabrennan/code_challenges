"""
Question #2 from Amazon Coding Challenge,
as described on Leet Code blog post:
https://leetcode.com/discuss/interview-question/797541/amazon-online-assessment-2-sde-1-new-graduate-2021-coding-2-questions-with-solutions

It appears to be a graph problem - minimum path.
"""

from collections import deque

class Node:
    def __init__(self, name=""):
        self.name = name
        self.children = []
    

def min_connection_cost(connections, num):
    node_connections = {}
    for conn in connections:
        server1 = conn[0]
        server2 = conn[1]
        cost = conn[2]
        if server1 not in node_connections:
            node = Node(server1)
            node.children.append((server2, cost))
            node_connections[server1] = node
        else:
            node_connections[server1].children.append((server2, cost))
           
        if server2 not in node_connections:
            node = Node(server2)
            node.children.append((server1, cost))
            node_connections[server2] = node
        else:
            node_connections[server2].children.append((server1, cost))

    min_costs = []    
    for node, conns in node_connections.items():
        pass
    return node_connections

def min_conns2(connections, num):
    # make an adjacency list, but don't
    # use a custom class, rather, simply
    # a dict for each node, and a list of adjacent
    # nodes and associated costs
    graph = {}
    for node1, node2, cost in connections:
        if node1 not in graph:
            graph[node1] = [(node2, cost)]
        else:
            graph[node1].append((node2, cost))
    nodes = [node for node in graph.keys()]

    # now, for each distinct node, find the shortest
    # path of all of its adjacent nodes and pair themnj
    nodes.sort()
    print(nodes)
    min_cost = []
    for node in nodes:
        min_node = min(graph[node], key=lambda x: x[1])[0]
        min_cost.append((node, min_node))

    return min_cost


def bfs(connections):
    Q = deque()
    unique_nodes = set()
    # we still need to create the graph (adjacency list):
    graph = {}
    for node1, node2, cost in connections:
        if node1 not in graph:
            graph[node1] = [(node2, cost)]
        else:
            graph[node1].append((node2, cost))
    # now assume we are looking to get from "A" to "E"
    # let's do a BFS from "A" to "E"
    start_node = "A"
    end_node = "E"
    unique_set = set(start_node)
    path = {start_node:None}
    Q.append(start_node)
    while Q:
        cur_node = Q.popleft()
        if cur_node == end_node:
            break
        for neighbor, _ in graph[cur_node]:
            if neighbor not in unique_set:
                unique_set.add(neighbor)
                Q.append(neighbor)
                path[neighbor] = cur_node

    shortest_path = []
    cur_node = end_node
    while cur_node:
        shortest_path.append(cur_node)
        cur_node = path[cur_node]
    shortest_path.reverse() 
    return shortest_path


"""
TEST CASES

connections denote:
node (server) --> node (servier) --> cost
"""
num = 5
connections = [
     ["A","B",1],
 	 ["B","C",4],
 	 ["B","D",6],
 	 ["D","E",5],
 	 ["C","E",1]
    ]

print(connections)
#print(min_connection_cost(connections, num))

#print(min_conns2(connections, num))

print(bfs(connections))
