from data.database import session_factory
from data.model.sala_model import Salas

session = session_factory()

class Sala_dao():


    def create_sala(cam_name, max_al):
    
        sala_create = Salas(name=cam_name, max_allowed=max_al)


        session.add(sala_create)
        session.commit()

        session.close()

        return sala_create


    def get_sala(id):
    
        sala_get = session.query(Salas).filter(Salas.id == id).first()
        session.close()

        return sala_get


    def delete_sala(id):

        sala_delete = session.query(Salas).filter(Salas.id == id).delete()

        session.commit()

        return sala_delete


    def update_sala(id, name):

        sala_update = session.query(Salas).filter(Salas.id == id).update({Salas.name:(name)})
        session.commit()

        return sala_update