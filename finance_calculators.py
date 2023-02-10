import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment   - to calculate the amount of interest you'll earn on interest")
print("bond         - to calculate the amount you'll have to pay on a home loan")

user_choice=input("Enter your choice: (investment/bond)").lower()

#Calculates the amount the user will get after an investment of a certain period of years
if user_choice == "investment":
    deposit=float(input("What amount do you want to deposit: "))
    interest_rate=float(input("What is your interest rate as a percentage? "))
    num_years=float(input("Enter the number of years you want to invest for: "))
    interest=input("Do you want simple or compound interest? (simple/compound)").lower()


#Calculates the amount if the user chooses to use simple interest
    if interest== "compound":
        total_amount=deposit * math.pow(1 + (interest_rate/100),num_years)
        total_amount_round=round(total_amount,2)
        print(f"The total amount you will get is {total_amount_round} after {num_years} years at an interest rate of {interest_rate}%.")


#Calculates the amount if the user chooses to use compound
    if interest =="simple":
       total_amount=deposit * (1 + (interest_rate/100) * num_years)
       total_amount_round=round(total_amount,2)
       print(f"The total amount you will get is {total_amount_round} after {num_years} years at an interest rate of {interest_rate}%.")


#Calculates the amount the user will repay if they do a home loan
if user_choice == "bond":
    house_value=float(input("What is your present value of your house? "))
    interest_rate=float(input("What is your interest rate as a percentage? "))
    months_to_repay=int(input("Enter the number of months you plan to repay the bond: "))
    i=interest_rate/12
    amount_to_be_repaid=(i/100*house_value)/(1-(1+i/100)**(- months_to_repay))
    amount_to_be_repaid_round=round(amount_to_be_repaid,2)
    print(f"The total amount to repay every month is {amount_to_be_repaid_round}.")

    



    
                      
    
    


