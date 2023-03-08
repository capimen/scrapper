SELECT `product_commerce_detail`.`id`,
    `product_commerce_detail`.`id_product`,
    `product_commerce_detail`.`id_commerce`,
    `product_commerce_detail`.`url`,
    `product_commerce_detail`.`reg_date`
FROM `scraper`.`product_commerce_detail`;

INSERT INTO `scraper`.`product_commerce_detail`
(`id`,
`id_product`,
`id_commerce`,
`url`,
`reg_date`)
VALUES
(<{id: }>,
<{id_product: }>,
<{id_commerce: }>,
<{url: }>,
<{reg_date: CURRENT_TIMESTAMP}>);
