# coding=utf-8
import mysql.connector
from mysql.connector import Error
import requests
import json
import datetime

dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

try:
    # recupera dataset do chat
    url_json = "http://raw.githubusercontent.com/camilabianchi/graces_desafio/master/datasets/chatOnline.jsonl"
    req = requests.get(url_json)
    dicionario = json.loads(req.text)

    if len(dicionario) > 0:
        # abre conexao com o banco
        connection = mysql.connector.connect(host='localhost', port='3306', database='[db]', user='[user]',
                                             password='[pwd]')
        # percorre registros
        for item in dicionario:
            # data em formato string
            data_inicio_str = item["Data da conversa (Inicio)"].replace("/", "-")
            data_fim_str = item["Data da conversa (Fim)"].replace("/", "-")

            # calculo data final com base na duracao da chamada
            dt_inicio = datetime.datetime.strptime(data_inicio_str, '%d-%m-%Y %H:%M')
            dt_termino = datetime.datetime.strptime(data_fim_str, '%d-%m-%Y %H:%M')

            # valores do insert
            email = item["Visitor_Email"]
            nome = item["Visitor_Email"]
            agente = item["Agente"]
            status = "Atendido" if item["Atendido"] == "Sim" else "Não atendido"
            origem = 'Chat'
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
