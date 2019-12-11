# Bootcamp WomakersCode
### Desafio Data Engineer - ClickBus

Como projeto final de conclusão do Bootcamp Data Science, recebemos o desafio Click Bus – Data Engineer onde necessitava modelar o Customer Experience, que
consiste na integração de todos os dados dos seguintes datasets (Ura telefônica, Chat Online, Whatsapp e e-mail) para conseguir extrair as melhores informações referentes ao cliente.

Como linguagem e ferramentas, optamos por utilizar:

* Python
* Banco de dados MySQL
* Airflow

## Primeiro desafio

> Construa uma modelagem de dados para consulta, integrando todos datasets, visando a melhor forma de padronizá-los. Crie um script de criação do schema e das tabelas que serão utilizadas para o contexto descrito anteriormente. Informando como e com quais tecnologias você efetuaria a integração desses dados.

### Solução Proposta

* <a href="https://github.com/camilabianchi/graces_desafio/tree/master/1_modelagem">Scripts de criação das tabelas</a>

Modelagem dos dados:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/1_modelagem/modelagem.jpg?raw=true" title="Img" alt="Img" style="max-width:80%;">

Como proposta de solução para esse desafio criamos um fluxo no airflow que processa os dados dos atendimentos e faz a ingestão no banco de dados criado em MySQL para armazenar todos os contatos do Customer Experience.

## Segundo desafio

> Crie um script para efetuar extração, transformação e carregamento desses dados no banco de dados que você modelou acima (python)

### Solução Proposta

Criamos uma DAG no Airflow para cada dataset e com o modelo de Customer Experience criado pelo Airflow conseguimos fazer a integração de todos e posteriormente os agendamentos de serviços necessários.

* <a href="https://github.com/camilabianchi/graces_desafio/tree/master/2_importacao_python_airflow">Scripts de importação em python</a>
* <a href="https://github.com/camilabianchi/graces_desafio/tree/master/2_importacao_python_airflow/airflow_dags">DAG's do Airflow utilizadas para o agendamento da execução das importações</a>

## Terceiro desafio

> A partir da sua modelagem, construa três queries para responder:

1. > A quantidade de contatos nas últimas 24h por cliente

### Solução Proposta


<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_1.JPG?raw=true" title="Img" alt="Img" style="max-width:80%;">


2. > Todas a interações de cada plataforma por cliente

### Solução Proposta


Qualitativo:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_2_ql.JPG" title="Img" alt="Img" style="max-width:80%;">


Quantitativo:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_2_qt.JPG" title="Img" alt="Img" style="max-width:80%;">


3. > Última interação e qual plataforma por cliente


### Solução Proposta


<img src="https://github.com/camilabianchi/graces_desafio/blob/master/3_queries/questao3_3.JPG" title="Img" alt="Img" style="max-width:80%;">



## Quarto desafio

> Caso tenha conhecimento em AWS/GCP(Google Cloud Platform), quais serviços você utilizaria para garantir a performance da sua arquitetura de dados.

### Solução Proposta

Sobre performance, existem 3 grandes empresas que oferecem sistema robustos para lidar com uma grande quantidade de dados de várias formas, incluindo real time. São elas Amazon Web Service que é uma plataforma de computação na nuvem oferecida pela Amazon.com, Google Cloud Platform que é uma suíte de computação em nuvem oferecida pelo Google e a Microsoft Azure que é uma plataforma destinada à execução de aplicativos e serviços baseada nos conceitos de computação em nuvem.

As 3 oferecem ótimas opções que ajudam a lidar com uma massa de dados grande sendo possível realizar análises e tirar insights relevantes para a área de negócios.

Utilizando a plataforma do Azure, podemos representar a arquitetura de real time:

<img src="https://github.com/camilabianchi/graces_desafio/blob/master/4_documentacao/azure.jpg" title="Img" alt="Img" style="max-width:80%;">


## Integrantes do grupo

* Angelina Inacio - <a href="https://www.linkedin.com/in/angelinainacio/" target="_blank">@angelinainacio</a>
* Camila Bianchi - <a href="https://www.linkedin.com/in/camilabianchi/" target="_blank">@camilabianchi</a>
* Camila Lima - <a href="https://www.linkedin.com/in/camilamlima/" target="_blank">@camilamlima</a>
* Sara Santana - <a href="https://www.linkedin.com/in/sara-ss/" target="_blank">@sara-ss</a>
