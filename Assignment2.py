def magicise(child,previous,g,h,f):
	return (child,previous,g,h,f)
	
	
	
	
	
	
	

def func_3(e,n):
	for a,b,c,d,e in e:
		if n==a:
			return True
	return False









def checker(neighbours,path_till_now,frontier,explored_nodes):
	lenght = len(neighbours)
	cop = []
	for i in range(lenght):
		if(neighbours[i] > 0):
			cop.append(i)
	for i in range(len(cop)):
		j=cop.pop()
		if target(j,explored_nodes):
			continue
		else:
			path  = path_till_now.copy()
			path.append(j)
			newelement = (j,path)
			frontier.append(newelement)
	return None



	
	
	
	
	
	
def func_1(neighbours,path_cost_till_now, path_till_now,frontier):
	lenght = len(neighbours)
	for i in range(lenght):
		if(neighbours[i] > 0):
			sum_path = path_cost_till_now + neighbours[i]
			path = path_till_now.copy()
			path.append(i)
			newelement = (sum_path, path)
			frontier.append(newelement)
	return None
           
           
           
           
           

def f_5(exploredSet, node):
	for item in exploredSet:
		if item[0]==node:
			return item
	return
	
	
	
	
	
	
	
def target(start_point, goals):
	for n in goals:
		if (start_point == n):
			return 1
		else :
			continue
	return 0
    
    
    
    
    
    
    

def DFS_Traversal(cost, start_point, goals):
	l = []
	explored_nodes = list();
	l.append(start_point)
	if target(start_point,goals):
		return l
	node = start_point
    
	frontier = [(node , l)]
	while len(frontier) > 0:	
		r = frontier.pop()
		c_node, path_till_now = r[0],r[1]    
		if target(c_node,explored_nodes):
			continue
		else:
			explored_nodes.append(c_node)

			if target(c_node,goals):
				return path_till_now
			neighbours = cost[c_node]
			checker(neighbours, path_till_now,frontier,explored_nodes)
	return None









def UCS_Traversal(cost, start_point, goals):
	l = []
	explored_nodes = list()
	l.append(start_point)
	if target(start_point,goals):
		return l
	path_cost = 0
    
	frontier = [(path_cost , l)]
	while len(frontier) > 0:
		r = frontier.pop()
		path_cost_till_now, path_till_now = r[0], r[1]    
		current_node = path_till_now[-1] 
		if target(current_node,explored_nodes):
			continue
		else:
			explored_nodes.append(current_node)

			if target(current_node,goals):
				return path_till_now
			neighbours = cost[current_node]
			func_1(neighbours,path_cost_till_now, path_till_now,frontier)
			frontier.sort(reverse = True)

	return []










def A_star_Traversal(cost, heuristic, start_point, goals):
	l = []

	exploredSet=[]
	frontier=[]
	startinfo=magicise(start_point,None,0,heuristic[start_point],heuristic[start_point])
	frontier.append(startinfo)
	while len(frontier)>0:
		priorityNode=frontier[0]
		offset=0
		for index,node in enumerate(frontier):
			if  node[4] < priorityNode[4]:
				priorityNode=node
				offset=index
			elif node[4]==priorityNode[4]:
				if node[0]<priorityNode[0]:
					priorityNode=node
					offset=index


		frontier.pop(offset)
		exploredSet.append(priorityNode)
		childnodes=[]
		for index,rowvalue in enumerate(cost[priorityNode[0]]):
			if rowvalue not in [0,-1]:
				childnodes.append(index)
		for node in childnodes:
			if func_3(exploredSet,node):
				continue
			g=priorityNode[2] + cost[priorityNode[0]][node]
			h=heuristic[node]
			f=g+h
			newnode=magicise(node,priorityNode[0],g,h,f)
			done=0
			for i1,i2,i3,i4,i5 in frontier:
				if newnode[0]==i1:
					if newnode[4]<i5:
						frontier.remove((i1,i2,i3,i4,i5))
						frontier.append(newnode)
						done=1
			if not done:
				frontier.append(newnode)
 
	
	
	
	states=[]
	final=(0,None,0,0,0)
    
	for item in exploredSet:
		if item[0] in goals:
			states.append(item)
	if len(states)==0:
		final=(0,None,0,0,0)	
	else:
		final = min(states, key = lambda i : i[4]) 
	

	present=final
	if present==(0,None,0,0,0):
		return []
	while present[1] is not None:
		l.append(present[0])
		present = f_5(exploredSet, present[1])
	l.append(present[0])

	return l[::-1]
                   




'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you can call in the given fucntion
'''

def tri_Traversal(cost, heuristic, start_point, goals):
	l = []

	t1 = DFS_Traversal(cost, start_point, goals)
	t2 = UCS_Traversal(cost,start_point, goals)

    
	t3 = A_star_Traversal(cost, heuristic, start_point, goals)

	l.append(t1)
	l.append(t2)
	l.append(t3)
	return l

