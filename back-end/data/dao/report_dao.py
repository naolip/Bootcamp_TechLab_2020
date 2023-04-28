from data.database import session_factory
from data.model.report_model import Reports

session = session_factory()


class Report_dao():


    def create_report(report_name, report_txt):

        report_create = Reports(name=report_name, report_text=report_txt)

        session.add(report_create)
        session.commit()

        session.close()

        return report_create


    def get_report(id):

        report_get = session.query(Reports).filter(Reports.id == id).first()
        session.close()

        return report_get


    def delete_report(id):

        report_delete = session.query(Reports).filter(Reports.id == id).delete()
        session.commit()

        return report_delete


    def update_report(id, name):

        report_update = session.query(Reports).filter(Reports.id == id).update({Reports.name : (name)})
        session.commit()

        return report_update