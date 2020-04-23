#Apriori Algorithm

MINIMUM_SUPPORT = 0.0
MINIMUM_CONFIDENCE = 0.0

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

def generateNextFrequent(items, count):
	newItemsList = []
	confidenceList = []
	for index, item in enumerate(items):
		for i in range(index+1,len(items)):
			for value in item:
				setToRemoveDuplicates = set(list(items[i]+[value])) 
				if len(setToRemoveDuplicates) == len(item)+1:
					newList = list(setToRemoveDuplicates)
					newList.sort()
					if newList in newItemsList:
						continue #already in the list
					else:
						Confidence = float(count[i]/INDIVIDUAL_ITEM_COST[INDIVIDUAL_ITEM.index([value])])
						if(Confidence >= MINIMUM_CONFIDENCE):
							confidenceList.append(Confidence) 
							newItemsList.append(newList)
        
	return newItemsList, confidenceList


def apriori(ItemsList):
	itemsCount = calculateSupportCount(ItemsList)
	minimunSupportItems, itemsCount = minimunSupport(ItemsList, itemsCount)
	print("----------------------------------------------------------")
	for i,val in enumerate(minimunSupportItems):
		print(val, "-> Support :", str(int((itemsCount[i]/20.0)*100)))
	if(len(minimunSupportItems) == 0):
		#found the end for the apriori algorithm
		print(ItemsList)
		return ItemsList
	else:
		nextFrequrentItemSet, confidenceList = generateNextFrequent(minimunSupportItems, itemsCount)
		apriori(nextFrequrentItemSet)



FileName = input("Please Enter the name of file with the transactions:\n")
file_input = open(FileName+".txt","r")
MINIMUM_SUPPORT = float(input("Please Enter the Minimum Support:\n"))
MINIMUM_CONFIDENCE = float(input("Please Enter the Minimum Confidence:\n"))


for transactionLine in file_input:
	transactionLine = transactionLine.split()
	TRANSACTIONLIST.append(transactionLine)
	for item in transactionLine:
		if [item] in INDIVIDUAL_ITEM:
			continue
		else:
			INDIVIDUAL_ITEM.append([item])

INDIVIDUAL_ITEM_COST = calculateSupportCount(INDIVIDUAL_ITEM)


finalresult = apriori(INDIVIDUAL_ITEM)
