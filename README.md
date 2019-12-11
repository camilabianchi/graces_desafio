# Bootcamp WomakersCode - Desafio Data Engineer - ClickBus

Como projeto final de conclusão do Bootcamp Data Science, recebemos o desafio Click Bus – Data Engineering onde necessitava modelar o Customer Experience que
consiste na integração todos os dados dos seguintes datasets (Ura telefônica, Chat Online, Whatsapp e e-mail) para conseguir extrair as melhores informações referentes ao cliente.

Como linguagem e ferramentas, optamos por utilizar:

* Python
* Banco de dados MySQL
* Airflow

## Primeiro desafio

Construa uma modelagem de dados para consulta, integrando todos datasets, visando a melhor forma de padronizá-los (pequena explicação). Crie um script de criação do schema e das tabelas que serão utilizadas para o contexto descrito anteriormente. Informando como e com quais tecnologias você efetuaria a integração desses dados.

### Solução Proposta

Criamos uma DAG no Airflow de cada dataset e com o modelo de Customer Experience criado pelo Airflow conseguimos fazer a integração de todos e posteriormente os agendamentos de serviços necessários.

## Segundo desafio

Como proposta de solução para esse desafio criamos um fluxo no airflow que processa os dados dos atendimentos e faz a ingestão no banco de dados criado em MySQL para armazenar todos os contatos do Customer Experience.

### Solução Proposta

Criamos uma DAG no Airflow de cada dataset e com o modelo de Customer Experience criado pelo Airflow conseguimos fazer a integração de todos e posteriormente os agendamentos de serviços necessários.

## Terceiro desafio

A partir da sua modelagem, construa três queries para responder:

* A quantidade de contatos nas últimas 24h por cliente

### Solução Proposta


<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_1.JPG?raw=true" title="Img" alt="Img">


* Todas a interações de cada plataforma por cliente

### Solução Proposta


Qualitativo:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_2_ql.JPG" title="Img" alt="Img">


Quantitativo:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_2_qt.JPG" title="Img" alt="Img">


* Última interação e qual plataforma por cliente


### Solução Proposta


<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_3.JPG" title="Img" alt="Img">



## Quarto desafio

Caso tenha conhecimento em AWS/GCP(Google Cloud Platform), quais serviços você utilizaria para garantir a performance da sua arquitetura de dados.

### Solução Proposta

[EM ANDAMENTO]
 

## Integrantes do grupo

* Angelina Inacio - <a href="https://www.linkedin.com/in/angelinainacio/">@angelinainacio</a>
* Camila Bianchi - <a href="https://www.linkedin.com/in/camilabianchi/">@camilabianchi</a>
* Camila Lima - <a href="https://www.linkedin.com/in/camilamlima/">@camilamlima</a>
* Sara Santana - <a href="https://www.linkedin.com/in/sara-ss/">@sara-ss</a>
