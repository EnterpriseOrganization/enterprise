/*
Navicat MySQL Data Transfer

Source Server         : 1
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : enterprise

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-06-15 14:37:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `(material)requistion`
-- ----------------------------
DROP TABLE IF EXISTS `(material)requistion`;
CREATE TABLE `(material)requistion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `distributionDate` datetime(6) NOT NULL,
  `requistioner` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `checker` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `(material)requistion_workshopID_7cfec4e2_fk_workshop_id` (`workshopID`),
  CONSTRAINT `(material)requistion_workshopID_7cfec4e2_fk_workshop_id` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of (material)requistion
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add user', '2', 'add_user');
INSERT INTO `auth_permission` VALUES ('5', 'Can change user', '2', 'change_user');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete user', '2', 'delete_user');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add material class', '7', 'add_materialclass');
INSERT INTO `auth_permission` VALUES ('20', 'Can change material class', '7', 'change_materialclass');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete material class', '7', 'delete_materialclass');
INSERT INTO `auth_permission` VALUES ('22', 'Can add material', '8', 'add_material');
INSERT INTO `auth_permission` VALUES ('23', 'Can change material', '8', 'change_material');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete material', '8', 'delete_material');
INSERT INTO `auth_permission` VALUES ('25', 'Can add order', '9', 'add_order');
INSERT INTO `auth_permission` VALUES ('26', 'Can change order', '9', 'change_order');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete order', '9', 'delete_order');
INSERT INTO `auth_permission` VALUES ('28', 'Can add product class', '10', 'add_productclass');
INSERT INTO `auth_permission` VALUES ('29', 'Can change product class', '10', 'change_productclass');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete product class', '10', 'delete_productclass');
INSERT INTO `auth_permission` VALUES ('31', 'Can add product', '11', 'add_product');
INSERT INTO `auth_permission` VALUES ('32', 'Can change product', '11', 'change_product');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete product', '11', 'delete_product');
INSERT INTO `auth_permission` VALUES ('34', 'Can add workshop', '12', 'add_workshop');
INSERT INTO `auth_permission` VALUES ('35', 'Can change workshop', '12', 'change_workshop');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete workshop', '12', 'delete_workshop');
INSERT INTO `auth_permission` VALUES ('37', 'Can add produce task basic', '13', 'add_producetaskbasic');
INSERT INTO `auth_permission` VALUES ('38', 'Can change produce task basic', '13', 'change_producetaskbasic');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete produce task basic', '13', 'delete_producetaskbasic');
INSERT INTO `auth_permission` VALUES ('40', 'Can add out warehouse', '14', 'add_outwarehouse');
INSERT INTO `auth_permission` VALUES ('41', 'Can change out warehouse', '14', 'change_outwarehouse');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete out warehouse', '14', 'delete_outwarehouse');
INSERT INTO `auth_permission` VALUES ('43', 'Can add supplier', '15', 'add_supplier');
INSERT INTO `auth_permission` VALUES ('44', 'Can change supplier', '15', 'change_supplier');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete supplier', '15', 'delete_supplier');
INSERT INTO `auth_permission` VALUES ('46', 'Can add inventory information', '16', 'add_inventoryinformation');
INSERT INTO `auth_permission` VALUES ('47', 'Can change inventory information', '16', 'change_inventoryinformation');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete inventory information', '16', 'delete_inventoryinformation');
INSERT INTO `auth_permission` VALUES ('49', 'Can add in warehouse', '17', 'add_inwarehouse');
INSERT INTO `auth_permission` VALUES ('50', 'Can change in warehouse', '17', 'change_inwarehouse');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete in warehouse', '17', 'delete_inwarehouse');
INSERT INTO `auth_permission` VALUES ('52', 'Can add role', '18', 'add_role');
INSERT INTO `auth_permission` VALUES ('53', 'Can change role', '18', 'change_role');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete role', '18', 'delete_role');
INSERT INTO `auth_permission` VALUES ('55', 'Can add inware house product', '19', 'add_inwarehouseproduct');
INSERT INTO `auth_permission` VALUES ('56', 'Can change inware house product', '19', 'change_inwarehouseproduct');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete inware house product', '19', 'delete_inwarehouseproduct');
INSERT INTO `auth_permission` VALUES ('58', 'Can add material requistion', '20', 'add_materialrequistion');
INSERT INTO `auth_permission` VALUES ('59', 'Can change material requistion', '20', 'change_materialrequistion');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete material requistion', '20', 'delete_materialrequistion');
INSERT INTO `auth_permission` VALUES ('61', 'Can add order product', '21', 'add_orderproduct');
INSERT INTO `auth_permission` VALUES ('62', 'Can change order product', '21', 'change_orderproduct');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete order product', '21', 'delete_orderproduct');
INSERT INTO `auth_permission` VALUES ('64', 'Can add out product', '22', 'add_outproduct');
INSERT INTO `auth_permission` VALUES ('65', 'Can change out product', '22', 'change_outproduct');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete out product', '22', 'delete_outproduct');
INSERT INTO `auth_permission` VALUES ('67', 'Can add product material', '23', 'add_productmaterial');
INSERT INTO `auth_permission` VALUES ('68', 'Can change product material', '23', 'change_productmaterial');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete product material', '23', 'delete_productmaterial');
INSERT INTO `auth_permission` VALUES ('70', 'Can add purchase', '24', 'add_purchase');
INSERT INTO `auth_permission` VALUES ('71', 'Can change purchase', '24', 'change_purchase');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete purchase', '24', 'delete_purchase');
INSERT INTO `auth_permission` VALUES ('73', 'Can add purchase product', '25', 'add_purchaseproduct');
INSERT INTO `auth_permission` VALUES ('74', 'Can change purchase product', '25', 'change_purchaseproduct');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete purchase product', '25', 'delete_purchaseproduct');
INSERT INTO `auth_permission` VALUES ('76', 'Can add requisition material', '26', 'add_requisitionmaterial');
INSERT INTO `auth_permission` VALUES ('77', 'Can change requisition material', '26', 'change_requisitionmaterial');
INSERT INTO `auth_permission` VALUES ('78', 'Can delete requisition material', '26', 'delete_requisitionmaterial');
INSERT INTO `auth_permission` VALUES ('79', 'Can add supplier material', '27', 'add_suppliermaterial');
INSERT INTO `auth_permission` VALUES ('80', 'Can change supplier material', '27', 'change_suppliermaterial');
INSERT INTO `auth_permission` VALUES ('81', 'Can delete supplier material', '27', 'delete_suppliermaterial');
INSERT INTO `auth_permission` VALUES ('82', 'Can add user table', '28', 'add_usertable');
INSERT INTO `auth_permission` VALUES ('83', 'Can change user table', '28', 'change_usertable');
INSERT INTO `auth_permission` VALUES ('84', 'Can delete user table', '28', 'delete_usertable');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$6nghkzs9rekH$BKpHa2Iy+nnLEgkV4I9+vdt0ilTGQTYTe7/njDI7Ma0=', '2018-06-13 23:29:26.064802', '1', 'yhl', '', '', '', '1', '1', '2018-06-12 06:57:00.000000');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$36000$s6IDKvni3zY1$6O6X5GUMVo6bs50IC7gDyKTFQh6EuiDoRXyUSajg6EE=', '2018-06-13 23:28:00.000000', '0', 'demo', '', '', '', '0', '1', '2018-06-12 07:17:00.000000');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$36000$xNZE5u3t07qb$TUmuOAJSJyC9BVSH2gYhjqH7FG9FAMZtrJWkCktoJb0=', '2018-06-13 20:08:00.000000', '0', 'zcc', '', '', '', '0', '1', '2018-06-13 20:08:00.000000');
INSERT INTO `auth_user` VALUES ('4', 'pbkdf2_sha256$36000$afOgsjJIJ2IV$zy03xvkQdcuej3cvIDUhIfm7jg4ltDZNJFgY+6fp8n8=', '2018-06-13 21:45:10.769776', '0', 'myh', 'myh', '', '', '0', '1', '2018-06-13 21:44:00.000000');
INSERT INTO `auth_user` VALUES ('5', 'pbkdf2_sha256$36000$p4DkIhJvHBVe$ZUmoVxGtj1jByy28D8227Uwmg+bYRuvVOvRds16qg48=', '2018-06-14 02:24:21.708008', '1', 'root', 'root', '', 'yh_meng@qq.com', '1', '1', '2018-06-13 21:49:00.000000');
INSERT INTO `auth_user` VALUES ('6', 'pbkdf2_sha256$36000$1fnNcPU2buAG$hQjyklBBbYtPN6oqif3/M6OevYgxE9SWbhzizziWPcI=', '2018-06-14 02:02:51.622708', '0', 'yanhua', '', '', '', '0', '1', '2018-06-14 00:03:00.000000');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=568 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES ('85', '1', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('86', '1', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('87', '1', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('88', '1', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('89', '1', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('90', '1', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('91', '1', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('92', '1', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('93', '1', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('94', '1', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('95', '1', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('96', '1', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('97', '1', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('98', '1', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('99', '1', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('100', '1', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('101', '1', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('102', '1', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('103', '1', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('104', '1', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('105', '1', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('106', '1', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('107', '1', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('108', '1', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('109', '1', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('110', '1', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('111', '1', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('112', '1', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('113', '1', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('114', '1', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('115', '1', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('116', '1', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('117', '1', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('118', '1', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('119', '1', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('120', '1', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('121', '1', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('122', '1', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('123', '1', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('124', '1', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('125', '1', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('126', '1', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('127', '1', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('128', '1', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('129', '1', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('130', '1', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('131', '1', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('132', '1', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('133', '1', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('134', '1', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('135', '1', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('136', '1', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('137', '1', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('138', '1', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('139', '1', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('140', '1', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('141', '1', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('142', '1', '58');
INSERT INTO `auth_user_user_permissions` VALUES ('143', '1', '59');
INSERT INTO `auth_user_user_permissions` VALUES ('144', '1', '60');
INSERT INTO `auth_user_user_permissions` VALUES ('145', '1', '61');
INSERT INTO `auth_user_user_permissions` VALUES ('146', '1', '62');
INSERT INTO `auth_user_user_permissions` VALUES ('147', '1', '63');
INSERT INTO `auth_user_user_permissions` VALUES ('148', '1', '64');
INSERT INTO `auth_user_user_permissions` VALUES ('149', '1', '65');
INSERT INTO `auth_user_user_permissions` VALUES ('150', '1', '66');
INSERT INTO `auth_user_user_permissions` VALUES ('151', '1', '67');
INSERT INTO `auth_user_user_permissions` VALUES ('152', '1', '68');
INSERT INTO `auth_user_user_permissions` VALUES ('153', '1', '69');
INSERT INTO `auth_user_user_permissions` VALUES ('154', '1', '70');
INSERT INTO `auth_user_user_permissions` VALUES ('155', '1', '71');
INSERT INTO `auth_user_user_permissions` VALUES ('156', '1', '72');
INSERT INTO `auth_user_user_permissions` VALUES ('157', '1', '73');
INSERT INTO `auth_user_user_permissions` VALUES ('158', '1', '74');
INSERT INTO `auth_user_user_permissions` VALUES ('159', '1', '75');
INSERT INTO `auth_user_user_permissions` VALUES ('160', '1', '76');
INSERT INTO `auth_user_user_permissions` VALUES ('161', '1', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('162', '1', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('163', '1', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('164', '1', '80');
INSERT INTO `auth_user_user_permissions` VALUES ('165', '1', '81');
INSERT INTO `auth_user_user_permissions` VALUES ('166', '1', '82');
INSERT INTO `auth_user_user_permissions` VALUES ('167', '1', '83');
INSERT INTO `auth_user_user_permissions` VALUES ('168', '1', '84');
INSERT INTO `auth_user_user_permissions` VALUES ('490', '2', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('491', '2', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('492', '2', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('493', '2', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('494', '2', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('495', '2', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('496', '2', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('497', '2', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('498', '2', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('499', '2', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('500', '2', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('501', '2', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('502', '2', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('503', '2', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('504', '2', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('505', '2', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('506', '2', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('507', '2', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('508', '2', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('509', '2', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('510', '2', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('511', '2', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('512', '2', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('513', '2', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('310', '2', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('311', '2', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('312', '2', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('514', '2', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('515', '2', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('516', '2', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('517', '2', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('518', '2', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('519', '2', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('520', '2', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('521', '2', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('522', '2', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('523', '2', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('524', '2', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('525', '2', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('526', '2', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('527', '2', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('528', '2', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('318', '2', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('319', '2', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('320', '2', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('529', '2', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('530', '2', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('531', '2', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('532', '2', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('533', '2', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('534', '2', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('535', '2', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('536', '2', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('537', '2', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('538', '2', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('539', '2', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('540', '2', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('541', '2', '58');
INSERT INTO `auth_user_user_permissions` VALUES ('542', '2', '59');
INSERT INTO `auth_user_user_permissions` VALUES ('543', '2', '60');
INSERT INTO `auth_user_user_permissions` VALUES ('313', '2', '61');
INSERT INTO `auth_user_user_permissions` VALUES ('314', '2', '62');
INSERT INTO `auth_user_user_permissions` VALUES ('315', '2', '63');
INSERT INTO `auth_user_user_permissions` VALUES ('544', '2', '64');
INSERT INTO `auth_user_user_permissions` VALUES ('545', '2', '65');
INSERT INTO `auth_user_user_permissions` VALUES ('546', '2', '66');
INSERT INTO `auth_user_user_permissions` VALUES ('547', '2', '67');
INSERT INTO `auth_user_user_permissions` VALUES ('548', '2', '68');
INSERT INTO `auth_user_user_permissions` VALUES ('549', '2', '69');
INSERT INTO `auth_user_user_permissions` VALUES ('307', '2', '70');
INSERT INTO `auth_user_user_permissions` VALUES ('308', '2', '71');
INSERT INTO `auth_user_user_permissions` VALUES ('309', '2', '72');
INSERT INTO `auth_user_user_permissions` VALUES ('550', '2', '73');
INSERT INTO `auth_user_user_permissions` VALUES ('551', '2', '74');
INSERT INTO `auth_user_user_permissions` VALUES ('552', '2', '75');
INSERT INTO `auth_user_user_permissions` VALUES ('553', '2', '76');
INSERT INTO `auth_user_user_permissions` VALUES ('554', '2', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('555', '2', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('321', '2', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('316', '2', '80');
INSERT INTO `auth_user_user_permissions` VALUES ('317', '2', '81');
INSERT INTO `auth_user_user_permissions` VALUES ('556', '2', '82');
INSERT INTO `auth_user_user_permissions` VALUES ('557', '2', '83');
INSERT INTO `auth_user_user_permissions` VALUES ('558', '2', '84');
INSERT INTO `auth_user_user_permissions` VALUES ('253', '3', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('254', '3', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('255', '3', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('256', '3', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('257', '3', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('258', '3', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('193', '3', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('194', '3', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('195', '3', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('259', '3', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('260', '3', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('261', '3', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('262', '3', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('263', '3', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('264', '3', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('265', '3', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('266', '3', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('267', '3', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('268', '3', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('269', '3', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('270', '3', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('271', '3', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('272', '3', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('273', '3', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('274', '3', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('275', '3', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('276', '3', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('277', '3', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('278', '3', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('279', '3', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('280', '3', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('281', '3', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('282', '3', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('283', '3', '58');
INSERT INTO `auth_user_user_permissions` VALUES ('284', '3', '59');
INSERT INTO `auth_user_user_permissions` VALUES ('285', '3', '60');
INSERT INTO `auth_user_user_permissions` VALUES ('286', '3', '61');
INSERT INTO `auth_user_user_permissions` VALUES ('287', '3', '62');
INSERT INTO `auth_user_user_permissions` VALUES ('288', '3', '63');
INSERT INTO `auth_user_user_permissions` VALUES ('289', '3', '64');
INSERT INTO `auth_user_user_permissions` VALUES ('290', '3', '65');
INSERT INTO `auth_user_user_permissions` VALUES ('291', '3', '66');
INSERT INTO `auth_user_user_permissions` VALUES ('292', '3', '67');
INSERT INTO `auth_user_user_permissions` VALUES ('293', '3', '68');
INSERT INTO `auth_user_user_permissions` VALUES ('294', '3', '69');
INSERT INTO `auth_user_user_permissions` VALUES ('295', '3', '70');
INSERT INTO `auth_user_user_permissions` VALUES ('296', '3', '71');
INSERT INTO `auth_user_user_permissions` VALUES ('297', '3', '72');
INSERT INTO `auth_user_user_permissions` VALUES ('298', '3', '73');
INSERT INTO `auth_user_user_permissions` VALUES ('299', '3', '74');
INSERT INTO `auth_user_user_permissions` VALUES ('300', '3', '75');
INSERT INTO `auth_user_user_permissions` VALUES ('301', '3', '76');
INSERT INTO `auth_user_user_permissions` VALUES ('302', '3', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('303', '3', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('304', '3', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('305', '3', '80');
INSERT INTO `auth_user_user_permissions` VALUES ('306', '3', '81');
INSERT INTO `auth_user_user_permissions` VALUES ('322', '4', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('323', '4', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('324', '4', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('325', '4', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('326', '4', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('327', '4', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('328', '4', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('329', '4', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('330', '4', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('331', '4', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('332', '4', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('333', '4', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('334', '4', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('335', '4', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('336', '4', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('337', '4', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('338', '4', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('339', '4', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('340', '4', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('341', '4', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('342', '4', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('343', '4', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('344', '4', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('345', '4', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('346', '4', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('347', '4', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('348', '4', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('349', '4', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('350', '4', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('351', '4', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('352', '4', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('353', '4', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('354', '4', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('355', '4', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('356', '4', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('357', '4', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('358', '4', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('359', '4', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('360', '4', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('361', '4', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('362', '4', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('363', '4', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('364', '4', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('365', '4', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('366', '4', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('367', '4', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('368', '4', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('369', '4', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('370', '4', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('371', '4', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('372', '4', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('373', '4', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('374', '4', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('375', '4', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('376', '4', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('377', '4', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('378', '4', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('379', '4', '58');
INSERT INTO `auth_user_user_permissions` VALUES ('380', '4', '59');
INSERT INTO `auth_user_user_permissions` VALUES ('381', '4', '60');
INSERT INTO `auth_user_user_permissions` VALUES ('382', '4', '61');
INSERT INTO `auth_user_user_permissions` VALUES ('383', '4', '62');
INSERT INTO `auth_user_user_permissions` VALUES ('384', '4', '63');
INSERT INTO `auth_user_user_permissions` VALUES ('385', '4', '64');
INSERT INTO `auth_user_user_permissions` VALUES ('386', '4', '65');
INSERT INTO `auth_user_user_permissions` VALUES ('387', '4', '66');
INSERT INTO `auth_user_user_permissions` VALUES ('388', '4', '67');
INSERT INTO `auth_user_user_permissions` VALUES ('389', '4', '68');
INSERT INTO `auth_user_user_permissions` VALUES ('390', '4', '69');
INSERT INTO `auth_user_user_permissions` VALUES ('391', '4', '70');
INSERT INTO `auth_user_user_permissions` VALUES ('392', '4', '71');
INSERT INTO `auth_user_user_permissions` VALUES ('393', '4', '72');
INSERT INTO `auth_user_user_permissions` VALUES ('394', '4', '73');
INSERT INTO `auth_user_user_permissions` VALUES ('395', '4', '74');
INSERT INTO `auth_user_user_permissions` VALUES ('396', '4', '75');
INSERT INTO `auth_user_user_permissions` VALUES ('397', '4', '76');
INSERT INTO `auth_user_user_permissions` VALUES ('398', '4', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('399', '4', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('400', '4', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('401', '4', '80');
INSERT INTO `auth_user_user_permissions` VALUES ('402', '4', '81');
INSERT INTO `auth_user_user_permissions` VALUES ('403', '4', '82');
INSERT INTO `auth_user_user_permissions` VALUES ('404', '4', '83');
INSERT INTO `auth_user_user_permissions` VALUES ('405', '4', '84');
INSERT INTO `auth_user_user_permissions` VALUES ('406', '5', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('407', '5', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('408', '5', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('409', '5', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('410', '5', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('411', '5', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('412', '5', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('413', '5', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('414', '5', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('415', '5', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('416', '5', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('417', '5', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('418', '5', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('419', '5', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('420', '5', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('421', '5', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('422', '5', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('423', '5', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('424', '5', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('425', '5', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('426', '5', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('427', '5', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('428', '5', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('429', '5', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('430', '5', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('431', '5', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('432', '5', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('433', '5', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('434', '5', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('435', '5', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('436', '5', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('437', '5', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('438', '5', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('439', '5', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('440', '5', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('441', '5', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('442', '5', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('443', '5', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('444', '5', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('445', '5', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('446', '5', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('447', '5', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('448', '5', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('449', '5', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('450', '5', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('451', '5', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('452', '5', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('453', '5', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('454', '5', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('455', '5', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('456', '5', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('457', '5', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('458', '5', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('459', '5', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('460', '5', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('461', '5', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('462', '5', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('463', '5', '58');
INSERT INTO `auth_user_user_permissions` VALUES ('464', '5', '59');
INSERT INTO `auth_user_user_permissions` VALUES ('465', '5', '60');
INSERT INTO `auth_user_user_permissions` VALUES ('466', '5', '61');
INSERT INTO `auth_user_user_permissions` VALUES ('467', '5', '62');
INSERT INTO `auth_user_user_permissions` VALUES ('468', '5', '63');
INSERT INTO `auth_user_user_permissions` VALUES ('469', '5', '64');
INSERT INTO `auth_user_user_permissions` VALUES ('470', '5', '65');
INSERT INTO `auth_user_user_permissions` VALUES ('471', '5', '66');
INSERT INTO `auth_user_user_permissions` VALUES ('472', '5', '67');
INSERT INTO `auth_user_user_permissions` VALUES ('473', '5', '68');
INSERT INTO `auth_user_user_permissions` VALUES ('474', '5', '69');
INSERT INTO `auth_user_user_permissions` VALUES ('475', '5', '70');
INSERT INTO `auth_user_user_permissions` VALUES ('476', '5', '71');
INSERT INTO `auth_user_user_permissions` VALUES ('477', '5', '72');
INSERT INTO `auth_user_user_permissions` VALUES ('478', '5', '73');
INSERT INTO `auth_user_user_permissions` VALUES ('479', '5', '74');
INSERT INTO `auth_user_user_permissions` VALUES ('480', '5', '75');
INSERT INTO `auth_user_user_permissions` VALUES ('481', '5', '76');
INSERT INTO `auth_user_user_permissions` VALUES ('482', '5', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('483', '5', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('484', '5', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('485', '5', '80');
INSERT INTO `auth_user_user_permissions` VALUES ('486', '5', '81');
INSERT INTO `auth_user_user_permissions` VALUES ('487', '5', '82');
INSERT INTO `auth_user_user_permissions` VALUES ('488', '5', '83');
INSERT INTO `auth_user_user_permissions` VALUES ('489', '5', '84');
INSERT INTO `auth_user_user_permissions` VALUES ('564', '6', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('565', '6', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('566', '6', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('559', '6', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('560', '6', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('561', '6', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('567', '6', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('562', '6', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('563', '6', '33');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-06-12 07:17:48.393203', '2', 'demo', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-06-12 07:17:56.724156', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-06-13 11:59:15.699565', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-06-13 19:48:17.287196', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-06-13 19:48:46.276171', '1', 'yhl', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-06-13 19:49:15.925963', '1', 'yhl', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-06-13 19:54:07.766105', '1', 'yhl', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-06-13 19:59:28.893032', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-06-13 20:08:18.332213', '3', 'zcc', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-06-13 20:08:27.015851', '3', 'zcc', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-06-13 20:24:34.394695', '3', 'zcc', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-06-13 20:25:25.095523', '3', 'zcc', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-06-13 21:02:26.778520', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-06-13 21:05:36.019764', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-06-13 21:26:56.264966', '1', 'yhl', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2018-06-13 21:27:22.613114', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2018-06-13 21:43:38.119344', '1', 'yhl', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2018-06-13 21:44:12.684334', '4', 'myh', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2018-06-13 21:44:24.675457', '4', 'myh', '2', '[{\"changed\": {\"fields\": [\"first_name\", \"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2018-06-13 21:50:11.786100', '5', 'root', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('21', '2018-06-13 21:51:26.463553', '5', 'root', '2', '[]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('22', '2018-06-13 22:02:27.035250', '5', 'root', '2', '[{\"changed\": {\"fields\": [\"first_name\"]}}]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('23', '2018-06-13 22:15:31.391010', '5', 'root', '2', '[{\"changed\": {\"fields\": [\"email\", \"last_login\"]}}]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('24', '2018-06-13 23:29:57.925169', '2', 'demo', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2018-06-14 00:03:27.229694', '6', 'yanhua', '1', '[{\"added\": {}}]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('26', '2018-06-14 00:04:03.595847', '6', 'yanhua', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '5');
INSERT INTO `django_admin_log` VALUES ('27', '2018-06-14 00:21:49.560723', '6', 'yanhua', '2', '[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]', '2', '5');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('16', 'enterprise', 'inventoryinformation');
INSERT INTO `django_content_type` VALUES ('17', 'enterprise', 'inwarehouse');
INSERT INTO `django_content_type` VALUES ('19', 'enterprise', 'inwarehouseproduct');
INSERT INTO `django_content_type` VALUES ('8', 'enterprise', 'material');
INSERT INTO `django_content_type` VALUES ('7', 'enterprise', 'materialclass');
INSERT INTO `django_content_type` VALUES ('20', 'enterprise', 'materialrequistion');
INSERT INTO `django_content_type` VALUES ('9', 'enterprise', 'order');
INSERT INTO `django_content_type` VALUES ('21', 'enterprise', 'orderproduct');
INSERT INTO `django_content_type` VALUES ('22', 'enterprise', 'outproduct');
INSERT INTO `django_content_type` VALUES ('14', 'enterprise', 'outwarehouse');
INSERT INTO `django_content_type` VALUES ('13', 'enterprise', 'producetaskbasic');
INSERT INTO `django_content_type` VALUES ('11', 'enterprise', 'product');
INSERT INTO `django_content_type` VALUES ('10', 'enterprise', 'productclass');
INSERT INTO `django_content_type` VALUES ('23', 'enterprise', 'productmaterial');
INSERT INTO `django_content_type` VALUES ('24', 'enterprise', 'purchase');
INSERT INTO `django_content_type` VALUES ('25', 'enterprise', 'purchaseproduct');
INSERT INTO `django_content_type` VALUES ('26', 'enterprise', 'requisitionmaterial');
INSERT INTO `django_content_type` VALUES ('18', 'enterprise', 'role');
INSERT INTO `django_content_type` VALUES ('15', 'enterprise', 'supplier');
INSERT INTO `django_content_type` VALUES ('27', 'enterprise', 'suppliermaterial');
INSERT INTO `django_content_type` VALUES ('28', 'enterprise', 'usertable');
INSERT INTO `django_content_type` VALUES ('12', 'enterprise', 'workshop');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-06-12 06:44:14.494770');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-06-12 06:44:29.675689');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-06-12 06:44:32.965612');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-06-12 06:44:33.035609');
INSERT INTO `django_migrations` VALUES ('5', 'app_product', '0001_initial', '2018-06-12 06:44:33.490230');
INSERT INTO `django_migrations` VALUES ('6', 'app_product', '0002_delete_producetest', '2018-06-12 06:44:33.850223');
INSERT INTO `django_migrations` VALUES ('7', 'contenttypes', '0002_remove_content_type_name', '2018-06-12 06:44:39.657454');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2018-06-12 06:44:41.114508');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2018-06-12 06:44:41.354540');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2018-06-12 06:44:41.424490');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2018-06-12 06:44:42.343331');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2018-06-12 06:44:42.413328');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2018-06-12 06:44:42.483323');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2018-06-12 06:44:44.293957');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-06-12 06:44:45.033911');
INSERT INTO `django_migrations` VALUES ('16', 'enterprise', '0001_initial', '2018-06-12 06:46:50.153803');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1ik8c6dbpmaz4phjmaxjmi1hc7ob5g5e', 'MmFlZTBmMmEwNmYwMjRmNWNmNzY2Zjg3NzVlYjIwODE1YWI2MzgyZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDgxMmQ5MzdhMmRjNmY4MGZkYTBiZjg0MWQ1NGYxOWQwNmZkNjdkZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=', '2018-06-27 22:15:53.371825');
INSERT INTO `django_session` VALUES ('1rjym5w7kp66agpbvf9ww69p1mtpmf1e', 'ZjAyNDhiYWE2ZTc3OTM4MDE1ZDhkNmMxOTA0ZjhhYWQ2MDQ4NzdhNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTEyNzU0MmE2NmFmMzc2NWIzY2M1MjI0NDE4ODQyOGUwZDA5M2I2MiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-06-27 19:55:44.775967');
INSERT INTO `django_session` VALUES ('9sxb2u78md8bywnqgb9t5q0u3bjlfycn', 'MjMyZTAxMzVlMTMzYjljNDgzZmJhN2RmMjBkMDg2NzA4MGMxYTMwYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjA4MTJkOTM3YTJkYzZmODBmZGEwYmY4NDFkNTRmMTlkMDZmZDY3ZGQiLCJfYXV0aF91c2VyX2lkIjoiNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-06-27 23:42:07.873618');
INSERT INTO `django_session` VALUES ('bm7y5hrdrrf6zvi7dkzrs6sfq2ixp1dl', 'N2NkMjc5MTY5YmUzZDIyZDQzMTc3YjJkZDVlNTBlOTRmOWZhM2FjNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWRkMjk5MWYwMmY4ZTYxOTg2MGE0ZjI1ODI3MTRlZTFmNmU3NGU3ZiIsIl9hdXRoX3VzZXJfaWQiOiI1In0=', '2018-06-28 02:24:21.848926');
INSERT INTO `django_session` VALUES ('c6yw1kzt67b9wj89ldwtcj9xziibivi1', 'YTA4OTkzYjYwYmExODY1OGJmZjRiNTBkMTZhZDkyZmJkNGM4ZjJlOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjUiLCJfYXV0aF91c2VyX2hhc2giOiIwODEyZDkzN2EyZGM2ZjgwZmRhMGJmODQxZDU0ZjE5ZDA2ZmQ2N2RkIn0=', '2018-06-27 23:01:38.869649');
INSERT INTO `django_session` VALUES ('dy9yj0i5l2olo7y86d9zgkzo7qd5ani9', 'YTA4OTkzYjYwYmExODY1OGJmZjRiNTBkMTZhZDkyZmJkNGM4ZjJlOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjUiLCJfYXV0aF91c2VyX2hhc2giOiIwODEyZDkzN2EyZGM2ZjgwZmRhMGJmODQxZDU0ZjE5ZDA2ZmQ2N2RkIn0=', '2018-06-27 22:24:35.162316');
INSERT INTO `django_session` VALUES ('hr63oh96sqcnkmwati39bste0v59kzcf', 'MjMyZTAxMzVlMTMzYjljNDgzZmJhN2RmMjBkMDg2NzA4MGMxYTMwYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjA4MTJkOTM3YTJkYzZmODBmZGEwYmY4NDFkNTRmMTlkMDZmZDY3ZGQiLCJfYXV0aF91c2VyX2lkIjoiNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-06-27 23:42:07.784203');
INSERT INTO `django_session` VALUES ('i9dg4ryfcywoxtswc2kppg9y2cmwkur8', 'YTA4OTkzYjYwYmExODY1OGJmZjRiNTBkMTZhZDkyZmJkNGM4ZjJlOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjUiLCJfYXV0aF91c2VyX2hhc2giOiIwODEyZDkzN2EyZGM2ZjgwZmRhMGJmODQxZDU0ZjE5ZDA2ZmQ2N2RkIn0=', '2018-06-27 23:12:21.017281');
INSERT INTO `django_session` VALUES ('ksoq1k28kdmu4fn1eud0qb2ex1nkmjfk', 'ODYxYmQ1OTVlODJlNjA4MTk2OTc3Mjg1MGE3NzE5YzM0ZTU2ZjI1OTp7fQ==', '2018-06-27 12:34:04.182802');
INSERT INTO `django_session` VALUES ('pnmb2i2kxolclc51hap5ad2cenu5rqml', 'ODM1YzM1YmU5MDgyZGZhZGQ5NjI0YzQ4OThhNWUzNDk3OWFmNDA0Yjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjE3YzZkN2M1NDMwZDlmOGE3OGVkMTliNTMyMGUzYmM0ODQxMzk4In0=', '2018-06-27 22:56:33.447803');
INSERT INTO `django_session` VALUES ('s31dgq0g1goklp7wnixmcopthxqqjncg', 'ODYxYmQ1OTVlODJlNjA4MTk2OTc3Mjg1MGE3NzE5YzM0ZTU2ZjI1OTp7fQ==', '2018-06-27 12:34:04.177804');
INSERT INTO `django_session` VALUES ('uswi70831b04y6v0qg0lio3mirx3kno0', 'N2NkMjc5MTY5YmUzZDIyZDQzMTc3YjJkZDVlNTBlOTRmOWZhM2FjNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWRkMjk5MWYwMmY4ZTYxOTg2MGE0ZjI1ODI3MTRlZTFmNmU3NGU3ZiIsIl9hdXRoX3VzZXJfaWQiOiI1In0=', '2018-06-28 01:31:44.627460');
INSERT INTO `django_session` VALUES ('uz0tsb7wx3ezqpytn5mn97ow1mll8oev', 'N2NkMjc5MTY5YmUzZDIyZDQzMTc3YjJkZDVlNTBlOTRmOWZhM2FjNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWRkMjk5MWYwMmY4ZTYxOTg2MGE0ZjI1ODI3MTRlZTFmNmU3NGU3ZiIsIl9hdXRoX3VzZXJfaWQiOiI1In0=', '2018-06-28 01:26:23.259260');
INSERT INTO `django_session` VALUES ('vzbwsqyerfaj8j1mvj27d3w4ed0pe4sz', 'ODYxYmQ1OTVlODJlNjA4MTk2OTc3Mjg1MGE3NzE5YzM0ZTU2ZjI1OTp7fQ==', '2018-06-27 12:34:04.177804');
INSERT INTO `django_session` VALUES ('yoxqklqc6gff2rdtcny4h9iowel943rb', 'ODYxYmQ1OTVlODJlNjA4MTk2OTc3Mjg1MGE3NzE5YzM0ZTU2ZjI1OTp7fQ==', '2018-06-27 12:34:04.131830');
INSERT INTO `django_session` VALUES ('yzw4sp8cv31wypj1iau1lw2l3qdf7jwq', 'ZjZjNzg0MmMxMWUyZTJiOTZlNjNlY2JlMWI1Y2FlYjAzYjc2YTM0NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNmNWRmYmZmYjEyNzE2MjkyOGQwZDNkYWY0NWIyM2RkZjM0ODc2MDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=', '2018-06-28 00:04:43.772335');

-- ----------------------------
-- Table structure for `inventoryinformation`
-- ----------------------------
DROP TABLE IF EXISTS `inventoryinformation`;
CREATE TABLE `inventoryinformation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shelfNumber` varchar(45) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `threshold` int(11) DEFAULT NULL,
  `newestInWarehouseDate` datetime(6) NOT NULL,
  `(material)ID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `(material)ID` (`(material)ID`),
  CONSTRAINT `inventoryinformation_(material)ID_815b8b53_fk_material_id` FOREIGN KEY (`(material)ID`) REFERENCES `material` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of inventoryinformation
-- ----------------------------
INSERT INTO `inventoryinformation` VALUES ('1', 'A', '21', '43', '2018-06-14 01:39:07.851797', '1');
INSERT INTO `inventoryinformation` VALUES ('2', 'A', '32', '43', '2018-06-13 21:47:58.000000', '2');
INSERT INTO `inventoryinformation` VALUES ('3', 'a', '12', '100', '2018-06-14 01:37:34.879827', '4');
INSERT INTO `inventoryinformation` VALUES ('4', 'A', '2', '100', '2018-06-13 23:02:27.283322', '5');

-- ----------------------------
-- Table structure for `inwarehouse`
-- ----------------------------
DROP TABLE IF EXISTS `inwarehouse`;
CREATE TABLE `inwarehouse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inDate` datetime(6) NOT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `operator` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of inwarehouse
-- ----------------------------
INSERT INTO `inwarehouse` VALUES ('1', '2018-06-13 23:01:53.977624', 's', 's');
INSERT INTO `inwarehouse` VALUES ('2', '2018-06-13 23:02:26.990474', 'a', 'a');
INSERT INTO `inwarehouse` VALUES ('3', '2018-06-14 00:31:24.852168', 'adf', 'asdfsf');
INSERT INTO `inwarehouse` VALUES ('4', '2018-06-14 01:36:32.907579', 'asdf', 'adsf');
INSERT INTO `inwarehouse` VALUES ('5', '2018-06-14 01:37:34.723915', 'asdf', 'asd');
INSERT INTO `inwarehouse` VALUES ('6', '2018-06-14 01:39:07.765848', 'asdf', 'asdf');

-- ----------------------------
-- Table structure for `inwarehouseproduct`
-- ----------------------------
DROP TABLE IF EXISTS `inwarehouseproduct`;
CREATE TABLE `inwarehouseproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `inwarehouseID` int(11) DEFAULT NULL,
  `(material)ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `inwarehouseproduct_inwarehouseID_bd4ec6a1_fk_inwarehouse_id` (`inwarehouseID`),
  KEY `inwarehouseproduct_(material)ID_1044816c_fk_material_id` (`(material)ID`),
  CONSTRAINT `inwarehouseproduct_(material)ID_1044816c_fk_material_id` FOREIGN KEY (`(material)ID`) REFERENCES `material` (`id`),
  CONSTRAINT `inwarehouseproduct_inwarehouseID_bd4ec6a1_fk_inwarehouse_id` FOREIGN KEY (`inwarehouseID`) REFERENCES `inwarehouse` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of inwarehouseproduct
-- ----------------------------
INSERT INTO `inwarehouseproduct` VALUES ('1', '1', '1', '4');
INSERT INTO `inwarehouseproduct` VALUES ('2', '2', '2', '5');
INSERT INTO `inwarehouseproduct` VALUES ('3', '1', '3', '4');
INSERT INTO `inwarehouseproduct` VALUES ('4', '10', '4', '1');
INSERT INTO `inwarehouseproduct` VALUES ('5', '10', '5', '4');
INSERT INTO `inwarehouseproduct` VALUES ('6', '2', '6', '1');

-- ----------------------------
-- Table structure for `material`
-- ----------------------------
DROP TABLE IF EXISTS `material`;
CREATE TABLE `material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `class_obj_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `material_class_obj_id_b68114a9_fk_materialclass_id` (`class_obj_id`),
  CONSTRAINT `material_class_obj_id_b68114a9_fk_materialclass_id` FOREIGN KEY (`class_obj_id`) REFERENCES `materialclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of material
-- ----------------------------
INSERT INTO `material` VALUES ('1', 'a', '1');
INSERT INTO `material` VALUES ('2', 'b', '1');
INSERT INTO `material` VALUES ('3', 'material3', '1');
INSERT INTO `material` VALUES ('4', 'sen', '2');
INSERT INTO `material` VALUES ('5', 's', '2');

-- ----------------------------
-- Table structure for `materialclass`
-- ----------------------------
DROP TABLE IF EXISTS `materialclass`;
CREATE TABLE `materialclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(45) NOT NULL,
  `parent_class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `materialclass_parent_class_id_6f92dd92_fk_materialclass_id` (`parent_class_id`),
  CONSTRAINT `materialclass_parent_class_id_6f92dd92_fk_materialclass_id` FOREIGN KEY (`parent_class_id`) REFERENCES `materialclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of materialclass
-- ----------------------------
INSERT INTO `materialclass` VALUES ('1', 'root', '1');
INSERT INTO `materialclass` VALUES ('2', '2', '1');

-- ----------------------------
-- Table structure for `order`
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `indentor` varchar(45) DEFAULT NULL,
  `receiver` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `recevierAddress` varchar(200) DEFAULT NULL,
  `indentorPhoneNumber` varchar(45) DEFAULT NULL,
  `totalPrice` decimal(10,3) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `deliveryDate` datetime(6) NOT NULL,
  `paymentWay` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('13', '2018-06-12 16:00:00.000000', 'asd', 'asd', 'asd', '210106sd', '17713582805', '96.000', '0', '2018-06-12 16:00:00.000000', '1');
INSERT INTO `order` VALUES ('14', '2018-06-13 23:44:01.396168', 'yh', 'yh', 'yh', '210106sd', '17713582805', '64.000', '1', '2018-06-13 23:44:01.396168', '1');
INSERT INTO `order` VALUES ('16', '2018-06-14 01:16:19.229579', 'indentor 0', 'reveiver 0', 'checker 0', null, null, null, '0', '2018-06-14 01:16:19.229579', 'default paymentway');
INSERT INTO `order` VALUES ('17', '2018-06-14 01:16:19.428531', 'indentor 1', 'reveiver 1', 'checker 1', null, null, null, '1', '2018-06-14 01:16:19.428531', 'default paymentway');
INSERT INTO `order` VALUES ('18', '2018-06-14 01:16:19.563454', 'indentor 2', 'reveiver 2', 'checker 2', null, null, null, '2', '2018-06-14 01:16:19.563454', 'default paymentway');
INSERT INTO `order` VALUES ('19', '2018-06-14 01:16:19.638410', 'indentor 3', 'reveiver 3', 'checker 3', null, null, null, '3', '2018-06-14 01:16:19.638410', 'default paymentway');
INSERT INTO `order` VALUES ('20', '2018-06-14 01:16:19.738360', 'indentor 4', 'reveiver 4', 'checker 4', null, null, null, '0', '2018-06-14 01:16:19.738360', 'default paymentway');
INSERT INTO `order` VALUES ('21', '2018-06-14 01:16:19.821305', 'indentor 5', 'reveiver 5', 'checker 5', null, null, null, '1', '2018-06-14 01:16:19.821305', 'default paymentway');
INSERT INTO `order` VALUES ('22', '2018-06-14 01:16:19.871276', 'indentor 6', 'reveiver 6', 'checker 6', null, null, null, '2', '2018-06-14 01:16:19.871276', 'default paymentway');
INSERT INTO `order` VALUES ('23', '2018-06-14 01:16:19.921247', 'indentor 7', 'reveiver 7', 'checker 7', null, null, null, '3', '2018-06-14 01:16:19.921247', 'default paymentway');
INSERT INTO `order` VALUES ('24', '2018-06-14 01:16:19.971254', 'indentor 8', 'reveiver 8', 'checker 8', null, null, null, '0', '2018-06-14 01:16:19.972234', 'default paymentway');
INSERT INTO `order` VALUES ('25', '2018-06-14 01:16:20.038180', 'indentor 9', 'reveiver 9', 'checker 9', null, null, null, '1', '2018-06-14 01:16:20.038180', 'default paymentway');
INSERT INTO `order` VALUES ('26', '2018-06-14 01:16:20.071162', 'indentor 10', 'reveiver 10', 'checker 10', null, null, null, '2', '2018-06-14 01:16:20.071162', 'default paymentway');
INSERT INTO `order` VALUES ('27', '2018-06-14 01:16:20.130127', 'indentor 11', 'reveiver 11', 'checker 11', null, null, null, '3', '2018-06-14 01:16:20.130127', 'default paymentway');
INSERT INTO `order` VALUES ('28', '2018-06-14 01:16:20.188093', 'indentor 12', 'reveiver 12', 'checker 12', null, null, null, '0', '2018-06-14 01:16:20.188093', 'default paymentway');
INSERT INTO `order` VALUES ('29', '2018-06-14 01:34:55.074035', '123', '123', '123', '110101123', '12345678901', '210.000', '0', '2018-06-14 01:34:55.074035', '1');

-- ----------------------------
-- Table structure for `orderproduct`
-- ----------------------------
DROP TABLE IF EXISTS `orderproduct`;
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of orderproduct
-- ----------------------------
INSERT INTO `orderproduct` VALUES ('15', '2', '32', '13', '4');
INSERT INTO `orderproduct` VALUES ('16', '2', '32', '14', '3');
INSERT INTO `orderproduct` VALUES ('18', '10', '21', '29', '5');

-- ----------------------------
-- Table structure for `outproduct`
-- ----------------------------
DROP TABLE IF EXISTS `outproduct`;
CREATE TABLE `outproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `(material)ID` int(11) DEFAULT NULL,
  `outwarehouseID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `outproduct_outwarehouseID_(material)ID_ba38dffb_uniq` (`outwarehouseID`,`(material)ID`),
  KEY `outproduct_(material)ID_e8a241c5_fk_material_id` (`(material)ID`),
  CONSTRAINT `outproduct_(material)ID_e8a241c5_fk_material_id` FOREIGN KEY (`(material)ID`) REFERENCES `material` (`id`),
  CONSTRAINT `outproduct_outwarehouseID_70146b26_fk_outwarehouse_id` FOREIGN KEY (`outwarehouseID`) REFERENCES `outwarehouse` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of outproduct
-- ----------------------------
INSERT INTO `outproduct` VALUES ('1', '11', '1', '1');
INSERT INTO `outproduct` VALUES ('2', '1', '1', '2');

-- ----------------------------
-- Table structure for `outwarehouse`
-- ----------------------------
DROP TABLE IF EXISTS `outwarehouse`;
CREATE TABLE `outwarehouse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outDate` datetime(6) NOT NULL,
  `receiver` varchar(45) DEFAULT NULL,
  `checker` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of outwarehouse
-- ----------------------------
INSERT INTO `outwarehouse` VALUES ('1', '2018-06-13 23:25:01.454413', 'a', 'a');
INSERT INTO `outwarehouse` VALUES ('2', '2018-06-14 01:36:56.644695', 'fasdf', 'asdf');

-- ----------------------------
-- Table structure for `producetaskbasic`
-- ----------------------------
DROP TABLE IF EXISTS `producetaskbasic`;
CREATE TABLE `producetaskbasic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `personInCharge` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `accurateDate` date DEFAULT NULL,
  `number` int(11) NOT NULL,
  `beginDate` date NOT NULL,
  `done_checker` varchar(100) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `material_getter` varchar(100) NOT NULL,
  `material_checker` varchar(100) NOT NULL,
  `material_distributon_date` date DEFAULT NULL,
  `orderID` int(11) DEFAULT NULL,
  `workshopID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producetaskbasic_orderID_9d80e3eb_fk_order_id` (`orderID`),
  KEY `producetaskbasic_workshopID_55daec85_fk_workshop_id` (`workshopID`),
  CONSTRAINT `producetaskbasic_orderID_9d80e3eb_fk_order_id` FOREIGN KEY (`orderID`) REFERENCES `order` (`id`),
  CONSTRAINT `producetaskbasic_workshopID_55daec85_fk_workshop_id` FOREIGN KEY (`workshopID`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of producetaskbasic
-- ----------------------------
INSERT INTO `producetaskbasic` VALUES ('5', '', '', '0', null, '2', '2018-06-14', '', null, '', '', null, '14', '9');

-- ----------------------------
-- Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `price` decimal(3,0) NOT NULL,
  `class_obj_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_class_obj_id_9afe0b17_fk_productclass_id` (`class_obj_id`),
  CONSTRAINT `product_class_obj_id_9afe0b17_fk_productclass_id` FOREIGN KEY (`class_obj_id`) REFERENCES `productclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', 'sen', '32', '1');
INSERT INTO `product` VALUES ('2', 'wts', '32', '1');
INSERT INTO `product` VALUES ('3', 'yhl', '32', '1');
INSERT INTO `product` VALUES ('4', '啊', '32', '1');
INSERT INTO `product` VALUES ('5', 'yyh', '21', '1');
INSERT INTO `product` VALUES ('6', 'B1', '23', '2');
INSERT INTO `product` VALUES ('7', 'Product 0', '0', '1');
INSERT INTO `product` VALUES ('8', 'Product 1', '10', '1');
INSERT INTO `product` VALUES ('9', 'Product 2', '20', '1');
INSERT INTO `product` VALUES ('10', 'Product 3', '30', '1');
INSERT INTO `product` VALUES ('11', 'Product 4', '40', '1');
INSERT INTO `product` VALUES ('12', 'Product 5', '50', '1');
INSERT INTO `product` VALUES ('13', 'Product 6', '60', '1');
INSERT INTO `product` VALUES ('14', 'Product 7', '70', '1');
INSERT INTO `product` VALUES ('15', 'Product 8', '80', '1');
INSERT INTO `product` VALUES ('16', 'Product 9', '90', '1');
INSERT INTO `product` VALUES ('17', 'Product 10', '100', '1');
INSERT INTO `product` VALUES ('18', 'Product 11', '110', '1');
INSERT INTO `product` VALUES ('19', 'Product 12', '120', '1');
INSERT INTO `product` VALUES ('20', 'Product 13', '130', '1');
INSERT INTO `product` VALUES ('21', 'Product 14', '140', '1');
INSERT INTO `product` VALUES ('22', 'Product 15', '150', '1');
INSERT INTO `product` VALUES ('23', 'Product 16', '160', '1');
INSERT INTO `product` VALUES ('24', 'Product 17', '170', '1');
INSERT INTO `product` VALUES ('25', 'Product 18', '180', '1');
INSERT INTO `product` VALUES ('26', 'Product 19', '190', '1');
INSERT INTO `product` VALUES ('27', 'Product 20', '200', '1');
INSERT INTO `product` VALUES ('28', 'Product 21', '210', '1');

-- ----------------------------
-- Table structure for `productclass`
-- ----------------------------
DROP TABLE IF EXISTS `productclass`;
CREATE TABLE `productclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(45) NOT NULL,
  `parent_class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productclass_parent_class_id_e23b7e9d_fk_productclass_id` (`parent_class_id`),
  CONSTRAINT `productclass_parent_class_id_e23b7e9d_fk_productclass_id` FOREIGN KEY (`parent_class_id`) REFERENCES `productclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of productclass
-- ----------------------------
INSERT INTO `productclass` VALUES ('1', 'root', '1');
INSERT INTO `productclass` VALUES ('2', 'root2', '2');
INSERT INTO `productclass` VALUES ('3', 'BaseClass', null);
INSERT INTO `productclass` VALUES ('4', 'ProductClass 0', '3');
INSERT INTO `productclass` VALUES ('5', 'ProductClass 1', '3');
INSERT INTO `productclass` VALUES ('6', 'ProductClass 2', '3');
INSERT INTO `productclass` VALUES ('7', 'ProductClass 3', '2');
INSERT INTO `productclass` VALUES ('8', 'ProductClass 4', '3');
INSERT INTO `productclass` VALUES ('9', 'ProductClass 5', '4');
INSERT INTO `productclass` VALUES ('10', 'ProductClass 6', '5');
INSERT INTO `productclass` VALUES ('11', 'ProductClass 7', '6');
INSERT INTO `productclass` VALUES ('12', 'ProductClass 8', '7');
INSERT INTO `productclass` VALUES ('13', 'ProductClass 9', '8');

-- ----------------------------
-- Table structure for `productmaterial`
-- ----------------------------
DROP TABLE IF EXISTS `productmaterial`;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of productmaterial
-- ----------------------------
INSERT INTO `productmaterial` VALUES ('1', '1', '1', '1', '1', '2');
INSERT INTO `productmaterial` VALUES ('2', '1', '1', '1', '2', '1');
INSERT INTO `productmaterial` VALUES ('3', '3', '23', 'as', '3', '3');

-- ----------------------------
-- Table structure for `purchase`
-- ----------------------------
DROP TABLE IF EXISTS `purchase`;
CREATE TABLE `purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `purchaser` varchar(45) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `checker` varchar(45) DEFAULT NULL,
  `totalPrice` decimal(10,3) DEFAULT NULL,
  `supplier` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_supplier_be57dc8b_fk_supplier_id` (`supplier`),
  CONSTRAINT `purchase_supplier_be57dc8b_fk_supplier_id` FOREIGN KEY (`supplier`) REFERENCES `supplier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of purchase
-- ----------------------------
INSERT INTO `purchase` VALUES ('1', 'MYH', '2018-06-13 12:09:43.582112', 'TPS', '12.000', '1');

-- ----------------------------
-- Table structure for `purchaseproduct`
-- ----------------------------
DROP TABLE IF EXISTS `purchaseproduct`;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of purchaseproduct
-- ----------------------------
INSERT INTO `purchaseproduct` VALUES ('1', '5', '12', '1', '1');
INSERT INTO `purchaseproduct` VALUES ('2', '5', '12', '2', '1');

-- ----------------------------
-- Table structure for `requisitionmaterial`
-- ----------------------------
DROP TABLE IF EXISTS `requisitionmaterial`;
CREATE TABLE `requisitionmaterial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `materialID` int(11) DEFAULT NULL,
  `requisitionID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `requisitionmaterial_requisitionID_materialID_bb56e7a6_uniq` (`requisitionID`,`materialID`),
  KEY `requisitionmaterial_materialID_971289b6_fk_material_id` (`materialID`),
  CONSTRAINT `requisitionmaterial_materialID_971289b6_fk_material_id` FOREIGN KEY (`materialID`) REFERENCES `material` (`id`),
  CONSTRAINT `requisitionmaterial_requisitionID_9afad47d_fk_(material` FOREIGN KEY (`requisitionID`) REFERENCES `(material)requistion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of requisitionmaterial
-- ----------------------------

-- ----------------------------
-- Table structure for `role`
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` int(11) NOT NULL,
  `permission` varchar(32) DEFAULT NULL,
  `positionName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of role
-- ----------------------------

-- ----------------------------
-- Table structure for `supplier`
-- ----------------------------
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE `supplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of supplier
-- ----------------------------
INSERT INTO `supplier` VALUES ('1', 'yunfei', 'no', '17713582805', 'Nk');
INSERT INTO `supplier` VALUES ('2', 'test', 'no', '12345678901', 'test');

-- ----------------------------
-- Table structure for `suppliermaterial`
-- ----------------------------
DROP TABLE IF EXISTS `suppliermaterial`;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of suppliermaterial
-- ----------------------------
INSERT INTO `suppliermaterial` VALUES ('1', '123', '1', '1');
INSERT INTO `suppliermaterial` VALUES ('2', '100', '3', '2');
INSERT INTO `suppliermaterial` VALUES ('3', '11', '1', '2');

-- ----------------------------
-- Table structure for `user_table`
-- ----------------------------
DROP TABLE IF EXISTS `user_table`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of user_table
-- ----------------------------

-- ----------------------------
-- Table structure for `workshop`
-- ----------------------------
DROP TABLE IF EXISTS `workshop`;
CREATE TABLE `workshop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `workshop_productID_59c77987_fk_product_id` (`productID`),
  CONSTRAINT `workshop_productID_59c77987_fk_product_id` FOREIGN KEY (`productID`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of workshop
-- ----------------------------
INSERT INTO `workshop` VALUES ('1', 'work1', null);
INSERT INTO `workshop` VALUES ('2', 'work2', null);
INSERT INTO `workshop` VALUES ('3', 'work3', null);
INSERT INTO `workshop` VALUES ('4', 'Workshop 0', '1');
INSERT INTO `workshop` VALUES ('5', 'Workshop 1', '2');
INSERT INTO `workshop` VALUES ('6', 'Workshop 2', '3');
INSERT INTO `workshop` VALUES ('7', 'Workshop 3', '1');
INSERT INTO `workshop` VALUES ('8', 'Workshop 4', '2');
INSERT INTO `workshop` VALUES ('9', 'Workshop 5', '3');
INSERT INTO `workshop` VALUES ('10', 'Workshop 6', '1');
INSERT INTO `workshop` VALUES ('11', 'Workshop 7', '2');
INSERT INTO `workshop` VALUES ('12', 'Workshop 8', '3');
INSERT INTO `workshop` VALUES ('13', 'Workshop 9', '1');
