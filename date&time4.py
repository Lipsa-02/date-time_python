from datetime import datetime
today=datetime.now()
tds=today.strftime("%w")
print("D&T:",today)
print("Today date&time details:",today.strftime("%w"))
print("Day no.of the week is:",today.strftime("%W"))
print("Today is:",today.strftime("%A"))
print("date in format of d-m-y:",today.strftime("%d-%m-%Y"))
print("Month in words:",today.strftime("%B"))