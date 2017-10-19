#!/usr/bin/python
from flask import Flask, render_template, request
import sqlite3
#Name of Database
db_name='kk.db'


def lstpass_tbuser(Email):
 try:
   conn = sqlite3.connect(db_name)
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute('select Id,Email,Password from tbuser where Email= ?',[Email])
   rows = cur.fetchone();
   return rows["Password"]
 except:
	 
         return "-1"


#login
def login(Email,Password):
       try:     
   	 conn = sqlite3.connect(db_name)
	 conn.row_factory = sqlite3.Row
         cur = conn.cursor()
	 cur.execute('select Id,Email,Password from tbuser where Email= ?',[Email])
         rows = cur.fetchone();
         rows["Email"]
	 rows["Password"]
         print rows["Password"]
	 if rows["Password"]==Password:
            print "login"
	    return rows["Id"]
	 else:
           print "wrong pass"
	   return "0"
    
       except sqlite3.Error:
	 print "wrong user"
       


#crud code of registeration

#insert
def save_rec_tbuser(Name,Email,Password,DOR):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tbuser(Name,Email,Password,DOR) VALUES (?,?,?,?)",(str(Name),str(Email),str(Password),str(DOR)));
   conn.commit()
   conn.close()
 except:
    return render_template('error_pages/error.html')
 
#display
def disp_rec_tbuser():
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("select * from tbuser");
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#delete
def del_rec_tbuser(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tbuser where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#find

def find_rec_tbuser(Id):
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("SELECT * from tbuser where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]






#update
def upd_rec_tbuser(Id,Name,Email,Password,DOR):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("UPDATE tbuser set NAME="+Name+","+"Email="+Email+","+"Password="+Password+","+"DOR="+DOR+" Where Id="+Id)
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]





#end of crud code of registeration

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#crud code of log table

#insert
def save_rec_tblog(Uid,LogName,LogDesc,LogTime):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tblog (Uid,LogName,LogDesc,LogTime) \
    VALUES (?,?,?,?)",(int(Uid),str(LogName),str(LogDesc),str(LogTime)));
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#display
def disp_rec_tblog():
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("select * from tblog");
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#delete
def del_rec_tblog(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tblog where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#find
def find_rec_tblog(Id):
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("SELECT * from tblog where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]



#update
def upd_rec_tblog(Id,Uid,LogName,LogDesc,LogTime):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("UPDATE tblog set Uid="+Uid+","+"LogName="+LogName+","+"LogDesc="+LogDesc+","+"LogTime="+LogTime+"where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]




#end of crud code of log table

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#crud code of I/O TABLE
#insert
def save_rec_tbIO(Uid,DvcName,IpAddr,PinConfig):
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tbIO (Uid,DvcName,IpAddr,PinConfig) VALUES (?,?,?,?)",(int(Uid),str(DvcName),str(IpAddr),int(PinConfig)));
   conn.commit()
   conn.close()
       
#display
def disp_rec_tbIO():
 con = sqlite3.connect(db_name)
 con.row_factory = sqlite3.Row
 cur = con.cursor()
 cur.execute("select * from tbIO")
 rows = cur.fetchall();
 return rows
 #return render_template('frmdispipdvc.html',rows = rows)

def disp_rec_tbIO_input():
 con = sqlite3.connect(db_name)
 con.row_factory = sqlite3.Row
 cur = con.cursor()
 cur.execute("select * from tbregipdvc")
 rows = cur.fetchall();
 return rows

#delete
def del_rec_tbIO(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tbIO where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#find
def find_rec_tbIO(Id):
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("SELECT * from tbIO where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]



#update 
def upd_rec_tbIO(Id,Uid,Name,DvcName,Desc,PinConfig):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("Update tbIO set Uid="+Uid+","+"Name="+Name+","+"DvcName="+DvcName+","+"Desc="+Desc+","+"PinConfig="+PinConfig+"where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]





#end of crud code of I/O TABLE

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


#crud code of notification status 

#insert
def save_rec_tbNotiSts(Uid,Nid,Sts):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tbNotiSts (Uid,Nid,Sts) \
    VALUES (?,?,?)",(int(Uid),int(Nid),int(Sts)));
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#display
def disp_rec_tbnotists():
 con = sqlite3.connect(db_name)
 con.row_factory = sqlite3.Row
 cur = con.cursor()
 cur.execute("select * from tbIO")
 rows = cur.fetchall();
 return render_template('frmdispipdvc.html',rows = rows)
#delete
def del_rec_tbnotists(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tbnotists where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#find
def find_rec_tbnotists(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("SELECT * from tbnotists where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]



#update 
def upd_rec_tbNotiSts(Id,Uid,Nid,Sts):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("update tbNotiSts set Uid="+Uid+","+"Nid="+Nid+","+"Sts="+Sts+"where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]







#end of crud code of notification status

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


#crud code of notification service
#insert
def save_rec_tbNotiSrc(NotiName,NotiDesc):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tbNotiSrc (NotiName,NotiDesc) \
    VALUES (?,?,?)",(str(NotiName),str(NotiDesc)));
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#display
def disp_rec_tbnotisrc():
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("select * from tbnotisrc");
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#delete
def del_rec_tbnotisrc(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tbnotisrc where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]
#find
def find_rec_tbnotisrc(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("SELECT * from tbnotisrc where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#update 
def upd_rec_tbNotiSrc(Id,NotiName,NotiDesc):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("Update tbNotiSrc set NotiName="+NotiName+","+"NotiDesc"+NotiDesc+"where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]




#end of crud code of notification service

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#crud code of automation table
#insert
def save_rec_tbautomate(Uid,Name,Desc,Minute,Hour,DOM,Month,DOW):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tbautomate (Uid,Name,Desc,Minute,Hour,DOM,Month,DOW) \
    VALUES (?,?,?,?,?,?,?,?)",(int(Uid),str(Name),str(Desc),int(Minute),int(Hour),int(DOM),int(Month),int(DOW)));
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]



#display
def disp_rec_tbautomate():
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("select * from tbautomate");
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#delete
def del_rec_tbautomate(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tbautomate where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#update 
def upd_rec_tbautomate(Id,Uid,Name,Desc,Minute,Hour,DOM,Month,DOW):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("Update tbautomate set Uid="+Uid+","+"Name="+Name+","+"Desc="+Desc+","+"Minute="+Minute+","+"Hour="+Hour+","+"DOM="+DOM+","+"Month="+Month+","+"DOW="+DOW+"Where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]




#end of crud code of automation table

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


#crud code of live status mgr
#insert
def save_rec_tblivstsmgr(IOID,Sts,Datetime):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("INSERT INTO tblivstsmgr (NotiName,NotiDesc) \
    VALUES (?,?,?)",(int(IOID),int(Sts),str(Datetime)));
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]




#display
def disp_rec_tblivstsmgr():
 try:
   conn = sqlite3.connect(db_name)
   cursor=conn.execute("select * from tblivstsmgr");
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]



#delete
def del_rec_tblivstsmgr(Id):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("DELETE from tblivstsmgr where ID = "+Id+";")
   conn.commit()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]

#update 


def upd_rec_tblivstsmgr(Id,IOID,Sts,Datetime):
 try:
   conn = sqlite3.connect(db_name)
   conn.execute("Update tblivstsmgr set IOID="+IOID+","+"Sts="+Sts+","+"DateTime="+Datetime+"where Id="+Id);
   conn.commit()
   conn.close()
 except sqlite3.Error:
	 print "Error open db.\n"
         return False
         cur = conn.cursor()
         return [conn, cur]


#end of crud code of live status mgr

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------



