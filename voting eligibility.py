def  checking_voting_eligiblity(age):
    if age>=18:
        return "you are eligible to voting"
    else:
        return "you can'nt vote yet"
        
user_age=int(input("Enter your age " ""))

result=checking_voting_eligiblity(user_age)
print(result)