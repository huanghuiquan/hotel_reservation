CREATE TABLE `hotels_location` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `country` varchar(30) NOT NULL,
    `city` varchar(60) NOT NULL,
    `province` varchar(30) NOT NULL
)
;
CREATE TABLE `hotels_hotel` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `star` integer NOT NULL,
    `address` varchar(50) NOT NULL,
    `description` longtext NOT NULL,
    `located_id` integer NOT NULL
)
;
ALTER TABLE `hotels_hotel` ADD CONSTRAINT `located_id_refs_id_4bc9e7a3` FOREIGN KEY (`located_id`) REFERENCES `hotels_location` (`id`);
CREATE TABLE `hotels_room` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `adult` integer NOT NULL,
    `children` integer NOT NULL,
    `belongto_id` integer NOT NULL,
    `price` double precision NOT NULL,
    `roomNumber` integer NOT NULL
)
;
ALTER TABLE `hotels_room` ADD CONSTRAINT `belongto_id_refs_id_5f49dcef` FOREIGN KEY (`belongto_id`) REFERENCES `hotels_hotel` (`id`);
CREATE TABLE `hotels_client` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `smoking` bool NOT NULL,
    `firstname` varchar(20) NOT NULL,
    `lastname` varchar(20) NOT NULL,
    `requirement` longtext NOT NULL
)
;
CREATE TABLE `hotels_order` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `checkin` date NOT NULL,
    `checkout` date NOT NULL,
    `total` double precision NOT NULL,
    `date` datetime NOT NULL,
    `client_id` integer NOT NULL,
    `code` varchar(45) NOT NULL
)
;
ALTER TABLE `hotels_order` ADD CONSTRAINT `client_id_refs_id_883965cd` FOREIGN KEY (`client_id`) REFERENCES `hotels_clie
nt` (`id`);
CREATE TABLE `hotels_booked` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `room_id` integer NOT NULL,
    `order_id` integer NOT NULL
)
;
ALTER TABLE `hotels_booked` ADD CONSTRAINT `room_id_refs_id_ade00406` FOREIGN KEY (`room_id`) REFERENCES `hotels_room` (`id`);
ALTER TABLE `hotels_booked` ADD CONSTRAINT `order_id_refs_id_44747afd` FOREIGN KEY (`order_id`) REFERENCES `hotels_order` (`id`);
CREATE INDEX `hotels_hotel_6bec2eb2` ON `hotels_hotel` (`located_id`);
CREATE INDEX `hotels_room_3d9f8eea` ON `hotels_room` (`belongto_id`);
CREATE INDEX `hotels_order_4fea5d6a` ON `hotels_order` (`client_id`);
CREATE INDEX `hotels_booked_c9f5884f` ON `hotels_booked` (`room_id`);
CREATE INDEX `hotels_booked_68d25c7a` ON `hotels_booked` (`order_id`);
