#3.3) Última interação e qual plataforma por cliente.

set @email = '';

select a.Email, a.Nome, a.data_inicio as DataInicio, a.data_termino as DataTermino, a.Agente, 
	a.Status, a.origem as Plataforma, a.Semana, a.semana_nome as SemanaNome, a.data_importacao as DataInclusaoRegistro
from contatos as a
inner join(
	select email, max(data_inicio) as ultima_interacao
	from contatos
	where (@email = '' or email = @email) #se o email não for informado, retorna todos os registros
	group by email
) as b on a.email = b.email and a.data_inicio = b.ultima_interacao
order by a.email;
