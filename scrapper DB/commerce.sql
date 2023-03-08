SELECT `commerce`.`id`,
    `commerce`.`name`,
    `commerce`.`priceclass`,
    `commerce`.`pricetag`,
    `commerce`.`nameclass`,
    `commerce`.`nametag`
FROM `scraper`.`commerce`;



INSERT INTO `scraper`.`commerce`
(`id`,
`name`,
`priceclass`,
`pricetag`,
`nameclass`,
`nametag`)
VALUES
(<{id: }>,
<{name: }>,
<{priceclass: }>,
<{pricetag: }>,
<{nameclass: }>,
<{nametag: }>);
