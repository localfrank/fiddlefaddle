'''Models'''
from datetime import datetime
from dashboard import db


class User(db.Model):
    '''User table'''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    api_user = db.Column(db.Boolean, default=False, nullable=False)
    bots = db.relationship('Bot', backref='account', lazy=True)

    def __repr__(self):
        return "User(public_id: {}, username: {}, email: {}, admin: {}, active: {}, api_user: {})".format(self.public_id, self.username, self.email, self.admin, self.active, self.api_user)


class Bot(db.Model):
    '''Bot feature table'''
    __tablename__ = 'bot'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    date_registered = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'user.public_id'), nullable=False)

    def __repr__(self):
        return "Bot({}, {}, {})".format(self.name, self.description, self.active)


# class Department(db.Model):
#     '''Departments'''
#     __table__ = 'department'
#     id = db.Column(db.Integer, primary_key=True)
#     department_id = db.Column(db.String(10), unique=True, nullable=False)
#     department_name = db.Column(db.String(20), unique=True, nullable=False)


# class Project(db.Model):
#     '''Project'''
#     __table__ = 'project'
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.String(10), unique=True, nullable=False)
#     project_name = db.Column(db.String(20), unique=True, nullable=False)
#     client = db.Column(db.String(120), nullable=False)
#     stage = db.Column(db.String(20), nullable=False)


# class Role(db.Model):
#     '''Role: Engagement manager, BA, developer etc'''
#     __table__ = 'role'
#     id = db.Column(db.Integer, primary_key=True)
#     role_id = db.Column(db.String(10), unique=True, nullable=False)
#     role_name = db.Column(db.String(20), unique=True, nullable=False)


# class Stage(db.Model):
#     '''Stage of the project: Interest, RPF, Ongoing ...'''
#     __table__ = 'stage'
#     id = db.Column(db.Integer, primary_key=True)
#     stage_id = db.Column(db.String(10), unique=True, nullable=False)
#     stage_name = db.Column(db.String(20), unique=True, nullable=False)


# class Client(db.Model):
#     '''Client table'''
#     __table__ = 'client'
#     id = db.Column(db.Integer, primary_key=True)
#     client_id = db.Column(db.String(10), unique=True, nullable=False)
#     client_name = db.Column(db.String(20), unique=True, nullable=False)
#     description = db.Column(db.Text, nullable=True)


# class Task(db.Model):
#     '''Task table: billable or non-billable'''
#     __table__ = 'task'
#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.String(10), unique=True, nullable=False)
#     task_name = db.Column(db.String(20), unique=True, nullable=False)


# class Expense_Approval_Status(db.Model):
#     ''' Expense approval status: Open, Not submitted, Received, Rejected, Approved etc'''
#     __table__ = 'expense_approval_status'
#     id = db.Column(db.Integer, primary_key=True)
#     status_id = db.Column(db.String(10), unique=True, nullable=False)
#     status_name = db.Column(db.String(20), unique=True, nullable=False)

# TODO
# class Expense(db.Model):
    '''Expense table: implement in mongo'''
    # __table__ = 'expense'
    # id = db.Column(db.Integer, primary_key=True)
    # date_created = db.Column(
    #     db.DateTime, default=datetime.utcnow, nullable=False)
    # expense_type = db.Column(db.String(10), nullable=False)
    # project = db.Column(db.String(20), nullable=False)
    # purpose = db.Column(db.String(20), nullable=False)
    # payment_method = db.Column(db.String(20), nullable=False)
    # currency = db.Column(db.String(10), nullable=False)
    # tax_type = db.Column(db.String(10), nullable=False)
    # net_amount = db.Column(db.Numeric(), nullable=False)
    # amount = db.Column(db.Numeric(), nullable=False)
    # description = db.Column(db.Text, nullable=True)

# TODO
# class Utilization(db.Model):
    '''Utilization: implement in mongo'''
    # __table__ = 'utilization'
    # id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.Date, nullable=False)
    # client = db.Column(db.String(20), nullable=False)
    # project = db.Column(db.String(20), nullable=False)
    # task = db.Column(db.String(20), nullable=False)
