import msvcrt
import time

def read_card():
    """
    Records user input until a semicolon is encountered, then records until a question mark is encountered.
    
    Returns:
        str: The recorded data as a string, with leading and trailing whitespace removed.
    """
    data = ""
    semicolon_found = False
    
    while True:
        char = msvcrt.getwch()  # Get a character without requiring Enter
        data += char
        
        if char == ";" and not semicolon_found:
            semicolon_found = True
            data = char  # Start recording from semicolon
        elif semicolon_found and char == "?":
            data += char  # Record until question mark is found
            break
            
    return data.rstrip('\n')

def getID(raw_output):
    """
    Extracts the card ID from the given raw output string.

    Parameters:
        raw_output (str): The raw output string containing the card ID.

    Returns:
        str: The extracted card ID.
    """
    # Find the index of the substring after the second '=' character
    start_index = raw_output.find('=', raw_output.find('=') + 1) + 1
    
    # Find the index of the substring after the third '=' character
    end_index = raw_output.find('=', start_index) 
    
    # Extract the substring between the second and third '=' characters
    card_id = raw_output[start_index:end_index]
    
    return card_id

if __name__ == '__main__' :
    #Below are the Test Cases!

    # INIT STATEMENT
    # ----------------------------------------------------------------------------
    print("Please insert your card...")

    # TESTCASE FOR record_raw
    # ----------------------------------------------------------------------------
    recorded_data = read_card()
    print("Recorded data:",recorded_data)

    # TESTCASE FOR getID
    # ----------------------------------------------------------------------------
    
    #print(getID(";000000000=1229=0032628840=01?"))
    # Expected output: 0032628840

    extracted_id = getID(recorded_data)
    print("Extracted ID:", extracted_id)

    # EXIT STATEMENT
    # ----------------------------------------------------------------------------
    print("Exiting...")
    time.sleep(5)


    