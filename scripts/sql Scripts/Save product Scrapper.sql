call putProduct(
	'Mi Vida sin Rosa',
    12000,
	6,    -- category
    1,     -- comercio (1 - Buscalibre)
    'https://www.buscalibre.cl/libro-mi-vida-sin-rosa/9788418419683/p/54367207',
    @lastProductDetail
);
select 	p.name as product_name,
		d.url as  product_url
from 	`scraper`.`product` p,
		`scraper`.`product_commerce_detail` d
where p.id = @lastProductDetail
and   d.id_product = p.id;



-- '1', 'Escritores Chilenos', '30', '1', '2021-06-29 16:31:05'
-- '2', 'Literatura Inglesa', '30', '1', '2021-06-29 16:31:05'
-- '3', 'Literatura Juvenil', '30', '1', '2021-06-29 16:31:05'
-- '4', 'Sin Categoria', '30', '1', '2021-06-29 11:54:11'
-- '5', 'Literatura Clasica', '30', '1', '2021-12-31 10:25:39'
-- '6', 'Novela Grafica', '30', '1', '2021-12-31 10:44:49'
-- '7', 'Literatura Infantil', '30', '1', '2021-12-31 10:49:34'
-- '8', 'Literatura Latinoamericana', '30', '1', '2021-06-29 11:54:11'
-- '9', 'Mejores libros de este siglo', '30', '1', '2021-06-29 11:54:11'
-- '10', 'Mariana', '30', '1', '2021-12-31 10:57:00'
-- '11', 'Comics Superheroes', '30', '1', '2021-12-30 15:31:48'
-- '12', 'Manga', '25', '1', '2021-12-31 10:22:57'
-- '13', 'Manga Ingles', '25', '6', '2021-12-31 10:58:10'
-- '14', 'Literatura Ciencia Ficcion', '30', '1', '2022-10-11 10:00:31'

