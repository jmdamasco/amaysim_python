# amaysim_python
Shopping cart exercise

-- This exercise is compose of the following files:
File : amaysim_shopping_cart.py
Description : This is the main file to be used. I have tested this using Python 2.7
              You may run the application via commandline ./amaysim_shopping_cart.py
              
File : shopping_cart.py
Description : This is the class I have created for this exercise.

File : amaysim_display.py
Description : This is the simple interface for the user.

-- This is the configuration files I have created for this exercise.
-- I have opted in using a config file since the number of items given is fairly small.
-- However for larger scope, a database will be well suited.
File : special_promotions.config
Description : This is where i have configure the special promos.
              Initially I have envisoned that the promos will be flexible in terms of the following:
              
              PRODUCT_CODE | MINIMUM_ITEM | NEW_PRICE_PER_ITEM | FREEBIES | No OF FREEBIES | PAY_ONLY_NO_OF_ITEM
              
              This is the header to the configuration file.
              1.) Checks if the PRODUCT_CODE has an a available promo.
              2.) Checks if the items bought is within the MINIMUM_ITEM
              3.) Checks if there is a definition in the NEW_PRICE_ITEM
                  If yes, it will change the price to the new price as set out in the configuration.
                  If no, it will proceed with the next checking.
              4.) Checks if there is a definition in the FREEBIES and No OF FREEBIES
                  If yes, it will get the description of the freebies and compute the quantity.
                  If no, it will proceed with the next checking.
              5.) Checks if there is a definition in the PAY_ONLY_NO_OF_ITEM
                  If yes, it will get compute the new quantity to be billed.
                  If no, it will proceed with the total computation.
              
File : product_code.config
Description : This is where I have configured the list of the products.
              
              PRODUCT_CODE | DESCRIPTION | PRICE

File : promo_codes.config
Description : This is where I have configured the list of valide promos and there discount rate.

              PROMO_CODE | DISCOUNT_RATE
               

-- The following are the assumptions I had when developing this exercise:

1.) That for each product_code it has only one counterpart in the special promos.

2.) That the promocode will be applied only once, regardless if the application will ask for promocode every other item         bought. In the case of entering another promocode wherein the user already has already supplied a promocode, the application will prompt if the user wants to change the promocode.

3.) That there will always be a unique product code for each item.

4.) That the special promos flexiblity will only be available for the following:
    * New price per item if reached a minimum number of items
    * 1 Freebie product, no matter how many the quantity as long as it is just one product.
    * Promo codes
    * Buy 3(x) pay 2(y) scheme. The x and y variables can be changed to any number. 
