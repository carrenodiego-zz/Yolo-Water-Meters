import csv

# names of files to read from
r_filenameTSV = '.\data\data.tsv'

# data structures to hold the data

tsv_labels = []
tsv_data = []


with open(r_filenameTSV, 'r') as tsv_in:
    tsv_reader = csv.reader(tsv_in, delimiter='\t')

    tsv_labels = tsv_reader.__next__()
   
    for record in tsv_reader:
        tsv_data.append(record)

# print the labels
#print(tsv_labels, '\n')

# print the first 10 records
print(type(tsv_data[0][2]),'\n')