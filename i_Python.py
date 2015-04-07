import Tkinter
import sqlite3
import ttk

conn = sqlite3.connect('medha.db')
c= conn.cursor()

def put(*args):
	try:
		e_name = str(i_name.get())
		e_pay = int(i_pay.get())
#	conn = sqlite3.connect('medha.db')
#	c = conn.cursor()
		c.execute('create table if not exists employee(id integer primary key autoincrement, name text, salary integer)')
		print e_name
		print type(e_name)
		print e_pay
		print type(e_pay)
		c.execute('insert into employee(name, salary) values(?,?)',(e_name,e_pay))
#	conn.close()
		notice.set('insertion successful')
		sel_list()
		i_name.delete(0,'end')
		i_pay.delete(0,'end')
	except:
		notice.set('insert proper values')
		i_name.set('')
		i_pay.set('')

def del_id(*args):
	try:
		e_id = int(d_del.get())
#		conn = sqlite3.connect('medha.db')
#		c = conn.cursor()
		print e_id
		print type(e_id)
		c.execute('delete from employee where id =?',(e_id,))
		notice.set('deleted successfully')
#		conn.close()
		sel_list()
		d_del.set('')
	except:
		notice.set('insert proper values')
		d_del.set('')

def del_name(*args):
	try:
		e_name = str(d_del.get())
#		conn = sqlite3.connect('medha.db')
#		c = conn.cursor()
		c.execute('delete from employee where name = ?',(e_name,))
		print e_name
		print type(e_name)
		notice.set('deleted successfully')
#		conn.close()
		sel_list()
		d_del.set('')
	except:
		notice.set('insert proper values')
		d_del.set('')


def ser_name(*args):
	try:
		e_name = str(s_ser.get())
#		conn = sqlite3.connect('medha.db')
#		c = conn.cursor()
		c.execute('select * from employee where name = ?',(e_name,))
		print e_name
		print type(e_name)
		notice.set('query successful')
#		conn.close()
		re = c.fetchall()
		count = len(re)
		l1.delete(0,'end')
		l2.delete(0,'end')
		l3.delete(0,'end')
		print re
		cur = 0
		for i in re:
			l1.insert(cur,i[0])
			l2.insert(cur,i[1])
			l3.insert(cur,i[2])
			cur = cur+1
		s_ser.set('')
	except:
		notice.set('entered Name not found')
		s_ser.set('')


def ser_id(*args):
	try:
		e_id = int(s_ser.get())
#		conn = sqlite3.connect('medha.db')
#		c = conn.cursor()
		c.execute('select * from employee where id = ?',(e_id,))
		print e_id
		print type(e_id)
		notice.set('query successful')
#		conn.close()
		re = c.fetchall()
		count = len(re)
		l1.delete(0,'end')
		l2.delete(0,'end')
		l3.delete(0,'end')
		print re
		cur = 0
		for i in re:
			l1.insert(cur,i[0])
			l2.insert(cur,i[1])
			l3.insert(cur,i[2])
			cur = cur+1
		s_ser.set('')
	except:
		notice.set('entered ID not found')
		s_ser.set('')

def sel_list():
	lli = []
	ll2 = []
	ll3 = []
#	conn = sqlite3.connect('medha.db')
#	c = conn.cursor()
	c.execute('select * from employee')
	re = c.fetchall()
	count = len(re)
	l1.delete(0,'end')
	l2.delete(0,'end')
	l3.delete(0,'end')
	print re
	cur = 0
	for i in re:
		l1.insert(cur,i[0])
		l2.insert(cur,i[1])
		l3.insert(cur,i[2])
		cur = cur+1
	
#	conn.close()
root = Tkinter.Tk()
root.title('Python Projet - gui and db')

mainframe = ttk.Frame(root,padding='3 3 12 12' )
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight =1)

i_name = Tkinter.StringVar()
i_id = Tkinter.StringVar()
i_pay = Tkinter.StringVar()
notice = Tkinter.StringVar()
d_del = Tkinter.StringVar()
s_ser = Tkinter.StringVar()

i_name_entry = ttk.Entry(mainframe, width =7, textvariable = i_name)
i_name_entry.grid(column = 1, row = 1, sticky = 'nw')

i_pay_entry = ttk.Entry(mainframe, width =7, textvariable = i_pay)
i_pay_entry.grid(column = 3, row = 1, sticky = 'nw')

i_del_entry = ttk.Entry(mainframe, width =7, textvariable = d_del)
i_del_entry.grid(column = 1, row =4, sticky = 'nw')

i_ser_entry = ttk.Entry(mainframe, width =7, textvariable = s_ser)
i_ser_entry.grid(column = 1, row =7, sticky = 'nw')

ttk.Label(mainframe, text ='Name of Employee').grid(column = 1, row = 0, sticky = 'nw')
ttk.Label(mainframe, text ='Name/ID of Employee to SEARCH').grid(column = 1, row = 6, sticky = 'nw')
ttk.Label(mainframe, text ='Employee Pay').grid(column = 3, row =0, sticky = 'nw')
ttk.Label(mainframe, text ='Employee Pay').grid(column = 3, row=10, sticky = 'new')
ttk.Label(mainframe, text ='Employee ID').grid(column = 1, row=10, sticky = 'nw')
ttk.Label(mainframe, text ='Employee Name').grid(column = 2, row=10,sticky = 'nw')
ttk.Label(mainframe, text ='Name/ID of Employee to delete').grid(column = 1, row=3, sticky= 'nw')
ttk.Label(mainframe, textvariable = notice).grid(column = 1, row = 9, sticky = 'nw')

ttk.Button(mainframe, text='Insert', command = put).grid(column=3, row=2, sticky='nw')
ttk.Button(mainframe, text='Delete By ID', command = del_id).grid(column =3, row = 4, sticky = 'nw')
ttk.Button(mainframe, text='Delete By Name', command = del_name).grid(column = 3, row=5, sticky = 'nw')
ttk.Button(mainframe, text='Search By ID', command = ser_id).grid(column =3, row = 7, sticky = 'nw')
ttk.Button(mainframe, text='Search By Name', command = ser_name).grid(column = 3, row=8, sticky = 'nw')

l1 = Tkinter.Listbox(mainframe, height=3)
l1.grid(column=1, row=11, sticky = 'nw')
l2 = Tkinter.Listbox(mainframe, height=3)
l3 = Tkinter.Listbox(mainframe, height=3)
l2.grid(column=2, row=11, sticky ='nw')
l3.grid(column=3, row=11, sticky = 'nw')
#s1 = ttk.Scrollbar(mainframe,  command=l1.yview)
#s2 = ttk.Scrollbar(mainframe,  command=l2.yview)
#s3 = ttk.Scrollbar(mainframe,  command=l3.yview)
#s1.grid(column=2, row=9)
#s2.grid(column=4, row=9)
#s3.grid(column=6, row=9)
#l1['yscrollcommand'] = s1.set
#l2['yscrollcommand'] = s2.set
#l3['yscrollcommand'] = s3.set
ttk.Sizegrip().grid(column=999, row=999, sticky='se' )
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(1, weight =1)


for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
i_name_entry.focus()

root.mainloop()
