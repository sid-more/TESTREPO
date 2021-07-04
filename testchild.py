try:  
    a=10  
    print (a)  
    raise NameError("Hello")  
except NameError as e:  
        print ("An exception occurred")  
        print (e) 

#Custom Exception

class ErrorInCode(Exception):  
     def __init__(self, data):  
       self.data = data  
     def __str__(self):  
        return repr(self.data)  
  
try:  
    raise ErrorInCode(2000)  
except ErrorInCode as ae:  
    print ("Received error:", ae.data)
