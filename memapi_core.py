






class Store:
    def __init__(self):
        """Stores objects"""
        self._stored_objects={}
        self._pk_id=1
        self._stored_objects_by_type=[] #{"type":X,"stored_objects":{},"typeid":1}
        self._last_tid=1
        
          
    def append(self,obj):
        self._stored_objects[self._pk_id]=obj
        self._pk_id+=1
        
        if type(obj) in [x["type"] for x in self._stored_objects_by_type]:
            index=[x["type"] for x in self._stored_objects_by_type].index(type(obj))
            
            self._stored_objects_by_type[index]["pk_id"]+=1
            type_pk_id=self._stored_objects_by_type[index]["pk_id"]
            self._stored_objects_by_type[index]["stored_objects"][type_pk_id]=obj
        else:
            self._stored_objects_by_type.append({"type":type(obj),"stored_objects":{1:obj},"pk_id":1,"tid":self._last_tid}) #if type does not exist
            self._last_tid+=1
        
    def get_all_by_type(self,typ):
        result=[]
        for i,obj in enumerate(self._stored_objects.values()):
            print(obj,type(obj))
            if type(obj)==typ:
                result.append(obj)
                
        return(result)
          
      
    def get_all(self):
        return(self._stored_objects.values())


    def get_object_id(self,obj):
        occurences=[x for x in self._stored_objects.keys() if self._stored_objects[x]==obj]
        assert len(occurences)<=1
        return(occurences[0])
        
    
    def get_object_specific_type_id(self,obj):
        stored_objects_by_specific_type=[x for x in self._stored_objects_by_type if x["type"]==type(obj)][0]
        occurences=[x for x in stored_objects_by_specific_type["stored_objects"].keys() if obj ==stored_objects_by_specific_type["stored_objects"][x]]
        assert len(occurences)<=1
        return(occurences[0])


    def get_count_by_type(self,typ):
        objs=self.get_all_by_type(typ)
        return(len(objs))
    

    def remove_object(self,obj):
        index=[x for x in self._stored_objects.values()].index(obj)
        object_id=self._stored_objects.keys()[index]
        del self._stored_objects[object_id]
            
    
    def remove_object_id(self,object_id):
        del self._stored_objects[object_id]
            
            
        




def infinite_loop():
    done=False
    while not done:
        
        action=input("Next action:\n")
        
    
    
  
store=Store()
    
#infinite_loop()