# coding=utf-8
import mysql.connector
from mysql.connector import Error
import csv
import dateutil.parser
import requests

dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

try:
    # recupera o dataset do E-mail
    url = 'http://raw.githubusercontent.com/camilabianchi/graces_desafio/master/datasets/email.csv'

    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        csv_file = list(cr)

        if len(csv_file) > 0:
            # abre conexao com o banco
            connection = mysql.connector.connect(host='localhost', port='3306', database='[db]', user='[user]',
                                                 password='[pwd]')
            cont = 0
            for item in csv_file:
                if cont > 0:
                    email = item[7]
                    nome = item[7]
                    data_inicio = dateutil.parser.parse(item[3])
                    data_termino = dateutil.parser.parse(item[4])
                    agente = "Não Aplicável"
                    status = "Não Aplicável"
                    origem = "E-mail"
                    semana = 0 if data_inicio.weekday() == 6 else data_inicio.weekday() + 1
                    semana_nome = dias_semana[semana]

                    if connection.is_connected():
                        cursor = connection.cursor()

                        sql_insert = """INSERT INTO contatos(email, nome, data_inicio, data_termino, agente, status, origem, semana, semana_nome) 
                                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
                        record = (email, nome, data_inicio, data_termino, agente, status, origem, semana, semana_nome)

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
                cont += 1

            # fecha conexao com o banco
            if connection.is_connected():
                connection.close()

except Error as e:
    print("Error while connecting to MySQL", e.msg)
