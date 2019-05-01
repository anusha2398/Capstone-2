from models import *

def sign_up(name, email, contact, password):
	UsersAccount.create(name=name, email_id=email, contact=contact, password=password)


def sign_in(name, upassword):
	user_instance = UsersAccount.select().where(UsersAccount.name == name)

	x = ''

	for i in user_instance:
		x += i.password
		
	print(x)

	if x == None:
		return False
	elif x != upassword:
		return False
	else:
		return True

def service_type(ty2):
	Service.create(ty2=type_of_service)


def company_details(type, company, gstin):
	CompanyDetails.create(type=type_of_service, company=company_name, gstin=gstin)


def sales(name, amount):
	Sales.create(name=name, amount=amount)


def see_sales():
	sale = []
	for sale in Sales.select():
		purchase.append([sale.date, sale.name, sale.amount, sale.total_amount])
	return sale


def purchase(company, amount):
	Purchase.create(company=company_name, amount=amount)


def see_purchase():
	purchase = []
	for purchase in Purchase.select():
		purchase.append([purchase.date, purchase.types_of_goods, CompanyDetails.get(purchase.company_id).company_name, 
						  purchase.amount, purchase.total_amount])
	return purchase