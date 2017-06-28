#!/usr/bin/python

class ScreenDisplay(object):
    def __init__(self, itemsToDisplay):
        self.itemsToDisplay = itemsToDisplay

    def start_page(self, ):

        print("***************************************")
        print("*What items would you like to buy?    *")
        print("***************************************")

        numberOfItemsDisplayed = 1

        for items in self.itemsToDisplay:
            print("%d.) %s" % (numberOfItemsDisplayed, items))
            numberOfItemsDisplayed += 1

        self.additional_options()

        return raw_input()

    def additional_options(self, ):

        print("\n\nTo view your cart type in 'view'")
        print("To exit type in 'exit'")

    def add_item_page(self, ):

        print("***************************************")
        print("*How many would you like to buy?      *")
        print("***************************************")

        print("a.) Back")

        return raw_input()

    def promocode_page(self, ):

        print("***************************************")
        print("*Enter Promocode:                     *")
        print("***************************************")

        print("a.) Continue without Promocode")

        return raw_input()

    def update_promocode_page(self, item, currentPromoCode, newPromoCode=None):

        print("You have already entered a Promocode for item : %s" % item)
        print("Would you like to change from %s to %s? [Y|N]" % (currentPromoCode, newPromoCode))

        return raw_input()

    def display_total(self, totalItem, cartList, totalPrice):

        freebies = None

        print("***************************************")
        print("*View cart                            *")
        print("***************************************")

        for item in totalItem:

            description = cartList[str(item) + "_description"]
            quantity = cartList[str(item) + "_quantity"]

            if str(item) + "_freebies" in cartList:
                freebies = cartList[str(item) + "_freebies"]
                noOfFreebies = cartList[str(item) + "_noOfFreebies"]

                freebies = ("%s x %s\n" % (noOfFreebies, freebies))

            print("%s x %s" % (quantity, description))

        if freebies: print(freebies)
        print("\n\nTotal amount: $%s" % totalPrice)

    def end_page(self, ):

        print("Thank you for using amaysim page!")