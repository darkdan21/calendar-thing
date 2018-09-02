#!/bin/python
from . import event
import glob

class eventmanager:
    storagepath = "events/"
    extension = ".yml"
    def __init__(self):
        self.events = []
        self.get_existing()

    def create_event(self,parameters:dict):
        e = event.event(0,self.storagepath,self.extension)
        for p in parameters:
            e.fileyaml.setattr(p,parameters[p])

    def get_existing(self):
        search =self.storagepath +"*"+self.extension
        files = glob.glob(search)
        files = [x[len(self.storagepath):-len(self.extension)] for x in files] #get just the number ID
            
        self.events += [event.event(number,self.storagepath,self.extension) for number in files]

    def walkyaml(self,yml,tokens:dict):
        if type(yml) == dict:
            for x in yml:
                tokens[x] = yml[x]
                if type(yml[x]) == dict:
                    self.walkyaml(dict(yml[x]),tokens)

    def getevents(self,formatstring:str):
        #formatstring format:
        #   tokens begin with %
        #   if a variable does not exist in any event the format string will be printed
        #   if it exists in some but not all, it will be printed as: NULL

        for ev in self.events:
            tokens = {}
            yml = ev.fileyaml.listattr()
            self.walkyaml(yml,tokens)
            output = self.prepareoutput(formatstring,tokens)
            print(output)

    def prepareoutput(self,formatstring,tokens):
        for token in tokens:
            split = formatstring.split("%"+token)
            output = ""
            while(len(split) > 0):
                if(len(split) == 1):
                    output +=split[0]
                    split = split[1:]
                else:
                    output+=split[0]
                    output+=str(tokens[token])
                    split = split[1:]
            formatstring = output

        return output
