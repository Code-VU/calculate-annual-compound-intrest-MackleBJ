def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you

    # Funcion to gather client information.
    def getClientInfo():
        principal = float(input("Principle (amount): "))
        time =      float(input("Time:               "))
        rate =      float(input("Rate:               "))

        return principal, time, rate

    # Function to calculate amount.
    def calculateAmount(principal, rate, time):
        amount = principal*(1+(rate/100))**time

        return amount

    # Function to calculate compound interest.
    def calculateCompoundInterest(amount, principal):
        compound_interest = amount - principal

        return compound_interest

    client_one_principal, client_one_time, client_one_rate = getClientInfo()
    client_one_amount = calculateAmount(client_one_principal, client_one_rate, client_one_time)
    client_one_compound_interest = calculateCompoundInterest(client_one_amount, client_one_principal)
    print("Compound Interest: {:.2f}".format(client_one_compound_interest))

    print("---")

    client_two_principal, client_two_time, client_two_rate = getClientInfo()
    client_two_amount = calculateAmount(client_two_principal, client_two_rate, client_two_time)
    client_two_compound_interest = calculateCompoundInterest(client_two_amount, client_two_principal)
    print("Compound Interest: {:.2f}".format(client_two_compound_interest))

    print("---")

    client_three_principal, client_three_time, client_three_rate = getClientInfo()
    client_three_amount = calculateAmount(client_three_principal, client_three_rate, client_three_time)
    client_three_compound_interest = calculateCompoundInterest(client_three_amount, client_three_principal)
    print("Compound Interest: {:.2f}".format(client_three_compound_interest))

 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

# calculateCompoundInterest()
