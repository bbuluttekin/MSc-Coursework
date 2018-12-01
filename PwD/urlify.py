# Turn string with spaces to %20 and returns the string


def urlify(input_str):
    """
    Takes string as input and returns it as url accepted for if it.
    Parameters:
    ===========
    input_str: (str) String you want to urlify
    retuns: (str)
    """
    non_space_str = input_str.split(" ")
    return "%20".join(non_space_str)


print(urlify("Mr John Smith"))  # Prints Mr%20John%20Smith
