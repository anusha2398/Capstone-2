import peewee as pw

db = pw.SqliteDatabase('e-gst_app.db')


class UsersAccount(pw.Model):
	name = pw.TextField()
	email_id = pw.TextField()
	contact = pw.TextField()
	password = pw.TextField()

	class Meta:
		database = db


class Service(pw.Model):
	ty2 = pw.TextField()

	class Meta:
		database = db


class CompanyDetails(pw.Model):
	type_of_service = pw.TextField()
	company_name = pw.TextField()
	gstin = pw.TextField()

	class Meta:
		database = db


class Sales(pw.Model):
	name = pw.TextField()
	amount = pw.TextField()

	class Meta:
		database = db


class Purchase(pw.Model):
	company_name = pw.TextField(CompanyDetails)
	amount = pw.TextField()

	class Meta:
		database = db

db.connect()
db.create_tables([UsersAccount, Service, CompanyDetails, Sales, Purchase])