from item import Item
class intern(Item):
    all=[]
    def __init__(self,name:str,salary:int,position=str,days=0):
        super().__init__(name,salary,position)
        self.days=days
        intern.all.append(self)