SELECT `historical`.`id`,
    `historical`.`id_product`,
    `historical`.`price`,
    `historical`.`reg_date`,
    `historical`.`id_commerce`,
    `historical`.`id_product_commerce_detail`
FROM `scraper`.`historical`;

INSERT INTO `scraper`.`historical`
(`id`,
`id_product`,
`price`,
`reg_date`,
`id_commerce`,
`id_product_commerce_detail`)
VALUES
(<{id: }>,
<{id_product: }>,
<{price: }>,
<{reg_date: CURRENT_TIMESTAMP}>,
<{id_commerce: }>,
<{id_product_commerce_detail: }>);

