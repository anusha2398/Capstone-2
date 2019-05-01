from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from PIL import Image, ImageTk

#from views import service_type, company_details, add_sales, see_sales, add_purchase, see_purchase
from views import *

#assigning font 
LARGE_FONT=("Times New Roman",24)
MED_FONT=("Times New Roman",18)



class Project(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)
		Tk.configure(self)
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("750x480")
		self.show_frame(Main)


	def show_frame(self, cont):
		frame=cont(parent=self.container, controller=self)
		frame.grid(row=0,column=0,sticky="nsew")
		frame.tkraise()


class Main(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		"""
		Executed by interpreter to create an instance of this class.
		Attributes:
			self.parent
			self.controller
		"""

		heading_label = Label(self, text="e-GST", font=LARGE_FONT)
		sign_up_btn = Button(self, text='Sign Up', command=lambda:controller.show_frame(SignUp))
		login_btn = Button(self, text='Log In', command=lambda:controller.show_frame(LogIn))

		"""
		grid lines for the label and buttons
		"""
		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		sign_up_btn.grid(row=5, column=3, padx=120, pady=100)
		login_btn.grid(row=5, column=5, padx=120, pady=100)


class Main2(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		"""
		Executed by interpreter to create an instance of this class.
		Attributes:
			self.parent
			self.controller
		"""
		heading_label = Label(self, text="Choose an option", font=LARGE_FONT)
		service_type_btn = Button(self, text='Service Type', command=lambda:controller.show_frame(ServiceType))
		company_details_btn = Button(self, text='Company Details', command=lambda:controller.show_frame(CompanyDetails))
		add_sales_btn = Button(self, text='Add Sales', command=lambda:controller.show_frame(AddSales))
		see_sales_btn = Button(self, text='See Sales', command=lambda:controller.show_frame(SeeSales))
		add_purchase_btn = Button(self, text='Add Purchase', command=lambda:controller.show_frame(AddPurchase))
		see_purchase_btn = Button(self, text='See Purchase', command=lambda:controller.show_frame(SeePurchase))
		log_out_btn = Button(self, text="Logout", command=lambda:controller.show_frame(Main))


		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		service_type_btn.grid(row=4, column=4, padx=80, pady=10)
		company_details_btn.grid(row=4, column=5, padx=80, pady=10)
		add_sales_btn.grid(row=4, column=6, padx=80, pady=10)
		see_sales_btn.grid(row=6, column=4, padx=80, pady=10)
		add_purchase_btn.grid(row=6, column=5, padx=80, pady=10)
		see_purchase_btn.grid(row=6, column=6, padx=80, pady=10)
		log_out_btn.grid(row=9, column=5, padx=120, pady=10)


class SignUp(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Sign Up", font=LARGE_FONT)
		name = Label(self, text="Name:")
		email_id = Label(self, text="Email Id:")
		contact_number = Label(self, text="Contact Number:")
		password = Label(self, text="Password:")

		"""
		to enter text box
		"""

		self.project_name = Text(self, height=1, width=30)
		self.email_id = Text(self, height=1, width=30)
		self.contact_number = Text(self, height=1, width=30)
		self.password = Text(self, height=1, width=30)

		self.sign_up_btn = Button(self, text="Sign Up", command=self.sign_up_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main))

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		name.grid(row=5, column=3, padx=120, pady=20)
		email_id.grid(row=6, column=3, padx=120, pady=20)
		contact_number.grid(row=7, column=3, padx=120, pady=20)
		password.grid(row=8, column=3, padx=120, pady=20)

		self.sign_up_btn.grid(row=10, column=3, padx=50, pady=50)
		self.back_btn.grid(row=10, column=4, padx=50, pady=50)

		self.project_name.grid(row=5, column=4, padx=50, pady=20)
		self.email_id.grid(row=6, column=4, padx=50, pady=20)
		self.contact_number.grid(row=7, column=4, padx=50, pady=20)
		self.password.grid(row=8, column=4, padx=50, pady=20)

		"""
		to show pop-up message in case of any error
		"""
			
	def sign_up_function(self):
		if len(self.project_name.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Name')

		elif len(self.email_id.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Email Id')

		elif len(self.contact_number.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Contact Number')

		elif len(self.password.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Password')

		else:
			name=self.project_name.get("1.0", "end-1c")
			email_id=self.email_id.get("1.0", "end-1c")
			contact_number=self.contact_number.get("1.0", "end-1c")
			password=self.password.get("1.0", "end-1c")
			sign_up(name=name, email=email_id, contact=contact_number, password=password)
			self.controller.show_frame(Main)

"""
to login using the sign up details
"""

class LogIn(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Log In", font=LARGE_FONT)
		name = Label(self, text="Name:")
		password = Label(self, text="Password:")

		"""
		to create text box
		"""

		self.project_name = Text(self, height=1, width=30)
		self.password = Text(self, height=1, width=30)

		self.login_btn = Button(self, text="Log In", command=self.log_in_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main))

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		name.grid(row=5, column=3, padx=120, pady=20)
		password.grid(row=6, column=3, padx=120, pady=20)

		self.project_name.grid(row=5, column=4, padx=50, pady=20)
		self.password.grid(row=6, column=4, padx=50, pady=20)

		self.login_btn.grid(row=8, column=3, padx=50, pady=50)
		self.back_btn.grid(row=8, column=4, padx=10, pady=50)

		"""
		to show a pop up in case of wrong name or password
		"""

	def log_in_function(self):
		if len(self.project_name.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Enter User Name")
		elif len(self.password.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Enter password")
		else:
			name=self.project_name.get("1.0", "end-1c")
			password = self.password.get("1.0", "end-1c")
			state = sign_in(name=name, upassword=password)

			if state:
				print("Inside condition")
				self.controller.show_frame(Main2)
			else:
				self.popup = messagebox.showwarning("Warning!", "Password or Username is wrong.")

	
class ServiceType(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller


		heading_label = Label(self, text="Service Type", font=LARGE_FONT)
		type1 = Label(self, text="Type:")

		"""
		to create text box
		"""
		self.type1 = Text(self, height=1, width=30)


		self.save_btn = Button(self, text="Save", command=self.service_type_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main2))


		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		type1.grid(row=5, column=3, padx=120, pady=20)


		self.save_btn.grid(row=9, column=3, padx=120, pady=20)
		self.back_btn.grid(row=9, column=4, padx=10, pady=20)

		self.type1.grid(row=5, column=4, padx=50, pady=20)

		"""
		to show a pop up in case of wrong service
		"""

	def service_type_function(self):
		if len(self.ty2.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Incorrect service")
		else:
			ty2 = self.type1.get("1.0", "end-1c")
			service_type(type1=ty2)
			self.controller.show_frame(Main2)


class CompanyDetails(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Company Details", font=LARGE_FONT)
		company_name = Label(self, text="Company Name:")
		gstin = Label(self, text="GST Number:")

		"""
		to create text box
		"""

		self.company_name = Text(self, height=1, width=30)
		self.gstin = Text(self, height=1, width=30)

		heading_label.grid(row=3, column=3, padx=100, pady=20, columnspan=3)
		company_name.grid(row=4, column=5, padx=100, pady=50)
		gstin.grid(row=5, column=5,padx=120, pady=50)

		self.company_name.grid(row=4, column=6, padx=40, pady=10)
		self.gstin.grid(row=5, column=6, padx=40, pady=10)

		self.save_btn = Button(self, text="Save", command=self.company_detail_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main2))

		self.save_btn.grid(row=7, column=5, padx=50, pady=20)
		self.back_btn.grid(row=7, column=6, padx=10, pady=50)


		"""
		to show pop up in case of wrong company name and GST number
		"""

	def company_detail_function():
		if len(self.company_name.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Incorrect name")
		elif len(self.gstin.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Incorrect number")
		else:
			name1 = self.company_name.get("1.0", "end-1c")
			gst = self.gstin.get("1.0", "end-1c")
			company_details(company_name=name1, gstin=gst)
			self.controller.show_frame(Main2)


class AddSales(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Add Sales", font=LARGE_FONT)
		name = Label(self, text="Name:")
		amount = Label(self, text="Amount:")

		"""
		to create text box
		"""
		
		self.project_name = Text(self, height=1, width=30)
		self.amount = Text(self, height=1, width=30)

		self.save_btn = Button(self, text="Save", command=self.add_sale_function)
		self.add_btn = Button(self, text="Add", command=self.add_sale_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main2))	

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		name.grid(row=5, column=3, padx=120, pady=20)
		amount.grid(row=6, column=3, padx=120, pady=20)

		self.project_name.grid(row=5, column=4, padx=50, pady=20)
		self.amount.grid(row=6, column=4, padx=50, pady=20)

		self.save_btn.grid(row=8, column=3, padx=10, pady=20)
		self.back_btn.grid(row=8, column=4, padx=10, pady=20)
		self.add_btn.grid(row=8, column=5, padx=10, pady=20)

		"""
		to show a pop up message 
		"""

	def add_sale_function():
		if len(self.name.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Incorrect name")
		elif len(self.gstin.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Incorrect number")
		else:
			name1 = self.company_name.get("1.0", "end-1c")
			amount1 = self.amount.get("1.0", "end-1c")
			sales(name=name1, amount=amount1)
			self.controller.show_frame(Main2)


class SeeSales(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="See Sales", font=LARGE_FONT)

		"""
		to create a table
		"""

		sales_tree=Treeview( self, columns=('#1','#2','#3','#4','#5'))

		"""
		to create headings in a table
		"""
		sales_tree.heading('#1',text='Sl No.')
		sales_tree.heading('#2',text='Date')
		sales_tree.heading('#3',text='Name')
		sales_tree.heading('#4',text='Amount')
		sales_tree.heading('#5',text='Total Amount')
		
		"""
		to create columns
		"""
		sales_tree.column('#1',stretch=YES,anchor=CENTER)
		sales_tree.column('#2',stretch=YES,anchor=CENTER)
		sales_tree.column('#3',stretch=YES,anchor=CENTER)
		sales_tree.column('#4',stretch=YES,anchor=CENTER)
		sales_tree.column('#5',stretch=YES,anchor=CENTER)

		sales_tree.grid(row=4, column=5, padx=2, pady=10, columnspan=2, sticky='nsew')
		sales_tree['show']='headings'

		sales_list = see_sales()

		for sales in sales_list:
			sales_tree.insert("",'end',values=sales)

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main2))
		back_btn.grid(row=18, column=5, padx=10, pady=20)


class AddPurchase(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Add Purchase", font=LARGE_FONT)
		company_name = Label(self, text="Company Name:")
		amount = Label(self, text="Amount:")

		"""
		to create text box
		"""
		
		self.company_name = Text(self, height=1, width=30)
		self.amount = Text(self, height=1, width=30)


		self.save_btn = Button(self, text="Save", command=self.add_purchase_function)
		self.add_btn = Button(self, text="Add", command=self.add_purchase_function)
		self.back_btn = Button(self, text="Back", command=lambda:controller.show_frame(Main2))

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)
		company_name.grid(row=5, column=3, padx=120, pady=20)
		amount.grid(row=6, column=3, padx=120, pady=20)
		
		self.company_name.grid(row=5, column=4, padx=50, pady=20)
		self.amount.grid(row=6, column=4, padx=50, pady=20)


		self.save_btn.grid(row=8, column=3, padx=10, pady=20)
		self.back_btn.grid(row=8, column=4, padx=10, pady=20)
		self.add_btn.grid(row=8, column=5, padx=10, pady=20)

		"""
		to show a pop up in case of error
		"""

	def add_purchase_function():
		if len(self.company_name.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Enter Company name")
		elif len(self.amount.get("1.0", "end-1c")) == 0:
			self.popup = messagebox.showwarning("Warning!", "Enter amount")
		else:
			name1 = self.company_name.get("1.0", "end-1c")
			amount1 = self.amount.get("1.0", "end-1c")
			purchase(name=name1, amount=amount1)
			self.controller.show_frame(Main2)				


class SeePurchase(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller

		heading_label = Label(self, text="See Sales", font=LARGE_FONT)

		"""
		to create a table
		"""

		purchase_tree=Treeview( self, columns=('#1','#2','#3','#4','#5','#6'))

		purchase_tree.heading('#1',text='Sl No.')
		purchase_tree.heading('#2',text='Date')
		purchase_tree.heading('#3',text='Types of goods')
		purchase_tree.heading('#4',text='Type of company')
		purchase_tree.heading('#5',text='Amount')
		purchase_tree.heading('#6',text='Total Amount')
		

		purchase_tree.column('#1',stretch=YES,anchor=CENTER)
		purchase_tree.column('#2',stretch=YES,anchor=CENTER)
		purchase_tree.column('#3',stretch=YES,anchor=CENTER)
		purchase_tree.column('#4',stretch=YES,anchor=CENTER)
		purchase_tree.column('#5',stretch=YES,anchor=CENTER)
		purchase_tree.column('#5',stretch=YES,anchor=CENTER)

		purchase_tree.grid(row=4, column=5, padx=2, pady=10, columnspan=2, sticky='nsew')
		purchase_tree['show']='headings'

		purchase_list = see_purchase()

		for purchase in purchase_list:
			purchase_tree.insert("",'end',values=purchase)

		heading_label.grid(row=3, column=3, padx=120, pady=20, columnspan=3)

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main2))
		back_btn.grid(row=18, column=5, padx=10, pady=20)

app = Project()
app.mainloop()