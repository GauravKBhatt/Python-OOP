import csv

class Item:
    
    #class ttributes
    all=[]
    
    def __init__(self,name:str,salary:int,position=str):
        
        #validations for the data
        assert salary>=0, f"salary {salary} should not be negative."
        
        #assigning the data
        self.name=name
        self.salary=salary
        self.position=position

        #appending every instance of instance to the all class attribute.
        Item.all.append(self)

    #method to print the information of the instance.
    def print(self):
        return f"{self.name} is the employee in {self.position} having salary {self.salary}"

    #execution of the repr method to print all the instances of the class in a stringed format
    def __repr__(self):
        return f"Item('{self.name}',{self.salary},'{self.position}')"

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
#creating the instances
# item1 = item("Gaurav",50000,"CEO")
# item2 = item("Pralov",20000,"CFO")
# item3 = item("Ayush",35000,"CTO")

#using the fucntion to instntiate the instances from the csv file.
Item.instantiate_from_csv()

#printing all the instances of the item
for instance in Item.all:
    print(instance.name)

#printing the all function 
# print(item.all)


