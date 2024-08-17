-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2024 at 11:37 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lib`
--

-- --------------------------------------------------------

--
-- Table structure for table `addbook`
--

CREATE TABLE `addbook` (
  `studentid` int(11) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `bookid` int(11) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `author` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addbook`
--

INSERT INTO `addbook` (`studentid`, `studentname`, `bookid`, `bookname`, `author`) VALUES
(1, 'suba', 26, 'Mistery of book', 'suba'),
(2, 'priya', 27, 'colourfull life', 'priya');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Id` int(11) NOT NULL,
  `name` text NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Id`, `name`, `password`) VALUES
(1, 'Sri', 'sql');

-- --------------------------------------------------------

--
-- Table structure for table `bookdetail`
--

CREATE TABLE `bookdetail` (
  `bookid` int(11) DEFAULT NULL,
  `bookname` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `sno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookdetail`
--

INSERT INTO `bookdetail` (`bookid`, `bookname`, `author`, `sno`) VALUES
(10, 'Mistrey of book', 'Sara', 1),
(11, 'UI/UX Design', 'Steve Schoger', 2),
(12, 'Python Fundamentals', 'Rayan Marvin', 3),
(13, 'C Fundamentals', 'Brian Kernighan', 4),
(15, 'Advanced SQL', 'Joe Celko', 5),
(16, 'Java for Dummies', 'Barry A.Burd', 6),
(17, 'C++', 'John Smiley', 7),
(18, 'JavaScript Fundamentals', 'Marjin Haverbeke', 8),
(19, 'Designing with Figma', 'Fabio Staiano', 9),
(20, 'Html for Webdesigner', 'Elisabeth Robson', 10),
(21, 'JQUERY', 'Yehuda Katz', 11),
(23, 'ReactJS', 'Jordan Walke', 12),
(25, 'Freedom of bird', 'suba', 13),
(26, 'Mistery of book', 'suba', 14),
(27, 'colourfull life', 'priya', 15);

-- --------------------------------------------------------

--
-- Table structure for table `issuebook`
--

CREATE TABLE `issuebook` (
  `studentid` int(11) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `bookid` int(11) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL,
  `issuebook` text NOT NULL,
  `currentdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `issuebook`
--

INSERT INTO `issuebook` (`studentid`, `studentname`, `bookid`, `bookname`, `author`, `issuebook`, `currentdate`) VALUES
(1, 'suba', 25, 'Freedom of bird', 'suba', 'page 45 is damage', '2024-08-15');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `card_number` varchar(16) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `cvv` varchar(4) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_date` date NOT NULL DEFAULT current_timestamp(),
  `studentid` int(11) UNSIGNED NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `bookid` varchar(30) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `name`, `card_number`, `expiry_date`, `cvv`, `amount`, `payment_date`, `studentid`, `studentname`, `bookid`, `bookname`, `author`) VALUES
(3, 'atm', '2345', '2024-08-27', '123', 100.00, '2024-08-13', 1, 'suba', '10', 'tree', 'suba'),
(4, 'atm', '1234', '2024-08-29', '123', 100.00, '2024-08-15', 1, 'suba', '25', 'Freedom of bird', 'suba');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `studentid` int(11) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(30) NOT NULL,
  `conformpassword` varchar(30) NOT NULL,
  `cardname` varchar(30) NOT NULL,
  `cardnumber` int(16) NOT NULL,
  `cvv` int(11) NOT NULL,
  `regdate` date DEFAULT current_timestamp(),
  `amount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`studentid`, `studentname`, `email`, `phone`, `password`, `conformpassword`, `cardname`, `cardnumber`, `cvv`, `regdate`, `amount`) VALUES
(1, 'suba', 'suba@gmail.com', '7010601140', 'Suba@2004', 'Suba@2004', 'Atm', 1234, 123, '2024-08-13', 100.00);

-- --------------------------------------------------------

--
-- Table structure for table `returnbook`
--

CREATE TABLE `returnbook` (
  `studentid` int(11) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `bookid` int(11) UNSIGNED NOT NULL,
  `bookname` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `returnbook`
--

INSERT INTO `returnbook` (`studentid`, `studentname`, `bookid`, `bookname`, `author`, `return_date`) VALUES
(9, '', 25, 'Freedom of bird', 'suba', '2024-08-15');

-- --------------------------------------------------------

--
-- Table structure for table `takebook`
--

CREATE TABLE `takebook` (
  `studentid` int(11) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `bookid` int(11) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL,
  `due_date` date DEFAULT NULL,
  `date_borrowed` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `takebook`
--

INSERT INTO `takebook` (`studentid`, `studentname`, `bookid`, `bookname`, `author`, `due_date`, `date_borrowed`) VALUES
(1, 'suba', 25, 'Freedom of bird', 'suba', '2024-08-29', '2024-08-15');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addbook`
--
ALTER TABLE `addbook`
  ADD UNIQUE KEY `bookid` (`bookid`),
  ADD UNIQUE KEY `bookname` (`bookname`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `bookdetail`
--
ALTER TABLE `bookdetail`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `id` (`bookid`),
  ADD UNIQUE KEY `id_2` (`bookid`),
  ADD UNIQUE KEY `bookname` (`bookname`),
  ADD UNIQUE KEY `bookname_2` (`bookname`);

--
-- Indexes for table `issuebook`
--
ALTER TABLE `issuebook`
  ADD PRIMARY KEY (`studentid`),
  ADD UNIQUE KEY `bookid` (`bookid`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`studentid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `returnbook`
--
ALTER TABLE `returnbook`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `takebook`
--
ALTER TABLE `takebook`
  ADD PRIMARY KEY (`studentid`),
  ADD UNIQUE KEY `bookid` (`bookid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookdetail`
--
ALTER TABLE `bookdetail`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `issuebook`
--
ALTER TABLE `issuebook`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `returnbook`
--
ALTER TABLE `returnbook`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `takebook`
--
ALTER TABLE `takebook`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
