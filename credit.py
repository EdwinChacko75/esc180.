"""The Credit Card Simulator starter code
You should complete every incomplete function,
and add more functions and variables as needed.
Ad comments as required.
Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.
Author: Michael Guerzhoy.  Last modified: Oct. 3, 2022
"""

# You should modify initialize()
def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None    
    
    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    return day1 == day2 and month1 == month2 or day1 > day2 and month1 == month2 or month1 > month2
#print(date_same_or_later(12,12,3,12))

def all_three_different(c1, c2, c3):
    return c1 != c2 != c3 != c1 
#print(all_three_different(1,2,3))
    
def purchase(amount, day, month, country):
    global last_country, last_country2, last_update_day, last_update_month, cur_balance_owing_intst, cur_balance_owing_recent
    if country != last_country != last_country2:
        return 'error'
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    if month == last_update_month:
        cur_balance_owing_recent += amount
    else:
        cur_balance_owing_intst += amount
    last_country2, last_country = last_country, country
    last_update_day, last_update_month = day, month 
    #print(cur_balance_owing_intst)

def amount_owed(day, month):
    global last_country, last_country2, last_update_day, last_update_month, cur_balance_owing_intst, cur_balance_owing_recent
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    if month != last_update_month != 1:
        cur_balance_owing_intst = cur_balance_owing_intst * (1.05 ** (month - last_update_month)) + cur_balance_owing_recent * (1.05 ** (month - last_update_month - 1))
        cur_balance_owing_recent = 0

    last_update_day, last_update_month = day, month 

    return cur_balance_owing_intst + cur_balance_owing_recent
#intst var not maintaining value after adding shit
    
    
def pay_bill(amount, day, month):
    global last_country, last_country2, last_update_day, last_update_month, cur_balance_owing_intst, cur_balance_owing_recent
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    day, month = last_update_day, last_update_month
    if cur_balance_owing_intst != 0 and cur_balance_owing_intst > amount:
        cur_balance_owing_intst -= amount
    else:
        amount -= cur_balance_owing_intst
        cur_balance_owing_intst = 0
        cur_balance_owing_recent -= amount



        

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0                              (Test1)
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)                 (Test2)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)               (Test3)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)               (Test4)
    pay_bill(30, 7, 3)      
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)               (Test5)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05) (Test6)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375                          (Test7)
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in    (Test8)
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase     (Test9)
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)          (Test10)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375                        (Test11)
                                                # (43.65375*1.05+40
