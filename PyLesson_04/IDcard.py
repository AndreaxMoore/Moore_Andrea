def printf(name,term):
    print("*"+"{:>14}{:>18}".format(name,term)+" *")
name1 = input("Enter your first name: ")
term1 = input("Enter your last name: ")
name2 = input("Enter your title: ")
term2 = input("Enter the school site: ")
name3 = input("Enter the school year: ")
term3 = input("What is your subject: ")
print("***********************************")
printf(term2,name3)
printf(name1,term1)
printf(name2,term3)
print("***********************************")


