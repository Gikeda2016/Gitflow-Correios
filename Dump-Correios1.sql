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
  `codigocp` varchar(18) DEFAULT NULL,
  `statuscp` varchar(50) DEFAULT NULL,
  `datast` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `local` varchar(40) DEFAULT NULL,
  `finalizado` tinyint(1) DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL,
  `site` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (9,'Mamys','Memória 8Gb DDR4 Adata','2021-02-06','LB194177404HK','## JÁ CHEGOU!!! ##','2021-03-02','10:45:00','Cond. Japy',NULL,NULL,NULL),(11,'Mamys','Reletech ssd m2 512Gb','2021-02-08','LB214871100SG','Objeto em trânsito -','2021-02-11','22:53:00','CINGAPURA -->> BR',NULL,NULL,NULL),(32,'Papys','SSD 480Gb 2.5 SATA3','2021-02-06','LB196119948HK','## JÁ CHEGOU!!! ##','2021-03-10','11:39:00','Cond. Japy',NULL,'',NULL),(34,'Mamys','Mouse 3200dpi usb','2021-03-07','LP00435360528985','','0000-00-00','00:00:00','',NULL,'',NULL),(35,'Mamys','PenDrive 32GB SanDisk','2021-03-07','LP00435294361912','','0000-00-00','00:00:00','',NULL,'',NULL);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagamentos`
--

DROP TABLE IF EXISTS `pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagamentos` (
  `idpg` int NOT NULL AUTO_INCREMENT,
  `idcp` int DEFAULT NULL,
  `datapg` date NOT NULL,
  `valor` float NOT NULL,
  `parcelas` int DEFAULT NULL,
  `valorparc` float DEFAULT NULL,
  `statuspg` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idpg`),
  KEY `idcp` (`idcp`),
  CONSTRAINT `pagamentos_ibfk_1` FOREIGN KEY (`idcp`) REFERENCES `compras` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagamentos`
--

LOCK TABLES `pagamentos` WRITE;
/*!40000 ALTER TABLE `pagamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagamentos` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rastreios`
--

LOCK TABLES `rastreios` WRITE;
/*!40000 ALTER TABLE `rastreios` DISABLE KEYS */;
INSERT INTO `rastreios` VALUES (1,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-03-02','10:45','JUNDIAI / SP','Objeto entregue ao destinatário rogerio ferreira'),(2,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-03-02','08:37','JUNDIAI / SP','Objeto saiu -->> entrega ao destinatário'),(3,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-03-01','13:49','INDAIATUBA / SP','Objeto em trânsito - INDAIATUBA-SP -->> JUNDIAI-SP'),(4,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-22','09:28','CURITIBA / PR','Objeto em trânsito - CURITIBA-PR -->> INDAIATUBA-SP'),(5,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-22','09:26','CURITIBA / PR','Fiscalização aduaneira finalizada'),(6,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-22','07:49','CURITIBA / PR','Objeto recebido pelos Correios do Brasil '),(7,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-16','17:35','HONG KONG /','Objeto em trânsito - HONG KONG -->> BR '),(8,9,'Mamys','Memória 8Gb DDR4 Adata','LB194177404HK','2021-02-16','15:29','HONG KONG /','Objeto postado '),(9,11,'Mamys','Reletech ssd m2 512Gb','LB214871100SG','2021-02-11','22:53','CINGAPURA /','Objeto em trânsito - CINGAPURA -->> BR '),(10,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-10','11:39','JUNDIAI / SP','Objeto entregue ao destinatário'),(11,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-10','08:56','JUNDIAI / SP','Objeto saiu -->> entrega ao destinatário'),(12,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-08','08:01','INDAIATUBA / SP','Objeto em trânsito - INDAIATUBA-SP -->> JUNDIAI-SP'),(13,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-04','09:59','CURITIBA / PR','Objeto em trânsito - CURITIBA-PR -->> INDAIATUBA-SP'),(14,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-04','09:57','CURITIBA / PR','Fiscalização aduaneira finalizada'),(15,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-03-02','12:22','CURITIBA / PR','Objeto recebido pelos Correios do Brasil '),(16,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-02-24','15:10','HONG KONG /','Objeto em trânsito - HONG KONG -->> BR '),(17,32,'Papys','SSD 480Gb 2.5 SATA3','LB196119948HK','2021-02-23','16:52','HONG KONG /','Objeto postado ');
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

-- Dump completed on 2021-03-11  9:45:58
