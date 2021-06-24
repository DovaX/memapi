


import memapi_core as mc






class Dog:
    def __init__(self,name,age,typ):
        self.name=name
        self.age=age
        self.typ=typ
        

class Cat:
    def __init__(self,name,age,typ):
        self.name=name
        self.age=age
        self.typ=typ
        





#dogs=[]


#dogs.append(Dog("Wolf",3,"Husky"))




mc.store.append(Dog("Wolf",3,"Husky"))
mc.store.append(Dog("Wolf",3,"Husky"))
mc.store.append(Cat("Whisker",2,"British"))
mc.store.append(Cat("Whisker",2,"British"))
mc.store.append(Dog("Wolf",3,"Husky"))


print(mc.store._stored_objects_by_type)




dogs=mc.store.get_all_by_type(Dog)
cats=mc.store.get_all_by_type(Cat)



obj_id=mc.store.get_object_id(dogs[2])

dog_id=mc.store.get_object_specific_type_id(dogs[2])
cat_id=mc.store.get_object_specific_type_id(cats[0])


no_cats=mc.store.get_count_by_type(Cat)

print(dogs)

