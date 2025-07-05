# Simple Voting System

# Dictionary to store candidates and their vote count
candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Number of voters
num_voters = int(input("Enter the number of voters: "))

# Voting loop
for i in range(num_voters):
    print("\nCandidates:", ", ".join(candidates.keys()))
    vote = input(f"Voter {i + 1}, enter the name of your chosen candidate: ")

    # Validate vote
    if vote in candidates:
        candidates[vote] += 1
        print("Vote recorded.")
    else:
        print("Invalid candidate name. Vote not counted.")

# Show vote count for each candidate
print("\n--- Voting Results ---")
for name, count in candidates.items():
    print(f"{name}: {count} vote(s)")

# Find the winner
winner = max(candidates, key=candidates.get)
max_votes = candidates[winner]

# Check for tie
winners = [name for name, count in candidates.items() if count == max_votes]

if len(winners) == 1:
    print(f"\nWinner: {winner} with {max_votes} vote(s)!")
else:
    print(f"\nIt's a tie between: {', '.join(winners)} with {max_votes} vote(s) each.")
