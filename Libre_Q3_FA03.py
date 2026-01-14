Name =  [ "Otto", "Gon", "Jerome"]
Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
    
for x in range(len(Steps)):
    total = 0
    highest = Steps[x][0]
    lowest = Steps[x][0]
    
    for y in range(len(Steps[x])):
        total += Steps[x][y]
        if Steps[x][y] > highest:
            highest = Steps[x][y]
        elif Steps[x][y] < lowest:
            lowest = Steps[x][y]
            
    avrg = total/5
    
    print(
        Name[x],
        "- Total Steps: ", total,
        "| Average: ", avrg,
        "| Min: ", lowest,
        "| Max: ", highest
        )
