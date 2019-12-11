#3.2) Todas a interações de cada plataforma por cliente -- Quantitativo

set @email = '';

select Email, Origem as Plataforma, count(distinct contato_id) as TotalInteracoes
from contatos
where (@email = '' or email = @email) #se o email não for informado, retorna todos os registros
group by email, origem;
