from controller.user_account_function import account_operation

def banking_auth(user_account_number):

    print("-------------------------------------------------------------------")
    print("Press 1 for logout")
    print("-------------------------------------------------------------------")
    print("Press 2 for banking_operation")
    print("-------------------------------------------------------------------")

    user_choice=int(input("Enter choice: "))
    if user_choice==1:
        return 
    elif user_choice==2:
        account_operation(user_account_number)
