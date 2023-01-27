import pickle


with open("iris.data", "r") as f:
    item = f.read()
    parsed = item.split("\n")

lol = [i.split(",") for i in parsed]


with open("iris.pkl", "wb") as f:
    pickle.dump(lol, f)


with open("iris.pkl", "rb") as f:
    print(pickle.load(f))
