# Twitter + FFMPEG + Google Vision

This miniproject combines the above APIs to fetch images from a Twitter account and, by default, analyzes 10 images using the Google Vision API. 

Enjoy! 


## Usage

The parameters can be directly inputted from the command line: 

    python twitterAnalyzer.py username --num --retweets --replies
	    
    // username is the twitter account name such as @Hkane
    // --num is the number of tweets to retrieve
    // --retweets is True/False depending on whether or not to retireve retweets 
    // --replies is True/False depending on whether or not to retireve replies

In the repo, the results are produced using the command 

	python twitterAnalyzer.py @HKane

Which retrieves 10 twitter images from Harry Kane's account: 

 <img src="https://github.com/bdhkim/EC500/blob/master/twitterPics/DS9ChxLWkAAbcwB.jpg.jpg" width = "320" height = "180" align=center /> <img src="https://github.com/bdhkim/EC500/blob/master/twitterPics/DTcn7bRX4AIKPaC.jpg.jpg" width = "320" height = "180" align=center />


## FFMPEG

The line below converts 100 frames of an image into a mp4 video output 

```python
	os.system("ffmpeg -r 100 -i {0} -vcodec mpeg4 -f mpeg {0}.mp4".format(filename))
```

## Google Vision

As the credentials have been hidden, you must input your own credentials to use the Vision API. 

To do so, either export the .json file containing the credentials or authenticate through the gcloud: 

	export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE

OR,

	gcloud auth application-default login

