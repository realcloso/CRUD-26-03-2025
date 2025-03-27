curl -X POST http://localhost:5000/produtos \
    -H "Content-Type: application/json" \
    -d '{"nome": "Teclado Mecânico",
         "fornecedor": "KeyTech",
         "endereco_fornecedor": "Avenida das Teclas, 202",
         "quantidade": 50,
         "endereco": "Depósito B",
         "preco_unitario": 450.00}'
