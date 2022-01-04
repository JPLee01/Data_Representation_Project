#Data Representation - Project
#John Paul Lee - G00387906
#Lecturer - Andrew Beatty
#Code is adapted from code generated through lectures through the semester

#Import required modules

from ElectronicDAO import electronicDAO

#print("ok!") # print ok to see if everything works

item1 = {
    'electronic_make':'Apple', 
    'electronic_model':'iWatch 2', 
    'electronic_price': 300
}
item2 = {
    'electronic_make':'Sony', 
    'electronic_model':'Playstation 4', 
    'electronic_price': 600
}

item3 = {
    'electronic_id':2,
    'electronic_make':'Microsoft One', 
    'electronic_model':'Xbox One', 
    'electronic_price': 550
}

#Testing out of electronicDAO functions

#returnValue = electronicDAO.create(item1)
#print("------------------------------------------------------------------------------------------------------------------------")
#print(returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")

#returnValue = electronicDAO.getAll()
#print("------------------------------------------------------------------------------------------------------------------------")
#print(returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")




#returnValue =  electronicDAO.findById(11) 
#print("Find by electronic_id")
#print("------------------------------------------------------------------------------------------------------------------------")
#print (returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")

#print("Update electronic_id")
#print("------------------------------------------------------------------------------------------------------------------------")
#returnValue =  electronicDAO.update(item3) 
#print (returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")

#print("Delete electronic_id")
#print("------------------------------------------------------------------------------------------------------------------------")
#returnValue =  electronicDAO.delete(1) 
#print (returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")


#print("Get all")
#print("------------------------------------------------------------------------------------------------------------------------")
#returnValue = electronicDAO.getAll()
#print(returnValue)
#print("------------------------------------------------------------------------------------------------------------------------")


