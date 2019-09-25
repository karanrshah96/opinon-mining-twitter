def plot_graph(query1,query2,p1,n1,p2,n2):
	import sys
	import numpy as np
	import matplotlib.pyplot as plt

	positive1 = p1
	negative1= n1
	firstvar=(positive1*100/(positive1+negative1),negative1*100/(positive1+negative1))

	rat1=positive1*100/negative1

	#firstvar=(positive1,negative1)

	positive2=p2
	negative2=n2
	secondvar=(positive2*100/(positive2+negative2),negative2*100/(positive2+negative2))


	rat2=positive2*100/negative2

	names=(query1,query2)
	rat=(rat1,rat2)


	#fig, ax = plt.subplots()

	ind = np.arange(2)  # the x locations for the groups
	width = 0.35       # the width of the bars

	plt.bar(ind, rat, width, color='r')

	# add some text for labels, title and axes ticks
	plt.ylabel('Sentiment Scores')
	plt.title(str('Scores by ' + query1 + ' and ' + query2))
	plt.xticks(ind,names)
	#ax.set_xticklabels(('Positive', 'Negative'))

	#ax.legend((rects1[0], rects2[0]), ('BJP', 'Congress'))
	plt.savefig('static/bar.png')
	plt.clf()
	plt.cla()
	plt.close()


	explode=(0,0.1)
	labels='Positive','Negative'

	plt.pie(firstvar,explode=explode,labels=labels,autopct='%1.1f%%', shadow=True,startangle=90)
	plt.axis('equal')
	plt.title(query1)

	plt.savefig('static/pie1.png')
	plt.clf()
	plt.cla()
	plt.close()


	plt.pie(secondvar,explode=explode,labels=labels,autopct='%1.1f%%', shadow=True,startangle=90)
	plt.axis('equal')
	plt.title(query2)
	plt.savefig('static/pie2.png')
	plt.clf()
	plt.cla()
	plt.close()


