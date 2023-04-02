class Protected:
    def __init__(self):
        self._privateVar = 822

def getPrivate(self):
    print(self._privateVar)

def setPrivate(self, private):
    self._privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(2000)
obj.getPrivate()

    


                
