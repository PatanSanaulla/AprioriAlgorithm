#BruteForce Algorithm

MINIMUM_SUPPORT = 0.0

TRANSACTIONLIST = []

INDIVIDUAL_ITEM = []
INDIVIDUAL_ITEM_COST = []


def calculateSupportCount(ItemsList):
	itemsCount = [0] * len(ItemsList)
	for index, item in enumerate(ItemsList):
		for transaction in TRANSACTIONLIST:
			if (set(item) & set(transaction)) == set(item):
				itemsCount[index] += 1
				
	return(itemsCount)
    

def minimunSupport(items, count): 
	for index in range(len(items)-1, -1, -1):
		if float(count[index]/20.0) < MINIMUM_SUPPORT:
			count.pop(index)
			items.pop(index)

	return items,count

def generateNextFrequent(items):
	newItemsList = []
	for item in items:
		for ITEM in INDIVIDUAL_ITEM:
			setToRemoveDuplicates = set(list(item)+ITEM)
			if len(setToRemoveDuplicates) == len(item)+1:
				newList = list(setToRemoveDuplicates)
				newList.sort()
				if newList in newItemsList:
					continue
				else:
					newItemsList.append(newList)

	return newItemsList



def bruteForce(ItemsList):
	itemsCount = calculateSupportCount(ItemsList)
	minimunSupportItems, itemsCount = minimunSupport(ItemsList, itemsCount)
	print("----------------------------------------------------------")
	for i,val in enumerate(minimunSupportItems):
		print(val, "-> Support :", str(int((itemsCount[i]/20.0)*100)))
	if(len(minimunSupportItems) == 0):
		#found the end for the brute force algorithm
		print(ItemsList)
		return ItemsList
	else:
		nextItemSet = generateNextFrequent(minimunSupportItems)
		bruteForce(nextItemSet)



FileName = input("Please Enter the name of file with the transactions:\n")
file_input = open(FileName+".txt","r")
MINIMUM_SUPPORT = float(input("Please Enter the Minimum Support:\n"))


for transactionLine in file_input:
	transactionLine = transactionLine.split()
	TRANSACTIONLIST.append(transactionLine)
	for item in transactionLine:
		if [item] in INDIVIDUAL_ITEM:
			continue
		else:
			INDIVIDUAL_ITEM.append([item])

INDIVIDUAL_ITEM_COST = calculateSupportCount(INDIVIDUAL_ITEM)


finalresult = bruteForce(INDIVIDUAL_ITEM)
