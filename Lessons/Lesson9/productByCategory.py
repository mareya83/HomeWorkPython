from variantChoose import variantChoose

def productByCategory(store, category):
     is_runing_category =True
     while is_runing_category:
         category_choose = variantChoose(category)
         if category_choose == 'q':
               is_runing_category = False
         else:
           for i in store:
               for key in i:
                    if key == category[category_choose]:
                         print(key)
                         for n in i[key]:
                              print(n)
                              is_runing_category = False
     
     return category_choose


                         