#!/usr/bin/python
import sys

salesTotal = 0
oldKey = None

total=0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        #continue

    thisKey, thisSale = data_mapped
    #store,item,cost,payment=data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    #if oldKey and oldKey != thisKey:
        #print(oldKey+"\t"+str(salesTotal))
        #oldKey = thisKey;
        #salesTotal = 0
    total = float(total) + float(thisSale)


    #oldKey = thisKey
    #salesTotal += float(thisSale)

# Escribe o ultimo par, unha vez rematado o bucle
#if oldKey != None:
 #   print(oldKey+"\t"+str(salesTotal))

#Ficheiro de probas


print(total)
