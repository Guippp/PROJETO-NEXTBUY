from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Solicitacao(db.Model):
    __tablename__ = 'solicitacao'
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    nome_pet = db.Column(db.String(100), nullable=False)
    tipo_servico = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    status = db.Column(db.String(50), default='Aberto')