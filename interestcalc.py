#air = Annual interest rate
#noy = number of year
#la = loan amount
#mir = monthly interet rate
#mirp = monthly interet rate percentage
#new changes
print ("good")
air=(eval(input ("Enter Annual interest rate:")))
op= air / 100
mir= air / 12
mirp = air / 1200
noy = eval(input("Enter number of year:"))
la = eval(input("Enter loan amount:"))
mon_pay= la * mirp / (1 - 1 / (1 + mirp) ** (noy * 12))
tot_pay= mon_pay * noy * 12

print("The monthly payment is", int(mon_pay * 100) / 100)
print("The total payment is", int(tot_pay * 100) /100)


