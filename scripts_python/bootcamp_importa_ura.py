import mysql.connector
from mysql.connector import Error
import csv
import codecs
import urllib.request
import requests
import json
import datetime
import time

dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

try:
    # recupera dataset da URA
    url_json = "https://raw.githubusercontent.com/camilabianchi/graces_desafio/master/datasets/UraTelefonica.jsonl"
    req = requests.get(url_json)
    dicionario = json.loads(req.text)

    if len(dicionario) > 0:

        # abre conexao com o banco
        connection = mysql.connector.connect(host='localhost', port='3306', database='clickbusbd', user='dscourse',
                                             password='D@t@Sc!enceC0urs3')

        # percorre registros
        for item in dicionario:
            # data em formato string
            data_inicio_str = item["data"].replace("/", "-") + " " + item["Horário"]

            # calculo duracao chamada em segundos
            duracao = time.strptime(item["duracao_total_da_chamada"], '%H:%M:%S')
            segundos = datetime.timedelta(hours=duracao.tm_hour, minutes=duracao.tm_min,
                                          seconds=duracao.tm_sec).total_seconds()

            # calculo data final com base na duracao da chamada
            dt_inicio = datetime.datetime.strptime(data_inicio_str, '%m-%d-%Y %H:%M:%S')
            dt_termino = dt_inicio + datetime.timedelta(seconds=segundos)

            # valores do insert
            email = item["email"]
            nome = item["cliente_nome"]
            agente = item["Agente"]
            status = item["Status"]
            origem = 'URA'
            semana = 0 if dt_inicio.weekday() == 6 else dt_inicio.weekday() + 1
            semana_nome = dias_semana[semana]

            if connection.is_connected():
                cursor = connection.cursor()

                sql_insert = """INSERT INTO contatos(email, nome, data_inicio, data_termino, agente, status, origem, semana, semana_nome) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
                record = (email, nome, dt_inicio, dt_termino, agente, status, origem, semana, semana_nome)

                try:
                    cursor.execute(sql_insert, record)
                    connection.commit()
                except Error as e:
                    sql_insert = """INSERT INTO log_erros(log_mensagem) VALUES (%s) """
                    record = (e.msg.replace("'", ""),)
                    cursor.execute(sql_insert, record)
                    connection.commit()
                finally:
                    cursor.close()

        # fecha conexao com o banco
        if connection.is_connected():
            connection.close()
except Error as e:
    print("Error while connecting to MySQL", e.msg)
