# import pickle
# cars = ["rolls royce", "lamborghini", "ferrari", "bugatti", "bmw", "volkswagen"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

import pickle
# cars = ["audi", "bmw"]
# file = "mycars.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycars.pkl"
fileobj = open(file, 'rb')
mycars = pickle.load(fileobj)
print(mycars)
print(type(mycars))
