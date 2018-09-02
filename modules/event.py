import time
from . import fileyaml

class event:

    def create_event(self):
        createtime = str(int(time.time()*10000000)) #'easy' way to remove the decimal point
        filename = self.storagepath + createtime + self.extension
        file_obj = open(filename,"w") #create the file
        file_obj.close() #close
        self.fileyaml = fileyaml.fileyaml(filename)



    def open_event(self,identifier:int):
        filename = self.storagepath + str(identifier)+self.extension
        self.fileyaml = fileyaml.fileyaml(filename)

    def __init__(self,identifier:int,storagepath:str,extension:str):
        self.storagepath = storagepath
        self.extension = extension
        if(identifier == 0):
            self.create_event()
        else:
            self.open_event(identifier)
