from ai import *

 
ques=raw_input("What is your name? ")
res=""
try:
 try:
  res = pywolf(ques)
  print res
 except:
   try:
    res = pywit(ques)
    print res
     
   except:
     res = pywiki(ques)
     print res

except: 
  print "search engine" 


    
