def MatrixMaxIndexCheck(Matrix,FirstRun,MatrixMaxIndex):
    if FirstRun == 1:
        MatrixMaxIndex = Matrix[-1][1]
        print(MatrixMaxIndex)
    return MatrixMaxIndex
def HelperFunctionCheckRowIndexShapeIndexMatrixIndex(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndexNumber,NewShapeSearch):
                             
        if row[1] == LocationOfEyeMovementIndex and row[2] == RowNumber and row[0].strip() != "" and NewShapeSearch == False:
                    return True
def HelperFunctionCheckRowIndexShapeIndexMatrixIndexSpaceInShape(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndexNumber, NewShapeSearch):
            if row[1] == LocationOfEyeMovementIndex and row[2] == RowNumber and row[0].strip() == "" and NewShapeSearch == False:
                    return True 
#Net 3 
def HelperFunctionCheckRowIndexShapeIndexMatrixIndexSpaceInShapeNotTrue(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndex,NewShapeSearch):           
            if RowNumber == row[2] and row[1] == ShapeIndex and row[0].strip() != "" and NewShapeSearch == True:
                    return True
#def HelperFunctionSpaceInNextRowNotTrue(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndexNumber):
            #if MatrixMaxIndex == ShapeIndexNumber and RowNumber != 0 and row[1] == ShapeIndexNumber and row[0].strip() != "":
              #      return True 
def HelperFunctionSpaceInNextRow(row,RowNumber,MatrixMaxIndex,ShapeIndexNumber):
            if RowNumber == 0 and row[1] == ShapeIndexNumber and row[0].strip() == "":
                    return True
def HelperFunctionSetTheShapeIndexNumber(Matrix,RowNumber,NewShapeSearch,MaxShapeOfRow,LocationOfEyeMovementIndex,MatrixMaxIndex):

    if NewShapeSearch == True:
        print(MatrixMaxIndex)
        print("Debugging function")
        print(LocationOfEyeMovementIndex)
        StepOfEyes = MatrixMaxIndex - LocationOfEyeMovementIndex
        print(StepOfEyes)
        print(MaxShapeOfRow)
       
        ShapeIndex = MaxShapeOfRow - StepOfEyes
        
    else:
        ShapeIndex = MaxShapeOfRow
    return ShapeIndex

def HelperFunctionMaxIndexShape(Matrix,RowNumber,NewShapeSearch):
    if NewShapeSearch == True:
        MaxIndexOfShapeRowlist = []
        for items in Matrix:
            if items[2] == RowNumber:
                MaxIndexOfShapeRowlist.append(items[1])
        MaxShapeOfRow = max(MaxIndexOfShapeRowlist)
        return MaxShapeOfRow
                    
def FirstRunCheckLocationOfEyeMovementIndex(FirstRun,Matrix,LocationOfEyeMovementIndexNumber):
    if FirstRun == 1:
        LocationOfEyeMovementIndex = Matrix[-1][1]
    return LocationOfEyeMovementIndex
def FirstRunCheckRowNumber(FirstRun,Matrix,RowNumber):
    if FirstRun == 1:
        RowNumber = Matrix[-1][2]
    else: 
        RowNumber = RowNumber
    return RowNumber
def FirstRunCheckNewShapeSearch(FirstRun,Matrix,NewShapeSearch):
    if FirstRun == 1:
        NewShapeSearch = False
    else: 
        NewShapeSearch = NewShapeSearch
    return NewShapeSearch

def FirstRunCheck(FirstRun):
    if FirstRun == 1:
        FirstRun = 2
    return FirstRun