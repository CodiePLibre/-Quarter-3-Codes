Name =  [ "Otto", "Gon", "Jerome"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
    
Total_daily = []

for x in range(len(Day)):
    total = 0
    
    for y in range(len(Steps)):
        total += Steps[y][x]
    Total_daily.append(total)
    
for z in enumerate(Total_daily):
    print(f"{Day[z[0]]}: {z[1]}")

mst_actv = Total_daily.index(max(Total_daily))

print("The most active day overall was", Day[mst_actv], "with a total step count of", Total_daily[mst_actv], "steps.")
