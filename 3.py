print("===3===")
drops = [3, 0, 5, 1, 0, 2, 4]
bad_days = 0
for d in drops:
    if d > 2:
        bad_days += 1
print("pis gunler:",bad_days)
