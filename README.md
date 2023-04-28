## SafePlace 

###### by CyberTech
###### Bootcamp de desenvolvimento de Software do Inteli - Instituto de Tecnologia e Liderança, de Setembro a Novembro de 2020. Ao todo foram 11 semanas, 56 aulas, 336 horas de dedicação e 6 professores. Trabalhei em grupos de 6 alunos para desenvolver uma solução de controle de aglomeração em espaços de trabalho compartilhados através da inteligência artificial - um projeto open source e encomendado pela empresa Exame junto ao banco BTG Pactual.

#### Uma solução Open Source criada no bootcamp desenvolvimento TechLab 

Visando facilitar e tornar mais segura a jornada de trabalho em tempos de pandêmia a solução faz uso das bibliotecas TensorFlow e OpenCV para desenvolver uma I.A. capaz de realizar a detecção de pessoas, do uso correto de mascaras de proteção além de checar o distânciamento entre pessoas de um mesmo ambiente.



### Tecnologias Empregadas



* Front-end
  *  Vue.js 
     * CoreUI
     * Node.js  - Integração API 



*    Back-end 
     * API 
       * Python Tornado 



* Application 
  * OpenCV 
    * Haar Cascade
  * TensorFlow 
    * Caffee



*  Data Base 
   * ORM 
     * SQLalchemy





## Requisitos



* Docker
* Docker-Compose 



## Como Rodar 

##### Clonar repositório 

Clone o repositório principal para a sua maquina com o seguinte comando: 

```
git clone https://github.com/Bootcamp-TechLab/grupo3-rep 
```

##### Criar arquivo YML 

Criar aquivo  __docker-compose.yml__  com o seguinte conteúdo: 



```
mysql:
 image: mysql
 cap_add:
   - SYS_NICE
 restart: always
 ports:
   - '50050:3306' 
 command: mysqld --lower_case_table_names=1
 environment:
   MYSQL_ROOT_PASSWORD: "12345678"

phpmyadmin:
 image: phpmyadmin/phpmyadmin
 restart: always
 links:
   - mysql:mysql
 environment:
   PMA_HOST: mysql
   PMA_PORT: 3306
   PMA_ARBITRARY: 1
 ports:
   - '50060:80'

deepo:
  image: ufoym/deepo
  ports:
    - '8899:8888'
    - '7000:8000'
  volumes:
    - /home/Documents/docker/volumes/deepo(CAMINHO PARA PASTA DOCKER DEEPO):/home
  command: jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token=NOME --notebook-dir='/home'
  # devices:
  #  - /dev/video0/:dev/video0
  # docker exec -it docker_deepo_1 bin/bash
  #  docker run -p 7000:8000 -it -v `pwd`/deepo/:/home --ipc=host ufoym/deepo bash
  #  docker run -it -v `pwd`/deepo/:/home --ipc=host ufoym/deepo bash

node:
    image: "node:10"
    user: "node"
    working_dir: /home/node/app
    environment:
      - NODE_ENV=development
    volumes:
      - .../grupo3-rep/front-end(CAMINHO PARA PASTA FRONT-END):/home/node/app

    ports:
      - '8080:8080'
    command: bash -c "npm install -S axios && npm install && npm run serve"

```

 

#### Instalar DOCKER e DOCKER-COMPOSE 

Para executar o arquivo __docer-compose.yml__ é necessário a instalação dos softwares docker e docker-compose.

##### Linux Debian e derivados -  Rode o seguinte comando no terminal:

###### docker 

```
sudo apt-get install docker 
```

###### docker-compose 

```
sudo apt-get install docker-compose 
```



#### Rodar docker-compose.yml

Após criar o documento  __docker-compose.yml__ e instalar suas dependências é hora de rodar o arquivo .yml.

Abra a pasta local do arquivo com o terminal e rode o seguinte comando: 

```
sudo docker-compose up 
```



#### Feito isto, a aplicação deverá estar rodando localmente nas seguintes portas: 

###### front-end 

```
localhost:8000
```

###### API  - Manutenção

```
localhost:8000 ou localhost:7000 
```

###### Banco de Dados - PhpMyAdmin

```
localhost:50060
```

### Planilha de User Stories e Requisitos:

 [Planilha](https://docs.google.com/spreadsheets/d/1ycDPItuhIysY-Hwc2hwD9GY4EiCI9KEYr7muG5JvnW0/edit?usp=sharing)

### Wireframes:

[Wireframes](https://drive.google.com/file/d/1cCsnVEDTfxDt4fi0xSj7J8wjEw7jbMda/view)

### Modelagem de Banco de Dados:

[Link para o Draw.io](https://drive.google.com/file/d/1dkrORrX57N5EjgdTrV-mCxYDesjZclcV/view?usp=sharing)



