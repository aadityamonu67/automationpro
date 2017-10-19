#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('kk.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE 
         (
	 Id INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
         Regipdvcsnsrid   INTEGER    NOT NULL ,
    
	 Snsrrdg       INTEGER     NOT NULL,
	       FOREIGN KEY (Regipdvcsnsrid) REFERENCES tbregipdvc1(Snsrid)
	 
);''')
print "Table created successfully";

conn.close()
