curl -X PUT http://localhost:5000/produtos/5 \
    -H "Content-Type: application/json" \
    -d '{"nome": "Monitor 27\" 4K", 
         "fornecedor": "UltraScreen", 
         "endereco_fornecedor": "Rua das Telas, 789", 
         "quantidade": 45, 
         "endereco": "Depósito C", 
         "preco_unitario": 1850.00}'
