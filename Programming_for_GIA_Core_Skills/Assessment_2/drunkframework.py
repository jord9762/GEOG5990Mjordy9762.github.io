import random

# Define a drunk class. This will decide wwhere the drunks begin their journey home
class Drunk():
    def __init__(self, environment, drunks, identification):
        self.drunks = drunks
        self.environment = environment
        self._x = 139 
        self._y = 141
        self.store = 0
        self.identification = identification
        #x and y are set to 139/141 as these are co-ordinates for the pub.
        #environment will house the CSV for house and pub data.
        #identification will house variables for each drunk so that they can stop when reaching their home. 
        
        
        
    def __str__(self):
        """
        

        Returns
        -------
        This will print the agents x and y co-ordinates once the iteration process is complete. str(self.store) allows the store value to be
        printed at each iteration.

        """
      

    # Getters and Setters for x and y properties
    
    def get_x(self):
        """
        

        Returns
        -------
        TYPE
             getter for x.

        """
       
        return self._x
        property(fget=self._x) 
    
    
    def set_x(self, value):
        """
        

        Parameters
        ----------
        value : TYPE
            setter for x

        Returns
        -------
        None.

        """
        self._x = value
     
   
    def get_y(self):
        return self._y

    
    def set_y(self, value):
        self._y = value

# Method to move.
# % is the modulus symbol which means to return the remainder. This will prevent any agents/drunks from exceeding or going lower than the specified
#300x300 grid or higher. Essentially this will move drunks up or down and left or right at eat iteration. 
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300

#Designed to help identify where drunks have travelled. This piece of code works by adding a value of 1 to the envrionment database at 
#each iteration.
    def track(self):
        self.environment[self._y][self._x] +=1
            

    
