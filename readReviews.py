import databaseModule;
import os;
import tempfile;
import stringProcessor;
server = "localhost";
user = "root";
password = "sbs37979";
database_name = "sentiment_analysis";
db = databaseModule.setup_database_connection(server,user,password,database_name);
#tempname = tempfile.mktemp('.blob');

dir_list = ["neg/","pos/"];
for i in dir_list:
	for j in range(1000):
		filename = i+"Rev"+str(j+1)+".txt";
		filepath = "~/Desktop/BEProject/"+i+"Rev"+str(j+1)+".txt";
		try:
			f = open(filename);
			content = f.read();
			#print(f);
			tokens = stringProcessor.tokenizeContent(content,False);
			tagged = stringProcessor.part_of_speach_tagging(tokens,False);
			adjective_list = stringProcessor.select_adjectives(tagged,False);
			adj_count = stringProcessor.count_adjectives(adjective_list,False);
			if i=="neg/":
				#print(f);
				#fileobject = open(tempname,'wb');
				#fileobject.write(content);
    				#fileobject.close();
				#tokens = stringProcessor.tokenizeContent(content,False);
				#tagged = stringProcessor.part_of_speach_tagging(tokens,False);
				#adjective_list = stringProcessor.select_adjectives(tagged,False);
				#adj_count = stringProcessor.count_adjectives(adjective_list,False);
				databaseModule.insert_into_adjective(adj_count,"negative",db,f,True);
				#databaseModule.insert_into_adjective(adj_count,"positive",db,True);
			elif i =="pos/":
				databaseModule.insert_into_adjective(adj_count,"positive",db,f,True);			
		except:
			#databaseModule.close_database_connection(db);
			print("IO exception");
		finally:
			#print();
			#databaseModule.close_database_connection(db);
			f.close();
			#os.remove(tempname);
print("Done Successfully");
databaseModule.close_database_connection(db);
#CREATE TABLE Review(rid INT NOT NULL AUTO_INCREMENT, content TEXT, type INT,PRIMARY KEY ( rid ));
#CREATE TABLE Adjective(aid INT NOT NULL AUTO_INCREMENT, aname varchar(255), pcount INT, ncount INT, tcount INT, PRIMARY KEY ( aid ));
#INSERT INTO Review(content,type) VALUES(LOAD_FILES('~/Desktop/BEProject/neg/Rev1.txt'),0);
