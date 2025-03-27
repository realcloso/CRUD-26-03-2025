#!/bin/bash

echo -e "\n=== Testando PUT /produtos/5 ==="
curl -X PUT http://localhost:5000/produtos/5 \
    -H "Content-Type: application/json" \
    -d '{
        "nome": "Monitor 27\" 4K",
        "fornecedor": "UltraScreen",
        "endereco_fornecedor": "Rua das Telas, 789",
        "quantidade": 45,
        "endereco": "Depósito C",
        "preco_unitario": 1850.00
    }'
echo -e "\n----------------------------------\n"

echo -e "\n=== Testando POST /produtos ==="
curl -X POST http://localhost:5000/produtos \
    -H "Content-Type: application/json" \
    -d '{
        "nome": "Teclado Mecânico",
        "fornecedor": "KeyTech",
        "endereco_fornecedor": "Avenida das Teclas, 202",
        "quantidade": 50,
        "endereco": "Depósito B",
        "preco_unitario": 450.00
    }'
echo -e "\n----------------------------------\n"

echo -e "\n=== Testando GET /produtos ==="
curl -X GET http://localhost:5000/produtos
echo -e "\n----------------------------------\n"

echo -e "\n=== Testando DELETE /produtos/3 ==="
curl -X DELETE http://localhost:5000/produtos/3
echo -e "\n----------------------------------\n"

echo "Testes finalizados!"