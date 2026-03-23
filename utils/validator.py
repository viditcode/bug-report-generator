valid_severity = ["Critical","Major","Minor"]
valid_priority = ["P0","P1","P2","P3"]

def get_valid_number(prmopt):
    # need to keep asking for valid severity
    while True:
        try:
            value = int(input(prmopt))
            if value <= 0:
                print("Please enter number more than 0.")
                continue
            return value
        except ValueError:
            print("Please enter the valid number.")

def get_non_empty(prompt):
    # need to keep asking until user enter non empty
    while True:

        value = input(prompt).strip()
        if value == "":
            print("This field can't be empty.")
        else:
            return value

def get_from_list(prompt, allowed):
    while True:
        value = input(prompt).strip()
        if value not in allowed:
            print("Invalid! Must be one of " + ",".join(allowed))
        else:
            return value
        



