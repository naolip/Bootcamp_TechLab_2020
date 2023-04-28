from data.database import session_factory
from data.model.usuario_model import Usuarios

session = session_factory()

class User_dao():
    
    
    def create_usr(usr_name, usr_t):

        usr_create = Usuarios(name=usr_name, usr_type=usr_t)

        session.add(usr_create)
        session.commit()

        session.close()

        return usr_create


    def get_usr(id):

        usr_get = session.query(Usuarios).filter(Usuarios.id == id).first()
        session.close()

        return usr_get


    def delete_usr(id):

        usr_delete = session.query(Usuarios).filter(Usuarios.id == id).delete()
        session.commit()

        return usr_delete


    def update_usr(id, name):
        usr_update = session.query(Usuarios).filter(Usuarios.id == id).update({Usuarios.name:(name)})
        session.commit()

        return usr_update