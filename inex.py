from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senha',
    'database': 'meu_banco'
}

def create_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        with create_db_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
            return jsonify(produtos if produtos else {'message': 'Nenhum produto encontrado'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    
    if not all(k in dados for k in ('nome', 'fornecedor', 'endereco_fornecedor', 'quantidade', 'endereco', 'preco_unitario')):
        return jsonify({'error': 'Dados incompletos'}), 400
    
    try:
        with create_db_connection() as conn, conn.cursor() as cursor:
            query = '''
                INSERT INTO produtos (nome, fornecedor, endereco_fornecedor, quantidade, endereco, preco_unitario)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (
                dados['nome'], dados['fornecedor'], dados['endereco_fornecedor'],
                dados['quantidade'], dados['endereco'], dados['preco_unitario']
            ))
            conn.commit()
            return jsonify({'message': 'Produto cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    
    try:
        with create_db_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM produtos WHERE id = %s', (id,))
            produto_existente = cursor.fetchone()
            
            if not produto_existente:
                return jsonify({'error': 'Produto não encontrado'}), 404
            
            query = '''
                UPDATE produtos 
                SET nome = %s, fornecedor = %s, endereco_fornecedor = %s, quantidade = %s,
                    endereco = %s, preco_unitario = %s
                WHERE id = %s
            '''
            valores = (
                dados.get('nome', produto_existente['nome']),
                dados.get('fornecedor', produto_existente['fornecedor']),
                dados.get('endereco_fornecedor', produto_existente['endereco_fornecedor']),
                dados.get('quantidade', produto_existente['quantidade']),
                dados.get('endereco', produto_existente['endereco']),
                dados.get('preco_unitario', produto_existente['preco_unitario']),
                id
            )
            cursor.execute(query, valores)
            conn.commit()
            return jsonify({'message': 'Produto atualizado com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover_produto(id):
    try:
        with create_db_connection() as conn, conn.cursor() as cursor:
            cursor.execute('SELECT 1 FROM produtos WHERE id = %s', (id,))
            if not cursor.fetchone():
                return jsonify({'error': 'Produto não encontrado'}), 404
            
            cursor.execute('DELETE FROM produtos WHERE id = %s', (id,))
            conn.commit()
            return jsonify({'message': 'Produto removido com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.errorhandler(404)
def nao_encontrado(error):
    return jsonify({'error': 'Recurso não encontrado'}), 404

@app.errorhandler(405)
def metodo_nao_permitido(error):
    return jsonify({'error': 'Método não permitido'}), 405

@app.errorhandler(501)
def nao_implementado(error):
    return jsonify({'error': 'Funcionalidade não implementada'}), 501

@app.errorhandler(502)
def erro_externo(error):
    return jsonify({'error': 'Erro externo'}), 502

if __name__ == '__main__':
    app.run(debug=True)
