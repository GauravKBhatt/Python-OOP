import csv
class Item:
    
    #class ttributes
    all=[]
    
    def __init__(self,name:str,salary:int,position=str):
        
        #validations for the data
        assert salary>=0, f"salary {salary} should not be negative."
        
        #assigning the data
        self.__name=name
        self.salary=salary
        self.position=position

        #appending every instance of instance to the all class attribute.
        Item.all.append(self)

    #method to print the information of the instance.
    def print(self):
        return f"{self.name} is the employee in {self.position} having salary {self.salary}"

    #execution of the repr method to print all the instances of the class in a stringed format. using the self.class.name to make sure it works properly in child classes too.
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.salary},'{self.position}')"

    #instantiating the instances from the csv file
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                salary=float(item.get('salary')),
                position=item.get('position'),
            )
    
    #creatinf the static method to check weather the number is integer or not

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integger()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    @property
    #property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    #property to set the readonly attribute name
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long")  
        else:  
            self.__name=value 