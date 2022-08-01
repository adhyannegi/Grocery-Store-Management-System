#importing libraries
import pickle
import os

#Creating and opening new datafile
f = open('grocerystore.dat', 'wb')
rec = ['Name', 'Price', 'Quantity']
pickle.dump(rec,f)
f.close()

#Function to add a new record into the datafile
def add_item():
  with open("grocerystore.dat","ab") as f:
    ans='y'
    while ans in 'Yy':
      name=input("Enter Name of Item: ")
      price=input("Enter Price in rupees: ")
      quantity=input("Enter Quantity in grams: ")
      rec=[name, price, quantity]     
      pickle.dump(rec,f)
      print('Item added.')
      ans=input("Enter more data Y/N:")

#Function to delete a record from the datafile
def delete_rec(name_of_item):
  ifile=open("grocerystore.dat","rb") 
  ofile=open("TEMP.dat","ab")     
  while True:
    try:
      rec=pickle.load(ifile)
      if rec[0]== name_of_item:
        pass              
      else:
        pickle.dump(rec,ofile)   
    except EOFError:
      break
  print('Item deleted.')
  ifile.close()
  ofile.close()
  os.remove("grocerystore.dat")
  os.rename("TEMP.dat","grocerystore.dat")

#Function to update the price of an item in the datafile
def update_price(name_of_item, new_price):
  found=False
  with open("grocerystore.dat","rb+") as f:        
    while True:
      rpos = f.tell() 
      try:
        rec=pickle.load(f)
        if rec[0] == name_of_item:
          rec[1] = new_price    
          f.seek(rpos) 
          pickle.dump(rec,f)
          found=True
          print('Price updated.')
      except EOFError:
        if found==False:
          print("No Record Found")
        break
    
#Function to update the quantity of an item in the datafile
def update_quantity(name_of_item, new_quantity):
  found=False
  with open("grocerystore.dat","rb+") as f:        
    while True:
      rpos = f.tell() 
      try:
        rec=pickle.load(f)
        if rec[0] == name_of_item:
          rec[2] = new_quantity   
          f.seek(rpos) 
          pickle.dump(rec,f)
          found=True
          print('Quantity updated.')
      except EOFError:
        if found==False:
          print("No Record Found")
        break
    

#Function to display the data
def display():
  with open("grocerystore.dat","rb") as f:
    while True:
      try:
        rec=pickle.load(f)    
        print(rec)
      except:     
        break

#Code for user interaction
print('Welcome to the Grocery Store.')
opt = 'y'
while opt in 'Yy':                                                             
    print('1. Add a record to file.')
    print('2. Delete a record from file.')
    print('3. Edit price of an item.')
    print('4. Edit quantity of an item.')
    print('5. Display all records')
    
    choice = int(input('Enter your choice:(1-5): '))
    if choice == 1:
        add_item()      
    elif choice == 2:
        name_of_item = input('Enter name of item to be deleted: ')
        delete_rec(name_of_item)
    elif choice == 3:
        name_of_item = input('Enter name of item: ')
        new_price = input('Enter new price: ')
        update_price(name_of_item, new_price)
    elif choice == 4:
        name_of_item = input('Enter name of item: ')
        new_quantity = input('Enter new quantity: ')
        update_quantity(name_of_item, new_quantity)
    elif choice == 5:
        display()    
  
    else:
        print('Invalid Choice.')
    opt = input('Do you want to continue(Y/N): ')

else:
  print('Data stored.')
    
