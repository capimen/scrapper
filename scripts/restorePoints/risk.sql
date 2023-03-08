-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: riskFactor
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `det_riskDataField_owner`
--

DROP TABLE IF EXISTS `det_riskDataField_owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `det_riskDataField_owner` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `idRiskDataField` int DEFAULT NULL,
  `idOwner` int DEFAULT NULL,
  `riskFactor` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `det_riskDataField_owner`
--

LOCK TABLES `det_riskDataField_owner` WRITE;
/*!40000 ALTER TABLE `det_riskDataField_owner` DISABLE KEYS */;
INSERT INTO `det_riskDataField_owner` VALUES (1,1,1,20);
/*!40000 ALTER TABLE `det_riskDataField_owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `det_user_RO`
--

DROP TABLE IF EXISTS `det_user_RO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `det_user_RO` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `idUser` varchar(45) DEFAULT NULL,
  `idDetRO` varchar(45) DEFAULT NULL,
  `valueRO` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `det_user_RO`
--

LOCK TABLES `det_user_RO` WRITE;
/*!40000 ALTER TABLE `det_user_RO` DISABLE KEYS */;
INSERT INTO `det_user_RO` VALUES (1,'1','1',5);
/*!40000 ALTER TABLE `det_user_RO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ownerApplication`
--

DROP TABLE IF EXISTS `ownerApplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ownerApplication` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `owner` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ownerApplication`
--

LOCK TABLES `ownerApplication` WRITE;
/*!40000 ALTER TABLE `ownerApplication` DISABLE KEYS */;
INSERT INTO `ownerApplication` VALUES (1,'Evaluador de riesgo');
/*!40000 ALTER TABLE `ownerApplication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riskDataField`
--

DROP TABLE IF EXISTS `riskDataField`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riskDataField` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `field` varchar(60) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riskDataField`
--

LOCK TABLES `riskDataField` WRITE;
/*!40000 ALTER TABLE `riskDataField` DISABLE KEYS */;
INSERT INTO `riskDataField` VALUES (1,'grasa','cantidad de grasa');
/*!40000 ALTER TABLE `riskDataField` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Cristhian Plaza');
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

-- Dump completed on 2022-11-28 12:33:26
