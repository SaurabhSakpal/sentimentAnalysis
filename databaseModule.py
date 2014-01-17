#!/usr/bin/python
import MySQLdb;

def setup_database_connection(server,user,password,database_name):
	db = None;	
	try:
		db = MySQLdb.connect(server,user,password,database_name);
	except:
		print("Error connecting to the database, Please check values");
	else:
		print("Successfully Connected to: %s" % database_name );
		return db;

def close_database_connection(db):
	try:
		db.close();
	except:
		print("Error while closing the database connection");
	else:
		print("Database Successfully Closed");
	

def insert_into_review(content, nature,db,ON):
	var = None
	cursor = db.cursor();
	if nature == "positive":
		var = 1;
	else:
		var = 0;
	try:
		query = "insert into Review(content,type) values ('"+str(content)+"',"+str(var)+")"; 
		cursor.execute(query);
		db.commit();
	except:
		print("Error Executing the Query");
		db.rollback();
		close_database_connection(db);
	else:
		if ON:
			print("Query Successfully Executed");
		close_database_connection(db);


def insert_into_adjective(adj_count, nature,db,f,ON):
	var = None
	for i in adj_count:
		cursor = db.cursor();
		j = str(adj_count[i]);
		try:
			query1 = "SELECT * FROM Adjective WHERE aname = '%s'" % i;
			#print(query1);			
			cursor.execute(query1);
			result = cursor.fetchone();
			if result == None:			
				sec_cursor = db.cursor();
				query2 = None;				
				if nature=="negative":
					query2 = "INSERT INTO Adjective(aname,pcount,ncount,tcount) VALUES ('"+i+"',0,"+j+","+j+")";
				elif nature == "positive":
					query2 = "INSERT INTO Adjective(aname,pcount,ncount,tcount) VALUES ('"+i+"',"+j+",0,"+j+")";
				sec_cursor.execute(query2);
				db.commit();
			else:
				#print(result);
				aname = result[1];
				pcount = result[2];
				ncount = result[3];
				tcount = result[4];
				query3 = None;
				if nature == "negative":
					query3 = "UPDATE Adjective SET tcount = tcount + "+j+" , ncount = ncount + "+j+" WHERE aname = '"+aname+"'";
				elif nature =="positive":
					query3 = "UPDATE Adjective SET tcount = tcount + "+j+" , pcount = pcount + "+j+" WHERE aname = '"+aname+"'";
				sec_cursor = db.cursor();
				sec_cursor.execute(query3);
				db.commit();
				#print("Success");			
		except:
			print("Couldn't Execute Query for: %s "% str(f));
			#close_database_connection(db);
	#close_database_connection(db);


