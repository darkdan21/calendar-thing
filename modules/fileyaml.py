#!/bin/python
import yaml
class fileyaml:
    def __init__(self,yamlfile):
        self.yamlfile = yamlfile
        file_object = open(yamlfile,"r")
        stryaml = yaml.load(file_object.read())
        self.yaml = stryaml 
        file_object.close()

    def getattr(self,attr):
        return self.yaml.attr;

    def listattr(self):
        return self.yaml

    def setattr(self,attr,value):
        self.yaml.attr = value
        file_data = yaml.dump(data)
        file_object = open(self.yamlfile,"w")
        file_object.write(file_data)
        file_object.close()

