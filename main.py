#------------------------------------------------------------HEADERFILES------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request
import datetime
import random
from db import *
#from cronss import *
from ai import *
from notify import *

#------------------------------------------------------------END OF HEADER FILES-----------------------------------------


app = Flask(__name__)

#--------------------------------main index page-------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
@app.route("/")
def Index():
	
    	return render_template('index.html')



#--------------------------------registration of user--------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#registration of user
#registration of user
@app.route("/disp_frmreg",methods = ['POST', 'GET'])
def disp_frmreg():
     	return render_template('frmreg.html')
 
    

@app.route("/frmreg",methods = ['POST', 'GET'])
def frmreg():
    if request.method == 'POST':
       frmnm=request.form["txtnm"]
       frmeml = request.form["txteml"]
       frmpwd = random.randint(1,99999999)
       datenow = datetime.datetime.now()
       save_rec_tbuser(frmnm,frmeml,frmpwd,datenow)
          #mail sent to the user check mail
       msg="hi you are registered your password is "+str(frmpwd)
       eml="Hackerbomzzzhack@gmail.com"
       pwd="Indiacan420"
       teml=frmeml
       gmail(msg,eml,pwd,teml)
       return render_template('success_pages/frmsuccess.html')




#--------------------------------registration of Input Device------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#registration of Input Device
@app.route("/disp_frmregipdvc")
def disp_frmregipdvc():
 rows = disp_rec_tbIO_input()
 return render_template('frmdispipdvc.html',rows = rows)



#register of input devices like sensors,etc
@app.route("/frmregipdvc")
def frmregipdvc():
    try:
     ipaddr = request.args["ipaddr"]
     dvcnm = request.args["dvcnm"]
     dvcnm=ipaddr.split(".")
     dvcnm=reuqets.args["dvcnm"]+dvcnm[3]
     save_rec_tbIO(uid,dvcnm,ipaddr,pinconfig)
#use unique coloumns in ip addr attribute
    except:
     return "soorry this sensor already registered"

     #after registeration send saving link of sensor data example http:localhost:5000/savesensordata?snsr_id=12&snsr_data=23.3

@app.route("/frmsavesensordata")
def frmsavesensordata():
    try:
     ipaddr = request.args["ipaddr"]
     snsrdata=request.args["snsr_data"]
     save_sensr_data()#create method and call it
     
     
    except:
     return "error message :something went wrong"	 
	 

#--------------------------------registration of Output Device------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#display of Output Device
@app.route("/disp_frmregopdvc")
def disp_frmdispopdvc():
 rows = disp_rec_tbIO()
 return render_template('frmdispopdvc.html',rows = rows)


#register of output devices like bulb,fan,ac,etc
@app.route("/frmregopdvc")
def frmregopdvc():
    try:
     uid='3'#session
     ipaddr = request.args["ipaddr"]#unique coloumn in ip address
     dvcnm = request.args["dvcnm"]
     pinconfig=request.args["pinconfig"]#relay size of wifi socket
     save_rec_tbIO(uid,dvcnm,ipaddr,pinconfig)
    except:
     return "This device is already registered"
      
         
        

#--------------------------------login of user---------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#login of user


@app.route("/disp_frmlgn",methods = ['POST', 'GET'])
def disp_frmlgn():
    return render_template('frmlgn.html')



@app.route("/frmlgn",methods = ['POST', 'GET'])
def frmlgn():
 try:
    if request.method == 'POST':
      	      frmeml = request.form["txteml"]
	      frmpwd = request.form["txtpwd"]
	      sesscod =login(str(frmeml),str(frmpwd))
            
             
       	      if sesscod=="0":
                 save_rec_tblog(Uid,LogName,LogDesc,LogTime)
		 return render_template('error.html')
                 
              else:
                 return render_template('index.html')
                 save_rec_tblog(Uid,LogName,LogDesc,LogTime)
                 #check for notification system availabilty n notify them accordingly
                  #session code storage,log file generation,email send
                 
     
   
 except:
        return render_template('error_pages/error.html')





#--------------------------------lost password of user-------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#lost password of user


@app.route("/disp_frmlstpass",methods = ['POST', 'GET'])
def disp_frmlstpass():
    return render_template('frmlstpass.html')


@app.route("/frmlstpass",methods = ['POST', 'GET'])
def frmlstpass():
 try:
    if request.method == 'POST':
      	      frmeml = request.form["txteml"]
	      usrpass=lstpass_tbuser(frmeml)
              msg="hi your registered your password is "+str(usrpass)
              eml="Hackerbomzzzhack@gmail.com"
              pwd="Indiacan420"
              teml=frmeml
              gmail(msg,eml,pwd,teml)
              return render_template('success_pages/frmsuccesslstpass.html')
             
     
   
 except:
        return render_template('error.html')




#--------------------------------Automation of user--------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@app.route("/disp_automation_dly",methods = ['POST', 'GET'])
def disp_automate_dvc_dly():
     rows = disp_rec_tbIO()
     return render_template('automate_dvc_dly.html',rows = rows)


@app.route("/disp_automation_cstmizd",methods = ['POST', 'GET'])
def disp_automate_dvc_cstmizd():
     rows = disp_rec_tbIO()
     return render_template('automate_dvc_cstmizd.html',rows = rows)


@app.route("/automation_cstmizd")
def automate_dvc_cstmizd():
     datetime = request.args["datetime"]
     dvcnm = request.args["dvcnm"]
     automatnnm=request.form["txtq"]
     return "you have successfully automated your"+dvcnm+" for "+datetime







#--------------------------------Artificial Intelligence of user---------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@app.route("/disp_test")
def disp_test():
     
     return render_template('test.html')

@app.route("/test",methods = ['POST', 'GET'])
def test():
 if request.method == 'POST':
  ques=request.form["txtq"]
  res=""
 try:
  try:
   res = pywolf(ques)
   return "wolf searched"
  except:
    try:
     res = pywit(ques)
     return "wit searched"
     
    except:
     res = pywiki(ques)
     return "wiki searched"

 except: 
    return "search engine" 
 
#--------------------------------TITLE--------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#TITLE


if __name__ == "__main__":
    app.debug = True
    app.run()
#from tornado.wsgi import WSGIContainer
    #from tornado.httpserver import HTTPServer
    #from tornado.ioloop import IOLoop

    #http_server = HTTPServer(WSGIContainer(app))
    #http_server.listen(80)
    #IOLoop.instance().start()
