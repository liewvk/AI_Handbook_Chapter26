summaries = 40
minutes_before = 30
minutes_after = 12
hourly_value = 35.0
monthly_cost = 80.0
hours_saved = summaries * (minutes_before - minutes_after) / 60
net_benefit = hours_saved * hourly_value - monthly_cost
print(f"Hours saved: {hours_saved:.1f}")
print(f"Estimated net benefit: RM {net_benefit:.2f}")

