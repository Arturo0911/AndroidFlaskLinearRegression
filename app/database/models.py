from app import db


# define the models to be inserted inserted into MySQL

class Department(db.Model):

    __tablename__ = 'Department'
    department_id = db.Column(db.Integer, primary_key= True)
    department_name = db.Column(db.String(100), index= True)



class Employee(db.Model):

    __tablename__ = 'Employee'
    employee_id = db.Column(db.Integer, primary_key= True)
    credentials = db.Column(db.String(100), index= True, unique=True,nullable=False)
    names = db.Column(db.String(100), index= True,nullable=False)
    last_names = db.Column(db.String(100), index= True,nullable=False)
    phone_number = db.Column(db.String(100), index= True,nullable=False)
    email_address = db.Column(db.String(100), index= True,nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('Department.department_id'))
    department_name = db.Column(db.String(100), index= True,nullable= False)
    username = db.Column(db.String(100), index= True,nullable=False)
    password = db.Column(db.String(100), index= True,nullable=False)

    def __repr__(self) -> str:
        return '<Employee {} {} {} {}>'.format(self.id, self.credentials, self.names, self.last_names)
    



class Product(db.Model):

    __tablename__ = 'Product'
    prouct_id = db.Column(db.Integer, primary_key= True)
    product_name = db.Column(db.String(100), index= True,nullable=False)

class Sales(db.Model):
    

    __tablename__ = 'Sales'
    sales_id = db.Column(db.Integer, primary_key= True)
    products_id = db.Column(db.Integer, db.ForeignKey('Product.prouct_id'))
    product_name = db.Column(db.String(100), index= True,nullable=False)
    time_start = db.Column(db.DateTime,nullable=False)
    time_end = db.Column(db.DateTime,nullable=False)
    profit = db.Column(db.Float,nullable=False)
    losses = db.Column(db.Float,nullable=False)


db.create_all()