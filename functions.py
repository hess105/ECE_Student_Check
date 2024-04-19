import msvcrt
import re
import time

def extract_id(input_string):
    pattern = r'=(\d{10})='  # Regular expression pattern to match 10 digits between '=' signs
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return None

def is_ece_student(input_string):

    # Implement binary search algorithm

    return False

def merge_sort(input_list):

    # Implement merge sort algorithm for csv data

    return input_list

def is_redeemable(input_string, dow):

    # 1-1 Search through the daily list

    return False

def log_snack_redemption(input_string, dow):

    # Add Purdue ID to daily list

    return False