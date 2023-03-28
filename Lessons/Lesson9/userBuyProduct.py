from userAddMoney import userAddMoney 
from variantChoose import variantChoose


def userBuyProduct(user, category, store):
    is_runing = True
    while is_runing:

        if user["money"] <= 0:
            print("Sorry , you have no money")
            userAddMoney(user)
            if user['money'] <= 0:
                is_runing = False
                break


        else:

            print("\n**** You can shop ***\n")

            choose_category = variantChoose(category)

            if choose_category == 'q':
                is_runing = False
                break

            else:
                
                products_in_category = store[choose_category][category[choose_category]] 

                product = variantChoose(products_in_category)
                if product == 'q':
                     is_runing = False
                     break

                if products_in_category[product]['Price'] <= user['money']:

                    user['money'] = user['money'] - products_in_category[product]['Price']

                    user['bag'].append({category[choose_category]: products_in_category[product]})

                    print("\nCongratulations, you bought the product\n")

                    shoping = input("Do you want to finish shopping?   'q', else pass:   ").lower()
                    if shoping == 'q':
                         is_runing = False   

                else:
                    print("Not enough money")

                    userAddMoney(user)    