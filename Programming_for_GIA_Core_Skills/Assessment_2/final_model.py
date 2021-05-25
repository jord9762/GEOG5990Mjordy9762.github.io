import matplotlib
import random
import operator
import csv
import drunkframework
import matplotlib.animation 
import matplotlib.pyplot




"""WARNING!!!!!"""
"""This code was tested using Spyder 5.0.4, should any problems be encountered using older
models please try using a Jupyter notebook."""

#creates a new empty list for what will be the csv environment data, see https://docs.python.org/3/library/csv.html for more
environment = []
#drunks adapted from agents from GUI's practical replacing "agents"
drunks = []
#density is an empty list which will track agent movement independent of the movement process
density= []
#specifies number of drunks/agents
num_of_drunks = 25
#outlines the number of iterations the line 64-78 code will undergo
num_of_iterations = 100


#sets the dimensions for the matplotlib plots
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



f = open('drunk.txt', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Used for testing purposes to ascertain the lay of the environment
#matplotlib.pyplot.xlim(0, 300)
#matplotlib.pyplot.ylim(0, 300)
#matplotlib.pyplot.imshow(environment)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

#Code on lines 46-50 appends the density list output to a 300x300 grid, this code is needed 
#to prevent the error "IndexError: list index out of range"                                
for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
    density.append(rowlist)
#matplotlib.pyplot.imshow(environment) run this in isolation to check the environment is
#correct


## Make drunks and assign them with an identification number.
for i in range(num_of_drunks):
    identification = ((1+i)*10) 
   # print(identification) #this should print 10-250 giving each of the drunks an identification number, later to be matched up with houses
    drunks.append(drunkframework.Drunk(environment, drunks, identification))
    


#This is is supposed to work whereby if the co-ordinates of stilldrunk match their identification number they are home 
#In the prototype density of the environment changed throughout the iterations, as such the drunks would
#often stop in areas which were not their home. The work around this was seperating the process of track
#and move through the creation of the density list. Track is left in but commented.
for i in range (num_of_drunks):
    stilldrunk = drunks[i]
    for j in range(num_of_iterations):
         while environment [stilldrunk._y][stilldrunk._x] != stilldrunk.identification:
                density[drunks[i]._y][drunks[i]._x]+=1
                drunks[i].move()
                #drunks[i].track() omitted from the final iteration of the application

#saves density list (see lines 68 to 73)
with open('density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in density:
        csvwriter.writerow(row)                
  
#lines 79 to 90 serve the purpose of display the density and drunks in relation
#to their finishing position within the environment
                              
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(density)

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.show(drunks)


matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)

#Code below just prints we're home for each of the 25 agents following a resolution of
#the code

for i in range(num_of_drunks):
        matplotlib.pyplot.scatter(drunks[i]._x, drunks[i]._y)
        print("we're home!")    
      


      
