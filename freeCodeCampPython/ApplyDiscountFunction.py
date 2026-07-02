def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return('The price should be a number')
    elif not isinstance(discount, (int, float)):
        return('The discount should be a number')
    elif price <= 0:
        return('The price should be greater than 0')
    elif discount < 0 or discount > 100:
        return('The discount should be between 0 and 100')
    elif discount == 0:
        return(price)
    else:
        final = price - (float(discount/100) * float(price))
        return(final)

apples = apply_discount(100, 20)
oranges = apply_discount(200, 50)
mango = apply_discount(50, 0)
banana = apply_discount(74.5, 20.0)
