import csv
import pandas as pd
from collections import Counter


with open('dataset.csv',newline='') as f:
    file=csv.reader(f)
    file_data=list(file)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    num=file_data[i][2]

    new_data.append(float(num))


#mean
num_of_data=len(new_data)

total = 0

for z in new_data:
    total+=z

mean=total/num_of_data

print('Mean: ',mean)

#median
new_data.sort()

print(num_of_data)

if num_of_data % 2 == 0:
    median1=float(new_data[num_of_data//2])
    median2=float(new_data[(num_of_data//2)+1])

    median=(median1+median2)/2

else:

    median=float(new_data[num_of_data//2])

print('Median: ',median)

data=Counter(new_data)

mode_data= {
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0,
}

for weight,occurence in data.items():
    if 75 < float(weight) < 85:
        mode_data['75-85']+=occurence
    elif 85 < float(weight) < 95:
        mode_data['85-95']+=occurence
    elif 95 < float(weight) < 105:
        mode_data['95-105']+=occurence
    elif 105 < float(weight) < 115:
        mode_data['105-115']+=occurence
    elif 115 < float(weight) < 125:
        mode_data['115-125']+=occurence    
    elif 125 < float(weight) < 135:
        mode_data['125-135']+=occurence
    elif 135 < float(weight) < 145:
        mode_data['135-145']+=occurence   
    elif 145 < float(weight) < 155:
        mode_data['145-155']+=occurence    
    elif 155 < float(weight) < 165:
        mode_data['155-165']+=occurence
    elif 165 < float(weight) < 175:
        mode_data['165-175']+=occurence  

mode_range,mode_occurence = 0,0

for q,occurence in mode_data.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(q.split('-')[0]),int(q.split('-')[1])],occurence

print('mode range',mode_range)
mode=float((mode_range[0]+mode_range[1])/2)

print(mode_occurence)
print('Mode: ',mode)





