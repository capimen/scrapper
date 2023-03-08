SELECT `category`.`id`,
    `category`.`name`,
    `category`.`discount`,
    `category`.`id_group`,
    `category`.`reg_date`
FROM `scraper`.`category`;


INSERT INTO `scraper`.`category`
(`id`,
`name`,
`discount`,
`id_group`,
`reg_date`)
VALUES
(<{id: }>,
<{name: }>,
<{discount: }>,
<{id_group: 1}>,
<{reg_date: CURRENT_TIMESTAMP}>);
