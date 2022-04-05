#!pip3 install snscrape
# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas
# Creating list to append tweet data 
tweets_list1 = []
def GetTweetsFromUserX(User,AmountOfTweets):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    TweetHandle = str(User).strip()
    SearchUser = 'from:' + TweetHandle
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(SearchUser).get_items()): #declare a username 
        if i>AmountOfTweets: #number of tweets you want to scrape
            break
        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
    return tweets_list1
# Creating a dataframe from the tweets list above 
#tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
def GetAllCharactersFromTweet(Tweet):
    EveryCharacter = []
    for item in Tweet:
        EveryCharacter.append(item)
    return EveryCharacter

def MatrixGeneratorIphone8ScrollVersion(TweetPerson):
    TweetOfPersonCharacters =  GetAllCharactersFromTweet(TweetPerson)
    TweetMatrix = []
    TweetRowX = []
    #while len(TweetOfPersonCharacters) != 0:
    #while len(TweetRowX) != 30:
    TweetRowXIndex = 0
    for item in TweetOfPersonCharacters:
        #Tweet Row Will Change based on the devices being used by the user or the way they view the tweet.
            if len(TweetRowX) != 40 and CheckIfCharacterLimitExceededInLoop(item,TweetOfPersonCharacters,TweetRowXIndex) == False :
                TweetRowX.append(item)
                print(item)
                TweetRowXIndex = TweetRowXIndex + 1
            else:
                TweetRowX.append(item)
                print(item)
                TweetMatrix.append(TweetRowX)
                TweetRowX = [] 
                TweetRowXIndex = 0
    return TweetMatrix
def CheckIfCharacterLimitExceededInLoop(Character, TweetRow, TweetRowIndex):
    CharacterOverSplillLimit = 0 
    for character in TweetRow[TweetRowIndex:]:
        if character.strip() != '' and TweetRowIndex != 30:
            CharacterOverSplillLimit = CharacterOverSplillLimit + 1 
        else:
            FinalCharacterCountForLimit = CharacterOverSplillLimit + TweetRowIndex
            if FinalCharacterCountForLimit > 40:
                return True
            else:
                return False
            

def GetParticularTweetFromUser(UsersTweets,TweetIndex):
    TweetsOfUserX = []
    for item in tweets_list1:
        TweetsOfUserX.append(item[2])
    #All Tweets Gathered of the particular person. Now Test out the cypher on a tweet.
    TweetTest = TweetsOfUserX[20]
    Results = MatrixGeneratorIphone8ScrollVersion(TweetTest)
    Results2 = Results
    #print(Results2)
    MatrixStarting = Results2[0]
    for letter in MatrixStarting:
            print(letter)
    ResultsIndex = 0
    ResultsIndexMaster = []
    ResultsRow = 0
    for matrix in Results:
        for rows in matrix:
            IndexResultList = []
            print(rows)
            IndexResultList.append(rows)
            IndexResultList.append(ResultsIndex)
            IndexResultList.append(ResultsRow)
            #print(ResultsIndex)
            ResultsIndexMaster.append(IndexResultList)
            ResultsIndex = ResultsIndex + 1
        ResultsRow = ResultsRow + 1
    return ResultsIndexMaster
    #print(TweetsOfUserX[20])

