accounts = {
    "Jonas" : "jon123",
    "Ulrich" : "ulc432",
    "Mikkel" : "mike22",             # Stored Usernames and Passwords
    "Noah" : "nn213x", 
    "No User" : "NA",
    "Suspended_User" : "9999"
} 

suspended = {"Suspended_User"}       # For users whose accounts are suspended

# No. of attempts available
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    Username = str(input("Enter username : "))
    Password = str(input("Enter password : "))

    if not Username or not Password:
        print("Cannot be empty, try again.")
        continue
    
    if Username in suspended:
        print("User suspended")
        pass
        attempts += 1
        continue

    if Username in accounts and accounts[Username] == Password:
        print("Welcome user!")
        break 
    else:
        print("Login unsuccessful")
        attempts += 1
        
if attempts == max_attempts:
    print("Limit breached, access denied")



