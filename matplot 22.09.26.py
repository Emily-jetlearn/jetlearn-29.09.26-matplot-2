import matplotlib.pyplot as plt
import numpy as np
#plot y=x
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
#plt.plot(x,y)
#plt.show()

'''#add red dotted circles
plt.plot(x,y,'ro')
plt.show()

#green arrows 
plt.plot(x,y,'g^')
plt.show()

#blue dashes
plt.plot(x,y,'b--')
plt.show()'''

#how to limit the numbers on each axis
#plt.axis(x1,xn,y1,yn)
plt.axis([0,10,0,200])
plt.show()

#add the label, titles, line width and legend
plt.plot(x,y,'r--',label = 'y=x',linewidth=5)
plt.axis([0,10,0,50])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("sample graph")
plt.legend()
plt.show()

#plot multiple lines on a single graph

plt.plot([1,2,3,4,5,6],[1,4,9,16,25,36],"ro",label = "y=x**2",linewidth=3)
plt.plot([1,2,3,4,5,6],[1,8,27,64,125,216],"g^",label="y=x**3",linewidth=2)
plt.axis([0,10,0,200])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("graphs of square and cube numbers")
plt.legend()
plt.show()


x = np.arange(0,10,0.2)
print(x)

y1 = x**2
y2 = x**3
plt.plot(x,y1,"b^",x,y2,"r-")
plt.show()

#bar chart
plt.bar([1,2,3,4,5],[12,24,48,96,182],color='b')
plt.show()


x = np.arange(-5,5,0.1)
print(f'\n values from -5-5 with step 0.1 \n {x}\n')
#plt.plot(x,y,'r--',label = 'y=x',linewidth=5)
plt.axis([-5,5,-5,5])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


#showing multiple bars in a single graph

plt.bar([1,3,5,7,9],[2,4,6,8,10],color="b")
plt.bar([12,14,16,18,20],[13,15,17,19,21],color="g")
plt.show()

#showing the categorial data using bar plot
plt.bar(["MaleLiteracy","FemaleLiteracy"],[90,95])
plt.show()
