import sys
class VotingEligibility(Exception):
    def __init__(self):
        print("You are not Eligible for Voting!!")

age = int(input("Enter Your Age:"))
try:
    if age<18:
        raise VotingEligibility
    else:
        print("You are eligible for voting...")
except:
    print(sys.exc_info()[0]," Exception Occurred!!")
