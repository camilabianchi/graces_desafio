#3.1) A quantidade de contatos nas últimas 24h por cliente.

set @email = '';

select Email, count(distinct contato_id) as QuantidadeContatos
from contatos
where (@email = '' or email = @email) #se o email não for informado, retorna todos os registros
	and data_inicio >= date_add(data_inicio, interval -24 hour)
group by email;
