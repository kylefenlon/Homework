months = {
    1: {
        "shortname": "Jan",
        "fullname": "January"
    },
    2: {

    }
}

def return_10():
    return 10

def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(words):
    return len(words)

def join_string(words, words1):
    return words + words1

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

def number_to_full_month_name(num):
    return months[num]["fullname"]

def number_to_short_month_name(num):
    if num == 1:
        return "Jan"
    if num == 2:
        return "Feb"
    if num == 3:
        return "Mar"
    if num == 4:
        return "Apr"
    if num == 5:
        return "May"
    if num == 6:
        return "Jun"
    if num == 7:
        return "Jul"
    if num == 8:
        return "Aug"
    if num == 9:
        return "Sep"
    if num == 10:
        return "Oct"
    if num == 11:
        return "Nov"
    if num == 12:
        return "Dec"
    
    return None


