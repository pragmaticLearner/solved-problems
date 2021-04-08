# https://www.codewars.com/kata/57e92e91b63b6cbac20001e5

def duty_free(price, discount, holiday_cost):
    return holiday_cost // ((discount / 100) * price)


print(duty_free(100, 5, 500))
