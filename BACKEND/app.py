from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Solicitacao

app = Flask(__name__)
CORS(app)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/solicitacoes', methods=['POST'])
def criar_solicitacao():
    dados = request.json
    try:
        nova_solicitacao = Solicitacao(
            nome_cliente=dados['nome_cliente'],
            nome_pet=dados['nome_pet'],
            tipo_servico=dados['tipo_servico'],
            descricao=dados.get('descricao', ''),
            status='Aberto'  # Todo pedido começa como 'Aberto'
        )
        
        db.session.add(nova_solicitacao)
        db.session.commit()
        
        # Retorna o ID para o cliente guardar-
        return jsonify({"id": str(nova_solicitacao.id)}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/api/solicitacoes', methods=['GET'])
def listar_solicitacoes():
    busca = request.args.get('busca', '').lower()
    
    query = Solicitacao.query
    if busca:
        query = query.filter(
            (Solicitacao.nome_cliente.ilike(f'%{busca}%')) |
            (Solicitacao.nome_pet.ilike(f'%{busca}%')) |
            (Solicitacao.tipo_servico.ilike(f'%{busca}%'))
        )
    
    lista = query.order_by(Solicitacao.criado_em.desc()).all()
    return jsonify([s.to_dict() for s in lista]), 200

@app.route('/api/solicitacoes/<int:id>/status', methods=['PATCH'])
def atualizar_status(id):
    dados = request.json
    novo_status = dados.get('status')
    
    solicitacao = Solicitacao.query.get(id)
    if not solicitacao:
        return jsonify({"erro": "Pedido não encontrado"}), 404
        
    try:
        solicitacao.status = novo_status
        db.session.commit()
        return jsonify({"mensagem": "Status atualizado"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/api/solicitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):
    solicitacao = Solicitacao.query.get(id)
    if not solicitacao:
        return jsonify({"erro": "Pedido não encontrado"}), 404
        
    try:
        db.session.delete(solicitacao)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)