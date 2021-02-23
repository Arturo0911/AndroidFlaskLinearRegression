from app import app
from app import db

from app.helpers.check_passwords import confirm_password
from app.database.models import Employee




def login_resolve_process(username, password):
    employee_resolve = Employee.query.filter_by(username = username).first()
    print(employee_resolve)
    try:

        if employee_resolve is not None:
            if  confirm_password(password, employee_resolve.password):
                
                return employee_resolve
            else:

                return "Clave errónea"
        else:
            return "Usuario no encontrado"
    except Exception as e:

        return str(e)
