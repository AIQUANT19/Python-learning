from hyperon import MeTTa

metta = MeTTa()

with open("graph_data.metta") as f:
    # data = f.read()
    # print(data)
    # print("Successfully opened!!")
    metta.run(f.read())
    output = metta.run('!(match &self (Bob son of $y) (Bob is son of $y))')
    print(output)
    output1 = metta.run('!(match &self ($x likes $y) ($x likes $y))')
    print(output1)
