import csv

file_path = 'C:/Users/Darkprincess/Hotel_Info/pankaj/Hotels.csv'
file = open(file_path)
Reader = csv.reader(file)
Data = list(Reader)
print(Data)