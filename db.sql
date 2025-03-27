CREATE DATABASE IF NOT EXISTS meu_banco;
USE meu_banco;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'senha';
FLUSH PRIVILEGES;


CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    fornecedor VARCHAR(255) NOT NULL,
    endereco_fornecedor VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    preco_unitario FLOAT NOT NULL
);

INSERT INTO produtos (nome, fornecedor, endereco_fornecedor, quantidade, endereco, preco_unitario) VALUES
('Notebook Ultrafino', 'TechNova', 'Avenida da Tecnologia, 500', 25, 'Depósito X', 4500.00),
('Headset Bluetooth', 'SoundMax', 'Rua do Áudio, 88', 75, 'Depósito Y', 320.00),
('Webcam Full HD', 'VisionTech', 'Travessa das Lentes, 212', 40, 'Depósito Z', 550.00),
('Mesa Digitalizadora', 'DesignPro', 'Rua dos Criadores, 404', 15, 'Depósito W', 890.00);


SELECT * FROM produtos;