from wit import Wit

access_token = "AIY2RONY77F5BA2SLKVIJYTYZ6J6XIPV"
client = Wit(access_token = access_token)

message_text = "switch on light"

resp = client.message(message_text)
print resp

entity=None
value = None
entity = list(resp['entities'])[0]
value = resp['entities'][entity][0]['value']

print entity
print value
if value=="sports":
    print "ok sir your sports news will ready"
#print resp['entities']['location'][0]['value']
