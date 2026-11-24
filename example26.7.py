actual = ["Urgent", "Routine", "Urgent", "Routine", "Urgent"]
predicted = ["Urgent", "Routine", "Routine", "Routine", "Urgent"]
correct = sum(a == b for a, b in zip(actual, predicted))
accuracy = correct / len(actual)
print(f"Accuracy: {accuracy:.0%}")

