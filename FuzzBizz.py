def FuzzBizz():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FuzzBizz")
        elif i % 3 == 0:
            result.append("Fuzz")
        elif i % 5 == 0:
            result.append("Bizz")
        else:
            result.append(str(i))
    print(result)

FuzzBizz()