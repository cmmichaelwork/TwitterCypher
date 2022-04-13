#%run DecryptDeviceXHelperFunctions.ipynb
%run GatheringTweetsFunctions.ipynb
%run HelperLocationFunctions.ipynb
#import * from DecryptDeviceXHelperFunctions
#import GatheringTweetsFunctions
TweetListOfUserX = GetTweetsFromUserX('parag',1000)

ResultsIndexMaster = GetParticularTweetFromUser(TweetListOfUserX,37)
#print(ResultsIndexMaster)
ResultsIndexMaster2 = ResultsIndexMaster
print(ResultsIndexMaster2)

#Take in a tweet, Find Max take the first word, keep an index then go to next row, I take a 
#TopLeft Off Place subtracked from 
#Index Of Starting Point word, add that to the min need min of each row.
#Index Of Starting Point word + to min of row that word and any location.
#Index add index next index, which is built on the previous index add up the indexes. to the min. 
#Repeat that process until you get to last row then start recursion 
# adding the previous indexs to the mins once you get to zero row.
#Then you do recursion 1+ space or multiple spaces. Recursion first character to first character. 
#Recursion row zero and you go to index starting point index + min + 1 for space as starting point of next index repeat until reach top row.
#If you get to top and nothing to build upon. # Opposite work with max and subtract. 
#To Reset index with row? 
%run HelperLocationFunctions.ipynb
def TwitterCypherDiagnoleBottomDiagnole(TweetIndexed,StartingPointIndex,FirstRun,RowIndex):
    #Find Max Of TweetIndexed
    if FirstRun == 1:
        StartingPointIndex = TweetIndexed[-1][1]
        RowIndex = TweetIndexed[-1][2]
    StartingPointIndexStop = StartingPointIndex
    #MatrixMinIndexCheck = MatrixMinIndexCheck(StartingPointIndex,Row)
    #print(TweetIndexed[-1][2])
    #print(RowIndex)
    #Row = int(TweetIndexed[-1][2])
    #print(TweetIndexed)
    #print('startingpointindex')
    #print(StartingPointIndex)
    #print(RowIndex)
    #print(TweetIndexed)
    MaxMatrixIndex = MatrixMaxIndexCheck(TweetIndexed,RowIndex)
    MinMatrixIndex = MatrixMinIndexCheck(TweetIndexed,RowIndex)
    #MaxMatrixIndexBreak = MaxMatrixIndex
    Shape = []
    print(StartingPointIndex)
    
    #BreakStartingPointIndex = StartingPointIndexStop + MinMatrixIndex
    #print(BreakStartingPointIndex)
    #print(FirstRun)
    print(MinMatrixIndex)
    print(StartingPointIndexStop)
    while StartingPointIndex > MinMatrixIndex :
        print('start') 
        #print(TweetIndexed[StartingPointIndex][0].strip())
        if FirstRun == 1 and TweetIndexed[StartingPointIndex][0].strip() == "":
            while TweetIndexed[StartingPointIndex][0].strip() == "":
                StartingPointIndex = StartingPointIndex -1
            
        while TweetIndexed[StartingPointIndex][0].strip() != "":
            ListShape = []
            ListShape.append(TweetIndexed[StartingPointIndex][0])
            ListShape.append(TweetIndexed[StartingPointIndex][1])
            Shape.append(ListShape)
            print(TweetIndexed[StartingPointIndex][0])
            StartingPointIndex = StartingPointIndex -1
            print(StartingPointIndex)
        #Find the min of the next row
        WIPPointIndexTopRow = MaxMatrixIndex - StartingPointIndex
        #WIPPointIndex = StartingPointIndex
        #MinRowIndex = MatrixMinIndexCheck(TweetIndexed,RowIndex)
        MaxNextRowIndex = MatrixMaxIndexCheck(TweetIndexed,RowIndex)
        NextRowIndexStart = MaxMatrixIndex - WIPPointIndexTopRow
        NextRowIndexIteration = NextRowIndexStart
        print(1)
        while RowIndex != -1: 
        #try
        #Cutoff = NextRowIndexStart - 1
            #if TweetIndexed[][0]
            IndexRemoved = MaxNextRowIndex - NextRowIndexIteration
            if RowIndex == 0:
                MaxNextRowIndex = MatrixMaxIndexCheck(TweetIndexed,RowIndex)
                RowIndex = RowIndex - 1 
                print(3)
                NextRowIndexStart = MaxNextRowIndex - WIPPointIndexTopRow + IndexRemoved
                print(NextRowIndexIteration)
                print('NextRowIndexIteration')
                while TweetIndexed[NextRowIndexIteration][0].strip() != "":
                    ListShape = []
                    ListShape.append(TweetIndexed[NextRowIndexIteration][0])
                    ListShape.append(TweetIndexed[NextRowIndexIteration][1])
                    Shape.append(ListShape)
                    print(ListShape)
                    NextRowIndexIteration = NextRowIndexIteration - 1
                    print(NextRowIndexIteration)
                    print('NextRowIndexIteration')
                IndexRemoved = MaxNextRowIndex - NextRowIndexIteration
                print(2)
            else: 
                print('row1other')
                MaxNextRowIndex = MatrixMaxIndexCheck(TweetIndexed,RowIndex - 1)
                RowIndex = RowIndex - 1
                NextRowIndexIteration = MaxNextRowIndex - WIPPointIndexTopRow + IndexRemoved
                #print('nextrow')
                print(MaxNextRowIndex)
                print('MaxNextRowIndex')
                print(RowIndex)
                print('RowIndex')
                print(NextRowIndexStart)
                print('NextRowIndexStart')
                print(NextRowIndexIteration)
                print('NextRowIndexIteration')
                while TweetIndexed[NextRowIndexIteration][0].strip() != "":
                    ListShape = []
                    ListShape.append(TweetIndexed[NextRowIndexIteration][0])
                    ListShape.append(TweetIndexed[NextRowIndexIteration][1])
                    print(ListShape)
                    Shape.append(ListShape)
                    print(NextRowIndexIteration)
                    print('NextRowIndexIteration')
                    NextRowIndexIteration = NextRowIndexIteration - 1
                IndexRemoved = MaxNextRowIndex - NextRowIndexIteration
            NextRowIndexIteration = MaxNextRowIndex - WIPPointIndexTopRow + IndexRemoved 
        
        print(4)
        RowIndex = TweetIndexed[-1][2]
        print('Recursion')
        print(StartingPointIndex)
        StartingPointIndex = StartingPointIndex -1
        TwitterCypherDiagnoleBottomDiagnole(TweetIndexed,StartingPointIndex,2,RowIndex)
    return Shape 

%run HelperLocationFunctions.ipynb
ResultsShape = TwitterCypherDiagnoleBottomDiagnole(ResultsIndexMaster2,[],1,'')

ShapesCharacters = [] 
for item in ResultsShape:
    print(item)
    ShapesCharacters.append(item[0])
import pprint
#ShapesCharactersReverse = ShapesCharacters.reverse()
print(ShapesCharacters)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(ShapesCharacters)


#ShapesCharacters = ShapesCharacters[:-1]
import pprint
#ShapesCharactersReverse = ShapesCharacters.reverse()
print(ShapesCharacters)
pp = pprint.PrettyPrinter(width=450, compact=True)
pp.pprint(ShapesCharacters)