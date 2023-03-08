Select *
from product
where status = 1
and id_category = 1
order by id desc


update product 
set id_category = 6
where id in (270,265,264)



update product 
set status = 0
where id in (34)


INSERT INTO `scraper`.`category`
(
`name`,
`discount`,
`id_group`)
VALUES
('Literatura Ciencia Ficcion',
30,
1
);



select	*
from 	category


update category
set name ='Manga Ingles'
where id = 13



select *
from 	product_commerce_detail
where id_product in (347,348)

select 	p.name as product_name,
		d.url as  product_url
from 	`scraper`.`product` p,
		`scraper`.`product_commerce_detail` d
where p.id = 15
and   d.id_product = p.id;


Select *
from product
order by 1 desc
limit 1



select	*
from product p
where lower(p.name)  like '%darth%'

update `scraper`.`product`
set reference_price = 60000,
	id_category = 11
where id = 72

--
update `scraper`.`product`
set status = false
where id in (106,108)
--


Select count(*)
from product
where status = 1


select	*
from 	product_commerce_detail
order by id_product desc



INSERT INTO `scraper`.`product_commerce_detail`
(
`id_product`,
`id_commerce`,
`url`
)
VALUES
(
278,
1,
'https://www.buscalibre.cl/libro-mobile-suit-gundam-the-origin-volume-9-lalah-libro-en-ingles/9781941220153/p/48437617'
);


select *
from 	`scraper`.`product_commerce_detail`
where id_product in (48,50)
order by id_product desc


update `scraper`.`product_commerce_detail`
set id_product = 272
where id = 233

select	*
from 	`scraper`.`historical`
order by reg_date desc

update `scraper`.`product`
set name = 'Crater'
where id = 379


--desactivar productos

update `scraper`.`product`
set status = false
where id in (397)

update `scraper`.`product`
set id_category = 12
where id = 388

update `scraper`.`product`
set reference_price = 20000
where id = 379

call getproducts();

select	*
from 	product p
where	lower(p.name) like '%puño%'

select	*
from 	product_commerce_detail
where 	id_product = 386


-- revision de URL con preventa
select	*
from 	product_commerce_detail
where lower(url) like '%puño%'

-- El Puño de la Estrella del Norte (Hokuto no Ken) nº 15


select *
from product

INSERT INTO `scraper`.`product`
(`id`,
`name`,
`reg_date`,
`reference_price`,
`id_category`,
`img_url`,
`status`)
VALUES
(<{id: }>,
<{name: }>,
<{reg_date: CURRENT_TIMESTAMP}>,
<{reference_price: }>,
<{id_category: 0}>,
<{img_url: }>,
<{status: 1}>);
