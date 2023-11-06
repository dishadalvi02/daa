def knapsack_01(values, weights, capacity):
	n=len(values)
	table=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
	
	for i in range(1,n+1):
		for w in range(capacity+1):
			if weights[i-1]<=w:
				table[i][w]=max(table[i-1][w],table[i-1][w-weights[i-1]]+values[i-1])
			else:
				table[i][w]=table[i-1][w]

	selected_items=[]
	i,w = n,capacity
	while i>0 and w>0:
		if table[i][w] != table[i-1][w]:
			selected_items.append(i-1)
			w-=weights[i-1]
		i-=1
	return table[n][capacity], selected_items
	
	

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_01(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)