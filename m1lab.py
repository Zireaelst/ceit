birth_year = 1998
current_year = 2024


birth_month = 4
current_month = 10


birth_day = 11
current_day = 25


years_alive = current_year - birth_year
months_alive = current_month - birth_month
days_alive = current_day - birth_day


total_days_alive = (years_alive * 365) + (months_alive * 30) + days_alive

total_hours_alive = total_days_alive * 24

print(f"The person has been living for {total_days_alive} days.")

print(f"The person has been living for {total_hours_alive} hours.")
