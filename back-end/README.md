## Seção Dedicada às Camadas de Back-end



#### Requerimentos:

* sqlalchemy
* tornado
* pymysql
* cryptography
* opencv-contrib-python



## Camadas 



#### ORM - Banco de Dados OO 

Banco de dados orientado a objeto e desenvolvido com a biblioteca SQLAlchemy em conjunto com mySQL e PhpMyAdmin.

##### Pastas & Arquivo

  * data 
  * database.py
  * model
  * dao



###### database.py 

Realiza a criação das tabelas modeladas na camada "model" e a conecta com o Banco de Dados desejado.

`engine=create_engine('mysql(DB)+pymysql(interface)://root(Usr):12345678(senha)@localhost:50050(Porta;IP/cybertech(NomeBanco)', *echo*=True(Comentarios de Saída/Opcional))`



###### model 

Responsável pela modelagem das tabelas:

	* alert
	* camera 
	* frame
	* report
	* sala
	* usuario



###### dao

Camada responsável pela manipulação dos dados do DB. Cada tabela criada em "model" tem seu respectivo "dao".

 

INSERT / DELETE / UPDATE /  SELECT 



#### API 

Desenvolvida com o uso de Python Tornado, a camada de API faz as requisições, POST e GET ao DB, além da conexão com a Aplicação (IA) e com o Front-end (Node/Vue.js). 

 

##### Pasta

###### service  

Camada responsável por todas as requisições POST e GET, além de fazer interface entre Aplicação, DB, e Front. 

Cada serviço tem seu documento e suas dependências. ~ Ex. alert_service.py necessita do alert_dao ~



#### Application 

Camada responsável pela aplicação, onde estão os scripts da IA e suas dependências (necessário Docker, OpenCV, TensorFlow e modelos de predição pré-treinados).
