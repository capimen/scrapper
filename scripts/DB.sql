create database scraper;

use scraper;

--Create Tables

CREATE TABLE product (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200) NOT NULL,
url VARCHAR(2000) NOT NULL,
id_commerce INT(6),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

CREATE TABLE commerce(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200),
priceclass VARCHAR(200),
pricetag VARCHAR(200),
nameclass VARCHAR(200),
nametag VARCHAR(200),
discount INT(3)
)

CREATE TABLE historical (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
id_product INT(6),
price int(12),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

CREATE TABLE comparator(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
id_product INT(6) NOT NULL,
product_name VARCHAR(200) NOT NULL,
price_newest INT(12),
price_average INT(12),
price_best INT(12),
price_worst INT(12),
discount_priceleft DOUBLE(24,12),
discount_percent DOUBLE(24,12),
average_safe INT(12),
average_safe_worst INT(12),
diff_best INT(12),
url VARCHAR(2000) NOT NULL,
best_historical_flag BOOLEAN,
umbral INT(3),
umbral_flag BOOLEAN,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)


CREATE TABLE product_commerce_detail (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
id_product INT(6) NOT NULL,
id_commerce INT(6),
url VARCHAR(2000) NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

CREATE TABLE category (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200),
discount INT(3),
id_group INT(6) default 1,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)


--Modifications Inserts
--migration
insert into product_commerce_detail (id_product, id_commerce, url)
(select 	p.id,
		c.id,
        p.url
from	product p,
		commerce c
where	p.id_commerce = c.id)

--ALTERS
--EJECUTAR DESPUES DEL INSERT DE product_commerce_detail
ALTER TABLE product
ADD reference_price int(12);

ALTER TABLE product
ADD id_category int(4) default 0;

ALTER TABLE product
DROP COLUMN url;

ALTER TABLE product
DROP COLUMN id_commerce;

ALTER TABLE historical
ADD id_commerce INT(6);

--ingreso de comercio en la tabla historical para buscalibre
update  historical
set 	id_commerce = 1

-- ingreso de comercio en la tabla historical para portalInmobiliario
update 	historical
set 	id_commerce = 2
where 	id_product in (175)


--insert para algunas categorias
INSERT INTO `scraper`.`category`(`name`)
VALUES ('Escritores Chilenos');

INSERT INTO `scraper`.`category`(`name`)
VALUES ('Literatura Inglesa');

INSERT INTO `scraper`.`category`(`name`)
VALUES ('Literatura Juvenil');

update product
set id_category = 1
where id in (1,2,3)

update product
set id_category = 2
where id in (4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

update product
set id_category = 3
where id in (26,27,28,29,30,31,32)


ALTER TABLE commerce
DROP COLUMN discount;


ALTER TABLE historical
ADD id_product_commerce_detail INT(6);

ALTER TABLE product
ADD img_url VARCHAR(2000);

ALTER TABLE product
ADD status BOOLEAN DEFAULT true;