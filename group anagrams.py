a = ["act", "god", "cat", "dog", "tac"]
result = {}  

for word in a:#act
    
    key = ''.join(sorted(word))  

    if key in result:     #act is not result       
        result[key].append(word) 
    else:
        result[key] = [word] 
        print(result[key],"w")
        print(result,"k")

print(result)
print(list(result.values()))