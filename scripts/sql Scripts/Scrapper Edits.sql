use  scraper;

call getproducts();

-- -------------------------
-- UPDATES -----------------
-- -------------------------

select	*
from 	product p
where	lower(p.name) like '%alicia%'

-- categoria
update product 
set id_category = 6
where id in (68)

-- precio
update `scraper`.`product`
set reference_price = 35000
where id in (520)

-- nombre
update `scraper`.`product`
set name = 'Gorazde (nueva edición)'
where id in (56)

-- Status (desactiva = False; Activa = True)
update `scraper`.`product`
set status = false
where id in (527,528)

update `scraper`.`comparator`
set product_name = 'Gorazde (nueva edición)'
where id = 174 


-- -------------------------
-- SELECTS -----------------
-- -------------------------

select  *
from comparator 
order by hasstock desc, discount_percent desc


select  *
from comparator 
where id_product = 56

select  count(*)
from comparator 

select	*
from product
where id = 59


select *
from product_commerce_detail
where id_product = 529

-- -------------------------
-- DELETE -----------------
-- -------------------------

DELETE FROM `scraper`.`comparator`
WHERE id_product = 415;



-- -------------------------
-- END -----------------
-- -------------------------











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




select	  p.id,
          p.name, 
          p.reference_price, 
          g.discount, 
          g.name 
from  	   product p, 
          category g 
where     p.id_category = g.id 
and       p.status = 1 
order by  p.priority asc,
		  p.id_category asc, 
          p.id asc;


update product 
set priority = 2
where id in (283)


select *
from comparator
where id_product = 283

UPDATE `scraper`.`comparator`
SET
`priority` = 2
WHERE `id`= 221;



UPDATE product  SET  name = 'Second Coming', reference_price = 13000, id_category = 11,  img_url = null,  status = False, priority = null  WHERE id = 398; 


Select *
from product
where status = 1
and id_category = 1
order by id desc


select	*
from product p
where lower(p.name)  like '%princesa%'

update product 
set status = 1
where id in (47)


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





update `scraper`.`product`
set reference_price = 60000,
	id_category = 11
where id = 72

--

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
set name = '100 Balas Libro 05 (de 5)'
where id = 442


