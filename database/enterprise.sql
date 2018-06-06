-- MySQL dump 10.13  Distrib 5.7.22, for Win64 (x86_64)
--
-- Host: localhost    Database: enterprise
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add supplier',7,'add_supplier'),(20,'Can change supplier',7,'change_supplier'),(21,'Can delete supplier',7,'delete_supplier'),(22,'Can add purchase product',8,'add_purchaseproduct'),(23,'Can change purchase product',8,'change_purchaseproduct'),(24,'Can delete purchase product',8,'delete_purchaseproduct'),(25,'Can add workshop',9,'add_workshop'),(26,'Can change workshop',9,'change_workshop'),(27,'Can delete workshop',9,'delete_workshop'),(28,'Can add order',10,'add_order'),(29,'Can change order',10,'change_order'),(30,'Can delete order',10,'delete_order'),(31,'Can add supplier material',11,'add_suppliermaterial'),(32,'Can change supplier material',11,'change_suppliermaterial'),(33,'Can delete supplier material',11,'delete_suppliermaterial'),(34,'Can add inventor information',12,'add_inventorinformation'),(35,'Can change inventor information',12,'change_inventorinformation'),(36,'Can delete inventor information',12,'delete_inventorinformation'),(37,'Can add user table',13,'add_usertable'),(38,'Can change user table',13,'change_usertable'),(39,'Can delete user table',13,'delete_usertable'),(40,'Can add out warehouse',14,'add_outwarehouse'),(41,'Can change out warehouse',14,'change_outwarehouse'),(42,'Can delete out warehouse',14,'delete_outwarehouse'),(43,'Can add product class',15,'add_productclass'),(44,'Can change product class',15,'change_productclass'),(45,'Can delete product class',15,'delete_productclass'),(46,'Can add inware house product',16,'add_inwarehouseproduct'),(47,'Can change inware house product',16,'change_inwarehouseproduct'),(48,'Can delete inware house product',16,'delete_inwarehouseproduct'),(49,'Can add product',17,'add_product'),(50,'Can change product',17,'change_product'),(51,'Can delete product',17,'delete_product'),(52,'Can add role',18,'add_role'),(53,'Can change role',18,'change_role'),(54,'Can delete role',18,'delete_role'),(55,'Can add material class',19,'add_materialclass'),(56,'Can change material class',19,'change_materialclass'),(57,'Can delete material class',19,'delete_materialclass'),(58,'Can add material requistion',20,'add_materialrequistion'),(59,'Can change material requistion',20,'change_materialrequistion'),(60,'Can delete material requistion',20,'delete_materialrequistion'),(61,'Can add produce task basic',21,'add_producetaskbasic'),(62,'Can change produce task basic',21,'change_producetaskbasic'),(63,'Can delete produce task basic',21,'delete_producetaskbasic'),(64,'Can add material',22,'add_material'),(65,'Can change material',22,'change_material'),(66,'Can delete material',22,'delete_material'),(67,'Can add product material',23,'add_productmaterial'),(68,'Can change product material',23,'change_productmaterial'),(69,'Can delete product material',23,'delete_productmaterial'),(70,'Can add purchase',24,'add_purchase'),(71,'Can change purchase',24,'change_purchase'),(72,'Can delete purchase',24,'delete_purchase'),(73,'Can add order product',25,'add_orderproduct'),(74,'Can change order product',25,'change_orderproduct'),(75,'Can delete order product',25,'delete_orderproduct'),(76,'Can add requisition material',26,'add_requisitionmaterial'),(77,'Can change requisition material',26,'change_requisitionmaterial'),(78,'Can delete requisition material',26,'delete_requisitionmaterial'),(79,'Can add out product',27,'add_outproduct'),(80,'Can change out product',27,'change_outproduct'),(81,'Can delete out product',27,'delete_outproduct'),(82,'Can add in warehouse',28,'add_inwarehouse'),(83,'Can change in warehouse',28,'change_inwarehouse'),(84,'Can delete in warehouse',28,'delete_inwarehouse');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(5,'contenttypes','contenttype'),(12,'enterprise','inventorinformation'),(28,'enterprise','inwarehouse'),(16,'enterprise','inwarehouseproduct'),(22,'enterprise','material'),(19,'enterprise','materialclass'),(20,'enterprise','materialrequistion'),(10,'enterprise','order'),(25,'enterprise','orderproduct'),(27,'enterprise','outproduct'),(14,'enterprise','outwarehouse'),(21,'enterprise','producetaskbasic'),(17,'enterprise','product'),(15,'enterprise','productclass'),(23,'enterprise','productmaterial'),(24,'enterprise','purchase'),(8,'enterprise','purchaseproduct'),(26,'enterprise','requisitionmaterial'),(18,'enterprise','role'),(7,'enterprise','supplier'),(11,'enterprise','suppliermaterial'),(13,'enterprise','usertable'),(9,'enterprise','workshop'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-05-30 08:48:12.993337'),(2,'auth','0001_initial','2018-05-30 08:48:14.401359'),(3,'admin','0001_initial','2018-05-30 08:48:14.666566'),(4,'admin','0002_logentry_remove_auto_add','2018-05-30 08:48:14.722607'),(5,'contenttypes','0002_remove_content_type_name','2018-05-30 08:48:15.111883'),(6,'auth','0002_alter_permission_name_max_length','2018-05-30 08:48:15.224463'),(7,'auth','0003_alter_user_email_max_length','2018-05-30 08:48:15.404091'),(8,'auth','0004_alter_user_username_opts','2018-05-30 08:48:15.447622'),(9,'auth','0005_alter_user_last_login_null','2018-05-30 08:48:15.556701'),(10,'auth','0006_require_contenttypes_0002','2018-05-30 08:48:15.567709'),(11,'auth','0007_alter_validators_add_error_messages','2018-05-30 08:48:15.585220'),(12,'auth','0008_alter_user_username_max_length','2018-05-30 08:48:15.684299'),(13,'enterprise','0001_initial','2018-05-30 08:48:22.095205'),(14,'sessions','0001_initial','2018-05-30 08:48:22.188271');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventorinformation`
--

DROP TABLE IF EXISTS `inventorinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventorinformation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shelfNumber` varchar(45) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `threshold` int(11) DEFAULT NULL,
  `newestInWarehouseDate` datetime(6) NOT NULL,
  `materialID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `materialID` (`materialID`),
  CONSTRAINT `inventorinformation_materialID_b9c0808e_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inDate` datetime(6) NOT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `operator` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `inwarehouseID` int(11) DEFAULT NULL,
  `materialID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `inwarehouseproduct_inwarehouseID_bd4ec6a1_fk_inwarehouse_id` (`inwarehouseID`),
  KEY `inwarehouseproduct_materialID_76447c95_fk_material_id` (`materialID`),
  CONSTRAINT `inwarehouseproduct_inwarehouseID_bd4ec6a1_fk_inwarehouse_id` FOREIGN KEY (`inwarehouseID`) REFERENCES `inwarehouse` (`id`),
  CONSTRAINT `inwarehouseproduct_materialID_76447c95_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `class_obj_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `material_class_obj_id_b68114a9_fk_materialclass_id` (`class_obj_id`),
  CONSTRAINT `material_class_obj_id_b68114a9_fk_materialclass_id` FOREIGN KEY (`class_obj_id`) REFERENCES `materialclass` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialclass`
--

DROP TABLE IF EXISTS `materialclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materialclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(45) NOT NULL,
  `parent_class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `materialclass_parent_class_id_6f92dd92_fk_materialclass_id` (`parent_class_id`),
  CONSTRAINT `materialclass_parent_class_id_6f92dd92_fk_materialclass_id` FOREIGN KEY (`parent_class_id`) REFERENCES `materialclass` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialclass`
--

LOCK TABLES `materialclass` WRITE;
/*!40000 ALTER TABLE `materialclass` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialrequistion`
--

DROP TABLE IF EXISTS `materialrequistion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materialrequistion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `distributionDate` datetime(6) NOT NULL,
  `requistioner` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `materialrequistion_workshopID_de009fe8_fk_workshop_id` (`workshopID`),
  CONSTRAINT `materialrequistion_workshopID_de009fe8_fk_workshop_id` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `indentor` varchar(45) DEFAULT NULL,
  `receiver` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `recevierAddress` varchar(200) DEFAULT NULL,
  `indentorPhoneNumber` varchar(45) DEFAULT NULL,
  `totalPrice` decimal(3,0) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `deliveryDate` datetime(6) NOT NULL,
  `paymentWay` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1000000008 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1000000000,'2018-05-30 00:00:00.000000','jack','nancy','brad','hsd','1511468',80,1,'2018-06-20 00:00:00.000000','wechat'),(1000000001,'2018-05-31 00:00:00.000000','ymk','wts','yanhua','100111','110',666,1,'2018-06-30 00:00:00.000000','wechat'),(1000000002,'2018-05-31 09:38:42.386654','jack','nancy','brad','hsd','1511468',80,1,'2018-05-31 09:38:42.440764','wechat'),(1000000003,'2018-06-06 14:28:12.703823','1','1','1','1301011','17602234658',2,0,'2018-06-06 14:28:12.706826','1'),(1000000004,'2018-06-06 15:49:53.360141','qwe','sdf','wt','130401','13882338086',8,0,'2018-06-06 15:49:53.360141','1'),(1000000005,'2018-06-06 15:53:12.529904','qwe','sdf','wt','130401','13882338086',8,0,'2018-06-06 15:53:12.529904','1'),(1000000006,'2018-06-06 16:08:46.203844','3445456','5345347','sdfh','120101ert','12345678900',278,0,'2018-06-06 16:08:46.204845','1'),(1000000007,'2018-06-06 16:11:23.323376','3445456','5345347','sdfh','120101ert','12345678900',278,0,'2018-06-06 16:11:23.324390','1');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderproduct`
--

DROP TABLE IF EXISTS `orderproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `price` decimal(3,0) NOT NULL,
  `orderID` int(11) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orderproduct_orderID_productID_305937dd_uniq` (`orderID`,`productID`),
  KEY `orderproduct_productID_1b0d0faf_fk_product_id` (`productID`),
  CONSTRAINT `orderproduct_orderID_ef417b74_fk_order_id` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`),
  CONSTRAINT `orderproduct_productID_1b0d0faf_fk_product_id` FOREIGN KEY (`productID`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderproduct`
--

LOCK TABLES `orderproduct` WRITE;
/*!40000 ALTER TABLE `orderproduct` DISABLE KEYS */;
INSERT INTO `orderproduct` VALUES (3,5,20,1000000000,1),(4,7,32,1000000000,2),(5,111,50,1000000007,3);
/*!40000 ALTER TABLE `orderproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outproduct`
--

DROP TABLE IF EXISTS `outproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `materialID` int(11) DEFAULT NULL,
  `outwarehouseID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `outproduct_outwarehouseID_materialID_2be8be1f_uniq` (`outwarehouseID`,`materialID`),
  KEY `outproduct_materialID_1151eef0_fk_material_id` (`materialID`),
  CONSTRAINT `outproduct_materialID_1151eef0_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `outproduct_outwarehouseID_70146b26_fk_outwarehouse_id` FOREIGN KEY (`outwarehouseID`) REFERENCES `outwarehouse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outDate` datetime(6) NOT NULL,
  `receiver` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outwarehouse`
--

LOCK TABLES `outwarehouse` WRITE;
/*!40000 ALTER TABLE `outwarehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `outwarehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producetaskbasic`
--

DROP TABLE IF EXISTS `producetaskbasic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producetaskbasic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `personInCharge` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `accurateDate` datetime(6) DEFAULT NULL,
  `number` int(11) NOT NULL,
  `beginDate` datetime(6) NOT NULL,
  `deadline` datetime(6) DEFAULT NULL,
  `orderID` int(11) DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producetaskbasic_orderID_9d80e3eb_fk_order_id` (`orderID`),
  KEY `producetaskbasic_workshopID_55daec85_fk_workshop_id` (`workshopID`),
  CONSTRAINT `producetaskbasic_orderID_9d80e3eb_fk_order_id` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`),
  CONSTRAINT `producetaskbasic_workshopID_55daec85_fk_workshop_id` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `price` decimal(3,0) NOT NULL,
  `class_obj_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_class_obj_id_9afe0b17_fk_productclass_id` (`class_obj_id`),
  CONSTRAINT `product_class_obj_id_9afe0b17_fk_productclass_id` FOREIGN KEY (`class_obj_id`) REFERENCES `productclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'testPro1',20,1),(2,'testPro2',32,1),(3,'luosi',50,1);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productclass`
--

DROP TABLE IF EXISTS `productclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(45) NOT NULL,
  `parent_class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productclass_parent_class_id_e23b7e9d_fk_productclass_id` (`parent_class_id`),
  CONSTRAINT `productclass_parent_class_id_e23b7e9d_fk_productclass_id` FOREIGN KEY (`parent_class_id`) REFERENCES `productclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productclass`
--

LOCK TABLES `productclass` WRITE;
/*!40000 ALTER TABLE `productclass` DISABLE KEYS */;
INSERT INTO `productclass` VALUES (1,'1',1),(2,'2',1);
/*!40000 ALTER TABLE `productclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productmaterial`
--

DROP TABLE IF EXISTS `productmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productmaterial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `procedure` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `comments` varchar(800) DEFAULT NULL,
  `materialID` int(11) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `productmaterial_productID_materialID_343e356f_uniq` (`productID`,`materialID`),
  KEY `productmaterial_materialID_c55fd103_fk_material_id` (`materialID`),
  CONSTRAINT `productmaterial_materialID_c55fd103_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `productmaterial_productID_47158ce5_fk_product_id` FOREIGN KEY (`productID`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `purchaser` varchar(45) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `totalPrice` decimal(3,0) NOT NULL,
  `supplier` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_supplier_be57dc8b_fk_supplier_id` (`supplier`),
  CONSTRAINT `purchase_supplier_be57dc8b_fk_supplier_id` FOREIGN KEY (`supplier`) REFERENCES `supplier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `price` decimal(3,0) NOT NULL,
  `materialID` int(11) DEFAULT NULL,
  `purchaseID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `purchaseproduct_purchaseID_materialID_19fdd9cb_uniq` (`purchaseID`,`materialID`),
  KEY `purchaseproduct_materialID_1d79e6f4_fk_material_id` (`materialID`),
  CONSTRAINT `purchaseproduct_materialID_1d79e6f4_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `purchaseproduct_purchaseID_9bf84e14_fk_purchase_id` FOREIGN KEY (`purchaseID`) REFERENCES `purchase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `materialID` int(11) DEFAULT NULL,
  `requisitionID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `requisitionmaterial_requisitionID_materialID_bb56e7a6_uniq` (`requisitionID`,`materialID`),
  KEY `requisitionmaterial_materialID_971289b6_fk_material_id` (`materialID`),
  CONSTRAINT `requisitionmaterial_materialID_971289b6_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `requisitionmaterial_requisitionID_9afad47d_fk_materialr` FOREIGN KEY (`requisitionID`) REFERENCES `materialrequistion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` int(11) NOT NULL,
  `permission` varchar(32) DEFAULT NULL,
  `positionName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(3,0) DEFAULT NULL,
  `materialID` int(11) DEFAULT NULL,
  `supplierID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suppliermaterial_supplierID_materialID_d2400962_uniq` (`supplierID`,`materialID`),
  KEY `suppliermaterial_materialID_58ef573a_fk_material_id` (`materialID`),
  CONSTRAINT `suppliermaterial_materialID_58ef573a_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `suppliermaterial_supplierID_61aca32d_fk_supplier_id` FOREIGN KEY (`supplierID`) REFERENCES `supplier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `gender` varchar(45) NOT NULL,
  `dateOfEntry` datetime(6) NOT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_table_position_0bc5084e_fk_role_id` (`position`),
  CONSTRAINT `user_table_position_0bc5084e_fk_role_id` FOREIGN KEY (`position`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `workshop_productID_59c77987_fk_product_id` (`productID`),
  CONSTRAINT `workshop_productID_59c77987_fk_product_id` FOREIGN KEY (`productID`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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

-- Dump completed on 2018-06-07  0:18:50
