import speech_recognition as sr
print(sr.__version__)
r=sr.Recognizer()
#
# harvard= sr.AudioFile('harvard.wav')
# with harvard as source:
#     # r.energy_threshold()
#     r.adjust_for_ambient_noise(source, duration=1)
#     audio = r.record(source)
# # type(audio)
# print(r.recognize_google(audio, show_all=True))
sr.Microphone.list_microphone_names()

r.energy_threshold = 1000 #minimum energy threshold of sound for it to be considered as recording. Sond below this energy is considered as noise
r.pause_threshold = 0.8 #maximum pause time when energy below the energy_threshold is considered as pause between phases. Pause time >= pause_timeout results in breaking off of phrase and recording to end
with sr.Microphone() as source:
    audio = r.adjust_for_ambient_noise(source)
    print("Speak Now") #while recording, adience has to explicitly dictate pronunciations like point for full stop, comma etc.
    audio = r.listen(source,timeout=None) # timeout is the maximum wait time system waits before recording to start. To explicitly end recording post a time e.g. 10 s, phrase_time_limit=10 can be passed as 3rd parameter

try:
    print("System Predicts:"+r.recognize_google(audio))

    f = open("OriginalText.txt", "w+")
    f.write(r.recognize_google(audio))
    f.close()

except Exception:
    print("Something went wrong")