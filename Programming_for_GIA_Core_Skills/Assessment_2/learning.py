#Interactive learning
""""This code focuses on animating the process of the drunks getting home, note this did not work in my version of Spyder
so it may be necessary to use a Jupyter Notebook"""
import matplotlib
matplotlib.use('TkAgg')
import random
import operator
import csv
import drunkframework
import matplotlib.animation 
import matplotlib.pyplot
import tkinter



"""WARNING!!!!!"""
"""Note to visualise the code in this file the code %matplotlib qt must be inputted in to the ipython console first. Or alternatively
the code can be ran in the command prompt. Note to run this code more than once in the Jupyter terminal may require a restart of the kernel."""

"""https://www.youtube.com/watch?v=8exB6Ly3nx0 this excellent resource had info on combining GUI with matplotlib data"""

#creates a new empty list for what will be the csv environment data, see https://docs.python.org/3/library/csv.html for more
environment = []
#drunks adapted from agents from GUI's practical
drunks = []
num_of_drunks = 25
num_of_iterations = 10

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

#used to call GUI 
root = tkinter.Tk()
root.wm_title("Model")
#Open window having dimension 700x700
root.geometry('700x700')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
#configures GUI background to green
root.configure(background="green")
#adds a close button, use this rather than x to ensure resolution of scipt
menu_bar.add_command(label="Close", command=root.destroy)

#my_button class and parameters below change the GUI button to blue
my_button = tkinter.Button(root, text="Run model", command=run, bg='blue')#https://pythonexamples.org/python-tkinter-button-background-color/#:~:text=You%20can%20change%20the%20background,bg%20property%20as%20shown%20below.&text=The%20default%20color%20of%20Tkinter%20Button%20is%20grey.
my_button.pack(side=tkinter.TOP)#https://www.youtube.com/watch?v=Uk2FivOD8qo got idea from here

#sets up a canvas for a tkinter GUI where the animated model will be embedded.
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



#Initial check to make sure the CSV is in correct directory
#with open('drunk.txt', newline='') as f:
   # reader = csv.reader(f)
    #for row in reader:
       # print(row)





f = open('drunk.txt', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

## Make drunks and assign them with an identification number.
for i in range(num_of_drunks):
    identification = ((1+i)*10) 
    print(identification) #this should print 10-250 giving each of the drunks an identification number, later to be matched up with houses
    drunks.append(drunkframework.Drunk(environment, drunks, identification))
    
def update(frame_number):
    
    fig.clear()   
    global carry_on

    

   #The following code is adapted from the final piece just to show the user how the drunks
   #move, note there is no stopping condition due to the omission of the while loop
    for i in range (num_of_drunks):
        for j in range(num_of_iterations):
                    drunks[i].move()
                    drunks[i].track()
                    
                    
                    
                    
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)

    
    for i in range(num_of_drunks):
            matplotlib.pyplot.scatter(drunks[i]._x, drunks[i]._y)
            
      

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on):
        #function returns generator
        yield a
        a = a + 1
tkinter.mainloop()

 #Prints out density as a file      
with open('density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        