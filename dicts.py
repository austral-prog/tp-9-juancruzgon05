def create_inventory(items):
	dic=dict()
	for i in items:
		dic[i]= items.count(i)
	return dic



def add_items(inventory, items):
	for i in items:
		if i in inventory:
			inventory[i]+=1
		else:
			inventory[i]=1
	return inventory

def decrement_items(inventory, items):
	for i in items:
		if inventory[i]>0:
			inventory[i]-=1
		else:
			inventory[i]=0
	return inventory
def remove_item(inventory, item):
	if item in inventory:
		del inventory[item]
	return inventory

def list_inventory(inventory):
	x=[]
	for ele in inventory.items():
		if ele[1]!=0:
			x += [ele]
	return x




