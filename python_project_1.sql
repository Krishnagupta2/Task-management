-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 04, 2022 at 12:22 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `addemployee`
--

CREATE TABLE `addemployee` (
  `id` int(11) NOT NULL,
  `EmpId` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Contact` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `DOJ` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addemployee`
--

INSERT INTO `addemployee` (`id`, `EmpId`, `Name`, `Email`, `Password`, `Contact`, `Address`, `DOJ`) VALUES
(1, 1, 'Ajay', 'ajay@gmail.com', '123456', '2147483647', 'jalandhar', '2022-07-04'),
(2, 2, 'aman', 'aman@gmail.com', '123', '9876543215', 'hoshiarpur', '2022-08-04');

-- --------------------------------------------------------

--
-- Table structure for table `addproject`
--

CREATE TABLE `addproject` (
  `id` int(11) NOT NULL,
  `ProName` varchar(30) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `details` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addproject`
--

INSERT INTO `addproject` (`id`, `ProName`, `date`, `details`) VALUES
(1, 'software', '2022-08-24', 'It is necessary'),
(6, 'website', '2022-08-04', 'new material');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `user_name`, `password`) VALUES
(1, 'sourav', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `assigntask`
--

CREATE TABLE `assigntask` (
  `id` int(11) NOT NULL,
  `EmpId` int(11) NOT NULL,
  `taskId` int(11) NOT NULL,
  `Startdate` date NOT NULL,
  `Enddate` date NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assigntask`
--

INSERT INTO `assigntask` (`id`, `EmpId`, `taskId`, `Startdate`, `Enddate`, `Status`) VALUES
(3, 1, 5, '2022-08-04', '2022-08-04', 'completed'),
(4, 2, 6, '2022-08-04', '2022-08-16', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Id` int(11) NOT NULL,
  `TaskName` varchar(30) NOT NULL,
  `EmpId` int(11) NOT NULL,
  `Feedback` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `projectId`, `name`) VALUES
(5, 1, 'management'),
(6, 1, 'webtech'),
(7, 6, 'register');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addemployee`
--
ALTER TABLE `addemployee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addproject`
--
ALTER TABLE `addproject`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ProName` (`ProName`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assigntask`
--
ALTER TABLE `assigntask`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_empId` (`EmpId`),
  ADD KEY `Foreign` (`taskId`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Foreign Key` (`projectId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addemployee`
--
ALTER TABLE `addemployee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `addproject`
--
ALTER TABLE `addproject`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `assigntask`
--
ALTER TABLE `assigntask`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assigntask`
--
ALTER TABLE `assigntask`
  ADD CONSTRAINT `FK_empId` FOREIGN KEY (`EmpId`) REFERENCES `addemployee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Foreign` FOREIGN KEY (`taskId`) REFERENCES `tasks` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `Foreign Key` FOREIGN KEY (`projectId`) REFERENCES `addproject` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
