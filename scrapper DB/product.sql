SELECT `product`.`id`,
    `product`.`name`,
    `product`.`reg_date`,
    `product`.`img_url`,
    `product`.`reference_price`,
    `product`.`id_category`
FROM `scraper`.`product`;


INSERT INTO `scraper`.`product`
(`id`,
`name`,
`reg_date`,
`img_url`,
`reference_price`,
`id_category`)
VALUES
(<{id: }>,
<{name: }>,
<{reg_date: CURRENT_TIMESTAMP}>,
<{img_url: }>,
<{reference_price: }>,
<{id_category: 1}>);
