#3.2) Todas a interações de cada plataforma por cliente -- Qualitativo

set @email = '';

select Email, Nome, data_inicio as DataInicio, data_termino as DataTermino, Agente, 
	Status, Origem as Plataforma, Semana, semana_nome as SemanaNome, data_importacao as DataInclusaoRegistro
from contatos
where (@email = '' or email = @email) #se o email não for informado, retorna todos os registros
group by email, origem, data_inicio;
