# /* --------------------------------------- */
#  * EC500 Mini Project 1 - Dong Hyun Kim    *
#  * Twitter + FFMPEG + Google Vision        *
#  * Enjoy!                                  *
# /* --------------------------------------- */                        


import tweepy # https://github.com/tweepy/tweepy
import os     # for creating outputfolder
from tweepy import OAuthHandler
import json   # for parsing json objects 
import wget   # for locally downloading images
import configparser # for parsing secrets
import ffmpy  #libary for FFMPEG
import io     #io stream for reading file

from google.cloud import vision
from google.cloud.vision import types

def vision_analysis(path):
  vision_client = vision.ImageAnnotatorClient()

  for filename in os.listdir(path):
    if (filename.endswith(".jpg")): 
      with io.open(filename,'rb') as image_file:
        content = image_file.read()

      image = types.Image(content=content)
      response = vision_client.label_detection(image=image)
      labels = response.label_annotations

      print("\nDescripion of " + filename + ": ")
      for label in labels:
        print(label.description)
    else:
      continue

def parse_config(config_file):
  config = configparser.ConfigParser()
  config.read(config_file)  
  return config 
  
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def init_tweepy():
  # Status() is the data model for a tweet
  tweepy.models.Status.first_parse = tweepy.models.Status.parse
  tweepy.models.Status.parse = parse
  # User() is the data model for a user profil
  tweepy.models.User.first_psarse = tweepy.models.User.parse
  tweepy.models.User.parse = parse

def authorise_twitter_api(config):
  auth = OAuthHandler(config['AUTH']['consumer_key'], config['AUTH']['consumer_secret'])
  auth.set_access_token(config['AUTH']['access_token'], config['AUTH']['access_secret'])
  return auth

def download_images(api, username, retweets, replies, num_tweets, output_folder):
  tweets = api.user_timeline(screen_name=username, count=200, include_rts=retweets, exclude_replies=replies)
  if not os.path.exists(output_folder):   #create output folder 
      os.makedirs(output_folder)

  # Exit if no there are no tweets at all 
  if (len(tweets) == 0):
    print("Looks like you just started twitter! No tweet image is available ")

  # Continue if there are tweets 
  else: 
    downloaded = 0
    while (len(tweets) != 0):    
      last_id = tweets[-1].id
      
      for status in tweets:
        media = status.entities.get('media', []) # only retrieve tweets with images

        # if (not status.entities['media']):
        #   print("Can't find any pictures in your twitter. Come on go upload some! ")
        #   break

        if(len(media) > 0 and downloaded < num_tweets):
          wget.download(media[0]['media_url'], out=output_folder)   # only retrieve the first image if there are many 
          downloaded += 1
          print(" Downloading picture " + str(downloaded))        

      tweets = api.user_timeline(screen_name=username, count=200, include_rts=retweets, exclude_replies=replies, max_id=last_id-1)

def ffmpeg_convert(path):

  path = os.curdir
  for filename in os.listdir(path):
    if (filename.endswith(".jpg")): 
        os.system("ffmpeg -r 100 -i {0} -vcodec mpeg4 -f mpeg {0}.mp4".format(filename)) #convert 100 frames of image into a video with extension .mp4
    else:
        continue

def main(): 
  # configuration variables for twitter timeline   
  username = '@HKane'
  retweets = False    # exclue retweets
  replies = False     # exclue replies 
  num_tweets = 10     # limit the number of pictures to 10 
  output_folder = os.curdir
  config = parse_config('../secrets.cfg')
  auth = authorise_twitter_api(config)   
  api = tweepy.API(auth)

  # for downloading iamges 
  download_images(api, username, retweets, replies, num_tweets, output_folder)

  # for FFMPEG Conversion
  ffmpeg_convert(output_folder)

  # running vision alaysis 
  vision_analysis(output_folder)


if __name__=='__main__':
    main()
