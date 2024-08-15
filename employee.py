name  = input("Enter name:")
print(name)

print("--------------------------Monthly Salary-------------------------------------------------------")
salary = 2028
print(salary)
print("--------------------------Unsociadle All---------------------------------------------------------")
uns = 60
reit_n = 3.86
total_un = float(uns) * float(reit_n)
print(total_un)

print("------------------------- All Rate---------------------------------------------------------------")

print("-----Day Rate------\n")
reit_day = 11.70
print(reit_day)
print("--Unsocial all Rate-\n")
reit_n = 3.86
print(reit_n)
print("---Over Day Rate----\n")
oh1 = 17.55
print(oh1)
print("--Over Night Rate---\n")
oh1n = 23.34
print(oh1n)

print("---- Add  Overtime----")


print("---------------------------------------------------------------------------------------------------")
over_d = input("Over done on Day:\n")

print("---------------------------------------------------------------------------------------------------")
over_n = input("Over done on Night:\n")

print("---------------------------------------------------------------------------------------------------")

total_d = float(oh1) * float(over_d)
print(str(total_d) + " "  + str("Total Overtime  Day ")+ " " + over_d)
#print("Total Overtime Day")

total_n = float(oh1n) * float(over_n)
print(str(total_n) + " "  + str("Total Overtime Night") + " " + over_n)
#print("Total Overtime Night-")



total = salary + total_un + total_d + total_n
print(total)
#tax = 20
#total_f = Total % tax


print("---------------------------------------------Append Script--------------------------------------------")

a = open("sorin.txt", 'a')

#print(x.readline())

print(a.write(


    name +"\n\n"+
    str(salary) +" "+ str("salary of  the Monthly  ")+"\n\n"+
    str(total_un) +" "+ str("Unsociadle All  ")+"\n\n"+
    str(reit_day) +" "+ str("Day Rate  ")+"\n\n"+
    str(reit_n) +" "+ str("Unsociadle Rate  ")+"\n\n"+
    str(oh1) +" "+ str("Overtime Day Rate  ")+"\n\n"+
    str(oh1n) +" "+ str("Overtime Night Rate  ")+"\n\n"+
    str(total_n) +" "+ str("Total Overtime Night  ") + over_n +"\n\n"+
    str(total_d) + " "  + str("Total Overtime Day  ") + over_d  +"\n\n"+
    str(total) +" "+ str("Grosse Salary ")+"\n\n"
  

              
             +"\n" ))

a.close()


print("---------------------------------------------Record----------------------------------------------------")

a = open("sorin.txt", 'r')
#print(x.readline())
print(a.read())

a.close()
