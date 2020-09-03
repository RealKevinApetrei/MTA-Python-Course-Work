class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Pair: (x={self.x}, y={self.y})>"

    def __getattr__(self, attrname):
        return "Singularity has occured."

    def __getattribute__(self, attrname):
        print("__getattribute__" + attrname)
        if attrname == "z":
            return self.x + self.y
        return super().__getattribute__(attrname)
        
    def __dir__(self):
        return [key for key in self.__dict__] + ["z"]

    
pair = Pair(3, 7)