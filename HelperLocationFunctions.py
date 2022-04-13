def MatrixMinIndexCheck(Matrix,RowLocation):
    MatrixLocal = Matrix
    Row = RowLocation
    MinList = []
    #print(MatrixLocal)
    #print(type(MatrixLocal))
    for item in MatrixLocal:
        if item[2] == Row:
            MinList.append(item[1])
    MinListIndex = min(MinList)
    print(MatrixLocal)
    return MinListIndex
def MatrixMaxIndexCheck(Matrix,RowLocation):
    MatrixLocal = Matrix
    Row = RowLocation
    MaxList = []
    #print(MatrixLocal)
    #print(type(MatrixLocal))
    for item in MatrixLocal:
        if item[2] == Row:
            MaxList.append(item[1])
    MaxListIndex = max(MaxList)
    return MaxListIndex