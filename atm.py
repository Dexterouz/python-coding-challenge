# creating the bank account database
account_db = {
    '0023547564' : {
        'first_name' : 'Godson',
        'last_name' : 'Dexterous',
        'email_addr' : 'dexterouskc@gmail.com',
        'password' : '199866',
        'acct_bal' : 80000,
        'acct_type' : 'savings'
    },
    '0023877434' : {
        'first_name' : 'Zubby',
        'last_name' : 'Egwuchukwu',
        'email_addr' : 'zubby707@gmail.com',
        'password' : '1996',
        'acct_bal' : 90000,
        'acct_type' : 'current'
    }
}

# function for transferring money
def transfer(user_acct_nos):
    '''For making money transfer to another user'''

    # retrieving the sender account balance
    sender_acct_bal = account_db[user_acct_nos]['acct_bal']

    # a flag to control the loop
    flag = True

    while flag:
        # prompt user to enter account number and 
        # enter amount to transfer
        get_recepient_acct_no = input("\nEnter recepient account no: ")
        amt_to_transfer = int(input("Enter the amount to transfer: "))

        # check whether recipient account number is in the
        # Database
        if get_recepient_acct_no not in account_db:
            print("\nRecepient account number not found")
            flag = True
            
        # check if the amount to transfer is greater than balance
        elif amt_to_transfer > sender_acct_bal:
            print("\nYou have an insufficient balance to make this transaction")
            print("Your account balance is $"+str(sender_acct_bal))
            flag = True

        # if everything is ok, display transaction report
        else:
            flag = False
            # update the balance database
            sender_acct_bal -= amt_to_transfer

            # recipient name
            recepient_f_name = account_db[get_recepient_acct_no]['first_name']
            recepient_l_name = account_db[get_recepient_acct_no]['last_name']

            print("\nTransfer of $" + str(amt_to_transfer) + " to " + recepient_f_name + " " + recepient_l_name + " was successful")
            print("Your account balance is $" + str(sender_acct_bal))



# function for withdrawal
def withdraw(user_acct_nos):
    '''For withdrawing money from a user's account'''

    # retrieving withdrawer's account balance
    withdrawer_acct_bal = account_db[user_acct_nos]['acct_bal']

    # a flag to control loop
    flag = True
    while flag:
        # prompt user to enter withdrawing amount
        withdraw_amt = int(input("\nEnter the amount to withdraw: "))

        # check if the amount to withdraw is greater
        # than the account balance
        if (withdraw_amt > withdrawer_acct_bal):
            print("You have an insufficient balance to make this transaction")
            flag = True
        else:
            flag = False
            # update the balance in the database
            withdrawer_acct_bal -= withdraw_amt

            # display transaction report
            print("\nWithdrawal of $" + str(withdraw_amt) + " was successful")
            print("Your account balance is $" + str(withdrawer_acct_bal))



def balance(user_acct_nos):
    '''For getting user account balance'''

    acct_bal = account_db[user_acct_nos]['acct_bal']
    
    # return balance
    return "Your account balance is $" + str(acct_bal)


# the main function
def main():
    '''This is the main function that runs the ATM'''

    # validate the account number
    flag = True
    while flag:
        account_no = input("Enter your account number: ")
        if account_no not in account_db:
            print("Account number do not exist")
            flag = True
        else:
            flag = False

            flag2 = True
            while flag2:
                acct_password = input("\nEnter your password: ")
                if (acct_password) != (account_db[account_no]['password']):
                    print("Incorrect password")
                    flag = True
                else:
                    flag2 = False

                    flag3 = True
                    # get user fullname
                    first_name = account_db[account_no]['first_name']
                    last_name = account_db[account_no]['last_name']

                    while flag3:
                        # print welcome message
                        print("\n\tWelcome " + first_name + " " + last_name)
                        print("\t-- Here are your menu --")
                        print("\n1) Press 1 for transfer")
                        print("2) Press 2 for withdrawal")
                        print("3) Press 3 for checking balance")
                        print("4) Press 4 to quit")

                        menu_no = int(input("\nEnter your menu number: "))
                        if menu_no == 1:
                            transfer(account_no)
                            question = input("\nDo you want to conduct another transaction: (y/n) ")
                            if question == 'y':
                                flag3 = True
                            else:
                                flag3 = False
                        elif menu_no == 2:
                            withdraw(account_no)
                            question = input("\nDo you want to conduct another transaction: (y/n) ")
                            if question == 'y':
                                flag3 = True
                            else:
                                flag3 = False
                        elif menu_no == 3:
                            print(balance(account_no))
                            question = input("\nDo you want to conduct another transaction: (y/n) ")
                            if question == 'y':
                                flag3 = True
                            else:
                                flag3 = False
                        else:
                            break
                            
# calling the main function
main()