class Jar:

    def __init__(self, capacity=12):
        if not capacity:
            raise ValueError("Invalid Capacity")
        self.capacity = capacity

    def __str__(self):
        return self.size()*"🍪"

    def deposit(self, n):
        self.capacity  = self.capacity - n
        if self._capacity < 0:
            self._capacity = 0
            print("Jar is Full")
        return self.size()

    def withdraw(self, n):
        self.capacity  = self.capacity + n
        if self._capacity >= 12:
            self.capacity = 12
            print("Jar is Empty")

        return self.size()


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            self.capacity = 0
           # raise ValueError("The Jar is Full")
        else: self._capacity = capacity
        

    def size(self):
        return 12 - self._capacity 
        
