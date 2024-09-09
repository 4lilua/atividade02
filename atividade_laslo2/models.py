from database import db

class Usuario(db.Model):
    __tablename__= "usuario"
    id_cliente = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.Integer)

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def __repr__(self):
        return "<Usuario {}>.format(self.nome)"