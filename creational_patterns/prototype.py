import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name_obj, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name_obj))
        obj.__dict__.update(attr)

        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)

#Create prototype
c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

#Clone objects
c1 = prototype.clone("skylark")
print(c1)

attr = {"name": "Mustang", "color": "Blue"}
c2 = prototype.clone("skylark", **attr)
print(c2)
