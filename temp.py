import csv
list1 = [1,2,3,4,5,6,7]
with open("CSV/temp.csv", 'wb') as g:
	    writer = csv.writer(g)
	    writer.writerow(['SentimentText'])
	    for item in list1:
	        writer.writerow([item])