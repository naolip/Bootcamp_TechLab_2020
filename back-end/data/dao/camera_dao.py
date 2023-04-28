from data.database import session_factory
from data.model.camera_model import Cameras 

session = session_factory()


class Camera_dao():

    
    def create_camera(name):
        
        camera_create = Cameras(name)

        session.add(camera_create)
        session.commit()

        session.close()

        return camera_create


    def get_camera(id):

        camera_get = session.query(Cameras).filter(Cameras.id == id).first()
        session.close()

        return camera_get

    def delete_camera(id):

        camera_delete = session.query(Cameras).filter(Cameras.id == id).delete()
        session.commit()

        return camera_delete


    def update_camera(id, name):

        camera_update = session.query(Cameras).filter(Cameras.id == id).update({Cameras.name:(name)})
        session.commit()

        return camera_update