Name =  [ "Me", "Lia", "Jake"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    ["4500", "5200", "4800", "5000", "5300"],
    ["4000", "4100", "3900", "4200", "4600"],
    ["6000", "5800", "5900", "6100", "6200"]
    ]
    
Jake = Name.index("Jake")
Wday = Day.index("Wednesday")

print("Jake's steps on Wednesday:", Steps[Jake][Wday])

Me = Name.index("Me")
print("My steps...", Steps[Me])

Thday = Day.index("Thursday")
Steps[Me][Thday] = "5500"

print("Updating my Thursday steps to 5500.")
 
print("My updated steps:", Steps[Me])
