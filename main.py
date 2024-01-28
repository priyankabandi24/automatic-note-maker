import smtplib
#import speech_recognition as sr
#import speech_recognition as sr
import pyttsx3 
#import speech_recognition as sr
#import pyttsx3
import smtplib
import googletrans
#import speech_recognition as sr
#import pyttsx3 
import googletrans
import speech_recognition as sr
import pyttsx3 
import nltk 
import bs4 as bs
import urllib.request
import re
import smtplib
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize, sent_tokenize
from googletrans import Translator 
from pprint import pprint
print("1. CHOOSE 1 FOR AUDIO FILE")
print(".")
print("2. CHOOSE 2 FOR LIVE SPEECH FOR ENGLISH")
print(".")
print("3. CHOOSE 3 FOR OTHER LANGUAGES(OTHER COUNTRY)")
print(".")
print("4. CHOOSE 4 TO TRANSLATE MESSAGE LANGUAGE")
print(".")
print("5.CHOOSE 5 TO SEARCH DATA AND GET SUMARIZED INFO")
MyText=""
n=int(input())
if(n==1):
	print("upload audio file(.wav)")
	#filename="hello.wav"
	filename=input()
	r=sr.Recognizer()
	print("converting...")
	print("you have uploaded an audio file")
	print(". . . .")
	with sr.AudioFile(filename) as source:
		audio_data=r.record(source)
		text=r.recognize_google(audio_data)
		print(text)
	#from email.mime.multipart import smtplib
	str1="hello!! WELCOME TO MAJOR PROJECT                                                                                                                                                                                                            You just spoke------------>"+text+"                                                                                                                                                                                                                                                        -----------Thank You--------------"
	sender_email="4majorproject@gmail.com"
	print("enter receivers mail")
	rec_email=str(input())
	#rec_email="4majorproject@gmail.com"
	#password=input(str("please enter your password..."))
	#print(password)
	password="Major@432"
	#message="Hello welcome to test this project"
	server=smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(sender_email,password)
	print("login success")
	server.sendmail(sender_email,rec_email,str1)
	print("email has been sent to...")
	print(rec_email)
	server.quit()
elif(n==2):
	r = sr.Recognizer()

	# Function to convert text to
	# speech

	def SpeakText(command):

	# Initialize the engine
		engine = pyttsx3.init()
		engine.say(command) 
		engine.runAndWait()


	# Loop infinitely for user to
	# speak

	# Exception handling to handle
	# exceptions at the runtime
	try:

		# use the microphone as source for input.
		with sr.Microphone() as source2:

		# wait for a second to let the recognizer
		# adjust the energy threshold based on
	# the surrounding noise level
		print("enter the duration to speak")
		n=int(input())
		print("say something")
		r.adjust_for_ambient_noise(source2, duration=n)

		#listens for the user's input 
		audio2 = r.listen(source2)
		print("Recognizing....")  
	# Using ggogle to recognize audio
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()
		print("You just said....")
		print(MyText)
	#SpeakText(MyText)

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

	except sr.UnknownValueError:
		print("unknown error occured")
	#from email.mime.multipart import smtplib
	str1="hello!! WELCOME TO MAJOR PROJECT                                                                                                                                                                                                            You just spoke------------>"+MyText+"                                                                                                                                                                                                                                                        -----------Thank You--------------"
	sender_email="4majorproject@gmail.com"
	print("enter receivers mail")
	rec_email=str(input())
	#rec_email="4majorproject@gmail.com"
	#password=input(str("please enter your password..."))
	#print(password)
	password="Major@432"
	message="Hello welcome to test this project"
	server=smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(sender_email,password)
	print("login success")
	server.sendmail(sender_email,rec_email,str1)
	print("email has been sent to...")
	print(rec_email)
	server.quit()
elif(n==3):
    r = sr.Recognizer() 
print("...listing all supported languages...")
pprint(googletrans.LANGUAGES) 
#print(googletrans.LANGUAGES)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")  
    message=""  
# Function to convert text to
# speech
    def SpeakText(command):

    # Initialize the engine
        engine = pyttsx3.init()
engine.say(command) 
engine.runAndWait()


# Loop infinitely for user to
# speak


    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
print("enter the duration to speak")
            n=int(input())
print("please enter your language code from above")
            co=input()
print("say something")
r.adjust_for_ambient_noise(source2, duration=n)

            #listens for the user's input 
            audio2 = r.listen(source2)
            print("................Recognizing..............")  
            #print("enter laguage code from above")
            # Using ggogle to recognize audio
MyText = r.recognize_google(audio2,language=co)
MyText = MyText.lower()
print("You just said....")
print(MyText)
            message=MyText
            #SpeakText(MyText)

    except sr.RequestError as e:
print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
print("unknown error occured")
#from email.mime.multipart import smtplib
    str1="hello!! WELCOME TO MAJOR PROJECT                                                                                                                                                                                                            You just spoke------------>"+message+"                                                                                                                                                                                                            -----------Thank You--------------"
    message=str1
#str1="----------thankyou!!!-------------"
sender_email="4majorproject@gmail.com"
print("enter receivers mail")
rec_email=str(input())
#rec_email="4majorproject@gmail.com"
#password=input(str("please enter your password..."))
#print(password)
    message=str1.encode('utf-8')
    password="Major@432"
    server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email,rec_email,message)
print("email has been sent to...")
    print(rec_email)
server.quit()
elif(n==4):
    r = sr.Recognizer() 
print("...listing all supported languages...")
pprint(googletrans.LANGUAGES) 
#print(googletrans.LANGUAGES)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("please enter your language code from above")  
    y=input()
# Function to convert text to
# speech
    def SpeakText(command):

    # Initialize the engine
        engine = pyttsx3.init()
engine.say(command) 
engine.runAndWait()


# Loop infinitely for user to
# speak


    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
print("enter the duration to speak")
            n=int(input())
print("//..................say something.....................")
r.adjust_for_ambient_noise(source2, duration=n)

            #listens for the user's input 
            audio2 = r.listen(source2)
print("..........Recognizing your speech........")  
            # Using ggogle to recognize audio
MyText = r.recognize_google(audio2,language=y)
MyText = MyText.lower()
print("You just said....")
print(MyText)
            #SpeakText(MyText)

    except sr.RequestError as e:
print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
print("unknown error occured")

print("~~~~~~~~//~~~~~~~~~//~~~~~~~~~~~~~//~~~~~~~~~~~~~~//~~~~~~~~~~~~//~~~~~~~~~~~//~~~~~~")
print("can you please provide your destination code")
    x=input()
    translator=Translator()
#result=translator.translate("hello",src=y,dest=x)
    result=translator.translate(MyText,src=y,dest=x)
print(".....................................................................")
print("from language")
    print(result.src)
print("converted to language---------->")
    print(result.dest)
print(".")
print("converted message is----->")
    print(result.text)
    #from email.mime.multipart import smtplib
    str1="hello!! WELCOME TO MAJOR PROJECT                                                                                                                                                                                                            You just spoke------------>"+MyText+"~~~~~~~~~~~COnverted to-->"+result.text+"                                                                                                              -----------Thank You--------------"
sender_email="4majorproject@gmail.com"
print("enter receivers mail")
    #str1.decode('ascii','ignore')
    str2=str1.encode('utf-8')
rec_email=str(input())
#rec_email="4majorproject@gmail.com"
#password=input(str("please enter your password..."))
#print(password)
    password="Major@432"
    server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email,rec_email,str2)
print("email has been sent to...")
    print(rec_email)
server.quit()
else:
    #nltk.download('punkt')
    r = sr.Recognizer() 

# Function to convert text to
# speech
    def SpeakText(command):

    # Initialize the engine
        engine = pyttsx3.init()
engine.say(command) 
engine.runAndWait()


# Loop infinitely for user to
# speak

mytext=""      
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
print("enter the duration to speak")
            n=int(input())
print("say something")
r.adjust_for_ambient_noise(source2, duration=n)

            #listens for the user's input 
            audio2 = r.listen(source2)
print("Recognizing....")  
            # Using ggogle to recognize audio
MyText = r.recognize_google(audio2)
MyText = MyText.lower()
print("You just said....")
print(MyText)
            #SpeakText(MyText)
mytext=MyText.replace(" ","_")
            #print(mytext)
            #mytext=MyText  
    except sr.RequestError as e:
print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
print("unknown error occured")
    str2=mytext
#print(mytext)
scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/'+str2+' ')
    article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
article_text = ""
    for p in paragraphs:
article_text += p.text
#print(article_text)
#print("___________________________________________________________________________________________________________________")
#text = "Next"

# Tokenizing the text 

stopWords = set(stopwords.words("english")) 

    words = word_tokenize(article_text) 


# Creating a frequency table to keep the  
# score of each word 



freqTable = dict() 

    for word in words: 

        word = word.lower() 

        if word in stopWords: 

            continue

        if word in freqTable: 

freqTable[word] += 1

        else: 

freqTable[word] = 1


# Creating a dictionary to keep the score 
# of each sentence 

    sentences = sent_tokenize(article_text) 

sentenceValue = dict() 



    for sentence in sentences: 

        for word, freq in freqTable.items(): 

            if word in sentence.lower(): 

                if sentence in sentenceValue: 

sentenceValue[sentence] += freq

                else: 

sentenceValue[sentence] = freq







sumValues = 0

    for sentence in sentenceValue: 

sumValues += sentenceValue[sentence] 


# Average value of a sentence from the original text 



    average = int(sumValues / len(sentenceValue)) 


# Storing sentences into our summary. 

    summary = '' 

    for sentence in sentences: 

        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 

            summary += " " + sentence 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("SUMMARIZED FILE")
    print(summary)
print("........>>>>>>>>>>............")
    print(len(article_text))
    print(len(summary))
    srt1=summary
#from email.mime.multipart import smtplib
    str1="hello!! WELCOME TO MAJOR PROJECT                                                                                                                                                                                                            You just spoke------------>"+summary+"                                                                                                                                                                                                                                                        -----------Thank You--------------"
    message=str1.encode('utf-8')
#str1="----------thankyou!!!-------------"
sender_email="4majorproject@gmail.com"
print("enter receivers mail")
rec_email=str(input())
    password="Major@432"
    server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email,rec_email,message)
print("email has been sent to...")
    print(rec_email)
server.quit()




