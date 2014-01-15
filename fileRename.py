import os;

dir_list =["neg","pos"];
num = 1; 
for s in dir_list:
	file_list = os.listdir(s);
	for k in file_list:
		newname = "neg/Rev"+str(num)+".txt"
		#print(newname);
		oldname = s+"/"+k;
		#print(oldname); 
		os.rename(oldname,newname);
		num = num +1;
	#print(len(file_list));
file_list_copy = os.listdir("neg");




