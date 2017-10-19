import wolframalpha
import pyttsx
engine = pyttsx.init()
input = raw_input("question: ")
app_id = "K4R4QW-KVP6PPY874"
client =wolframalpha.Client(app_id)

res= client.query(input)

answer= next(res.results).text

print answer
engine.say(answer)
engine.runAndWait()
