/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - lgew
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lgew` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `lgew`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$PoU9JjIYchdy4PcuTpChXE$1kv4kuR2Fp/YDBObuRLULBWFk4p7J8joxlBKwzsxKzI=','2022-04-07 08:18:59.129033',1,'admin','','','admin@gmail.com',1,1,'2022-04-07 08:18:38.315647');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

/*Table structure for table `maincode_bank` */

DROP TABLE IF EXISTS `maincode_bank`;

CREATE TABLE `maincode_bank` (
  `BankId` int NOT NULL AUTO_INCREMENT,
  `AccountNumber` int NOT NULL,
  `IFSE_code` varchar(20) NOT NULL,
  `Amount` int NOT NULL,
  `PassangerId_id` int NOT NULL,
  PRIMARY KEY (`BankId`),
  KEY `MainCode_bank_PassangerId_id_0c99d199_fk_MainCode_` (`PassangerId_id`),
  CONSTRAINT `MainCode_bank_PassangerId_id_0c99d199_fk_MainCode_` FOREIGN KEY (`PassangerId_id`) REFERENCES `maincode_passenger` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_bank` */

insert  into `maincode_bank`(`BankId`,`AccountNumber`,`IFSE_code`,`Amount`,`PassangerId_id`) values 
(1,22,'22',599982,1);

/*Table structure for table `maincode_buslocation` */

DROP TABLE IF EXISTS `maincode_buslocation`;

CREATE TABLE `maincode_buslocation` (
  `LocationId` int NOT NULL AUTO_INCREMENT,
  `Latitude` double NOT NULL,
  `Longitude` double NOT NULL,
  `BusId_id` int NOT NULL,
  PRIMARY KEY (`LocationId`),
  KEY `MainCode_buslocation_BusId_id_34713584_fk_MainCode_` (`BusId_id`),
  CONSTRAINT `MainCode_buslocation_BusId_id_34713584_fk_MainCode_` FOREIGN KEY (`BusId_id`) REFERENCES `maincode_busregister` (`BusId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_buslocation` */

insert  into `maincode_buslocation`(`LocationId`,`Latitude`,`Longitude`,`BusId_id`) values 
(1,11.2570701,75.7845671,1);

/*Table structure for table `maincode_busregister` */

DROP TABLE IF EXISTS `maincode_busregister`;

CREATE TABLE `maincode_busregister` (
  `BusId` int NOT NULL AUTO_INCREMENT,
  `BusRegisterNUmber` varchar(40) NOT NULL,
  `SeatCapacity` int NOT NULL,
  `RouteId_id` int NOT NULL,
  PRIMARY KEY (`BusId`),
  KEY `MainCode_busregister_RouteId_id_6a9a03f1_fk_MainCode_` (`RouteId_id`),
  CONSTRAINT `MainCode_busregister_RouteId_id_6a9a03f1_fk_MainCode_` FOREIGN KEY (`RouteId_id`) REFERENCES `maincode_route` (`RouteId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_busregister` */

insert  into `maincode_busregister`(`BusId`,`BusRegisterNUmber`,`SeatCapacity`,`RouteId_id`) values 
(1,'232',45,1);

/*Table structure for table `maincode_busstop` */

DROP TABLE IF EXISTS `maincode_busstop`;

CREATE TABLE `maincode_busstop` (
  `StopId` int NOT NULL AUTO_INCREMENT,
  `stop` varchar(30) NOT NULL,
  `Latitude` double NOT NULL,
  `Longitude` double NOT NULL,
  `TicketCharge` int NOT NULL,
  `RouteId_id` int NOT NULL,
  PRIMARY KEY (`StopId`),
  KEY `MainCode_busstop_RouteId_id_a737228d_fk_MainCode_route_RouteId` (`RouteId_id`),
  CONSTRAINT `MainCode_busstop_RouteId_id_a737228d_fk_MainCode_route_RouteId` FOREIGN KEY (`RouteId_id`) REFERENCES `maincode_route` (`RouteId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_busstop` */

insert  into `maincode_busstop`(`StopId`,`stop`,`Latitude`,`Longitude`,`TicketCharge`,`RouteId_id`) values 
(1,'chettikulam',11.33110943,75.7469227,18,1);

/*Table structure for table `maincode_bustime` */

DROP TABLE IF EXISTS `maincode_bustime`;

CREATE TABLE `maincode_bustime` (
  `TimeId` int NOT NULL AUTO_INCREMENT,
  `Time` varchar(30) NOT NULL,
  `BusId_id` int NOT NULL,
  `StopId_id` int NOT NULL,
  PRIMARY KEY (`TimeId`),
  KEY `MainCode_bustime_BusId_id_03f14bf6_fk_MainCode_busregister_BusId` (`BusId_id`),
  KEY `MainCode_bustime_StopId_id_18073775_fk_MainCode_busstop_StopId` (`StopId_id`),
  CONSTRAINT `MainCode_bustime_BusId_id_03f14bf6_fk_MainCode_busregister_BusId` FOREIGN KEY (`BusId_id`) REFERENCES `maincode_busregister` (`BusId`),
  CONSTRAINT `MainCode_bustime_StopId_id_18073775_fk_MainCode_busstop_StopId` FOREIGN KEY (`StopId_id`) REFERENCES `maincode_busstop` (`StopId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_bustime` */

insert  into `maincode_bustime`(`TimeId`,`Time`,`BusId_id`,`StopId_id`) values 
(1,'09:02',1,1);

/*Table structure for table `maincode_conductor` */

DROP TABLE IF EXISTS `maincode_conductor`;

CREATE TABLE `maincode_conductor` (
  `UserId` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(20) DEFAULT NULL,
  `LastName` varchar(20) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `Place` varchar(20) DEFAULT NULL,
  `Post` varchar(20) DEFAULT NULL,
  `pin` bigint DEFAULT NULL,
  `Bus_id` int NOT NULL,
  `lid_id` int NOT NULL,
  PRIMARY KEY (`UserId`),
  KEY `MainCode_conductor_Bus_id_c34cd0ed_fk_MainCode_busregister_BusId` (`Bus_id`),
  KEY `MainCode_conductor_lid_id_5cc9f755_fk_MainCode_login_UserId` (`lid_id`),
  CONSTRAINT `MainCode_conductor_Bus_id_c34cd0ed_fk_MainCode_busregister_BusId` FOREIGN KEY (`Bus_id`) REFERENCES `maincode_busregister` (`BusId`),
  CONSTRAINT `MainCode_conductor_lid_id_5cc9f755_fk_MainCode_login_UserId` FOREIGN KEY (`lid_id`) REFERENCES `maincode_login` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_conductor` */

insert  into `maincode_conductor`(`UserId`,`FirstName`,`LastName`,`Contact`,`Place`,`Post`,`pin`,`Bus_id`,`lid_id`) values 
(1,'sunil','k',9089789098,'calicut','calicut',990909,1,2);

/*Table structure for table `maincode_feedback` */

DROP TABLE IF EXISTS `maincode_feedback`;

CREATE TABLE `maincode_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Feedback` varchar(120) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `User_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MainCode_feedback_User_id_id_3f828cfa_fk_MainCode_` (`User_id_id`),
  CONSTRAINT `MainCode_feedback_User_id_id_3f828cfa_fk_MainCode_` FOREIGN KEY (`User_id_id`) REFERENCES `maincode_passenger` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_feedback` */

insert  into `maincode_feedback`(`id`,`Feedback`,`Date`,`User_id_id`) values 
(1,'good','2022-04-04',1);

/*Table structure for table `maincode_login` */

DROP TABLE IF EXISTS `maincode_login`;

CREATE TABLE `maincode_login` (
  `UserId` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(25) NOT NULL,
  `Password` varchar(25) NOT NULL,
  `Type` varchar(25) NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_login` */

insert  into `maincode_login`(`UserId`,`Username`,`Password`,`Type`) values 
(1,'admin','admin','admin'),
(2,'suni','4321','conductor'),
(3,'sree','123','user');

/*Table structure for table `maincode_passenger` */

DROP TABLE IF EXISTS `maincode_passenger`;

CREATE TABLE `maincode_passenger` (
  `UserId` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(20) DEFAULT NULL,
  `LastName` varchar(20) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `Place` varchar(20) DEFAULT NULL,
  `Post` varchar(20) DEFAULT NULL,
  `pin` bigint DEFAULT NULL,
  `LoginId_id` int NOT NULL,
  PRIMARY KEY (`UserId`),
  KEY `MainCode_passenger_LoginId_id_ed31210d_fk_MainCode_login_UserId` (`LoginId_id`),
  CONSTRAINT `MainCode_passenger_LoginId_id_ed31210d_fk_MainCode_login_UserId` FOREIGN KEY (`LoginId_id`) REFERENCES `maincode_login` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_passenger` */

insert  into `maincode_passenger`(`UserId`,`FirstName`,`LastName`,`Contact`,`Place`,`Post`,`pin`,`LoginId_id`) values 
(1,'sreeya','s',9638527423,'calicut','calicut',639633,3);

/*Table structure for table `maincode_passengerbooking` */

DROP TABLE IF EXISTS `maincode_passengerbooking`;

CREATE TABLE `maincode_passengerbooking` (
  `BookingId` int NOT NULL AUTO_INCREMENT,
  `BusId_id` int NOT NULL,
  `PassengerId_id` int NOT NULL,
  `StopId_id` int NOT NULL,
  PRIMARY KEY (`BookingId`),
  KEY `MainCode_passengerbo_BusId_id_587f590e_fk_MainCode_` (`BusId_id`),
  KEY `MainCode_passengerbo_PassengerId_id_5b8251fa_fk_MainCode_` (`PassengerId_id`),
  KEY `MainCode_passengerbo_StopId_id_604de34a_fk_MainCode_` (`StopId_id`),
  CONSTRAINT `MainCode_passengerbo_BusId_id_587f590e_fk_MainCode_` FOREIGN KEY (`BusId_id`) REFERENCES `maincode_busregister` (`BusId`),
  CONSTRAINT `MainCode_passengerbo_PassengerId_id_5b8251fa_fk_MainCode_` FOREIGN KEY (`PassengerId_id`) REFERENCES `maincode_passenger` (`UserId`),
  CONSTRAINT `MainCode_passengerbo_StopId_id_604de34a_fk_MainCode_` FOREIGN KEY (`StopId_id`) REFERENCES `maincode_busstop` (`StopId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_passengerbooking` */

insert  into `maincode_passengerbooking`(`BookingId`,`BusId_id`,`PassengerId_id`,`StopId_id`) values 
(1,1,1,1);

/*Table structure for table `maincode_payment` */

DROP TABLE IF EXISTS `maincode_payment`;

CREATE TABLE `maincode_payment` (
  `PayId` int NOT NULL AUTO_INCREMENT,
  `Amount` double NOT NULL,
  `Status` varchar(110) NOT NULL,
  `Booking_Id_id` int NOT NULL,
  PRIMARY KEY (`PayId`),
  KEY `MainCode_payment_Booking_Id_id_7cc4a656_fk_MainCode_` (`Booking_Id_id`),
  CONSTRAINT `MainCode_payment_Booking_Id_id_7cc4a656_fk_MainCode_` FOREIGN KEY (`Booking_Id_id`) REFERENCES `maincode_passengerbooking` (`BookingId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_payment` */

insert  into `maincode_payment`(`PayId`,`Amount`,`Status`,`Booking_Id_id`) values 
(1,18,'payed',1);

/*Table structure for table `maincode_qrcode` */

DROP TABLE IF EXISTS `maincode_qrcode`;

CREATE TABLE `maincode_qrcode` (
  `id` int NOT NULL AUTO_INCREMENT,
  `BusId_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MainCode_qrcode_BusId_id_73534649_fk_MainCode_busregister_BusId` (`BusId_id`),
  CONSTRAINT `MainCode_qrcode_BusId_id_73534649_fk_MainCode_busregister_BusId` FOREIGN KEY (`BusId_id`) REFERENCES `maincode_busregister` (`BusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_qrcode` */

/*Table structure for table `maincode_route` */

DROP TABLE IF EXISTS `maincode_route`;

CREATE TABLE `maincode_route` (
  `RouteId` int NOT NULL AUTO_INCREMENT,
  `StartingStop` varchar(50) NOT NULL,
  `EndingStop` varchar(50) NOT NULL,
  PRIMARY KEY (`RouteId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `maincode_route` */

insert  into `maincode_route`(`RouteId`,`StartingStop`,`EndingStop`) values 
(1,'koyilandy','kozhikode');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
