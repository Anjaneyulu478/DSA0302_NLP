# DFA Simulator

# Accept DFA details
states = input("Enter states (comma separated): ").split(",")
alphabet = input("Enter input alphabet (comma separated): ").split(",")

states = [s.strip() for s in states]
alphabet = [a.strip() for a in alphabet]

# Transition table
transition = {}

print("\nEnter transition table:")

for state in states:
    transition[state] = {}

    for symbol in alphabet:
        next_state = input(
            f"Transition({state}, {symbol}) = "
        ).strip()

        transition[state][symbol] = next_state

# Initial state
initial_state = input("\nEnter initial state: ").strip()

# Final states
final_states = input(
    "Enter final state(s) (comma separated): "
).split(",")

final_states = [s.strip() for s in final_states]

# Number of input strings
n = int(input("\nEnter number of input strings: "))

# Process each string
for i in range(n):
    string = input(f"\nEnter input string {i + 1}: ").strip()

    current_state = initial_state
    path = [current_state]

    valid = True

    for symbol in string:
        if symbol not in alphabet:
            valid = False
            break

        current_state = transition[current_state][symbol]
        path.append(current_state)

    print("\nTransition Path:")
    print(" → ".join(path))

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
