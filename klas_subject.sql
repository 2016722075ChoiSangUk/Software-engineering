-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: klas
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `학정번호` varchar(255) NOT NULL,
  `과목명` varchar(255) DEFAULT NULL,
  `이수구분` varchar(255) DEFAULT NULL,
  `학점` int DEFAULT NULL,
  `시간` varchar(255) DEFAULT NULL,
  `담당교수` varchar(255) DEFAULT NULL,
  `강의시간` varchar(255) DEFAULT NULL,
  `강의유형` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`학정번호`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES ('H020-1-0019-01','C프로그래밍 C1','교필',3,'3','유지현','월3,수4',NULL),('H020-1-0019-02','C프로그래밍 C2','교필',3,'3','이우신','화4,목3',NULL),('H020-1-0019-03','C프로그래밍 C3','교필',3,'3','이우신','화5,목6',NULL),('H020-1-8101-01','컴퓨터공학입문세미나','전선',2,'2','박철수','수6,7','세미나강의'),('H020-2-0453-01','디지털논리회로1','전필',3,'3','유지현','금5,6',NULL),('H020-2-0453-02','디지털논리회로1','전필',3,'3','유지현','화1,목2',NULL),('H020-2-0819-01','선형대수학','기선',3,'3','박철수','목5','영어50%,원격수업50%이상'),('H020-2-0819-02','선형대수학','기선',3,'3','김상목','월5,수6','영어60%'),('H020-2-1234-01','진로탐색및설계','타학과생 수강불가',1,'2','이기훈','화2,3','원격수업100%'),('H020-2-1994-01','회로이론','전선',3,'3','황호영','월5,수6','영어50%'),('H020-2-1994-02','회로이론','전선',3,'3','황호영','월6,수5','영어50%'),('H020-2-8086-01','컴퓨터공학기초실험1','전선',2,'4','유지현','월0,1,2',NULL),('H020-2-8086-02','컴퓨터공학기초실험1','전선',2,'4','이형근','수0,1,2',NULL),('H020-2-8086-03','컴퓨터공학기초실험1','전선',2,'4','신동화','금0,1,2',NULL),('H020-2-8481-01','객체지향프로그래밍설계','전필',3,'3','심동규','월3,수4','영어50%,PBL강의'),('H020-2-8481-02','객체지향프로그래밍설계','전필',3,'3','신동화','월4,수3','영어50%,PBL강의'),('H020-2-8482-01','객체지향프로그래밍실습','전선',1,'2','신동화','목7,8',NULL),('H020-2-8482-02','객체지향프로그래밍실습','전선',1,'2','이기훈','금3,4',NULL),('H020-2-8482-03','객체지향프로그래밍실습','전선',1,'2','이혁준','화7,8',NULL),('H020-3-0922-01','시스템프로그래밍','전필',3,'3','김태석','월5,수6','영어50%'),('H020-3-0922-02','시스템프로그래밍','전필',3,'3','최상호','월2,수1','영어50%'),('H020-3-1647-01','컴퓨터구조','전필',3,'3','이성원','월3,수4','영어50%'),('H020-3-1654-01','컴퓨터네트워크','전선',3,'3','이혁준','화5,목6','영어50%'),('H020-3-1942-01','확률및통계','기선',3,'3','신동화','화6,목5',NULL),('H020-3-2004-01','신호및시스템','전선',3,'3','이성원','월4,수3','영어50%'),('H020-3-3704-01','시스템프로그래밍실습','전선',1,'2','최상호','금1,2',NULL),('H020-3-3704-02','시스템프로그래밍실습','전선',1,'2','이기훈','금5,6',NULL),('H020-3-3704-03','시스템프로그래밍실습','전선',1,'2','김태석','금7,8',NULL),('H020-3-3831-01','컴퓨터구조실험','전선',1,'2','이성원','수7,8',NULL),('H020-3-3831-02','컴퓨터구조실험','전선',1,'2','이혁준','금3,4',NULL),('H020-3-8993-01','소프트웨어프로젝트1','전선',3,'4','이우신','월1,7,8,수2',NULL),('H020-4-0846-01','소프트웨어공학','전선',3,'3','이기훈','월5,수6','영어50%'),('H020-4-3112-01','무선이동네트워크및5G','전선',3,'3','이형근','화5,목6','영어50%'),('H020-4-4136-01','컴퓨터비젼','전선',3,'3','심동규','월4,수3','영어50%'),('H020-4-5861-01','임베디드시스템S/W설계','전선',3,'3','김태석','월6,수5','영어50%'),('H020-4-8995-01','산학협력캡스톤설계1','전선',3,'3','이형근','화6,목5','영어50%,TBL강의');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-16 18:11:10
