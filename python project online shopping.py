import shelve
import pickle
import sys
import os
import math

print('MINI PROJECT:-- Online Retail Shopping')
print("-----"*30)
product_items={'Pasta': '60', 'Soda': '51', 'Bananas': '50', 'orange': '72'}



while 1:
    a = int(input('press 1 to go to admin module or\npress 2 to go to customer module:..'))
    if a==1:
        print('if you are a admin then only\n')
        b=input('type the password to enter the admin module :...')


        if b=='igs':
            print('welcome to online shopping admin module')
            print("*****" * 10)
            c = int(input( 'would u like to see the list of products or add products or something else \nif yes press 1 or press 2 to exit:..'))
            if c == 1:
                product_items = {'Pasta': '60', 'Soda': '51', 'Bananas': '50', 'orange': '72'}
                print(product_items)
                print('\nshopping stock options\n**************\n1: Add item\n2: Remove item\n3: View items\n4. Update items\n5: sign out')
                option = int(input('enter an option:..'))
                while option !=0:
                    if option == 1:
                        item = input('enter an item:.')
                        price = int(input('enter the price:.. '))
                        product_items[item] = price
                        print(product_items)
                    elif option == 2:
                        item = input('enter en item')
                        del (product_items[item])
                        print(product_items)
                    elif option == 3:
                        print(product_items)
                    elif option ==4:
                        f = int(input('press 1 if u want to update price of a item\npress 2 if u want to update name of item '))
                        if f==1:
                            print(product_items)
                            item = input('enter the item:..')
                            price = input('enter the price u want to update:..')
                            product_items[item] = price
                            print('new update of price ', product_items)
                        elif f==2:
                            print(product_items)
                            a=input('enter the registered item u want to change')
                            b=input(('what name u want to give'))
                            for key in product_items:
                                if key==a:
                                    newitem=b
                                    newprice=product_items[key]
                                    product_items[newitem]=newprice
                                    del(product_items[key])
                            print('new updated list ', product_items)
                        else:
                            print('invalid input')
                    elif option ==5:
                        print('exit')
                        print('admin logged out successfully')
                        break
                    option = int(input('enter an option'))

                else :
                    print('invalid input')
            else:
                print('\n****** exit ******\n')
        else:
            print('wrong password')


    elif a==2:
        print('welcome to online shopping customer module')
        print("*****" * 10)
        d = int(input('would u like to see our all products or add products or something else \nif yes press 1 or press 2 if no:..'))
        if d == 1:
            busket_items = {}
            print('products availability and prices :-- ',product_items)
            print('\nshopping busket option\n**************\n1: Add item\n2: Remove item\n3: View items in the online shop\n4.view item in your card\n5. Update items\n6.search product from online shop\n7.print billing invoice\n8. sign out')
            option = int(input('enter an option:..'))
            while option !=0:
                if option == 1:
                    item = input('enter an item')
                    if item  in product_items:
                        print('yes,this product is there in online shop')
                        quantity = int(input('enter the quanity:.. '))
                        busket_items[item] = quantity
                        print('user card consist of item name, quantity :-- ',busket_items)
                    else:
                        print('no,this product is not there')

                elif option == 2:
                    item = input('enter an item')
                    del (busket_items[item])
                elif option == 3:
                    print('product availability in online store ',product_items)
                elif option == 4:
                    print('items in card with quantity ',busket_items)
                elif option==5:
                    g=int(input('press 1 if u want to update quantity\npress 2 if u want to update item '))
                    if g==1:
                        print(busket_items)
                        item = input('enter the item:..')
                        quantity = input('enter the quantity u want to update:..')
                        busket_items[item] = quantity
                        print('new update of price', busket_items)
                    elif g==2:
                        print(busket_items)
                        item = input('enter the item u want to update:..')
                        # quantity = input('enter the quantity u want to update:..')
                        # busket_items[quantity] = item
                        a=input('enter new item with same quantity')
                        for key in product_items:
                            if key==a:
                                newquantity=busket_items[item]
                                del(busket_items[item])
                                busket_items[a]=newquantity
                            else:
                                print('no item named ',a)
                        print('new update of card', busket_items)
                    else:
                        print('invalid input')
                elif option==6:
                    print(product_items)
                    item=input('enter the product u want to search:..')
                    if item  in product_items:
                        print('yes,this product is there in online shop')
                    else:
                        print('no,this product is not there')
                elif option==7:
                    print('product , price and quantity u entered in your card :..',busket_items)

                    import datetime
                    now = datetime.datetime.now()
                    print("Date-", now.year, "/", now.month, "/", now.day)
                    print("Time-", now.hour, ":", now.minute, ":", now.second)
                    print(now.strftime("%B"))
                    print('product  ','quantity ','price')
                    count=0
                    for key in busket_items:
                        totalpriceofperticularitem = int(product_items[key])*int(busket_items[key])
                        print(key,' ',busket_items[key],'   ',totalpriceofperticularitem,'\n')
                        count+=totalpriceofperticularitem
                    print('total price to pay :-- ',count)

                elif option == 8:
                    print('exit')
                    print('customer logged out successfully')
                    print('\n')
                    print('********* thanks for shopping with us ***********')
                    print('...\n...\n...\n')
                    print('Developed by "Sudip & Debarati..."\nDeveloped at IIT-KANPUR')
                    print('    Software terminated    \n\n')
                    break
                option=int(input('enter an option:..'))

            else:
                print('invalid input')
        else:
            print('\n****** exit ******\n')

    else:
        print('invalid input')










