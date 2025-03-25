
arr = [3, 1, 5, 2, 4]
target = 9
seen = set()

for num in arr:
    complement = target - num 
    if complement in seen:
        print("The numbers are:", num, "and", complement)
        print("sum", num + complement)
        break
    seen.add(num)
    
else:
    print("No two numbers found with sum 9")
    


