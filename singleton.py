from tokenize import Single


class Borg:

    """The Borg design pattern"""

    _shared_data = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data #Make an attribute dictionary


class Singleton(Borg): 

    """The singleton class"""
    def __init__(self, **kwards):
        #Borg.__init__(self)
        super().__init__()
        self._shared_data.update(kwards) #Update the attribute dictionary

    def __str__(self):
        return str(self._shared_data)

# Create a singleton object
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)

# Create another singleton object
y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)

print(y.__dict__)  # 'x' or 'y' is indistintic, both have the same shared dict attribute
