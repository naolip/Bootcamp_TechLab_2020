from data.database import session_factory
from data.model.alert_model import Alerts

session = session_factory()

class Alert_dao():


    def create_alert(alert_name, alert_txt):
    
        alert_create = Alerts(name=alert_name, alert_text=alert_txt)


        session.add(alert_create)
        session.commit()

        session.close()

        return alert_create


    def get_alert(id):
        session = session_factory()

        alert_get = session.query(Alerts).filter(Alerts.id == id).first()
        session.close()

        return alert_get


    def delete_alert(id):
        session = session_factory()

        alert_delete = session.query(Alerts).filter(Alerts.id == id).delete()
        session.commit()

        return alert_delete


    def update_alert(id, name):
        session = session_factory()

        alert_update = session.query(Alerts).filter(Alerts.id == id).update({Alerts.name:(name)})
        session.commit()

        return alert_update