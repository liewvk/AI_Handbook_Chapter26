def make_prompt(task, facts):
    return (
        "You are a careful business assistant.\n"
        f"Task: {task}\n"
        f"Verified facts: {facts}\n"
        "Use only the verified facts. State uncertainty."
    )

print(make_prompt("Explain sales change", "Sales rose by 5%."))

