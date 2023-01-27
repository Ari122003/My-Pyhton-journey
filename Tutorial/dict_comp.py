

dic1 = {i: f"Item{i}" for i in range(1, 6)}

dic2 = {value: key for key, value in dic1.items()}

print(dic1)
print(dic2)
