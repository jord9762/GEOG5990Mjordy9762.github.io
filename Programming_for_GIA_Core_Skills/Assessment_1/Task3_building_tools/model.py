#allows the presentation of plots,graphs etc.. will be used to display agents
import random
#allows additional operations such as the itemgetter function
import operator
#importing the random package, able to create psuedo random number for testing purposes
import matplotlib.pyplot
#time package will be used to help check the efficency of the code. warnings arise for certain functions in this package being depricated
import time

"""we enter in agents row a and row b because this reduces our code for when the function is called, we now no longer need to express an agent 
as ([0][1],[0][0]) and we can now express in the more logical [0] and [1]"""
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
#Starts timer to assess efficency of code. 
start = time.clock()
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

#calculates euclidian distance between agents
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

"""answer = (((agents[2][0] - agents[3][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer) could get distance between different agents individually but obviously this would be very inefficent"""



answer = distance_between(agents[0], agents[1])
#below is a test to check code is running smoothly, print statements are important to help identify where problems may be occuring
print(answer)

"""so below here we are saying for everything i and j in our agents, do not calculate distance between the same agent, then calculate the distance
in positions 0 and 1 using the function specified at the start of our code in the distance between function."""

for i in range(num_of_agents):
    for j in range(num_of_agents):
#!= means not equal to and omitts distance between agents which are the same
        if agents[i] != agents[j]: 
            distance = distance_between(agents[0], agents[1])
            answer = distance_between(agents[i], agents[j])
             
            
 #lines 63 to 64 will print the time it takes for code to execute.      
end = time.clock()
print("time = " + str(end - start))
"""Time for 10 agents 0.15 seconds
Time for 100 agents 1.52 seconds
Time for 1000 agents 114 seconds """


"""Creates plots for agents"""
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
matplotlib.pyplot.show()
