def retail_report(recent_sales, lead_time, safety_stock, stock):
    if not recent_sales or lead_time < 0 or safety_stock < 0:
        raise ValueError("Invalid business inputs")
    average = sum(recent_sales) / len(recent_sales)
    reorder_point = average * lead_time + safety_stock
    decision = "REORDER" if stock <= reorder_point else "HOLD"
    return average, reorder_point, decision

average, point, decision = retail_report(
    recent_sales=[8, 10, 12], lead_time=4,
    safety_stock=10, stock=42
)
print(f"Average daily sales: {average:.1f}")
print(f"Reorder point: {point:.1f}")
print(f"Recommendation: {decision}")

