import os;
#dir_list =["neg","pos"];
#file_list = os.listdir("neg");
file_list = os.listdir("pos");
num = 1; 
for k in file_list:
	newname = "pos/Rev"+str(num)+".txt"
	#print(newname);
	oldname = "pos/"+k;
	#oldname = "neg/"+k;
	#print(oldname); 
	os.rename(oldname,newname);
	num = num +1;
#print(file_list.sort());






