from sqlalchemy import create_engine
import sqlalchemy as db

class FabricaDeConexao:
    sgbd = "mysql+pymysql"
    user = "root"
    password = "admin"
    ip = "localhost"
    bdname = "livroteca"

    engine = db.create_engine(f"{sgbd}://{user}:{password}@{ip}/{bdname}")

    def getConexao(self):
        return self.engine