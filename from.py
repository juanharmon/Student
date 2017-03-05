from gtts import gTTS
import wikipedia as wiki

query = input("audiobook wut\n")
result = wiki.page(title=query)
print("Got " + result.title +", now encoding into .mp3")
tts = gTTS(text=result.summary,lang='zh-yue')
tts.save(result.title + '.mp3')