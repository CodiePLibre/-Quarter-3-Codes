Name =  [ "Otto", "Gon", "Jerome"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
    
total = [sum(x) for x in Steps]
larg = total.index(max(total))
highest = max(total)
lowest = min(total)
diff = highest - lowest

print("The person with the highest step count is", Name[larg], "with a total of", highest,"steps.")
print("The difference between the highest and lowest total is", diff)
