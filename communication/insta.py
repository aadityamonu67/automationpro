import InstagramAPI

# /////// CONFIG ///////
username = 'aadityamonu67@gmail.com'
password = 'Indiacan420'
debug = False

photo = 'C:\Users\HP-pc\Desktop\Untitled.png'  # path to the photo
caption = 'awsmeee pic testpi'  # caption
# //////////////////////

i = InstagramAPI.Instagram(username, password, debug)

try:
    i.login()
except Exception as e:
    e.message
    exit()

try:
    i.uploadPhoto(photo, caption)
except Exception as e:
    print e.message
