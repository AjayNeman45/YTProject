from googleapiclient.discovery import build
from pprint import pprint

# api key 
api_key="Here comes your api key"

youtube=build('youtube','v3',developerKey=api_key)

# searching of the video and its statistics done by this function
def search_vid(query,max_result):
	request=youtube.search().list(
		q=query,
		part='id,snippet',
		maxResults=max_result
	)
	response=request.execute()

	vid_ids=[]       # storing for video id
	channel_name=[]  # storing for channle name
	vid_desc=[]     # storing  for video description

    
	for item in response['items']:
		channel_name.append(item['snippet']['channelTitle'])
		vid_desc.append(item['snippet']['description'])
		vid_ids.append(item['id']['videoId'])
		

	# for adding video statistics we have following lists
	vid_like_cnt=[]
	vid_dislike_cnt=[]
	vid_view_cnt=[]
	vid_comment_cnt=[]

	for ids in vid_ids:
		id_request=youtube.videos().list(
			part='statistics',
			id=ids
		)
		id_response=id_request.execute()
		vid_like_cnt.append(id_response['items'][0]['statistics']['likeCount'])
		vid_dislike_cnt.append(id_response['items'][0]['statistics']['dislikeCount'])
		vid_view_cnt.append(id_response['items'][0]['statistics']['viewCount'])
		vid_comment_cnt.append(id_response['items'][0]['statistics']['commentCount'])
	
    
	# creating an empty dictionary for all the information of each video
	finaldict={}
	for num in range(1,max_result+1):
		finaldict[num]={}

	num=1
	for name in channel_name:
		finaldict[num]['cn']=name
		num+=1
		
	num=1
	for desc in vid_desc:
		finaldict[num]['vd']=desc
		num+=1
		
	num=1
	for viewCnt in vid_view_cnt:
		finaldict[num]['vvc']=viewCnt
		num+=1
		
	num=1
	for vidLike in vid_like_cnt:
		finaldict[num]['vlc']=vidLike
		num+=1
		
	num=1
	for vidDis in vid_dislike_cnt:
		finaldict[num]['vdc']=vidDis
		num+=1
		
	num=1
	for vidComm in vid_comment_cnt:
		finaldict[num]['vcc']=vidComm
		num+=1


	for list in finaldict:
		print("Channel Name : - ",finaldict[list]['cn'])
		print("Video Description : - ",finaldict[list]['vd'])
		print("Video View Count: - ",finaldict[list]['vvc'])
		print("Video Like Count : - ",finaldict[list]['vlc'])
		print("Video Comment Count : - ",finaldict[list]['vcc'])
		print("Video Dislike Count : - ",finaldict[list]['vdc'])
		link = "https://www.youtube.com/watch?v="+vid_ids[list-1]
		print("Link for the video : - ",link)
		print()
		print("#----------------***----------------#")
		print()

# driver code  
if __name__=="__main__":

	query=input("what do you want to watch today : - ")
	max_result=int(input("How many results do you want : - "))
	print()

	search_vid(query,max_result)


