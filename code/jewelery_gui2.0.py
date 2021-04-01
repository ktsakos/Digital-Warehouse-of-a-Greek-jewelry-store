"""
DEVELOPER:TSAKOS KONSTANTINOS
PHONE NUMBER:6948908497
LOCATION:SAMOS,GREECE
THIS PROGRAMM IS NOT OPEN SOURCE AND ONLY THE DEVELOPER HAS ITS RIGHTS
"""
from tkinter import *
import psycopg2
import ttk
import datetime
window=Tk()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
#window.iconbitmap(r'/code/image.ico')
sorting=0

def validate(date_text):
	try:
		datetime.datetime.strptime(date_text, '%d-%m-%Y')
	except ValueError:
		return False
		
def Sorting_By_Column(tree,query,column):
	global sorting
	if (sorting % 2==0):
		type="DESC"
	else:
		type="ASC"
	for i in tree.get_children():
		tree.delete(i)
	lst=run_query("SELECT * FROM (%s) AS foo ORDER BY \"%s\" %s" % (query,column,type))
	for i in lst:
			tree.insert("",END,values=i)
	sorting=sorting+1

def Converter_double_Precision(number):
	position=-1
	for i in range(len(number)):
		if (number[i]=="," or number[i]=="."):
			position=i
			break;
	if (number==""):
		return ""
	elif (position==-1):#2 double precision for integer argument
		return number+".00"
	else:#for float argument
		result=""
		for i in range(position):#insert the chars before , or .
			result=result+number[i]
		result=result+"." #insert . no matter if it was . or , initially
		if(position==(len(number)-2)):#If we have only one decimal after , or .
			result=result+number[position+1]+"0" #Just concatenate the char after , or . and one 0
		else:#If we have 2 or more digits keep only 2 for double precision
			for i in range(position+1,position+3):
				result=result+number[i]
		return result

def run_query(query):
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query_result=cursor.execute(query)
		#conn.commit()
		lst=cursor.fetchall()
		conn.close()
		return lst

def clear():
	list=window.grid_slaves()
	for l in list:
		l.destroy()

########################################################## AGGREGATED QUERIES TO DATABASE IMPLEMENTATION #######################################################

def click5_frame2():
	clear()
	lst=run_query("SELECT \"Quality\",SUM(\"Weight\") FROM \"Gold Product\" GROUP BY \"Quality\" ORDER BY \"Quality\" DESC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνολικού Βάρους Χρυσού ανά Ποιότητα")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Ποιότητα","Συνολικό Βάρος")
	tree.column("Ποιότητα",width=200)
	tree.column("Συνολικό Βάρος",width=200)
	tree.heading("Ποιότητα", text="Ποιότητα")
	tree.heading("Συνολικό Βάρος", text="Συνολικό Βάρος(γρ)")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click6_frame2():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Συνολική Αξία σε Ασήμι και Γενικού Τύπου εμπορεύματα")
	result=run_query("SELECT SUM(\"Price\") FROM \"Silver Product\"")
	Label(window,text="Η συνολική αξία εμπορευμάτων εκτός χρυσού που υπάρχει αυτή τη στιγμή στην αποθήκη είναι: %s ευρώ" % (result[0]),fg="red",bg="white").grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click7_frame2():
	clear()
	lst=run_query("SELECT \"Company\",\"Quality\",SUM(\"Weight\") FROM \"Gold Product\" GROUP BY \"Company\",\"Quality\" ORDER BY \"Company\",\"Quality\" DESC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνολικού Βάρους Χρυσού ανά Προμηθευτή")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Προμηθευτής","Ποιότητα","Συνολικό Βάρος")
	tree.column("Προμηθευτής",width=200)
	tree.column("Ποιότητα",width=200)
	tree.column("Συνολικό Βάρος",width=200)
	tree.heading("Προμηθευτής", text="Προμηθευτής")
	tree.heading("Ποιότητα", text="Ποιότητα")
	tree.heading("Συνολικό Βάρος", text="Συνολικό Βάρος(γρ)")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click8_frame2():
	clear()
	lst=run_query("SELECT \"Company\",SUM(\"Price\") FROM \"Silver Product\" GROUP BY \"Company\" ORDER BY \"Company\" DESC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνολικής Αξίας σε Ασήμι και Γενικού Τύπου εμπορεύματα ανά προμηθευτή")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Προμηθευτής","Συνολική Αξία")
	tree.column("Προμηθευτής",width=200)
	tree.column("Συνολική Αξία",width=200)
	tree.heading("Προμηθευτής", text="Προμηθευτής")
	tree.heading("Συνολική Αξία", text="Συνολική Αξία(ευρώ)")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click9_frame2():
	clear()
	lst=run_query("SELECT \"Categorie\",SUM(\"Price\") FROM \"Silver Product\" GROUP BY \"Categorie\" ORDER BY \"Categorie\" DESC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνολικής Αξίας σε Ασήμι και Γενικού Τύπου εμπορεύματα ανά κατηγορία΄")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Συνολική Αξία")
	tree.column("Κατηγορία",width=200)
	tree.column("Συνολική Αξία",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Συνολική Αξία", text="Συνολική Αξία(ευρώ)")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click10_frame2():	
	clear()
	lst=run_query("SELECT \"Categorie\",COUNT(*) FROM \"Gold Product\" GROUP BY \"Categorie\" ORDER BY \"Categorie\" ASC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνόλου τεμαχίων ανά κατηγορία Χρυσού")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Τεμάχια")
	tree.column("Κατηγορία",width=200)
	tree.column("Τεμάχια",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Τεμάχια", text="Τεμάχια")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click11_frame2():	
	clear()
	lst=run_query("SELECT \"Categorie\",COUNT(*) FROM \"Silver Product\" GROUP BY \"Categorie\" ORDER BY \"Categorie\" ASC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνόλου τεμαχίων ανά κατηγορία σε ασήμι ή Γενικού Τύπου")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Τεμάχια")
	tree.column("Κατηγορία",width=200)
	tree.column("Τεμάχια",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Τεμάχια", text="Τεμάχια")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)	
	
def click12_frame2():	
	clear()
	lst=run_query("SELECT \"Categorie\",\"Company\",\"Quality\",COUNT(*) FROM \"Gold Product\" GROUP BY \"Categorie\",\"Company\",\"Quality\" ORDER BY \"Categorie\",\"Company\",\"Quality\" ASC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνόλου τεμαχίων ανά κατηγορία Χρυσού ανά προμηθευτή και ανά ποιότητα")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Προμηθευτής","Ποιότητα","Τεμάχια")
	tree.column("Κατηγορία",width=200)
	tree.column("Προμηθευτής",width=200)
	tree.column("Ποιότητα",width=200)
	tree.column("Τεμάχια",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Προμηθευτής", text="Προμηθευτής")
	tree.heading("Ποιότητα", text="Ποιότητα")
	tree.heading("Τεμάχια", text="Τεμάχια")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click13_frame2():	
	clear()
	lst=run_query("SELECT \"Categorie\",\"Company\",COUNT(*) FROM \"Gold Product\" GROUP BY \"Categorie\",\"Company\" ORDER BY \"Categorie\",\"Company\" ASC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνόλου τεμαχίων ανά κατηγορία Χρυσού ανά προμηθευτή")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Προμηθευτής","Ποιότητα","Τεμάχια")
	tree.column("Κατηγορία",width=200)
	tree.column("Προμηθευτής",width=200)
	tree.column("Τεμάχια",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Προμηθευτής", text="Προμηθευτής")
	tree.heading("Τεμάχια", text="Τεμάχια")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click14_frame2():	
	clear()
	lst=run_query("SELECT \"Categorie\",\"Company\",COUNT(*) FROM \"Silver Product\" GROUP BY \"Categorie\",\"Company\" ORDER BY \"Categorie\",\"Company\" ASC")
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Συνόλου τεμαχίων ανά κατηγορία σε ασήμι ή Γενικού Τύπου ανά προμηθευτή")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Προμηθευτής","Τεμάχια")
	tree.column("Κατηγορία",width=200)
	tree.column("Προμηθευτής",width=200)
	tree.column("Τεμάχια",width=200)
	tree.heading("Κατηγορία", text="Κατηγορία")
	tree.heading("Προμηθευτής", text="Προμηθευτής")
	tree.heading("Τεμάχια", text="Τεμάχια")
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="OK",width=100,command=frame1).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)
########################################################## END OF AGGREGATED QUERIES TO DATABASE	##############################################

########################################################## SILVER PRODUCT OPERATIONS IMPLEMENTATION ##############################################

def Delete_Silver_Product(tree):
	for selected_item in tree.selection():
			temp=[tree.set(selected_item,'#1'),tree.set(selected_item,'#2'),tree.set(selected_item,'#3'),tree.set(selected_item,'#4'),tree.set(selected_item,'#5')]
			temp2=[None]*5 #Initialization of an empty list,this will be used for the queries checks format
			temp3=[None]*5 #Initialization of an empty list,this will be used for the insertion's format
			for i in range(5):
				if (temp[i]=="None"):
					temp2[i]=" is NULL"
					temp3[i]="NULL"
				else:
					temp2[i]="='%s'" % (temp[i])
					temp3[i]="'%s'" % (temp[i])
			conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
			cursor=conn.cursor()
			query="SELECT COUNT(*) FROM \"Silver Product\" WHERE (\"Categorie\"%s AND \"Date\"%s AND \"Price\"%s AND \"Color\"%s AND \"Company\"%s)" % (temp2[0],temp2[1],temp2[2],temp2[3],temp2[4])
			cursor.execute(query)
			result=cursor.fetchone()
			query="DELETE FROM \"Silver Product\" WHERE (\"Categorie\"%s AND \"Date\"%s AND \"Price\"%s AND \"Color\"%s AND \"Company\"%s)" % (temp2[0],temp2[1],temp2[2],temp2[3],temp2[4])
			query_result=cursor.execute(query)
			for i in range(result[0]-1):
				query="INSERT INTO \"Silver Product\"(\"Categorie\",\"Date\",\"Price\",\"Color\",\"Company\") VALUES (%s,%s,%s,%s,%s);" % (temp3[0],temp3[1],temp3[2],temp3[3],temp3[4])
				query_result=cursor.execute(query)
			conn.commit()
			conn.close()
			tree.delete(selected_item)
	click4_frame2_click3_frame3()

def click4_frame2_click3_frame3_results(temp1,temp2,temp3):
	if(temp1=="" or temp2=="" or temp3==""):
		click4_frame2_click3_frame3()
		return;
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Διαγραφή Προϊόντων από Ασήμι ή Γενικού Τύπου")
	lst=run_query("SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3))
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Ημερομηνία","Τιμή","Χρώμα","Εταιρεία")
	tree.column("Κατηγορία",width=100)
	tree.column("Ημερομηνία",width=100)
	tree.column("Τιμή",width=100)
	tree.column("Χρώμα",width=100)
	tree.column("Εταιρεία",width=100)
	tree.heading("Κατηγορία", text="Κατηγορία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3),"Categorie"))
	tree.heading("Ημερομηνία", text="Ημερομηνία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3),"Date"))
	tree.heading("Τιμή", text="Τιμή",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3),"Price"))
	tree.heading("Χρώμα", text="Χρώμα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3),"Color"))
	tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Price\"='%s')" % (temp1,temp2,temp3),"Company"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή",width=100,command=lambda:Delete_Silver_Product(tree)).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click4_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)

def click4_frame2_click3_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Αναζήτηση Προϊόντων από Ασήμι ή Γενικού Τύπου για Διαγραφή")
	Label(window,text="Κατηγορία").grid(row=0,column=0)
	lst=run_query("SELECT * FROM \"Categories\"")
	data=[]
	for tuple in lst:
		data.append(tuple[0])
	E1=ttk.Combobox(window,width=100)
	E1.grid(row=1,column=0)
	E1['values']=data
	Label(window,text="Προμηθευτής").grid(row=2,column=0)
	lst=run_query("SELECT * FROM \"Supplier\"")
	data2=[]
	for tuple in lst:
		data2.append(tuple[0])
	E2=ttk.Combobox(window,width=100)
	E2.grid(row=3,column=0)
	E2['values']=data2
	Label(window,text="Τιμή").grid(row=4,column=0)
	E3=Entry(window,width=100,bg="white")
	E3.grid(row=5,column=0)
	Button(window, text="Αναζήτηση",width=100,command=lambda:click4_frame2_click3_frame3_results(E1.get(),E2.get(),Converter_double_Precision(E3.get()))).grid(row=6,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Καθάρισμα",width=100,command=click4_frame2_click3_frame3).grid(row=7,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click4_frame2).grid(row=8,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="*Όλα τα πεδία της αναζήτησης πρέπει να συμπληρωθούν!!").grid(row=9,column=0)
	Label(window,text="Created by Tsakos Kostas").grid(row=10,column=0)

def Add_Silver_Product(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8):#Insert Silver Product into DB
	if (len(temp1)==0 or len(temp3)==0 or len(temp5)==0):
		temp8.config(text='Αποτυχημένη καταχώρηση! Πρέπει να συμπληρωθούν τα πεδία με αστερίσκο (*)!')
		temp8.config(fg="red")
		temp7.config(text="")
	elif (len(temp2)!=0 and validate(temp2)==False):
		temp7.config(text='Η ημερομηνία δε δώθηκε σωστά!!')
		temp7.config(fg="red")
		temp8.config(text="")
	else:
		temp7.config(text="")
		temp8.config(text='Επιτυχής καταχώρηση!')
		temp8.config(fg="green")
		temp6.delete(0,'end')
		temp5="'"+temp5+"'"
		temp1="'"+temp1+"'"
		temp3="'"+temp3+"'"
		if (len(temp2)==0):
			temp2="NULL"
		else:
			temp2="'"+temp2+"'"
		if (len(temp4)==0):
			temp4="NULL"
		else:
			temp4="'"+temp4+"'"
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="INSERT INTO \"Silver Product\"(\"Categorie\",\"Date\",\"Price\",\"Color\",\"Company\") VALUES (%s,%s,%s,%s,%s);" % (temp1,temp2,temp3,temp4,temp5)
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()


def click4_frame2_click2_frame3_firsttime():
		clear()
		click4_frame2_click2_frame3()

def click4_frame2_click2_frame3():
	#clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Εισαγωγή Nέου Προϊόντος από Ασήμι ή Γενικού Τύπου")
	Label(window,text="Κατηγορία*").grid(row=0,column=0)
	lst=run_query("SELECT * FROM \"Categories\"")
	data=[]
	for tuple in lst:
		data.append(tuple[0])
	E1=ttk.Combobox(window,width=100)
	E1.grid(row=1,column=0)
	E1['values']=data
	Label(window,text="Ημερομηνία**").grid(row=2,column=0)
	E2=Entry(window,width=100,bg="white")
	E2.grid(row=3,column=0)
	L1=Label(window,text="")
	L1.grid(row=3,column=1)
	Label(window,text="Τιμή(*)(***)").grid(row=4,column=0)
	E3=Entry(window,width=100,bg="white")
	E3.grid(row=5,column=0)
	L2=Label(window,text="")
	L2.grid(row=5,column=1)
	Label(window,text="Χρώμα").grid(row=6,column=0)
	E4=ttk.Combobox(window,width=100)
	E4.grid(row=7,column=0)
	E4['values']=['ΑΣΠΡΟ','ΚΙΤΡΙΝΟ','ΡΟΖ']
	Label(window,text="Προμηθευτής*").grid(row=8,column=0)
	lst=run_query("SELECT * FROM \"Supplier\"")
	data2=[]
	for tuple in lst:
		data2.append(tuple[0])
	E5=ttk.Combobox(window,width=100)
	E5.grid(row=9,column=0)
	E5['values']=data2
	Button(window, text="Προσθήκη",width=100,command=lambda:Add_Silver_Product(E1.get(),E2.get(),Converter_double_Precision(E3.get()),E4.get(),E5.get(),E3,L1,L2)).grid(row=10,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Καθάρισμα",width=100,command=click4_frame2_click2_frame3_firsttime).grid(row=11,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click4_frame2).grid(row=12,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="*Τα πεδία είναι υποχρεωτικό να είναι συμπληρωμένα πριν την προσθήκη\n** Η ημερομηνία πρέπει να είναι της μορφής:dd-mm-yyyy\n***Το πεδίο Τιμή πρέπει να δωθεί με ακρίβεια 2 δεκαδικών ψηφίων").grid(row=13,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=14,column=0)

def click4_frame2_click1_frame3():
		clear()
		window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Προϊόντων από Ασήμι ή Γενικού Τύπου")
		lst=run_query("SELECT * FROM \"Silver Product\"")
		tree=ttk.Treeview(window,height=25,show=["headings"])
		tree["columns"]=("Κατηγορία","Ημερομηνία","Τιμή","Χρώμα","Εταιρεία")
		tree.column("Κατηγορία",width=100)
		tree.column("Ημερομηνία",width=100)
		tree.column("Τιμή",width=100)
		tree.column("Χρώμα",width=100)
		tree.column("Εταιρεία",width=100)
		tree.heading("Κατηγορία", text="Κατηγορία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\"","Categorie"))
		tree.heading("Ημερομηνία", text="Ημερομηνία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\"","Date"))
		tree.heading("Τιμή", text="Τιμή",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\"","Price"))
		tree.heading("Χρώμα", text="Χρώμα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\"","Color"))
		tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Silver Product\"","Company"))
		for i in lst:
			tree.insert("",END,values=i)
		tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Πίσω",width=100,command=click4_frame2).grid(row=1,column=0,padx=(10,10),pady=(10,10))
		Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click4_frame2():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προϊόντα από Ασήμι ή Γενικού Τύπου")
	Button(window, text="Προβολή Προϊόντων",width=100,command=click4_frame2_click1_frame3).grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Εισαγωγή Νέου Προϊόντος",width=100,command=click4_frame2_click2_frame3_firsttime).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή Προϊόντος",width=100,command=click4_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=frame1).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=4,column=0)


########################################################## END OF SILVER PRODUCT OPERATIONS #######################################################

########################################################## GOLD PRODUCTS OPERATIONS IMPLEMENTATION ###############################################

def Delete_Gold_Product(tree):
	for selected_item in tree.selection():
			temp=[tree.set(selected_item,'#1'),tree.set(selected_item,'#2'),tree.set(selected_item,'#3'),tree.set(selected_item,'#4'),tree.set(selected_item,'#5'),tree.set(selected_item,'#6'),tree.set(selected_item,'#7')]
			temp2=[None]*7 #Initialization of an empty list,this will be used for the queries checks format
			temp3=[None]*7 #Initialization of an empty list,this will be used for the insertion's format
			for i in range(7):
				if (temp[i]=="None"):
					temp2[i]=" is NULL"
					temp3[i]="NULL"
				else:
					temp2[i]="='%s'" % (temp[i])
					temp3[i]="'%s'" % (temp[i])
			conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
			cursor=conn.cursor()
			query="SELECT COUNT(*) FROM \"Gold Product\" WHERE (\"Categorie\"%s AND \"Date\"%s AND \"Price\"%s AND \"Color\"%s AND \"Company\"%s AND \"Quality\"%s AND \"Weight\"%s)" % (temp2[0],temp2[1],temp2[2],temp2[3],temp2[4],temp2[5],temp2[6])
			cursor.execute(query)
			result=cursor.fetchone()
			query="DELETE FROM \"Gold Product\" WHERE (\"Categorie\"%s AND \"Date\"%s AND \"Price\"%s AND \"Color\"%s AND \"Company\"%s AND \"Quality\"%s AND \"Weight\"%s)" % (temp2[0],temp2[1],temp2[2],temp2[3],temp2[4],temp2[5],temp2[6])
			query_result=cursor.execute(query)
			for i in range(result[0]-1):
				query="INSERT INTO \"Gold Product\"(\"Categorie\",\"Date\",\"Price\",\"Color\",\"Company\",\"Quality\",\"Weight\") VALUES (%s,%s,%s,%s,%s,%s,%s);" % (temp3[0],temp3[1],temp3[2],temp3[3],temp3[4],temp3[5],temp3[6])
				query_result=cursor.execute(query)
			conn.commit()
			conn.close()
			tree.delete(selected_item)
	click3_frame2_click3_frame3()

def click3_frame2_click3_frame3_results(temp1,temp2,temp3,temp4):
	if(temp1=="" or temp2=="" or temp3=="" or temp4==""):
		click3_frame2_click3_frame3()
		return;
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Διαγραφή Προϊόντων Χρυσού")
	lst=run_query("SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4))
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Κατηγορία","Ημερομηνία","Τιμή","Χρώμα","Εταιρεία","Ποιότητα","Βάρος")
	tree.column("Κατηγορία",width=100)
	tree.column("Ημερομηνία",width=100)
	tree.column("Τιμή",width=100)
	tree.column("Χρώμα",width=100)
	tree.column("Εταιρεία",width=100)
	tree.column("Ποιότητα",width=100)
	tree.column("Βάρος",width=100)
	tree.heading("Κατηγορία", text="Κατηγορία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Categorie"))
	tree.heading("Ημερομηνία", text="Ημερομηνία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Date"))
	tree.heading("Τιμή", text="Τιμή",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Price"))
	tree.heading("Χρώμα", text="Χρώμα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Color"))
	tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Company"))
	tree.heading("Ποιότητα", text="Ποιότητα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Quality"))
	tree.heading("Βάρος", text="Βάρος",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\" WHERE (\"Categorie\"='%s' AND \"Company\"='%s' AND \"Quality\"='%s' AND \"Weight\"='%s')" %(temp1,temp2,temp3,temp4),"Weight"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή",width=100,command=lambda:Delete_Gold_Product(tree)).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click3_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)

def click3_frame2_click3_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Αναζήτηση Προϊόντων Χρυσού για Διαγραφή")
	Label(window,text="Κατηγορία").grid(row=0,column=0)
	lst=run_query("SELECT * FROM \"Categories\"")
	data=[]
	for tuple in lst:
		data.append(tuple[0])
	E1=ttk.Combobox(window,width=100)
	E1.grid(row=1,column=0)
	E1['values']=data
	Label(window,text="Προμηθευτής").grid(row=2,column=0)
	lst=run_query("SELECT * FROM \"Supplier\"")
	data2=[]
	for tuple in lst:
		data2.append(tuple[0])
	E2=ttk.Combobox(window,width=100)
	E2.grid(row=3,column=0)
	E2['values']=data2
	Label(window,text="Ποιότητα").grid(row=4,column=0)
	E3=ttk.Combobox(window,width=100)
	E3.grid(row=5,column=0)
	E3['values']=['K9','K14','K18']
	Label(window,text="Βάρος").grid(row=6,column=0)
	E4=Entry(window,width=100,bg="white")
	E4.grid(row=7,column=0)
	Button(window, text="Αναζήτηση",width=100,command=lambda:click3_frame2_click3_frame3_results(E1.get(),E2.get(),E3.get(),Converter_double_Precision(E4.get()))).grid(row=8,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Καθάρισμα",width=100,command=click3_frame2_click3_frame3).grid(row=9,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click3_frame2).grid(row=10,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="*Όλα τα πεδία της αναζήτησης πρέπει να συμπληρωθούν!!").grid(row=11,column=0)
	Label(window,text="Created by Tsakos Kostas").grid(row=12,column=0)

def Add_Gold_Product(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10):#Insert Gold Product into DB
	if (len(temp1)==0 or len(temp5)==0 or len(temp6)==0 or len(temp7)==0):
		temp10.config(text='Αποτυχημένη καταχώρηση! Πρέπει να συμπληρωθούν τα πεδία με αστερίσκο (*)!')
		temp10.config(fg="red")
		temp9.config(text="")
	elif (len(temp2)!=0 and validate(temp2)==False):
		temp9.config(text='Η ημερομηνία δε δώθηκε σωστά!!')
		temp9.config(fg="red")
		temp10.config(text="")
	else:
		temp8.delete(0,'end')
		temp9.config(text="")
		temp10.config(text='Επιτυχής καταχώρηση')
		temp10.config(fg="green")
		temp1="'"+temp1+"'"
		temp5="'"+temp5+"'"
		temp6="'"+temp6+"'"
		temp7="'"+temp7+"'"
		if (len(temp2)==0):
			temp2="NULL"
		else:
			temp2="'"+temp2+"'"
		if (len(temp3)==0):
			temp3="NULL"
		else:
			temp3="'"+temp3+"'"
		if (len(temp4)==0):
			temp4="NULL"
		else:
			temp4="'"+temp4+"'"
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="INSERT INTO \"Gold Product\"(\"Categorie\",\"Date\",\"Price\",\"Color\",\"Company\",\"Quality\",\"Weight\") VALUES (%s,%s,%s,%s,%s,%s,%s);" % (temp1,temp2,temp3,temp4,temp5,temp6,temp7)
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()


def click3_frame2_click2_frame3_firsttime():
		clear()
		click3_frame2_click2_frame3()

def click3_frame2_click2_frame3():
	#clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Εισαγωγή Nέου Προϊόντος Χρυσού")
	Label(window,text="Κατηγορία*").grid(row=0,column=0)
	lst=run_query("SELECT * FROM \"Categories\"")
	data=[]
	for tuple in lst:
		data.append(tuple[0])
	E1=ttk.Combobox(window,width=100)
	E1.grid(row=1,column=0)
	E1['values']=data
	Label(window,text="Ημερομηνία**").grid(row=2,column=0)
	E2=Entry(window,width=100,bg="white")
	E2.grid(row=3,column=0)
	L1=Label(window,text="")
	L1.grid(row=3,column=1)
	Label(window,text="Τιμή***").grid(row=4,column=0)
	E3=Entry(window,width=100,bg="white")
	E3.grid(row=5,column=0)
	Label(window,text="Χρώμα").grid(row=6,column=0)
	E4=ttk.Combobox(window,width=100)
	E4.grid(row=7,column=0)
	E4['values']=['ΚΙΤΡΙΝΟ','ΑΣΠΡΟ','ΡΟΖ']
	Label(window,text="Προμηθευτής*").grid(row=8,column=0)
	lst=run_query("SELECT * FROM \"Supplier\"")
	data2=[]
	for tuple in lst:
		data2.append(tuple[0])
	E5=ttk.Combobox(window,width=100)
	E5.grid(row=9,column=0)
	E5['values']=data2
	Label(window,text="Ποιότητα*").grid(row=10,column=0)
	E6=ttk.Combobox(window,width=100)
	E6.grid(row=11,column=0)
	E6['values']=['K9','K14','K18']
	Label(window,text="Βάρος(*)(***)").grid(row=12,column=0)
	E7=Entry(window,width=100,bg="white")
	E7.grid(row=13,column=0)
	L2=Label(window,text="")
	L2.grid(row=13,column=1)
	Button(window, text="Προσθήκη",width=100,command=lambda:Add_Gold_Product(E1.get(),E2.get(),Converter_double_Precision(E3.get()),E4.get(),E5.get(),E6.get(),Converter_double_Precision(E7.get()),E7,L1,L2)).grid(row=14,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Καθάρισμα",width=100,command=click3_frame2_click2_frame3_firsttime).grid(row=15,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click3_frame2).grid(row=16,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="*Τα πεδία είναι υποχρεωτικό να είναι συμπληρωμένα πριν την προσθήκη\n** Η ημερομηνία πρέπει να είναι της μορφής:dd-mm-yyyy\n***Τα πεδία Τιμή και Βάρος πρέπει να δωθούν με ακρίβεια 2 δεκαδικών ψηφίων").grid(row=17,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=18,column=0)


def click3_frame2_click1_frame3():
		clear()
		window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Προϊόντων Χρυσού")
		lst=run_query("SELECT * FROM \"Gold Product\"")
		tree=ttk.Treeview(window,height=25,show=["headings"])
		tree["columns"]=("Κατηγορία","Ημερομηνία","Τιμή","Χρώμα","Εταιρεία","Ποιότητα","Βάρος")
		tree.column("Κατηγορία",width=100)
		tree.column("Ημερομηνία",width=100)
		tree.column("Τιμή",width=100)
		tree.column("Χρώμα",width=100)
		tree.column("Εταιρεία",width=100)
		tree.column("Ποιότητα",width=100)
		tree.column("Βάρος",width=100)
		tree.heading("Κατηγορία", text="Κατηγορία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Categorie"))
		tree.heading("Ημερομηνία", text="Ημερομηνία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Date"))
		tree.heading("Τιμή", text="Τιμή",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Price"))
		tree.heading("Χρώμα", text="Χρώμα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Color"))
		tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Company"))
		tree.heading("Ποιότητα", text="Ποιότητα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Quality"))
		tree.heading("Βάρος", text="Βάρος",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Gold Product\"","Weight"))
		for i in lst:
			tree.insert("",END,values=i)
		tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Πίσω",width=100,command=click3_frame2).grid(row=1,column=0,padx=(10,10),pady=(10,10))
		Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click3_frame2():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προϊόντα Χρυσού")
	Button(window, text="Προβολή Προϊόντων",width=100,command=click3_frame2_click1_frame3).grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Εισαγωγή Νέου Προϊόντος",width=100,command=click3_frame2_click2_frame3_firsttime).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή Προϊόντος",width=100,command=click3_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=frame1).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=4,column=0)

########################################################## END OF GOLD PRODUCTS OPERATIONS #######################################################

######################################################### CATEGORIES OPERATIONS IMPLEMENTATION #####################################################

def Delete_Category(tree):#Delete Categories from db
	for selected_item in tree.selection():
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="DELETE FROM \"Categories\" WHERE (\"Name\"='"+tree.set(selected_item,'#1')+"')"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()
		tree.delete(selected_item)
	click2_frame2_click4_frame3()

def click2_frame2_click4_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Διαγραφή Κατηγορίας")
	lst=run_query("SELECT * FROM \"Categories\"")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Όνομα")
	tree.column("Όνομα",width=600)
	tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Categories\"","Name"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή",width=100,command=lambda:Delete_Category(tree)).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click2_frame2).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)

def Edit_Category(temp1,temp2):
	if (len(temp1)==0):
		Label(window,text="Το πεδίο πρέπει να συμπληρωθεί για την ενημέρωση!!*",fg="red").grid(row=1,column=1,padx=(10,10),pady=(10,10))
	else:
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="UPDATE \"Categories\" SET \"Name\"='"+temp1+"' WHERE \"Name\"='"+temp2+"'"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()
		click2_frame2_click3_frame3()

def Edit_Cat(tree):
	if (len(tree)!=0):
		clear()
		window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Επεξεργασία Κατηγορίας")
		Label(window,text="Όνομα*").grid(row=0,column=0,padx=(10,10),pady=(10,10))
		E1=Entry(window,width=100,bg="white")
		E1.grid(row=1,column=0,padx=(10,10),pady=(10,10))
		E1.insert(END,tree[0])
		Button(window, text="Αποθήκευση",width=100,command=lambda:Edit_Category(E1.get(),tree[0])).grid(row=2,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Ακύρωση",width=100,command=click2_frame2_click3_frame3).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	else:
		click2_frame2_click3_frame3()

def click2_frame2_click3_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Επεξεργασία Κατηγορίας")
	lst=run_query("SELECT * FROM \"Categories\"")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Όνομα")
	tree.column("Όνομα",width=600)
	tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Categories\"","Name"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Επεξεργασία",width=100,command=lambda:Edit_Cat(tree.item(tree.selection())['values'])).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click2_frame2).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)

def Add_Category(temp1):
	if (len(temp1)==0):
		Label(window,text="Το πεδίο πρέπει να συμπληρωθεί πριν την εισαγωγή!!*",fg="red").grid(row=1,column=1,padx=(10,10),pady=(10,10))
	else:
		clear()
		click2_frame2()
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="INSERT INTO \"Categories\"(\"Name\") VALUES ('"+temp1+"');"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()

def click2_frame2_click2_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Εισαγωγή Νέας Κατηγορίας")
	Label(window,text="Όνομα*").grid(row=0,column=0,padx=(10,10),pady=(10,10))
	E1=Entry(window,width=100,bg="white")
	E1.grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Προσθήκη",width=100,command=lambda:Add_Category(E1.get())).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click2_frame2).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="* Τα πεδία ειναι υποχρεωτικά να συμπληρωθούν!!").grid(row=4,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=5,column=0)

def click2_frame2_click1_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Κατηγοριών")
	lst=run_query("SELECT * FROM \"Categories\"")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Όνομα")
	tree.column("Όνομα",width=600)
	tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Categories\"","Name"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click2_frame2).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)


def click2_frame2():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Κατηγορίες Προϊόντων")
	Button(window, text="Προβολή Κατηγοριών",width=100,command=click2_frame2_click1_frame3).grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Εισαγωγή Νέας Κατηγορίας",width=100,command=click2_frame2_click2_frame3).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Επεξεργασία Κατηγορίας",width=100,command=click2_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή Κατηγορίας",width=100,command=click2_frame2_click4_frame3).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=frame1).grid(row=4,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=5,column=0)

######################################################### END OF CATEGORIES OPERATIONS     #########################################################

######################################################### SUPPLIERS OPERATIONS IMPLEMENTATION #######################################################

def Edit_Supplier(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9):
	if (len(temp1)==0):
		Label(window,text="Πρέπει να δωθεί το όνομα της εταιρείας!!",fg="red").grid(row=1,column=1,padx=(10,10),pady=(10,10))
	else:
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="UPDATE \"Supplier\" SET \"Company\"='"+temp1+"',\"Name\"='"+temp2+"',\"Surname\"='"+temp3+"',\"Address\"='"+temp4+"',\"Phone\"='"+temp5+"',\"Mobile Phone\"='"+temp6+"',\"Bank Account\"='"+temp7+"',\"Bank Account2\"='"+temp8+"' WHERE (\"Company\"='"+temp9+"')"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()
		click1_frame2_click3_frame3()

def Edit_Sup(tree):#Edit Supplier from db
		if (len(tree)!=0): #Check in case nothing was checked!!
			clear()
			window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Επεξεργασία Προμηθευτή")
			Label(window,text="Εταιρεία*").grid(row=0,column=0,padx=(10,10),pady=(10,10))
			E1=Entry(window,width=100,bg="white")
			E1.grid(row=1,column=0,padx=(10,10),pady=(10,10))
			E1.insert(END,tree[0])
			Label(window,text="Όνομα").grid(row=2,column=0,padx=(10,10),pady=(10,10))
			E2=Entry(window,width=100,bg="white")
			E2.grid(row=3,column=0,padx=(10,10),pady=(10,10))
			E2.insert(END,tree[1])
			Label(window,text="Επίθετο").grid(row=4,column=0,padx=(10,10),pady=(10,10))
			E3=Entry(window,width=100,bg="white")
			E3.grid(row=5,column=0,padx=(10,10),pady=(10,10))
			E3.insert(END,tree[2])
			Label(window,text="Διεύθυνση").grid(row=6,column=0,padx=(10,10),pady=(10,10))
			E4=Entry(window,width=100,bg="white")
			E4.grid(row=7,column=0,padx=(10,10),pady=(10,10))
			E4.insert(END,tree[3])
			Label(window,text="Σταθερό Τηλέφωνο").grid(row=8,column=0,padx=(10,10),pady=(10,10))
			E5=Entry(window,width=100,bg="white")
			E5.grid(row=9,column=0,padx=(10,10),pady=(10,10))
			E5.insert(END,tree[4])
			Label(window,text="Κινητό").grid(row=10,column=0,padx=(10,10),pady=(10,10))
			E6=Entry(window,width=100,bg="white")
			E6.grid(row=11,column=0,padx=(10,10),pady=(10,10))
			E6.insert(END,tree[5])
			Label(window,text="Τραπεζικός Λογαριασμός").grid(row=12,column=0,padx=(10,10),pady=(10,10))
			E7=Entry(window,width=100,bg="white")
			E7.grid(row=13,column=0,padx=(10,10),pady=(10,10))
			E7.insert(END,tree[6])
			Label(window,text="Τραπεζικός Λογαριασμός2").grid(row=14,column=0,padx=(10,10),pady=(10,10))
			E8=Entry(window,width=100,bg="white")
			E8.grid(row=15,column=0,padx=(10,10),pady=(10,10))
			E8.insert(END,tree[7])
			Button(window, text="Αποθήκευση",width=100,command=lambda:Edit_Supplier(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),tree[0])).grid(row=16,column=0,padx=(10,10),pady=(10,10))
			Button(window, text="Ακύρωση",width=100,command=click1_frame2_click3_frame3).grid(row=17,column=0,padx=(10,10),pady=(10,10))
		else:
			click1_frame2_click3_frame3()


def click1_frame2_click3_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Επεξεργασία Προμηθευτή")
	lst=run_query("SELECT * FROM \"Supplier\"")
	tree=ttk.Treeview(window,height=25,show=["headings"])
	tree["columns"]=("Εταιρεία","Όνομα","Επίθετο","Διεύθυνση","Σταθερό Τηλέφωνο","Κινητό","Τραπεζικός Λογαριασμός","Τραπεζικός Λογαριασμός2")
	tree.column("Εταιρεία",width=100)
	tree.column("Όνομα",width=100)
	tree.column("Επίθετο",width=100)
	tree.column("Διεύθυνση",width=100)
	tree.column("Σταθερό Τηλέφωνο",width=200)
	tree.column("Κινητό",width=100)
	tree.column("Τραπεζικός Λογαριασμός",width=200)
	tree.column("Τραπεζικός Λογαριασμός2",width=200)
	tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Company"))
	tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Name"))
	tree.heading("Επίθετο", text="Επίθετο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Surname"))
	tree.heading("Διεύθυνση", text="Διεύθυνση",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Address"))
	tree.heading("Σταθερό Τηλέφωνο", text="Σταθερό Τηλέφωνο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Phone"))
	tree.heading("Κινητό", text="Κινητό",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Mobile Phone"))
	tree.heading("Τραπεζικός Λογαριασμός", text="Τραπεζικός Λογαριασμός",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account"))
	tree.heading("Τραπεζικός Λογαριασμός2", text="Τραπεζικός Λογαριασμός2",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account2"))
	for i in lst:
		tree.insert("",END,values=i)
	tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Επεξεργασία",width=100,command=lambda:Edit_Sup(tree.item(tree.selection())['values'])).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=click1_frame2).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)


def Add_Supplier(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8):#Insert Suppliers into DB
	if (len(temp1)==0):
		Label(window,text="Πρέπει να δωθεί η εταιρεία!!",fg="red").grid(row=1,column=1,padx=(10,10),pady=(10,10))
	else:
		clear()
		click1_frame2()
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="INSERT INTO \"Supplier\"(\"Company\",\"Name\",\"Surname\",\"Address\",\"Phone\",\"Mobile Phone\",\"Bank Account\",\"Bank Account2\") VALUES ('"+temp1+"','"+temp2+"','"+temp3+"','"+temp4+"','"+temp5+"','"+temp6+"','"+temp7+"','"+temp8+"');"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()

def click1_frame2_click2_frame3():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Εισαγωγή Προμηθευτή")
	Label(window,text="Εταιρεία*").grid(row=0,column=0,padx=(10,10),pady=(5,5))
	E1=Entry(window,width=100,bg="white")
	E1.grid(row=1,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Όνομα").grid(row=2,column=0,padx=(10,10),pady=(5,5))
	E2=Entry(window,width=100,bg="white")
	E2.grid(row=3,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Επίθετο").grid(row=4,column=0,padx=(10,10),pady=(5,5))
	E3=Entry(window,width=100,bg="white")
	E3.grid(row=5,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Διεύθυνση").grid(row=6,column=0,padx=(10,10),pady=(5,5))
	E4=Entry(window,width=100,bg="white")
	E4.grid(row=7,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Σταθερό Τηλέφωνο").grid(row=8,column=0,padx=(10,10),pady=(5,5))
	E5=Entry(window,width=100,bg="white")
	E5.grid(row=9,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Κινητό").grid(row=10,column=0,padx=(10,10),pady=(5,5))
	E6=Entry(window,width=100,bg="white")
	E6.grid(row=11,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Τραπεζικός Λογαριασμός").grid(row=12,column=0,padx=(10,10),pady=(5,5))
	E7=Entry(window,width=100,bg="white")
	E7.grid(row=13,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Τραπεζικός Λογαριασμός2").grid(row=14,column=0,padx=(10,10),pady=(5,5))
	E8=Entry(window,width=100,bg="white")
	E8.grid(row=15,column=0,padx=(10,10),pady=(5,5))
	Button(window, text="Προσθήκη",width=100,command=lambda:Add_Supplier(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get())).grid(row=16,column=0,padx=(10,10),pady=(5,5))
	Button(window, text="Πίσω",width=100,command=click1_frame2).grid(row=17,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="* Τα πεδία ειναι υποχρεωτικά να συμπληρωθούν!!").grid(row=18,column=0,padx=(10,10),pady=(5,5))
	Label(window,text="Created by Tsakos Kostas").grid(row=19,column=0)


def Delete_Supplier(tree):#Delete Suppliers from db
	for selected_item in tree.selection():
		conn=psycopg2.connect("host='postgres-db' dbname='jewelery' user='postgres' password='kostas581994'")
		cursor=conn.cursor()
		query="DELETE FROM \"Supplier\" WHERE (\"Company\"='"+tree.set(selected_item,'#1')+"')"
		query_result=cursor.execute(query)
		conn.commit()
		conn.close()
		tree.delete(selected_item)
	click1_frame2_click4_frame3()

def click1_frame2_click4_frame3():
		clear()
		window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Διαγραφή Προμηθευτών")
		lst=run_query("SELECT * FROM \"Supplier\"")
		tree=ttk.Treeview(window,height=25,show=["headings"])
		tree["columns"]=("Εταιρεία","Όνομα","Επίθετο","Διεύθυνση","Σταθερό Τηλέφωνο","Κινητό","Τραπεζικός Λογαριασμός","Τραπεζικός Λογαριασμός2")
		tree.column("Εταιρεία",width=100)
		tree.column("Όνομα",width=100)
		tree.column("Επίθετο",width=100)
		tree.column("Διεύθυνση",width=100)
		tree.column("Σταθερό Τηλέφωνο",width=200)
		tree.column("Κινητό",width=100)
		tree.column("Τραπεζικός Λογαριασμός",width=200)
		tree.column("Τραπεζικός Λογαριασμός2",width=200)
		tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Company"))
		tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Name"))
		tree.heading("Επίθετο", text="Επίθετο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Surname"))
		tree.heading("Διεύθυνση", text="Διεύθυνση",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Address"))
		tree.heading("Σταθερό Τηλέφωνο", text="Σταθερό Τηλέφωνο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Phone"))
		tree.heading("Κινητό", text="Κινητό",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Mobile Phone"))
		tree.heading("Τραπεζικός Λογαριασμός", text="Τραπεζικός Λογαριασμός",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account"))
		tree.heading("Τραπεζικός Λογαριασμός2", text="Τραπεζικός Λογαριασμός2",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account2"))
		for i in lst:
			tree.insert("",END,values=i)
		tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Διαγραφή",width=100,command=lambda:Delete_Supplier(tree)).grid(row=1,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Πίσω",width=100,command=click1_frame2).grid(row=2,column=0,padx=(10,10),pady=(10,10))
		Label(window,text="Created by Tsakos Kostas").grid(row=3,column=0)

def click1_frame2_click1_frame3():
		clear()
		window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προβολή Προμηθευτών")
		lst=run_query("SELECT * FROM \"Supplier\"")
		tree=ttk.Treeview(window,height=25,show=["headings"])
		tree["columns"]=("Εταιρεία","Όνομα","Επίθετο","Διεύθυνση","Σταθερό Τηλέφωνο","Κινητό","Τραπεζικός Λογαριασμός","Τραπεζικός Λογαριασμός2")
		tree.column("Εταιρεία",width=100)
		tree.column("Όνομα",width=100)
		tree.column("Επίθετο",width=100)
		tree.column("Διεύθυνση",width=100)
		tree.column("Σταθερό Τηλέφωνο",width=200)
		tree.column("Κινητό",width=100)
		tree.column("Τραπεζικός Λογαριασμός",width=200)
		tree.column("Τραπεζικός Λογαριασμός2",width=200)
		tree.heading("Εταιρεία", text="Εταιρεία",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Company"))
		tree.heading("Όνομα", text="Όνομα",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Name"))
		tree.heading("Επίθετο", text="Επίθετο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Surname"))
		tree.heading("Διεύθυνση", text="Διεύθυνση",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Address"))
		tree.heading("Σταθερό Τηλέφωνο", text="Σταθερό Τηλέφωνο",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Phone"))
		tree.heading("Κινητό", text="Κινητό",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Mobile Phone"))
		tree.heading("Τραπεζικός Λογαριασμός", text="Τραπεζικός Λογαριασμός",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account"))
		tree.heading("Τραπεζικός Λογαριασμός2", text="Τραπεζικός Λογαριασμός2",command=lambda:Sorting_By_Column(tree,"SELECT * FROM \"Supplier\"","Bank Account2"))
		for i in lst:
			tree.insert("",END,values=i)
		tree.grid(row=0,column=0,padx=(10,10),pady=(10,10))
		Button(window, text="Πίσω",width=100,command=click1_frame2).grid(row=1,column=0,padx=(10,10),pady=(10,10))
		Label(window,text="Created by Tsakos Kostas").grid(row=2,column=0)

def click1_frame2():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Προμηθευτές")
	Button(window, text="Προβολή Προμηθευτών",width=100,command=click1_frame2_click1_frame3).grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Εισαγωγή Προμηθευτή",width=100,command=click1_frame2_click2_frame3).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Επεξεργασία Προμηθευτή",width=100,command=click1_frame2_click3_frame3).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Διαγραφή Προμηθευτή",width=100,command=click1_frame2_click4_frame3).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Πίσω",width=100,command=frame1).grid(row=4,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=5,column=0)

##################################  END OF SUPPLIERS OPERATIONS   #########################################################################################

def frame1():
	clear()
	window.title("Ψηφιακή Αποθήκη Κοσμηματοπωλείου-Αρχική Σελίδα")
	Button(window, text="Προμηθευτές",width=100,command=click1_frame2).grid(row=0,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Κατηγορίες Προϊόντων",width=100,command=click2_frame2).grid(row=1,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Προϊόντα Χρυσού",width=100,command=click3_frame2).grid(row=2,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Προϊόντα από Ασήμι ή Γενικού Τύπου",width=100,command=click4_frame2).grid(row=3,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο σε Χρυσό",width=100,command=click5_frame2).grid(row=4,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Συνολική Αξία σε Ασήμι και Γενικού Τύπου εμπορεύματα",width=100,command=click6_frame2).grid(row=5,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο σε Χρυσό ανά προμηθευτή",width=100,command=click7_frame2).grid(row=6,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Συνολική Αξία σε Ασήμι και Γενικού Τύπου εμπορεύματα ανά προμηθευτή",width=100,command=click8_frame2).grid(row=7,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Συνολική Αξία σε Ασήμι και Γενικού Τύπου εμπορεύματα ανά κατηγορία",width=100,command=click9_frame2).grid(row=8,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο τεμαχίων ανά κατηγορία Χρυσού",width=100,command=click10_frame2).grid(row=9,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο τεμαχίων ανά κατηγορία σε Ασήμι ή Γενικού Τύπου",width=100,command=click11_frame2).grid(row=10,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο τεμαχίων ανά κατηγορία Χρυσού ανά Προμηθευτή και ανά ποιότητα",width=100,command=click12_frame2).grid(row=11,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο τεμαχίων ανά κατηγορία Χρυσού ανά Προμηθευτή",width=100,command=click13_frame2).grid(row=12,column=0,padx=(10,10),pady=(10,10))
	Button(window, text="Σύνολο τεμαχίων ανά κατηγορία σε ασήμι ή Γενικού Τύπου ανά Προμηθευτή",width=100,command=click14_frame2).grid(row=13,column=0,padx=(10,10),pady=(10,10))
	Label(window,text="Created by Tsakos Kostas").grid(row=14,column=0)

frame1()

window.mainloop()
