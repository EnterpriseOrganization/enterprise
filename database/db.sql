-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: enterprice
-- ------------------------------------------------------
-- Server version	5.6.24

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
-- Table structure for table `apply`
--

DROP TABLE IF EXISTS `apply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apply` (
  `id` int(11) NOT NULL,
  `workshopID` int(11) NOT NULL,
  `applier` varchar(45) NOT NULL,
  `date` datetime NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `workshopID2_idx` (`workshopID`),
  CONSTRAINT `workshopID2` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apply`
--

LOCK TABLES `apply` WRITE;
/*!40000 ALTER TABLE `apply` DISABLE KEYS */;
/*!40000 ALTER TABLE `apply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applymaterial`
--

DROP TABLE IF EXISTS `applymaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `applymaterial` (
  `applyID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`applyID`,`materialID`),
  KEY `materialID6_idx` (`materialID`),
  CONSTRAINT `applyID` FOREIGN KEY (`applyID`) REFERENCES `apply` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `materialID6` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applymaterial`
--

LOCK TABLES `applymaterial` WRITE;
/*!40000 ALTER TABLE `applymaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `applymaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventorinformation`
--

DROP TABLE IF EXISTS `inventorinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventorinformation` (
  `materialID` int(11) NOT NULL,
  `shelfNumber` varchar(45) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `threshold` int(11) DEFAULT NULL,
  `newestInWarehouseDate` datetime DEFAULT NULL,
  PRIMARY KEY (`materialID`),
  CONSTRAINT `materialID4` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventorinformation`
--

LOCK TABLES `inventorinformation` WRITE;
/*!40000 ALTER TABLE `inventorinformation` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventorinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inwarehouse`
--

DROP TABLE IF EXISTS `inwarehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inwarehouse` (
  `id` int(11) NOT NULL,
  `inDate` datetime NOT NULL,
  `checker` varchar(45) NOT NULL,
  `operator` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inwarehouse`
--

LOCK TABLES `inwarehouse` WRITE;
/*!40000 ALTER TABLE `inwarehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `inwarehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inwarehouseproduct`
--

DROP TABLE IF EXISTS `inwarehouseproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inwarehouseproduct` (
  `inwarehouseID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`inwarehouseID`),
  KEY `materialID2_idx` (`materialID`),
  CONSTRAINT `inwarehouseID` FOREIGN KEY (`inwarehouseID`) REFERENCES `inwarehouse` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `materialID2` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inwarehouseproduct`
--

LOCK TABLES `inwarehouseproduct` WRITE;
/*!40000 ALTER TABLE `inwarehouseproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `inwarehouseproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `class` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialrequistion`
--

DROP TABLE IF EXISTS `materialrequistion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materialrequistion` (
  `id` int(11) NOT NULL,
  `distributionDate` datetime DEFAULT NULL,
  `requistioner` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `workshopNumber_idx` (`workshopID`),
  CONSTRAINT `workshopID` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialrequistion`
--

LOCK TABLES `materialrequistion` WRITE;
/*!40000 ALTER TABLE `materialrequistion` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialrequistion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `indentor` varchar(45) NOT NULL,
  `recevier` varchar(45) NOT NULL,
  `checker` varchar(45) NOT NULL,
  `recevierAddress` varchar(200) NOT NULL,
  `indentorPhoneNumber` varchar(45) NOT NULL,
  `totalPrice` decimal(3,0) NOT NULL,
  `status` varchar(45) NOT NULL,
  `deliveryDate` datetime NOT NULL,
  `paymentWay` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderproduct`
--

DROP TABLE IF EXISTS `orderproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderproduct` (
  `orderID` int(11) NOT NULL,
  `productID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`orderID`,`productID`),
  KEY `productID_idx` (`productID`),
  CONSTRAINT `orderID` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productID0` FOREIGN KEY (`productID`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderproduct`
--

LOCK TABLES `orderproduct` WRITE;
/*!40000 ALTER TABLE `orderproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outproduct`
--

DROP TABLE IF EXISTS `outproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outproduct` (
  `outwarehouseID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`outwarehouseID`,`materialID`),
  KEY `materialID1_idx` (`materialID`),
  CONSTRAINT `materialID1` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `outwarehouseID` FOREIGN KEY (`outwarehouseID`) REFERENCES `outwarehouse` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outproduct`
--

LOCK TABLES `outproduct` WRITE;
/*!40000 ALTER TABLE `outproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `outproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outwarehouse`
--

DROP TABLE IF EXISTS `outwarehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outwarehouse` (
  `id` int(11) NOT NULL,
  `outDate` datetime NOT NULL,
  `receiver` varchar(45) NOT NULL,
  `checker` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outwarehouse`
--

LOCK TABLES `outwarehouse` WRITE;
/*!40000 ALTER TABLE `outwarehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `outwarehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producetask`
--

DROP TABLE IF EXISTS `producetask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producetask` (
  `orderID` int(11) NOT NULL,
  `produceID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `beginDate` datetime NOT NULL,
  `deadline` datetime NOT NULL,
  PRIMARY KEY (`orderID`,`produceID`),
  KEY `produceID_idx` (`produceID`),
  CONSTRAINT `orderID3` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `produceID` FOREIGN KEY (`produceID`) REFERENCES `producetaskbasic` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producetask`
--

LOCK TABLES `producetask` WRITE;
/*!40000 ALTER TABLE `producetask` DISABLE KEYS */;
/*!40000 ALTER TABLE `producetask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producetaskbasic`
--

DROP TABLE IF EXISTS `producetaskbasic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producetaskbasic` (
  `id` int(11) NOT NULL,
  `personInCharge` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `produceStatus` varchar(45) DEFAULT NULL,
  `accurateDate` datetime DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  `orderID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `workshopID3_idx` (`workshopID`),
  KEY `orderID_idx` (`orderID`),
  CONSTRAINT `orderID1` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `workshopID3` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producetaskbasic`
--

LOCK TABLES `producetaskbasic` WRITE;
/*!40000 ALTER TABLE `producetaskbasic` DISABLE KEYS */;
/*!40000 ALTER TABLE `producetaskbasic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `class` varchar(45) NOT NULL,
  `price` decimal(3,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productmaterial`
--

DROP TABLE IF EXISTS `productmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productmaterial` (
  `productID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `procedure` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `comments` varchar(800) DEFAULT NULL,
  PRIMARY KEY (`productID`,`materialID`),
  KEY `materialID_idx` (`materialID`),
  CONSTRAINT `materialID0` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productID` FOREIGN KEY (`productID`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productmaterial`
--

LOCK TABLES `productmaterial` WRITE;
/*!40000 ALTER TABLE `productmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `productmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase` (
  `id` int(11) NOT NULL,
  `purchaser` varchar(45) NOT NULL,
  `date` datetime NOT NULL,
  `checker` varchar(45) NOT NULL,
  `totalPrice` decimal(3,0) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchaseproduct`
--

DROP TABLE IF EXISTS `purchaseproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchaseproduct` (
  `purchaseID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `price` decimal(3,0) NOT NULL,
  PRIMARY KEY (`purchaseID`),
  KEY `materialID3_idx` (`materialID`),
  CONSTRAINT `materialID3` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `purchaseID` FOREIGN KEY (`purchaseID`) REFERENCES `purchase` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchaseproduct`
--

LOCK TABLES `purchaseproduct` WRITE;
/*!40000 ALTER TABLE `purchaseproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchaseproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requisitionmaterial`
--

DROP TABLE IF EXISTS `requisitionmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requisitionmaterial` (
  `requisitionID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`requisitionID`,`materialID`),
  KEY `materialID5_idx` (`materialID`),
  CONSTRAINT `materialID5` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `requistionID` FOREIGN KEY (`requisitionID`) REFERENCES `materialrequistion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requisitionmaterial`
--

LOCK TABLES `requisitionmaterial` WRITE;
/*!40000 ALTER TABLE `requisitionmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `requisitionmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `position` int(11) NOT NULL,
  `permission` varchar(32) NOT NULL,
  `positionName` varchar(45) NOT NULL,
  PRIMARY KEY (`position`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `contact` varchar(45) NOT NULL,
  `phoneNumber` varchar(45) NOT NULL,
  `address` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliermaterial`
--

DROP TABLE IF EXISTS `suppliermaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `suppliermaterial` (
  `supplierID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `price` decimal(3,0) DEFAULT NULL,
  PRIMARY KEY (`supplierID`,`materialID`),
  KEY `materialID_idx` (`materialID`),
  CONSTRAINT `materialID` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `supplierID` FOREIGN KEY (`supplierID`) REFERENCES `supplier` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliermaterial`
--

LOCK TABLES `suppliermaterial` WRITE;
/*!40000 ALTER TABLE `suppliermaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `suppliermaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_table`
--

DROP TABLE IF EXISTS `user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_table` (
  `user_id` int(11) NOT NULL,
  `password` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `gender` varchar(45) NOT NULL,
  `dateOfEntry` datetime NOT NULL,
  `position` int(11) NOT NULL,
  `phoneNumber` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `position_idx` (`position`),
  CONSTRAINT `position` FOREIGN KEY (`position`) REFERENCES `role` (`position`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_table`
--

LOCK TABLES `user_table` WRITE;
/*!40000 ALTER TABLE `user_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop`
--

DROP TABLE IF EXISTS `workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workshop` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop`
--

LOCK TABLES `workshop` WRITE;
/*!40000 ALTER TABLE `workshop` DISABLE KEYS */;
/*!40000 ALTER TABLE `workshop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-13 23:14:24
