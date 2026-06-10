
age = int(input("Enter your age: "))


is_accompanied_input = input("Are you accompanied by an adult? (yes/no): ").strip().lower()
is_accompanied = (is_accompanied_input == "yes")

has_ticket_input = input("Do you have a valid ticket? (yes/no): ").strip().lower()
has_ticket = (has_ticket_input == "yes")


if (age >= 13 or is_accompanied) and has_ticket:
    print("Access Allowed")
else:
    print("Access Denied")