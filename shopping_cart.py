#!/usr/bin/python

from amaysim_display import ScreenDisplay

class ShoppingCart(ScreenDisplay):
    def __init__(self, pricingRulesConfig, specialPromosConfig, promoCodeConfig):

        self.cartList = {} # Dictionary created for the list of attributes per each item the user buys
        self.pricingRules = {} # Dictionary created to store the loaded config for each product
        self.specialPromotions = {} # Dictionary created to store the loaded config each special promos
        self.promoCodes = {}

        self.forDisplay = [] # List created for the items in Display
        self.totalItem = [] # List created for the internal item code the user buys.

        self.appliedPromoCode = None
        self.lastItemCalled = 0

        # Call the load configuration before doing anything.
        self.set_pricing_rules(pricingRulesConfig)
        self.set_special_promos(specialPromosConfig)
        self.set_valid_promo_codes(promoCodeConfig)

    def set_valid_promo_codes(self, promoCodeConfig):
        ''' This function loads the valid promoCodes set in a configuration file
            and creates a Dictionary for it.
        '''
        fileObject = open(promoCodeConfig, 'r')

        for line in fileObject:

            rules = line.rstrip().split("|")
            self.promoCodes[rules[0]] = rules[1]

        fileObject.close()

    def set_pricing_rules(self, pricingRulesConfig):
        ''' This function loads the current pricing rules set in a configuration file
            and creates a Dictionary for it.
            It has 3 major keys namely: productCode, description, price 
        '''
        ctr = 1
        fileObject = open(pricingRulesConfig, 'r')

        for line in fileObject:

            rules = line.rstrip().split("|")

            self.forDisplay.append(rules[1])

            sctr = str(ctr)
            self.pricingRules[rules[0]] = ctr
            self.pricingRules[sctr + "_productCode"] = rules[0]
            self.pricingRules[sctr + "_description"] = rules[1]
            self.pricingRules[sctr + "_price"] = rules[2]

            ctr += 1
        fileObject.close()

    def set_special_promos(self, specialPromosConfig):
        ''' This function loads the special rules/promos current set in a configuration file
            and creates a Dictionary for it.
            It has 4 major keys namely: minimumItem, newPricePerItem, freebies, noOfFreebies, newQuantity
            The idea here is to generalize the code in which it can be flexible upon additional rules. 
        '''
        ctr = 1
        fileObject = open(specialPromosConfig, 'r')

        for line in fileObject:

            rules = line.rstrip().split("|")

            self.specialPromotions[rules[0] + "_minimumItem"] = rules[1]
            self.specialPromotions[rules[0] + "_newPricePerItem"] = rules[2]
            self.specialPromotions[rules[0] + "_freebies"] = rules[3]
            self.specialPromotions[rules[0] + "_noOfFreebies"] = rules[4]
            self.specialPromotions[rules[0] + "_newQuantity"] = rules[5]

            ctr += 1
        fileObject.close()

    def add_items(self, noOfItems, promoCode):
        ''' This function adds the items into the cartList as set out by the user. 
        '''
        item = self.lastItemCalled

        if promoCode.lower() == 'a':
            promoCode = self.appliedPromoCode
        elif self.appliedPromoCode is None:
            self.appliedPromoCode = promoCode

        if item + "_quantity" in self.cartList:
            self.cartList[item + "_quantity"] += int(noOfItems)             
        else:
            self.cartList[item + "_quantity"] = int(noOfItems)
            self.totalItem.append(item)

    def check_items(self, key):
        ''' This function checks if the answer to the start_page is within the agreeable answer.
        '''
        pricingRules = getattr(self, 'pricingRules', {})
        skey = str(key)
        if skey + "_description" in pricingRules:
            self.lastItemCalled = key
            return 0
        elif skey == "view":
            return 1
        elif skey == "exit":
            return 2

    def total(self,):
        ''' This function computes for the total prices and quantity as set out by the user. 
        '''

        # Initialize variables needed
        totalPrice = 0
        newQuantity = 0
        newPrice = 0

        for item in self.totalItem:
            key = str(item)

            if (str(item) + "_description") in self.pricingRules:

                quantity = self.cartList[key + "_quantity"]

                description = self.pricingRules[key + "_description"]
                productCode = self.pricingRules[key + "_productCode"]

                newPrice = self.pricingRules[key + "_price"]
                newQuantity = quantity

                # Run thru special promos
                if productCode + "_minimumItem" in self.specialPromotions:
                    if quantity >= int(self.specialPromotions[productCode + "_minimumItem"]):

                        # Special promo for new price item when reached a minimum number of items
                        if not (self.specialPromotions[productCode + "_newPricePerItem"] == "" or None):
                            newPrice = self.specialPromotions[productCode + "_newPricePerItem"]

                        # Special promo for freebies
                        if not (self.specialPromotions[productCode + "_freebies"] == "" or None):
                            noOfMultiplier = int(quantity / int(self.specialPromotions[productCode + "_minimumItem"])) 

                            freebies = self.specialPromotions[productCode + "_freebies"]
                            noOfFreebies = int(self.specialPromotions[productCode + "_noOfFreebies"]) * noOfMultiplier

                            itemCodeForFreebies = str(self.pricingRules[freebies])
                            self.cartList[key + "_freebies"] = self.pricingRules[itemCodeForFreebies + "_description"]
                            self.cartList[key + "_noOfFreebies"] = noOfFreebies

                        # Special promo for buy 3 for 2 items
                        if not (self.specialPromotions[productCode + "_newQuantity"] == "" or None):
                            noOfMultiplier = int(quantity / int(self.specialPromotions[productCode + "_minimumItem"]))
                            noOfLeftOutItem = int(quantity % int(self.specialPromotions[productCode + "_minimumItem"]))

                            newQuantity = (int(self.specialPromotions[productCode + "_newQuantity"]) * noOfMultiplier) + noOfLeftOutItem
                            

                self.cartList[key + "_price"] = int(newQuantity) * float(newPrice)
                self.cartList[key + "_quantity"] = quantity
                self.cartList[key + "_description"] = description


                totalPrice += self.cartList[key + "_price"]

        if self.appliedPromoCode in self.promoCodes:
            totalPrice = totalPrice * (float(100 - int(self.promoCodes[self.appliedPromoCode])) / 100)
        else:
            print("Promo code %s is not valid." % self.appliedPromoCode)

        return self.totalItem, self.cartList, totalPrice

