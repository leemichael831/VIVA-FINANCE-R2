#The script should be run as follows:
#python3 jsonToMD.py sample_data.json

import json 
import os.path
import sys
	
def jsonToMDTable(strpath):
  """
  Converts a JSON file consisting of an array of objects into a markdown table.

  :strpath - the path to the JSON file that needs to be converted
  """
  numObjsAdded = 0
  table = {}

  # Opening JSON file 
  f = open(strpath,) 
  filename = strpath.split(".")[0]
  
  # Overwrite if filename already exists, else, create new file
  if os.path.isfile(filename + ".md"):
    md = open(filename+".md", "w")
  else:
    md = open(filename+".md", "x")
    
  # Converting the JSON array of objects to a list of dicts
  data = json.load(f) 
  numObjsTotal = len(data)

  # iterate over every objDict in data
  for objDict in data:
    for key, value in objDict.items():
      # if encounter a key, add it into the "header" of the table
      if(key not in table.keys()):
        table[key] = []
        md.write("|" + key)

      # so that the entries are placed in the correct column
      while(len(table[key]) < numObjsAdded):
        table[key].append(None)
      
      # add the value of the key/value pair into the table[key], which is an array
      table[key].append(value)
      
    numObjsAdded += 1
  md.write("|\n")

  # adding the second row of horizontal lines as per markdown table syntax
  for i in range(0, len(table)):
    md.write("|---------")
  md.write("|\n")
  print(table)

  # completing the table with all the entries
  for i in range(0, numObjsTotal):
    for header, lst in table.items():
      if(i > len(lst)-1 or lst[i] == None):
        md.write("|                ")
      else:

        if(isinstance(lst[i], str)):
          md.write("|"+ lst[i]) # assuming lst[i] is a str
        else:
          md.write("|" + json.dumps(lst[i]))
    md.write("|\n")
  f.close() 
  md.close();
  
# takes command line args
if __name__== "__main__": 
    jsonToMDTable(sys.argv[1]) 