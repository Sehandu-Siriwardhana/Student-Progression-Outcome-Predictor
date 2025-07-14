#PART 1 - MAIN VERSION

    # Declaring variables
credits =[]
pass_credits =[]
defer_credits =[]
fail_credits =[]
total_credits =[]
outcome =[]
calculate_progression =[]
progression_data =[]
choice =[]
data =[]
text_file =[]

    # Declaring variables for histogram data
progress_count = 0
trailing_count = 0
retriever_count = 0
exclude_count = 0

#B. VALIDATION
    # Define the function to get credits from the user
def get_credits(credit_type):
    while True:
        try:
            credits = int(input(f"Please enter your credits at {credit_type}:"))
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.\n")
                continue
            return credits
        except ValueError:
            print("Integer required.\n")
#A. OUTCOMES
    # Define the function to calculate progression outcome
def calculate_progression(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits
    
    if pass_credits == 120:
        return "\nProgress\n"
    elif pass_credits == 100:
        return "\nProgress (module trailer)\n"
    elif fail_credits >= 80:
        return "\nExclude\n"
    else:
        return "\nDo not Progress - module retriever\n"

# Loop for multiple outcomes
while True:
    pass_credits = get_credits("pass")
    defer_credits = get_credits("defer")
    fail_credits = get_credits("fail")
    if pass_credits + defer_credits + fail_credits != 120:
        print("Total incorrect.\n")
        continue
    outcome = calculate_progression(pass_credits,defer_credits,fail_credits)
    progression_data.append((pass_credits, defer_credits, fail_credits, outcome))
    print(outcome)

#D. HISTROGRAM.
    # Update histogram data
    if outcome == "\nProgress\n":
        progress_count += 1
    elif outcome == "\nProgress (module trailer)\n":
        trailing_count += 1
    elif outcome == "\nDo not Progress - module retriever\n":
        retriever_count += 1
    else:
        exclude_count += 1

#C. MULTIPLE OUTCOMES
    choice = input("Do you want to enter grades for another student?\nEnter 'y' for yes or 'q' to quit and view result: : ")
    if choice == "q":
        print("\nExiting program...\n")
        break
    elif choice == "y":
        continue
    else:
     print("\nInvalid choice. Exiting program with output....\n")
     break
                    
    # Display the histogram
print("\n------------------------------------------------------------------------")
print("\n-----Histogram-----")
print(" \n     Progress  {} : {}".format(progress_count, '*'*progress_count))
print("     Trailer   {} : {}".format(trailing_count, '*'*trailing_count))
print("     Retriever {} : {}".format(retriever_count, '*'*retriever_count))
print("     Excluded  {} : {}".format(exclude_count, '*'*exclude_count))
print("\n------------------------------------------------------------------------")
print("  {} outcomes in total.".format(progress_count+trailing_count+retriever_count+exclude_count))

# PART 2 - LIST.
print("\n------------------------------------------------------------------------")
print("Part 2:")
for data in progression_data:
    print(f"{data[3]} - {data[0]}, {data[1]}, {data[2]}")

# PART 3 - TEXT FILE.
text_file = open("Text_file.txt", "w")
text_file.write("Part 3:\n")
for data in progression_data:
  text_file.write(f"{data[3]} - {data[0]}, {data[1]}, {data[2]} \n")
text_file.close()
