import mysql.connector
from mysql.connector import Error
import csv
import codecs
import urllib.request
import dateutil
import dateutil.parser

dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

try:
    # recupera o dataset do Whatsapp
    url = 'https://raw.githubusercontent.com/camilabianchi/graces_desafio/master/datasets/Whatsapp.csv'
    stream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(stream, 'utf-8'))
    list_csv = list(csvfile)

    if len(list_csv) > 0:

        # abre conexao com o banco
        connection = mysql.connector.connect(host='localhost', port='3306', database='[database]', user='[user]',
                                             password='[pwd]')
        contador = 0
        # percorre registros
        for item in list_csv:
            # ignora o header
            if contador > 0:
                # data em formato string
                data_inicio_str = item[0].replace("/", "-").strip()
                data_fim_str = item[1].replace("/", "-").strip()

                dt_inicio = dateutil.parser.parse(data_inicio_str)
                dt_termino = dateutil.parser.parse(data_fim_str)

                # valores do insert
                email = item[6]
                nome = item[6]
                agente = "-"
                status = "Finalizado" if item[5] == "Sim" else "Não finalizado"
                origem = 'Whatsapp'
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
            contador += 1

        # fecha conexao com o banco
        if connection.is_connected():
            connection.close()
except Error as e:
    print("Error while connecting to MySQL", e.msg)
