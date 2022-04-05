from DecryptDeviceXHelperFunctions import *
from GatheringTweetsFunctions import *
TweetListOfUserX = GetTweetsFromUserX('jack',1000)
ResultsIndexMaster = GetParticularTweetFromUser(TweetListOfUserX,18)
Shape = []
def ScannForShapesInMatrixesRowIndex(Matrix,Shape,LocationOfEyeMovementIndexInput,ShapeIndexNumber,NewShapeSearch,RowNumber,FirstRun,MatrixMaxIndex):
    #Shape
    #Set The ShapeIndexNumber Max Number 
    MaxShapeOfRow = HelperFunctionMaxIndexShape(Matrix,RowNumber,NewShapeSearch)
    #MaxShapeOfRow = max(MaxIndexOfShapeRow)
    #print(MaxShapeOfRow)
    #Set The ShapeIndexNumber
    #Check that the LocationofEyeMovementIndex Is First Run
    try:
        if LocationOfEyeMovementIndexInput == -1:
            LocationOfEyeMovementIndex = Matrix[-1][1]
        else:
            LocationOfEyeMovementIndex = LocationOfEyeMovementIndexInput
            LocationOfEyeMovementIndex
    except:
        LocationOfEyeMovementIndex = Matrix[-1][1]
    NewShapeSearch = FirstRunCheckNewShapeSearch(FirstRun,Matrix,NewShapeSearch)
    MatrixMaxIndex = MatrixMaxIndexCheck(Matrix,FirstRun,MatrixMaxIndex)
    RowNumber = FirstRunCheckRowNumber(FirstRun,Matrix,RowNumber)
    print(RowNumber)
    print("RowNumber")
    print(Matrix,RowNumber,NewShapeSearch,MaxShapeOfRow,MaxShapeOfRow,LocationOfEyeMovementIndex)
    print(MaxShapeOfRow)
    ShapeIndex = HelperFunctionSetTheShapeIndexNumber(Matrix,RowNumber,NewShapeSearch,MaxShapeOfRow,LocationOfEyeMovementIndex,MatrixMaxIndex)

    FirstRun = FirstRunCheck(FirstRun)
    #Feedback Variables
    ShapeGrower = 0
    print("Shape Index")
    print(ShapeIndex)
    #Need Function To Get Top row LocationOfEyeMovementIndex 
    while LocationOfEyeMovementIndex != 40:  
        for row in Matrix:
            ShapeTracker = []
            if HelperFunctionCheckRowIndexShapeIndexMatrixIndex(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndex,NewShapeSearch) == True:
                    ShapeGrower = ShapeGrower + 1
                    #ShapeTracker.append(ShapeGrower,row[0],row[1],row[2],LocationOfEyeMovementIndex)
                    ShapeTracker.append(ShapeGrower)
                    ShapeTracker.append(row[0])
                    ShapeTracker.append(row[1])
                    ShapeTracker.append(row[2])
                    ShapeTracker.append(LocationOfEyeMovementIndex)
                    Shape.append(ShapeTracker)
                    LocationOfEyeMovementIndex = LocationOfEyeMovementIndex - 1
                    print("Net1")
                    #Set RowNumber 
                    print(Shape)
                    print(LocationOfEyeMovementIndex)
            elif HelperFunctionCheckRowIndexShapeIndexMatrixIndexSpaceInShape(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndex,NewShapeSearch) == True:
                    print("Net2")
                    LocationOfEyeMovementIndex = LocationOfEyeMovementIndex - 1
                    print(Shape)
                    print("Row Number")
                    print(RowNumber)
                    #for row in Matrix:
                     #   if row[1] == ShapeIndex:
                            #RowNumber = row[2] 
                    RowNumber = RowNumber - 1
                    NewShapeSearch = True
                    print("recursion net 2")
                    return ScannForShapesInMatrixesRowIndex(Matrix,Shape,LocationOfEyeMovementIndex,ShapeIndex,NewShapeSearch,RowNumber,2,MatrixMaxIndex)
            elif HelperFunctionCheckRowIndexShapeIndexMatrixIndexSpaceInShapeNotTrue(LocationOfEyeMovementIndex,row,RowNumber,MatrixMaxIndex,ShapeIndex,NewShapeSearch)== True:
                    ShapeTracker = []
                    print("Shape Index")
                    print(ShapeIndex)
                    ShapeGrower = ShapeGrower + 1
                    #ShapeTracker.append(ShapeGrower,row[0],row[1],row[2],LocationOfEyeMovementIndex)
                    ShapeTracker.append(ShapeGrower)
                    ShapeTracker.append(row[0])
                    ShapeTracker.append(row[1])
                    ShapeTracker.append(row[2])
                    ShapeTracker.append(LocationOfEyeMovementIndex)
                    Shape.append(ShapeTracker)
                    print("Net3")
                    ShapeIndex = ShapeIndex + 1
                    print(Shape)
                    print("Before Recursion LocationOfEyeMovementIndex")
                 
            elif HelperFunctionSpaceInNextRow(row,RowNumber,MatrixMaxIndex,ShapeIndex):
                    #Reset to net three if another row else go back to the start of the matrix Eyepoint and generate a new shape from eyepoint 
                    #index, repeat this process until You reach the end of var 41. Recursion
                    #Reset Top Of Stack
                    print("Net4Recursion")
                    if RowNumber - 1 == -1:
                        for row in Matrix:
                            if row[1] == LocationOfEyeMovementIndex:
                                RowNumber = row[2]
                                NewShapeSearch = False
                        return ScannForShapesInMatrixesRowIndex(Matrix,Shape,LocationOfEyeMovementIndex,ShapeIndex,NewShapeSearch,RowNumber,2,MatrixMaxIndex)
                    else:
                        #Move down the Matrix 
                        RowNumber = RowNumber - 1
                        NewShapeSearch = True 
                        return ScannForShapesInMatrixesRowIndex(Matrix,Shape,LocationOfEyeMovementIndex,ShapeIndex,NewShapeSearch,RowNumber,2,MatrixMaxIndex)
            #else:
                #break    
    print("test")
    return Shape
print(len(ResultsIndexMaster))
ResultsIndexMaster2 = ResultsIndexMaster
Shapes = ScannForShapesInMatrixesRowIndex(ResultsIndexMaster2,[],-1,0,False,1,1,1)
ShapesCharacters = [] 
for item in Shapes:
    ShapesCharacters.append(item[1])
import pprint
ShapesCharactersReverse = ShapesCharacters.reverse()
print(ShapesCharacters)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(ShapesCharacters)