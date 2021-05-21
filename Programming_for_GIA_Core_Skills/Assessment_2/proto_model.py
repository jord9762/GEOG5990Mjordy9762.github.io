import matplotlib
import random
import operator
import csv
import drunkframework
import matplotlib.animation 
import matplotlib.pyplot




"""WARNING!!!!!"""
"""Note to visualise the code in this file the code %matplotlib qt must be inputted in to the ipython console first. Or alternatively
the code can be ran in the command prompt. Note to run this code more than once in the Jupyter terminal may require a restart of the kernel."""

"""https://www.youtube.com/watch?v=8exB6Ly3nx0 this excellent resource had info on combining GUI with matplotlib data"""

#creates a new empty list for what will be the csv environment data, see https://docs.python.org/3/library/csv.html for more
environment = []
#drunks adapted from agents from GUI's practical replacing "agents"
drunks = []
num_of_drunks = 25
num_of_iterations = 100



fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



f = open('drunk.txt', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

                                

#matplotlib.pyplot.imshow(environment) run this in isolation to check the environment is
#correct


## Make drunks and assign them with an identification number.
for i in range(num_of_drunks):
    identification = ((1+i)*10) 
   # print(identification) #this should print 10-250 giving each of the drunks an identification number, later to be matched up with houses
    drunks.append(drunkframework.Drunk(environment, drunks, identification))
    


#This is is supposed to work whereby if the co-ordinates of stilldrunk match their identification number they are home 
#However due to the density of track the values are changed throughout the iterations, as such the density was omitted.
#Turn on track to view the routes which the drunks take.
for i in range (num_of_drunks):
    stilldrunk = drunks[i]
    for j in range(num_of_iterations):
         while environment [stilldrunk._y][stilldrunk._x] != stilldrunk.identification:
                drunks[i].move()
                drunks[i].track()

                
                                
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)

 
for i in range(num_of_drunks):
        matplotlib.pyplot.scatter(drunks[i]._x, drunks[i]._y)
        print("we're home!")    
      


#Prints out density as a file, note this will not work while track is commented out.      
with open('proto.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        



