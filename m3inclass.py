age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
has_permit = input("Do you have any permit?(y/n): ").lower() == "yes"

def is_age_eligible(age):
    if age < 16:
        return  False #not eligible
    if 16 <= age <= 17:
        return "Permit" # eligible for a learner's permit
    if age >= 18:
        return True #eligible for a driver's licence

def is_test_passed(score):
    if score >= 70:
        return True
    else:
        return False

def is_eligible(age, score, has_permit=False):
    if is_age_eligible(age) and is_test_passed(score) is True:
        return "Licence"
    elif is_age_eligible(age) is True and is_test_passed(score) is False:
        return "Fail"
    elif is_age_eligible(age) == "Permit" and is_test_passed(score) is True:
        return "Permit"
    elif is_age_eligible(age) == "Permit" and is_test_passed(score) is False and has_permit:
        return "Licence(with permit)"
    elif is_age_eligible(age) == "Permit" and is_test_passed(score) is False:
        return "Fail"
    elif is_age_eligible(age) is False:
        return "Ineligible"


print(is_eligible(age, score, has_permit))


