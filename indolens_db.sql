-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2023 at 09:21 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `indolens_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accountant`
--

CREATE TABLE `accountant` (
  `accountant_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` int(12) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `name`, `email`, `phone`, `password`, `role`, `profile_pic`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Indolens Admin', 'admin@gmail.com', '973850521', 'admin', 1, 'profile_pic', 'indolens nelmangala', 'Aadhar', '', 'Pan', '', 1, 1, '2023-09-06 05:57:06', 1, '2023-09-06 05:57:06'),
(2, 'Sangeetha Thapa test', 'sangeetha@test.com', '1111111111', 'sangitest', 2, 'profile.png', ' peenya 1st stage test', 'Voter Id', '', '1', '', 1, 1, '2023-09-09 01:55:31', 1, '2023-09-09 13:46:09'),
(3, 'Darshan Bhandari', 'darshan@gmail.com', '9090909878', 'darshan', 2, 'profile_pic/profile_pic_profile.png_1694245762', '4rd Cross\r\n#A148', 'Aadhar', '', 'Pan Card', '', 1, 1, '2023-09-09 13:18:24', 1, '2023-09-09 13:18:24'),
(4, 'Nikshep Thapa', 'nikshep@gmail.com', '9090909090', 'Niru@123', 2, 'profile_pic/profile_pic_DSC_0179-removebg-preview (1).png_1694698633', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694698633\", \"documents/documents_user1-128x128.jpg_1694698633\"]', 'Pan Card', '[\"documents/documents_user2-160x160.jpg_1694698633\", \"documents/documents_user1-128x128.jpg_1694698633\"]', 1, 0, '2023-09-14 19:05:37', 0, '2023-09-14 19:05:37');

-- --------------------------------------------------------

--
-- Table structure for table `area_head`
--

CREATE TABLE `area_head` (
  `area_head_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_stores` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `area_head`
--

INSERT INTO `area_head` (`area_head_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_stores`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', 2147483647, '1234test', 'profile_pic/profile_pic_profile.png_1694343962', '2,4', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_wed2.jpg_1694343962\", \"documents/documents_wed1.jpg_1694343962\"]', 'Pan Card', '[\"documents/documents_greeting_logo (2).png_1694343962\", \"documents/documents_greeting_logo (1).png_1694343962\"]', 0, 1, '2023-09-10 16:34:46', 1, '2023-09-10 16:34:46'),
(2, 'Niraj Thapa', 'niraj@gmail.com', 2147483647, 'niraj', 'profile_pic/profile_pic_profile.png_1694349566', '2', 'peenya 1st stage bangalore 560058 ', 'Aadhar', '[\"documents/documents_greeting_logo (2).png_1694349566\"]', 'Pan Card', '[\"documents/documents_wed2.jpg_1694349566\", \"documents/documents_wed1.jpg_1694349566\"]', 1, 1, '2023-09-10 17:52:05', 1, '2023-09-10 17:52:05'),
(3, 'Darshan Bhandari', 'darshu@gmail.com', 2147483647, 'Darsh@123', 'profile_pic/profile_pic_DSC_0179-removebg-preview (1).png_1694700697', '', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694700697\", \"documents/documents_user1-128x128.jpg_1694700697\"]', 'Pan Card', '[\"documents/documents_user2-160x160.jpg_1694700697\", \"documents/documents_user1-128x128.jpg_1694700697\"]', 1, 1, '2023-09-14 19:39:46', 1, '2023-09-14 19:39:46'),
(4, 'Darshan Bhandari', 'darshu@gmail.com', 2147483647, 'Darsh@123', 'profile_pic/profile_pic_DSC_0179-removebg-preview (1).png_1694700793', '', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694700793\", \"documents/documents_user1-128x128.jpg_1694700793\"]', 'Pan Card', '[\"documents/documents_user2-160x160.jpg_1694700793\", \"documents/documents_user1-128x128.jpg_1694700793\"]', 1, 1, '2023-09-14 19:43:10', 1, '2023-09-14 19:43:10');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0v7cyevx5tss0fb6qbfjlevh4588wj1w', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qerqO:HRW9I1yrUvVh55DBEUukNZH4bO34138uodYFEKwSogA', '2023-09-23 06:53:24.171838'),
('5gj03vrfwajgoqzq1o48jz7yp48m3dtl', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qh1cR:Id6-gP3ffaZ5flRk1d7HRzC7nL2SpELZFKmJI_dMrno', '2023-09-29 05:43:55.156342'),
('5hre8c1y1e4robl9ame8jgsqrbesrlzi', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qgjg3:bNwp2HesoyhwiQ02rhL9epSiu4UWe54rbjc6-QXmnT4', '2023-09-28 10:34:27.213659'),
('b8l3vfkf2qtznvms7w09y1r6opo146ch', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qe8AS:AQWws2m8ssIEcc8FGwTvo-3kzJ0FO5JkIon0l_GqkRM', '2023-09-21 06:07:04.464787'),
('d7pwgjwjmmg7nxn8mlcqk7nkd4g5gd3e', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qi8Uu:P1GmoZkL0J9mZ1jWMKHHzbpD_v_pDTy_pksArtJGg-A', '2023-10-02 07:16:44.080677'),
('kwfqssbraq7v9k0sge34r9d4v6imow36', '.eJxNi0EKgCAQRa8Ss5YO4KqWnUJEJxkYR9FaRXdvDIKW773_L6DufMwkjktKGB0J2KOdaACzJwYLb17SoDmUDAbEZ9SwSSyM0qd1LNQ3xe-gWFvZidFVCmr_dD_zTym7:1qdkJR:pH9aDyhztk66uZHOD2ZKfn1S51ppkQ2f2OmhickWkAI', '2023-09-06 12:38:45.368165'),
('nxnsxhy0xnp6om110uebpnykwes3hvqe', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qi8XI:efTbMDgR1qtcuaz7stjO-AgGjXL9TK6zjbtS-Lgr6hc', '2023-10-02 07:19:12.333375'),
('p99wzi3peasn8a8tmlmu6rb6hao8kc1n', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qeUul:Weic5A0bPxB9kzKEzJLzeeLuMAmSNQD7_x1szm0lxgU', '2023-09-22 06:24:23.175906'),
('xhpbnmkif52qgusnthxpqpnqes0a0we3', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qfDd2:zdkjUO4uKjRM8XdYkyu9YWVcd_VH6dCrbPOnBDCpBNU', '2023-09-24 06:09:04.816750');

-- --------------------------------------------------------

--
-- Table structure for table `franchise_owner`
--

CREATE TABLE `franchise_owner` (
  `franchise_owner_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `franchise_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_owner`
--

INSERT INTO `franchise_owner` (`franchise_owner_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `franchise_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(7, 'test', 'test@gmail.com', 2147483647, 'Test@12', 'profile_pic/profile_pic_profile.png_1694762964', 0, '#A-148 3rd Cross 1st stage Peenya Industrial Estate Bangalore-58', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694762964\", \"documents/documents_user1-128x128.jpg_1694762964\"]', 'Pan Card', '[\"documents/documents_user1-128x128.jpg_1694762964\"]', 0, 1, '2023-09-15 12:54:16', 1, '2023-09-15 12:54:16');

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store`
--

CREATE TABLE `franchise_store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(255) NOT NULL,
  `store_display_name` varchar(255) NOT NULL,
  `store_phone` int(11) NOT NULL,
  `store_gst` varchar(255) NOT NULL,
  `store_email` varchar(255) NOT NULL,
  `store_city` varchar(255) NOT NULL,
  `store_state` varchar(255) NOT NULL,
  `store_zip` varchar(255) NOT NULL,
  `store_lat` double NOT NULL,
  `store_lng` double NOT NULL,
  `store_address` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store`
--

INSERT INTO `franchise_store` (`store_id`, `store_name`, `store_display_name`, `store_phone`, `store_gst`, `store_email`, `store_city`, `store_state`, `store_zip`, `store_lat`, `store_lng`, `store_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'franchise store 01', 'Santhosh lense store', 2147483647, 'GSTIN9087H', 'santhosh.lense.store@gmail.test', 'Madanayakahalli', 'Karnataka', '560058', 18.5204303, 73.8567437, '4rd Cross\r\n#A148  ', 1, 1, '2023-09-07 00:21:01', 1, '2023-09-07 11:58:51');

-- --------------------------------------------------------

--
-- Table structure for table `lab`
--

CREATE TABLE `lab` (
  `lab_id` int(11) NOT NULL,
  `lab_name` varchar(255) NOT NULL,
  `lab_display_name` varchar(255) NOT NULL,
  `lab_phone` int(11) NOT NULL,
  `lab_gst` varchar(255) NOT NULL,
  `lab_email` varchar(255) NOT NULL,
  `lab_city` varchar(255) NOT NULL,
  `lab_state` varchar(255) NOT NULL,
  `lab_zip` varchar(255) NOT NULL,
  `lab_lat` double NOT NULL,
  `lab_lng` double NOT NULL,
  `lab_address` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lab_technician`
--

CREATE TABLE `lab_technician` (
  `lab_technician_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_lab_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `marketing_head`
--

CREATE TABLE `marketing_head` (
  `marketing_head_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_area_head` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `optimetry`
--

CREATE TABLE `optimetry` (
  `optimetry_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `other_employees`
--

CREATE TABLE `other_employees` (
  `other_employee_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `own_store`
--

CREATE TABLE `own_store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(255) NOT NULL,
  `store_display_name` varchar(255) NOT NULL,
  `store_phone` varchar(255) NOT NULL,
  `store_gst` varchar(255) NOT NULL,
  `store_email` varchar(255) NOT NULL,
  `store_city` varchar(255) NOT NULL,
  `store_state` varchar(255) NOT NULL,
  `store_zip` varchar(255) NOT NULL,
  `store_lat` double NOT NULL,
  `store_lng` double NOT NULL,
  `store_address` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store`
--

INSERT INTO `own_store` (`store_id`, `store_name`, `store_display_name`, `store_phone`, `store_gst`, `store_email`, `store_city`, `store_state`, `store_zip`, `store_lat`, `store_lng`, `store_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(2, 'indolens ownstore 02', 'Indolense Mysore', '9890909090', 'GSTIN001', 'indolens.mysore@gmail.com', 'Mysore', 'Karnataka', '560058', 12.9532583, 77.5434616, ' 4rd Cross\r\n#A148', 1, 1, '2023-09-06 09:47:03', 1, '2023-09-07 11:40:07'),
(4, 'indolens ownstore 03', 'Indolense Mandya', '98765432345', 'GSTIN001', 'indolens.mandya@gmail.com', 'Mandya', 'Karnataka', '560058', 12.5218157, 76.89514880000002, '4rd Cross\r\n#A148', 1, 1, '2023-09-06 21:03:35', 1, '2023-09-06 21:03:35');

-- --------------------------------------------------------

--
-- Table structure for table `sales_executive`
--

CREATE TABLE `sales_executive` (
  `sales_executive_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_manager`
--

CREATE TABLE `store_manager` (
  `store_manager_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_manager`
--

INSERT INTO `store_manager` (`store_manager_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(4, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', 2147483647, '1234e', 'profile_pic/profile_pic_profile.png_1694121922', 2, '#A-148, 3rd cross, peenya industrial estate, peeny 1st stage,Bangalore 560059', 'Aadhar', '', '1', '', 1, 1, '2023-09-08 02:54:35', 1, '2023-09-08 02:54:35'),
(5, 'Nirmala', 'nirmala@gmail.com', 2147483647, 'nimmi', 'profile_pic/profile_pic_profile.png_1694155180', 0, '4rd Cross\r\n#A148', 'Aadhar', '', '1', '', 1, 1, '2023-09-08 12:07:59', 1, '2023-09-08 12:07:59'),
(6, 'Niraj', 'niraj@gmail.com', 2147483647, 'Niru@123', 'profile_pic/profile_pic_WhatsApp Image 2023-04-19 at 9.40.02 PM.jpeg_1694700006', 0, '4rd Cross\r\n#A148', 'Aadhar', '', 'Pan Card', '', 1, 1, '2023-09-14 19:29:47', 1, '2023-09-14 19:29:47');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accountant`
--
ALTER TABLE `accountant`
  ADD PRIMARY KEY (`accountant_id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `area_head`
--
ALTER TABLE `area_head`
  ADD PRIMARY KEY (`area_head_id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  ADD PRIMARY KEY (`franchise_owner_id`);

--
-- Indexes for table `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD PRIMARY KEY (`store_id`);

--
-- Indexes for table `lab`
--
ALTER TABLE `lab`
  ADD PRIMARY KEY (`lab_id`);

--
-- Indexes for table `lab_technician`
--
ALTER TABLE `lab_technician`
  ADD PRIMARY KEY (`lab_technician_id`);

--
-- Indexes for table `marketing_head`
--
ALTER TABLE `marketing_head`
  ADD PRIMARY KEY (`marketing_head_id`);

--
-- Indexes for table `optimetry`
--
ALTER TABLE `optimetry`
  ADD PRIMARY KEY (`optimetry_id`);

--
-- Indexes for table `other_employees`
--
ALTER TABLE `other_employees`
  ADD PRIMARY KEY (`other_employee_id`);

--
-- Indexes for table `own_store`
--
ALTER TABLE `own_store`
  ADD PRIMARY KEY (`store_id`);

--
-- Indexes for table `sales_executive`
--
ALTER TABLE `sales_executive`
  ADD PRIMARY KEY (`sales_executive_id`);

--
-- Indexes for table `store_manager`
--
ALTER TABLE `store_manager`
  ADD PRIMARY KEY (`store_manager_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accountant`
--
ALTER TABLE `accountant`
  MODIFY `accountant_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `area_head`
--
ALTER TABLE `area_head`
  MODIFY `area_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  MODIFY `franchise_owner_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `franchise_store`
--
ALTER TABLE `franchise_store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `lab`
--
ALTER TABLE `lab`
  MODIFY `lab_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lab_technician`
--
ALTER TABLE `lab_technician`
  MODIFY `lab_technician_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `marketing_head`
--
ALTER TABLE `marketing_head`
  MODIFY `marketing_head_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `optimetry`
--
ALTER TABLE `optimetry`
  MODIFY `optimetry_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `other_employees`
--
ALTER TABLE `other_employees`
  MODIFY `other_employee_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `own_store`
--
ALTER TABLE `own_store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sales_executive`
--
ALTER TABLE `sales_executive`
  MODIFY `sales_executive_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_manager`
--
ALTER TABLE `store_manager`
  MODIFY `store_manager_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
