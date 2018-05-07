# Twitter + FFMPEG + Google Vision + Mongo DB

This project combines the above APIs to fetch images from a Twitter account and, by default, analyzes 10 images using the Google Vision API. Then, the the description of images and most common descriptions will be stored in Mongo DB. 

Enjoy! 


## Usage

The parameters can be directly inputted from the command line: 

    python twitterAnalyzer.py username --num --retweets --replies
	    
    // username is the twitter account name such as @Hkane
    // --num is the number of tweets to retrieve
    // --retweets is True/False depending on whether or not to retireve retweets 
    // --replies is True/False depending on whether or not to retireve replies

Here is an example command: 

	python twitterAnalyzer.py @HKane

Example snapshot of the DB: 

 <img src="https://github.com/bdhkim/EC500/blob/master/MongoDB_Project/DB_Image.png" width = "420" height = "780" align=center /> 
 