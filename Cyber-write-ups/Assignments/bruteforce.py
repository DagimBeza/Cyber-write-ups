import time   # Time module to measure  how long the attack takes.


def brute_force(): # Function
    start = time.time()      # To record the starting time
    attempts = 0             # To count attempts
    
    print("Starting the Attack")
    
    for pin in range(10000):          # Loop to generate every PIN
        current_pin = f"{pin:04d}"    # String formatting to make the PIN four digits i.e string formatting
        attempts += 1                 # To count attempts
        
        print(f"Attempt {attempts}: Trying PIN {current_pin}")     # To display each attempted PIN
        
        if current_pin == secret_pin:    # Conditional statement to Compare the PINs
            end = time.time()            # To measure the end time
            elapsed = end - start        # To calculate time taken
        
            print(" PIN Found!!!")                         # To display that the PIN is found
            print(f"Correct PIN : {current_pin}")
            print(f"Attempts    : {attempts}")             # To display the number of attempts
            print(f"Time Taken  : {elapsed:.4f} seconds")  # To measure the time taken to crack the PIN
            break                                          # To Stop the loop or the program once the correct PIN is found


secret_pin = "1887"     # To store the secret PIN
brute_force()