def fractional_k(item,capacity):
	total_value=0.0
	selected_item=[]
	for item in items:
		item['ratio']=item['value']/item['weight']
	items.sort(key=lambda x:x['ratio'],reverse=True)

	for item in items:
		if capacity>=item['weight']:
			capacity-=item['weight']
			total_value+=item['value']
			selected_item.append((item['weight'],item['value']))
		else:
			fraction=capacity/item['weight']
			capacity-=fraction*item['weight']
			total_value+=fraction*item['value']
			selected_item.append((fraction*item['weight'],fraction*item['value']))
	return selected_item,total_value

			
			
	

n=int(input("enter the total no of items:"))
weight=values=items=[]
for i in range(n):
	weight=float(input(f"enter the weight for {i+1} item:"))
	value=float(input(f"enter the value for {i+1} item:"))
	items.append({'weight':weight,'value':value})
capacity=int(input("enter the capacity of the bag:"))
selected_items,total_value=fractional_k(items,capacity)
print("selected_items",selected_items)
print("total_value",total_value)

	