#!/usr/bin/python

from shopping_cart import ShoppingCart
from amaysim_display import ScreenDisplay

if __name__ == "__main__":

    # Initialize variables
    run_program = True
    cart = ShoppingCart("product_code.config", "special_promotions.config", "promo_codes.config") # This will load the configuration files.
    screen = ScreenDisplay(cart.forDisplay)

    # Loop until user chooses to exit
    while run_program:

        # Step 1 : Call start up page
        startPageAnswer = screen.start_page()

        # Step 2 : Validate input from user
        validation = cart.check_items(startPageAnswer)

        # Step 3 : Check if the user wants to add items, view cart or exit
        if validation == 0:
            numberOfItemsBought = screen.add_item_page()

            if numberOfItemsBought == 'a':
                continue

            promoCode = screen.promocode_page()

            if cart.appliedPromoCode is not None and not (promoCode == 'a'):
                changePromoCode = screen.update_promocode_page(cart.lastItemCalled, cart.appliedPromoCode, promoCode)

                if changePromoCode == 'Y':
                    cart.appliedPromoCode = promoCode

        elif validation == 1:
            listOfItemsBought, cartList, totalAmount = cart.total()
            screen.display_total(listOfItemsBought, cartList, totalAmount)
        elif validation == 2:
            exit(0)

        # Check if the user chooses to go back or if he/she had inserted an item.
        if not (numberOfItemsBought == 'a'):
            cart.add_items(numberOfItemsBought, promoCode)