# To import current time and one minute later
from datetime import datetime, timedelta
import time

def login_system():
    # To store users
    users = {
            "admin": "admin123",
            "dagim": "python2026",
            "student": "password123"
        }
    
    print("LOGIN SYSTEM")
     
     
     

    failed_attempts = 0

    lock_time = None
  


    while True:
        # To check if the account is locked
        
           current_time = datetime.now()
           
           if lock_time is not None and current_time < lock_time + timedelta(minutes=1):
              remaining = (lock_time + timedelta(minutes=1)) - current_time

              print("\nAccount is locked.")
              print("Try again after", int(remaining.total_seconds()), "seconds.\n")
             
              time.sleep(60)
            

           else:
                 # Unlock account if 1 minute has passed
              if lock_time is not None:
                 failed_attempts = 0
                 lock_time = None
                 print("\nAccount unlocked.\n")

        
              # To ask for username and password
              username = input("Username: ")  
              password = input("Password: ")    
    
              # To print Success
              if username in users and users[username] == password:
                 print("Login Successful!")
                 break
              else:
            
                  failed_attempts += 1
                  print(f"\nInvalid username or password.")
                  print(f"Failed Attempts: {failed_attempts}/5")
                        

                            
                  # To Lock account after 5 failures
                  if failed_attempts >= 5:

                     lock_time = datetime.now()

                     print("\nToo many failed attempts.")
                     print("Account locked for 1 minute.")
                     print("Locked at:", lock_time.strftime("%Y-%m-%d %H:%M:%S"))
                         
     
login_system()                