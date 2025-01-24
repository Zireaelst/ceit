

#Table 5-5. Shipping Costs Based on Country and Quantity
# United States Canada
# Quantity Cost Quantity Cost
# <= 50 6.25 <= 50 8.25
# <= 100 9.50 <= 100 12.50
# <= 150 12.75 <= 150 18.75
# Otherwise 15.00 Otherwise 25.00

quantity = int(input("Please enter the quantity of items you are shipping: "))
country = input("Where are you shipping to: ")

country = country.lower()

NOT_YET = "We don't ship there yet"

def shippingCalculation(country, quantity):
    if (country == 'usa') or (country == 'us') or (country == 'united states'):
        if quantity <= 50:
            shippingCost = 6.25
        elif quantity <= 100:
            shippingCost = 9.50
        elif quantity <= 150:
            shippingCost = 12.75
        else:
            shippingCost = 15.00

    elif country == 'canada':
        if quantity <= 50:
            shippingCost = 8.25
        elif quantity <= 100:
            shippingCost = 12.50
        elif quantity <= 150:
            shippingCost = 18.75
        else:
            shippingCost = 25.00
    else:
        shippingCost = NOT_YET

    return shippingCost


amountForShipping = shippingCalculation(country, quantity)

if amountForShipping == NOT_YET:
    print('Sorry, we do not ship to', country)
else:
    print('It will cost $', amountForShipping, 'to ship your package')
