#hw1

# Part. 1
# Import module
# csv -- fileIO operation
import csv

# Part. 2
# Read cwb weather data
cwb_filename = '106061255.csv'
data = []
header = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

# Part. 3
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.

whole_press = 0   # Declare a variable to store the value
a = 0             # Declare a variable to use later

# Remove the data whose value of the PRES column is '-99.000' or '-999.000'.

pres = []         # Store the data we want
pres = [i for i in data if not ((i['PRES'] == '-99.000')|(i['PRES'] == '-999.000'))]

# Store the data we want
target_C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', pres))
target_C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', pres))
target_C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', pres))
target_C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', pres))   
target_C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', pres))

# Sum up the pres value and calculate the mean
# Then store the value we want into target_data
# Print it in order
target_data = []

for i in range(len(target_C0A880)):
   whole_press = whole_press + float(target_C0A880[i]['PRES'])
   a = 1

target_data.append('COA880')
if a == 1:
   target_data.append(whole_press/len(target_C0A880))
else:
   target_data.append('\'None\'')
print('[',end='')
print(target_data,',',end='')


target_data = []     # Reset the list
whole_press = 0      # Reset the varible
a = 0                # Reset the varible

for i in range(len(target_C0F9A0)):
   whole_press = whole_press + float(target_C0F9A0[i]['PRES'])
   a = 1
target_data.append('C0F9A0')
if a == 1:
   target_data.append(whole_press/len(target_C0F9A0))
else:
   target_data.append('\'None\'')
print(target_data,',',end='')


target_data = []     # Reset the list
whole_press = 0      # Reset the varible
a = 0                # Reset the varible

for i in range(len(target_C0G640)):
   whole_press = whole_press + float(target_C0G640[i]['PRES'])
   a = 1
target_data.append('C0G640')
if a == 1:
   target_data.append(whole_press/len(target_C0G640))
else:
   target_data.append('\'None\'')
print(target_data,',',end='')


target_data = []     # Reset the list
whole_press = 0      # Reset the varible
a = 0                # Reset the varible

for i in range(len(target_C0R190)):
   whole_press = whole_press + float(target_C0R190[i]['PRES'])
   a = 1
target_data.append('C0R190')
if a == 1:
   target_data.append(whole_press/len(target_C0R190))
else:
   target_data.append('\'None\'')
print(target_data,',',end='')


target_data = []     # Reset the list
whole_press = 0      # Reset the varible
a = 0                # Reset the varible

for i in range(len(target_C0X260)):
   whole_press = whole_press + float(target_C0X260[i]['PRES'])
   a = 1
target_data.append('C0X260')
if a == 1:
   target_data.append(whole_press/len(target_C0X260))
else:
   target_data.append('\'None\'')
print(target_data,end='')
print(']')
