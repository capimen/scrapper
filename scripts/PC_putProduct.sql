DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `putProduct`(
		in 	product_name varchar(200),
		in	product_price_refernce int,
        in  product_category int,
        in  commerce_id int,
        in  commerce_url varchar(2000),
		out detail_id int
	)
begin

	INSERT INTO `scraper`.`product`
	(
		`name`,
		`reference_price`,
		`id_category`,
		`img_url`,
		`status`
	)
	VALUES
	(
		product_name,
		product_price_refernce,
		product_category,
		null,
		true
	);
    
    INSERT INTO `scraper`.`product_commerce_detail`
	(
		`id_product`,
		`id_commerce`,
		`url`
	)
	VALUES
	(
		(	Select id
			from `scraper`.`product`
			order by 1 desc
			limit 1
		),
		commerce_id,
		commerce_url
	);
    
    Select id_product
    into detail_id
	from `scraper`.`product_commerce_detail`
	order by 1 desc
	limit 1;	

end$$
DELIMITER ;
