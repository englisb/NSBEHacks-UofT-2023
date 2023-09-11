import speech_recognition as sr

def spchToTxtmp4(file_path):

    # initialize the recognizer
    r = sr.Recognizer()

    # use the AudioFile class to open the file
    with sr.AudioFile(file_path) as source:
    # read the audio data from the file
        print('converting...')
        audio_data = r.record(source)
        print('done')

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)

    # print the transcribed text
    return text



def spchToTxtmp3(file_path):
     # initialize the recognizer
    r = sr.Recognizer()

    # use the AudioFile class to open the file
    with sr.AudioFile(file_path) as source:
        print('converting...')
    # read the audio data from the file
        audio_data = r.record(source)
        print('done')

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)

    return text

def spchTotxt(file_path):
    if "mp3" in file_path:
        return spchToTxtmp3(file_path)
    elif "mp4" in file_path:
        return spchToTxtmp4(file_path)