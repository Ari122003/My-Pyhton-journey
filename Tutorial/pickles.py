import pickle

dic = {"Aritra": 81, "Souvik": 23, "Jyotisman": 39}

with open("Roll.pkl", "wb") as f:

    pickle.dump(dic, f)

with open("Roll.pkl", "rb") as f:
    print(pickle.load(f))


# with open("Roll.pkl", "rb") as f:
#     data = f.read()
# print(type(data))
# print(pickle.loads(data))
# print(type(pickle.loads(data)))
