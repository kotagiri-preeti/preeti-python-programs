Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak','age' : 21, 'pay' : 40000} 
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak','age' : 50, 'pay' : 50000} 
db = {} 
db['Omkar'] = Omkar 
db['Jagdish'] = Jagdish 

# For storing 
b = pickle.dumps(db)     # type(b) gives <class 'bytes'> 

# For loading 
myEntry = pickle.loads(b) 
print(myEntry) 
