import datetime

def CurrentDate():
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    return year, month, day

def AgeInTermsofDay(birth_year, birth_month, birth_day):
    current_year, current_month, current_day = CurrentDate()
    years = current_year - birth_year
    months = current_month - birth_month
    days = current_day - birth_day

    totalDays_alive = (years * 365) + (months * 30) + days
    return totalDays_alive

def TotalHours(totalDays_alive):
    total_hours = totalDays_alive * 24
    return total_hours

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

totalDays = AgeInTermsofDay(birth_year, birth_month, birth_day)

print("The person has been living for " + str(totalDays) + " days.")

totalHours = TotalHours(totalDays)

print("The person has been living for " + str(totalHours) + " hours.")



