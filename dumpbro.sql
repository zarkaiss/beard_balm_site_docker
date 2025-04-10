-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: bro1.ckgv95yeaaiv.us-east-2.rds.amazonaws.com    Database: bro1
-- ------------------------------------------------------
-- Server version	5.7.22-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `bro1`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `bro1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bro1`;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('1e7ccd30643f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedbackid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email1` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `approved` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,'Tom Landry','lol@lol.com','test','I have used Beard Brother\'s oil and balm for the past 5 months and have nothing but praises to give. On a daily basis I am complimented due to my beard being maintained. Every time I give you guys the full credit.',1),(2,'Gandalf the Grey','lol@lol.com','test','Beard Brother’s beard balm is has an awesome consistency that is easy applied begins to melt immediately you do not have to work hard to apply onto your beard. It gives you an awesome shine and trust me a little bit goes a LONG way.',1),(3,'Abe Lincoln','lawl@lawl.com','test','I absolutely love this beard balm! I don\'t know why I\'m just now putting in a review but I\'ve been using this for about three years and it\'s amazing! I like to put a little extra on especially when it\'s sunny because it glistens in the sun!',1),(4,'Charles Darwin','person@place.com','Test','The scent is very noticeable and at the same time not overwhelming at all. Reminds me of a favorite cologne of mine, but just a hint of the scent. Like the other Beard Brother\'s products, this really makes my fairly long beard so soft and manageable.',1);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `category` varchar(100) NOT NULL,
  `product_rating` decimal(10,0) DEFAULT NULL,
  `product_review` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (3,'Citrus Wax','Beard wax infused with citrus','https://i.imgur.com/lEFmvYU.jpg',15,1,'WAX',NULL,'Excellent smell'),(4,'Frankincense Balm','Made with shea butter, argan oil, jojoba, avocado oil, and frankincense all 100% organic','https://i.imgur.com/UUxccBO.jpg',15,1,'BALM',NULL,'First time buying this product can\'t wait to try it excellent customer service and fast shipping.'),(5,'Tobacco Vanilla Wax','Made with shea butter, jojobra, argan oil, avocado oil, and tobacco vanilla all 100% organic','https://i.imgur.com/NVxGQKn.jpg',15,1,'WAX',NULL,'Love the tobacco scent'),(6,'Sandalwood Beard Cream','Made with shea butter, jojobra, argan oil, avocado oil, and sandalwood all 100% organic','https://i.imgur.com/CBHCgv5.jpg',18,1,'CREAM',NULL,'Great product!!!'),(7,'Jasmine Beard Softener','Made with jojobra, argan oil, avocado oil, and jasmine all 100% organic','https://i.imgur.com/OejR3Qw.jpg',18,1,'SOFTENER',NULL,'Makes your beard silky smooth.'),(8,'Tea Tree Beard Conditioner','Made with argan oil,avocado oil,and tea tree oil designed to make your beard healthy and shiny','https://i.imgur.com/C7vE9tN.png',18,1,'CONDITIONER',NULL,'Awesome conditioner and has a great smell.');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `roleId` int(11) NOT NULL AUTO_INCREMENT,
  `username_id` int(11) DEFAULT NULL,
  `users_role` varchar(128) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_modified` datetime DEFAULT NULL,
  PRIMARY KEY (`roleId`),
  KEY `username_id` (`username_id`),
  CONSTRAINT `role_ibfk_1` FOREIGN KEY (`username_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,2,'Admin','2019-10-24 16:35:04','2019-10-24 16:35:04'),(2,3,'Customer','2019-10-24 16:35:33','2019-10-24 16:35:33');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'rod','lol@lol.com','pbkdf2:sha256:150000$HKVDcvJd$72ebc9db535ce377b04ab51e0b6186ea78c059c726329082786647db1565a752',1,1,'2019-10-21 20:57:17',NULL),(3,'test123','lol123@lol.com','pbkdf2:sha256:150000$fxWpZ0z4$f4901035e375d1d89cf62b504c5ec74f3824b325061743e16ce2ec06cc77a753',0,1,'2019-10-22 14:31:18',NULL),(4,'customer','customer@customer.com','pbkdf2:sha256:150000$qECb4aQo$dfb517429fcfea7448108b11cbc734bd748177c9d7b42ddd5b498d9b9e9017a2',0,1,'2019-10-24 16:37:37',NULL),(5,'blackie','dtyson986@gmail.com','pbkdf2:sha256:150000$gPSbpQZx$af4aef9628c930032ab40befff78fa7b7a70648241302bee0277399aef26eafe',1,1,'2019-10-24 19:32:28',NULL),(17,'testperson','starlingjarred@gmail.com','pbkdf2:sha256:150000$2hl8N23b$08d4c25a3e5c70f2e5f4ef4f472934b212bb528a5f1e42536d4e4452f0fea74a',0,1,'2019-11-04 20:52:15',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-22 16:22:37
