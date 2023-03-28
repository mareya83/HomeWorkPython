# 1) Store
# 2) Into store you might : a) Category ( [] )
#    b) Show All products
#    c) Admin mode
#    q) Quit
# if a) -> a) TV , b) Smartphone , c) Mp3 , d) DvD
#       a -> show all TV []
#       b -> show all Sm []
#       c -> show all Mp3 []
# products are dictionaries :
# { "label" : "..." , "price" : "..." , desc : ""... }
# 3) User might buy product if user has money (
#                   {
#                   "name" : "..." ,
#                   "money" : ... ,
#                   "bag" : []
#                   }
# )
# 4) Admin mode yields ->
#   1) add product to category ,
#   2) Delete product
#   3) Change name of product

#

from menu import menu

from createStore import createStore

from printStore import printStore

from productByCategory import productByCategory

from userRegister import userRegister 
from userBuyProduct import userBuyProduct
from userShowBag import userShowBag

from addProduct import addProduct
from deleteProduct import deleteProduct
from changeNameProduct import changeNameProduct


category = ['TV', 'Smartphone', 'Mp3', 'DvD']
label = ['Samsung', 'Lg', 'Philips']

store = createStore(category, label)

is_runing = True
while is_runing:
    print("\n MAIN MENU:")
    menu_choose = menu("a) Show All products", "b) Category", "c) User", "d) Admin", "q) Quit")

    if menu_choose == 'a':
          printStore(store)
 
         
    elif menu_choose == 'b':
          productByCategory(store, category)


    elif menu_choose == 'c':
          register_status = False
          is_runing_user = True
          user = {}

          while is_runing_user:

               user_choose = menu("a) Register", "b) Buy product", "c) Show bag", "q) Quit" )

               if user_choose == 'a':
                    user, register_status = userRegister() 

               elif user_choose == 'b':
                    if register_status:
                         userBuyProduct(user, category, store)
                    else:
                         print("\n You can buy the product after registration!\n")

               elif user_choose == 'c':
                    if register_status:
                         userShowBag(user)
                    else:
                         print("\nYou can show bag after registration!\n")

               elif user_choose == 'q':
                    is_runing_user = False

               else:
                   print("Incorrect chooce!")  

    
    elif menu_choose == 'd':

         is_runing_admin = True
         while is_runing_admin:
               admin_choose = menu("1) Add product to category", "2) Delete product", "3) Change name of product", "q) Quit")
               
               if admin_choose == '1':
                    addProduct(store, category)
               
               elif admin_choose == '2':
                    deleteProduct(store, category)

               elif admin_choose == '3':
                    changeNameProduct(store, category)
               
               elif admin_choose == 'q':
                    is_runing_admin = False
               
               else:
                    print("Incorrect chooce!")


    elif menu_choose == 'q':
         print("Goodby!!!")
         is_runing = False


    else:
        print("Incorrect chooce!")