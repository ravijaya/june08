from datetime import datetime



dob = datetime(1982, 1, 17, 16, 15)
ts = datetime.now()

print(ts - dob)
tot_days = (ts - dob).days
print(divmod(tot_days, 365.25))
