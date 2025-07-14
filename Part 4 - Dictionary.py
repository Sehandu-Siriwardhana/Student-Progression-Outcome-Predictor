# Create an empty dictionary
report = {}

# Define variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
total_credits = 0
outcome = ""

# Define the function to get credits
def get_credits(credit_type):
    while True:
        try:
            credits = int(input(f"Please enter your credits at {credit_type}: "))
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.\n")
            else:
                return credits
        except ValueError:
            print("Integer required.\n")

# Define the function to calculate progression outcome
def calculate_progression(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits
    if pass_credits == 120:
        return "Progress"
    elif pass_credits >= 100:
        return "Progress (module trailer)"
    elif fail_credits >= 80:
        return "Exclude"
    else:
        return "Do not progress - module retriever"

# Loop for multiple outcomes
while True:
    # Get credits for each type
    student_id = input("\nPlease enter the student ID: ")
    pass_credits = get_credits("pass")
    defer_credits = get_credits("defer")
    fail_credits = get_credits("fail")
    total_credits = pass_credits + defer_credits + fail_credits

    # Check if the total is correct
    if total_credits != 120:
        print("Total incorrect")
        continue

    # Calculate the progression outcome and store it in the report dictionary
    outcome = calculate_progression(pass_credits, defer_credits, fail_credits)
    report[student_id] = [outcome, pass_credits, defer_credits, fail_credits]
    print(outcome)

    # Prompt for continuation or exit
    choice = input("\nDo you want to enter grades for another student?\n Enter 'y' for yes or 'q' to quit and view result: ")
    if choice == "y":
        continue
    elif choice == "q":
        print("\nExiting program...\n")
        print("\n------------------------------------------------------------------------")
        print("\n-----Report-----\n")
        for key, value in report.items():
            print(f"{key}: {value[0]}, Pass: {value[1]}, Defer: {value[2]}, Fail: {value[3]}")
        print("\n------------------------------------------------------------------------")
        break
    else:
        print("\nInvalid choice. Check Again.\n")
