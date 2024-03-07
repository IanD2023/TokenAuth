from tokenbag.settings import DBSOCIN


class funcionarioPDV:

        def __init__(self,codigo):
                
                self.codigo=codigo

        def nome(self):

                DBSOCIN.reconnect()

                sql = DBSOCIN.cursor()

                try:

                        sql.execute(f"select nome from usuario_security where login={self.codigo}")

                        resultado = sql.fetchone()

                        nome=resultado[0]

                        return nome
        
                except:
                
                        return False