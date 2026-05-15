create table clientes(
# 1 cadastro dos clientes
	id int auto_increment primary key,
    nome varchar(100) not null,
    telefone varchar (20),
    endereco varchar(200)
);

select * from clientes;

create table pets(
# 2 cadastro pet
	id int auto_increment primary key,
    nome varchar(100) not null,
    tipo varchar(50), -- cachorro, gato, etc..
 	raca varchar(50),
    idade int,
    cliente_id int,
    foreign key (cliente_id) references clientes(id)
);

create table servicos(
# 3 cadastro dos tipos de serviços
	id int auto_increment primary key,
    nome varchar(100),
    descricao text,
    preco decimal(10,2)
);

create table pedidos(
# 4 onde solicitar pedidos
	id int auto_increment primary key,
    cliente_id int,
    pet_id int,
    data_pedido datetime default current_timestamp,
    status varchar(100), -- pendente, em andamento, concluído.
	descricao text,
    foreign key (cliente_id) references clientes(id),
    foreign key (pet_id) references pets(id)
);
    
create table pedido_servicos(
# 5 permita mais de um pedido
	ind int auto_increment primary key,
    pedido_id int,
    servico_id int,
    foreign key (pedido_id) references pedidos(id),
	foreign key (servico_id) references servicos(id)
);

insert into servicos (nome, descricao, preco) values
('Banho e tosa', 'Higienização completa do pet', 50.00),
('Consulta Veterinária', 'Avaliação médica', 120.00),
('Hospedagem pet', 'Estadia temporária', 80.00),
('Creche pet', 'Cuidados durante o dia', 60.00),
('Adestramento', 'Treinamento Comportamental', 150.00),
('Vacinação', 'Aplicação de vacinas', 90.00),
('Transporte pet', 'Transporte Especializado', 70.00),
('Spa pet', 'Tratamento relaxante', 100.00)
