CREATE DATABASE  IF NOT EXISTS `correios` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `correios`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: correios
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(55) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `produto` varchar(50) NOT NULL,
  `datacp` date DEFAULT NULL,
  `codigocp` varchar(15) DEFAULT NULL,
  `statuscp` varchar(50) DEFAULT NULL,
  `datast` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `local` varchar(40) DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL,
  `site` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (6,'Mamys','MousePad Rosa e Azul',NULL,'SYAE003321625','','0000-00-00','00:00:00','','Chegou 10-jan e sem possibilidade de rastreio','...'),(9,'Mamys','Memória 8Gb DDR4 Adata','2021-02-06','LB194177404HK','Objeto em trânsito -','2021-02-16','17:35:00','HONG KONG -->> BR',NULL,NULL),(10,'Mamys','Mouse 6 botões 3200dpi','2021-02-06','LB194153853HK','## JÁ CHEGOU!!! ##','2021-02-18','15:29:00','Cond. Japy',NULL,NULL),(11,'Mamys','Reletech ssd m2 512Gb','2021-02-08','LB214871100SG','Objeto em trânsito -','2021-02-11','22:53:00','CINGAPURA -->> BR',NULL,NULL),(32,'Papys','SSD 480Gb 2.5 SATA3','2021-02-06','LB196119948HK','','0000-00-00','00:00:00','','',NULL);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rastreios`
--

DROP TABLE IF EXISTS `rastreios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rastreios` (
  `idrst` int NOT NULL AUTO_INCREMENT,
  `idprod` int NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `produto` varchar(50) DEFAULT NULL,
  `codigo` varchar(15) DEFAULT NULL,
  `data` char(12) DEFAULT NULL,
  `hora` char(5) DEFAULT NULL,
  `local` varchar(20) DEFAULT NULL,
  `mens` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idrst`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rastreios`
--

LOCK TABLES `rastreios` WRITE;
/*!40000 ALTER TABLE `rastreios` DISABLE KEYS */;
INSERT INTO `rastreios` VALUES (1,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-16','17:35','HONG KONG /','Objeto em trânsito - HONG KONG -->> BR '),(2,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-16','15:29','HONG KONG /','Objeto postado '),(3,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-18','15:29','JUNDIAI / SP','Objeto entregue ao destinatário'),(4,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-18','08:37','JUNDIAI / SP','Objeto saiu -->> entrega ao destinatário'),(5,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-17','10:02','INDAIATUBA / SP','Objeto em trânsito - INDAIATUBA-SP -->> JUNDIAI-SP'),(6,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-15','09:28','CURITIBA / PR','Objeto em trânsito - CURITIBA-PR -->> INDAIATUBA-SP'),(7,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-15','09:26','CURITIBA / PR','Fiscalização aduaneira finalizada'),(8,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-13','10:24','CURITIBA / PR','Objeto recebido pelos Correios do Brasil '),(9,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-10','14:08','HONG KONG /','Objeto em trânsito - HONG KONG -->> BR '),(10,10,'Mamys','Mouse 6 botões 3200dpi','LB194153853HK','2021-02-09','17:12','HONG KONG /','Objeto postado '),(11,11,'Mamys','Reletech ssd m2 512Gb','LB214871100SG','2021-02-11','22:53','CINGAPURA /','Objeto em trânsito - CINGAPURA -->> BR ');
/*!40000 ALTER TABLE `rastreios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-19 22:45:54
