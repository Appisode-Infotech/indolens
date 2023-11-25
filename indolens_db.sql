-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2023 at 06:58 PM
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
  `phone` varchar(255) NOT NULL,
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

--
-- Dumping data for table `accountant`
--

INSERT INTO `accountant` (`accountant_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Accountant 1', 'accountant1@test.com', '9126431725', '$2b$12$eSIltnSFJhDZms48tlvVr.HDHX2BfZfOP6ia/rlS0rAR/bWNn2CIi', 'profile_pic/profile_pic_1700635966_accountant.webp', '#B-22, 10th floor, 1st cross, 2nd main, 3rd stage, HSR layout, Bangalore 560024', 'Aadhar', '[\"documents/documents_1700635966_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635966_pan.jpg\"]', 1, 5, '2023-11-22 12:22:46', 5, '2023-11-22 12:22:46'),
(2, 'Accountant 2', 'accountant2@test.com', '9126431726', '$2b$12$eSIltnSFJhDZms48tlvVr.HDHX2BfZfOP6ia/rlS0rAR/bWNn2CIi', 'profile_pic/profile_pic_1700635966_accountant.webp', '#B-22, 10th floor, 1st cross, 2nd main, 3rd stage, HSR layout, Bangalore 560024', 'Aadhar', '[\"documents/documents_1700635966_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635966_pan.jpg\"]', 0, 5, '2023-11-22 12:22:46', 5, '2023-11-22 12:22:46'),
(3, 'Accountant 3', 'accountant3@test.com', '9126431727', '$2b$12$eSIltnSFJhDZms48tlvVr.HDHX2BfZfOP6ia/rlS0rAR/bWNn2CIi', 'profile_pic/profile_pic_1700635966_accountant.webp', '#B-22, 10th floor, 1st cross, 2nd main, 3rd stage, HSR layout, Bangalore 560024', 'Aadhar', '[\"documents/documents_1700635966_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635966_pan.jpg\"]', 1, 5, '2023-11-22 12:22:46', 5, '2023-11-22 12:22:46');

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
(5, 'John Doe', 'admin@indolens.com', '1234567890', '$2b$12$GyX6AZELf3O.3NTiNRzvVuc.wivdpyT.zMGTfbPdL34nC9OClYNRq', 1, 'profile_pic.jpg', '123 Main St, City, Country', 'Document 1 Type', '{\"key\": \"value1\"}', 'Document 2 Type', '{\"key\": \"value2\"}', 1, 1, '2023-09-21 12:18:10', 1, '2023-09-21 12:18:10'),
(12, 'sub Admin 1', 'subadmin1@test.com', '98907234953', '$2b$12$.YxJiNLq1vr7/8vRqehuB.FFGvwcI6bAsHBWJs2eatEXV2lUEX3Ai', 2, 'profile_pic/profile_pic_1700379942_sub_admin.jpg', '#A-123, 1st floor, 2nd cross, 3rd main, Bashveshwaranager, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700379942_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700379942_pan.jpg\"]', 0, 0, '2023-11-19 13:15:42', 0, '2023-11-19 13:15:42'),
(13, 'sub Admin 2', 'subadmin2@test.com', '98907234953', '$2b$12$.YxJiNLq1vr7/8vRqehuB.FFGvwcI6bAsHBWJs2eatEXV2lUEX3Ai', 2, 'profile_pic/profile_pic_1700379942_sub_admin.jpg', '#A-123, 1st floor, 2nd cross, 3rd main, Bashveshwaranager, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700379942_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700379942_pan.jpg\"]', 0, 0, '2023-11-19 13:15:42', 0, '2023-11-19 13:15:42'),
(14, 'sub Admin 3', 'subadmin3@test.com', '98907234953', '$2b$12$.YxJiNLq1vr7/8vRqehuB.FFGvwcI6bAsHBWJs2eatEXV2lUEX3Ai', 2, 'profile_pic/profile_pic_1700379942_sub_admin.jpg', '#A-123, 1st floor, 2nd cross, 3rd main, Bashveshwaranager, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700379942_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700379942_pan.jpg\"]', 1, 0, '2023-11-19 13:15:42', 0, '2023-11-19 13:15:42');

-- --------------------------------------------------------

--
-- Table structure for table `area_head`
--

CREATE TABLE `area_head` (
  `area_head_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
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
(1, 'Area Head 01', 'areahead01@test.com', '9087123492', '$2b$12$HmYuI/VlYZEy0iRtlRZkr.cmL66aYzvGCLvxLKeX./F0Aiim.B8Qy', 'profile_pic/profile_pic_1700551516_area_head.png', '', '#A-01, 6th floor, D block, platinum city, SRS road, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700551516_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700551516_pan.jpg\"]', 0, 5, '2023-11-21 12:55:15', 5, '2023-11-21 12:55:15'),
(2, 'Area Head 02', 'areahead02@test.com', '9087123493', '$2b$12$wRlnsdDkzNrR5l5SobhAMuGTWClGs.XVK.DrdJNrFSQmAcpAHJWDi', 'profile_pic/profile_pic_1700551540_area_head.png', '', '#A-01, 6th floor, D block, platinum city, SRS road, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700551540_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700551540_pan.jpg\"]', 1, 5, '2023-11-21 12:55:37', 5, '2023-11-21 12:55:37'),
(3, 'Area Head 03', 'areahead03@test.com', '9087123494', '$2b$12$BADjfrk42.lcmyMYfLlE0.QT3CaR6Gum3cLThn7WuribW9KKPtCCu', 'profile_pic/profile_pic_1700551563_area_head.png', '', '#A-01, 6th floor, D block, platinum city, SRS road, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700551563_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700551563_pan.jpg\"]', 1, 5, '2023-11-21 12:56:00', 5, '2023-11-21 12:56:00');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `brand_id` int(11) NOT NULL,
  `brand_name` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  `brand_description` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`brand_id`, `brand_name`, `category_id`, `brand_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Indolens', 0, 'Indolens Own Brand', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Lens Guru', 0, 'Collabration Brand', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

-- --------------------------------------------------------

--
-- Table structure for table `central_inventory`
--

CREATE TABLE `central_inventory` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` varchar(255) NOT NULL,
  `product_images` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`product_images`)),
  `category_id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `frame_type_id` int(11) NOT NULL,
  `frame_shape_id` int(11) NOT NULL,
  `color_id` int(11) NOT NULL,
  `unit_id` int(11) NOT NULL,
  `origin` varchar(255) NOT NULL,
  `cost_price` int(11) NOT NULL,
  `sale_price` int(11) NOT NULL,
  `model_number` varchar(255) NOT NULL,
  `hsn` varchar(255) NOT NULL,
  `power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`power_attribute`)),
  `franchise_sale_price` double NOT NULL,
  `product_quantity` int(11) NOT NULL,
  `product_gst` float NOT NULL,
  `status` tinyint(1) NOT NULL,
  `discount` float NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `central_inventory`
--

INSERT INTO `central_inventory` (`product_id`, `product_name`, `product_description`, `product_images`, `category_id`, `brand_id`, `material_id`, `frame_type_id`, `frame_shape_id`, `color_id`, `unit_id`, `origin`, `cost_price`, `sale_price`, `model_number`, `hsn`, `power_attribute`, `franchise_sale_price`, `product_quantity`, `product_gst`, `status`, `discount`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'lens 1', '<p>first lens</p>', '[\"products/products_1699947030_frame03.jpg\", \"products/products_1699947030_frame02.jpg\", \"products/products_1699947030_frame01.jpg\"]', 1, 1, 1, 1, 1, 1, 2, 'Indian', 550, 900, 'M001', 'HSN001', '{\"vision_type\": \"single_vision\", \"index\": \"1.50\", \"sph\": \"2.0\", \"cyl\": \"2.5\", \"axis\": \"3.5\", \"add\": \"3\"}', 0, 10, 18, 1, 50, '2023-11-14 13:00:28', 5, '2023-11-14 13:00:28', 5),
(2, 'lens 2', '<p>Second lens</p>', '[\"products/products_1699947030_frame03.jpg\", \"products/products_1699947030_frame02.jpg\", \"products/products_1699947030_frame01.jpg\"]', 1, 1, 3, 2, 2, 2, 1, 'Foreign', 1000, 1500, 'M001', 'HSN001', '{\"vision_type\": \"single_vision\", \"index\": \"1.50\", \"sph\": \"2.0\", \"cyl\": \"2.5\", \"axis\": \"3.5\", \"add\": \"3\"}', 0, 145, 18, 1, 0, '2023-11-14 13:00:28', 5, '2023-11-14 13:13:54', 5),
(3, 'lens 3', '<p>Third lens</p>', '[\"products/products_1699947030_frame03.jpg\", \"products/products_1699947030_frame02.jpg\", \"products/products_1699947030_frame01.jpg\"]', 1, 1, 2, 3, 3, 3, 2, 'Domestic', 250, 500, 'M001', 'HSN001', '{\"vision_type\": \"single_vision\", \"index\": \"1.50\", \"sph\": \"2.0\", \"cyl\": \"2.5\", \"axis\": \"3.5\", \"add\": \"3\"}', 0, 250, 18, 1, 0, '2023-11-14 13:00:28', 5, '2023-11-14 13:13:54', 5),
(4, 'test single vision lens', '<p>test single vision lens</p>', '[\"products/products_1700928278_frame01.jpg\"]', 1, 1, 1, 1, 1, 1, 1, 'Indian', 400, 600, 'MDL9876', 'HSN9876', '{\"vision_type\": \"single_vision\", \"index\": \"1.50\", \"sph\": \"2.0\", \"cyl\": \"2.5\", \"axis\": \"3.5\", \"add\": \"3\"}', 500, 100, 9, 0, 10, '2023-11-25 21:34:36', 5, '2023-11-25 21:34:36', 5),
(5, 'test single vision lens', '<p>test single vision lens</p>', '[\"products/products_1700928380_frame01.jpg\"]', 1, 1, 1, 1, 1, 1, 1, 'Indian', 400, 600, 'MDL9876', 'HSN9876', '{\"vision_type\": \"single_vision\", \"index\": \"1.50\", \"sph\": \"2.0\", \"cyl\": \"2.5\", \"axis\": \"3.5\", \"add\": \"3\"}', 500, 100, 9, 0, 10, '2023-11-25 21:36:17', 5, '2023-11-25 21:36:17', 5);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_by_employee_id` int(11) NOT NULL,
  `created_by_store_id` int(11) NOT NULL,
  `created_by_store_type` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `updated_by_employee_id` int(11) NOT NULL,
  `updated_by_store_id` int(11) NOT NULL,
  `updated_by_store_type` int(11) NOT NULL,
  `updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `gender`, `age`, `phone`, `email`, `language`, `city`, `address`, `created_by_employee_id`, `created_by_store_id`, `created_by_store_type`, `created_on`, `updated_by_employee_id`, `updated_by_store_id`, `updated_by_store_type`, `updated_on`) VALUES
(1, 'Customer 1', 'M', 32, '9807543127', 'customer1@test.com', 'Hindi, Kannada, English', 'Bangalore', '#A-123, 2nd floor, 3rd cross, Bangalore 7890087', 1, 1, 1, '2023-11-20 08:30:17', 1, 1, 1, '2023-11-20 08:30:17'),
(2, 'Customer 2', 'M', 32, '9807543128', 'customer2@test.com', 'Hindi, Kannada, English', 'Bangalore', '#A-123, 2nd floor, 3rd cross, Bangalore 7890087', 1, 1, 1, '2023-11-20 08:30:17', 1, 1, 1, '2023-11-20 08:30:17'),
(3, 'Customer 3', 'M', 32, '9807543129', 'customer3@test.com', 'Hindi, Kannada, English', 'Bangalore', '#A-123, 2nd floor, 3rd cross, Bangalore 7890087', 1, 1, 1, '2023-11-20 08:30:17', 1, 1, 1, '2023-11-20 08:30:17');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
('h769ghhhyh8dv233k9m74cpph1vglxam', '.eJxNjbsOwjAMRX-l8twWshTaCUYGxICYo6gxkaXEqeIghBD_Tko7sNn33McbSLTkmFD76BxaTQxDTg-sgSwMqgY2AWGAs2HjMFUKasBgyBctLJo6ZJTcjjEUtpStoRPb6JGlujy5us7kl188-TXNnlkwIuS4rC9kXZ5SvJNHPdFYfH_f5u_Wquv7fqt23V7fBJM0RxuISXIypayhMXI7sYPPFzEpUU8:1r2o7K:yFDAvtr8UTsJRVAb3QNAwXCD3PEftwhdHHZb8a6NQfw', '2023-11-28 07:45:50.052790'),
('jd4p49www8vw0v5rkkk3hsvborv6iatf', '.eJxNjbsOwjAMRX-l8twWshTaCUYGxICYo6gxkaXEqeIghBD_Tko7sNn33McbSLTkmFD76BxaTQxDTg-sgSwMqgY2AWGAs2HjMFUKasBgyBctLJo6ZJTcjjEUtpStoRPb6JGlujy5us7kl188-TXNnlkwIuS4rC9kXZ5SvJNHPdFYfH_f5u_Wquv7fqt23V7fBJM0RxuISXIypayhMXI7sYPPFzEpUU8:1r6wYA:jBPnwAtQRdxs2fSOi8cSC_SFqf53yMQ-jrP7oafytj0', '2023-12-09 17:34:38.513401'),
('turp8wrxg6w8cxp04xqc6rl2ydlh9m05', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1r5Jlq:AHsztn2aZH_sj_NXrLsqFzk8KEM3PGg7OGBm0jPH6wM', '2023-12-05 05:58:02.212010');

-- --------------------------------------------------------

--
-- Table structure for table `frame_shapes`
--

CREATE TABLE `frame_shapes` (
  `shape_id` int(11) NOT NULL,
  `shape_name` varchar(255) NOT NULL,
  `shape_description` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_shapes`
--

INSERT INTO `frame_shapes` (`shape_id`, `shape_name`, `shape_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Oval', 'Oval Shape Frame', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Cat ', 'Cat Eye Shape', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(3, 'Square', 'Square Shape Frame', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(4, 'Round', 'Round Shape Frame', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

-- --------------------------------------------------------

--
-- Table structure for table `frame_types`
--

CREATE TABLE `frame_types` (
  `frame_id` int(11) NOT NULL,
  `frame_type_name` varchar(255) NOT NULL,
  `frame_type_description` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_types`
--

INSERT INTO `frame_types` (`frame_id`, `frame_type_name`, `frame_type_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Round ', 'Round Frames', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Oval Frames', 'Soften & Balance Defined Square Face Line', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(3, 'Coloured Frames', 'Draws Attention To Eyes', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

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
(1, 'Indolens Franchise Store 1', 'Indolense Tumkur', 2147483647, 'GSTIN0013556889', 'indolenstumkur@gmail.com', 'Tumkur', 'Karnataka', '560041', 13.3378762, 77.117325, '12th Cross\r\n#A148', 1, 5, '2023-11-13 19:53:28', 5, '2023-11-13 19:53:28'),
(2, 'Indolens Franchise Store 02', 'Indolense Hubbli Niraj', 2147483647, 'GSTIN0011234567', 'indolenshubbli@gmail.com', 'Hubbli', 'Karnataka', '560699', 15.3647083, 75.1239547, '19rd Cross\r\n#C-546 ', 1, 5, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12');

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store_employees`
--

CREATE TABLE `franchise_store_employees` (
  `employee_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store_employees`
--

INSERT INTO `franchise_store_employees` (`employee_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `role`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`, `certificates`) VALUES
(1, 'Franchise Owner 1', 'franchiseowner1@test.com', '9087123594', '$2b$12$O1whVb9hG77U6pgCdfE23uZKrUtgawAMhbeKooJSBiVc.Lj9JMZ8a', 'profile_pic/profile_pic_1699946182_hello.png', 0, '  #A-143, 3rd cross, 4th main, near  Madanayakanahalli ploce station, Bangalore 560098', 'Aadhar', '[\"documents/documents_1699946182_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699946182_pan.jpg\"]', 0, 1, 5, '2023-11-14 12:46:20', 5, '2023-11-19 13:57:41', NULL),
(2, 'Franchise Owner 2', 'franchiseowner2@test.com', '9087123595', '$2b$12$O1whVb9hG77U6pgCdfE23uZKrUtgawAMhbeKooJSBiVc.Lj9JMZ8a', 'profile_pic/profile_pic_1699946182_hello.png', 0, '#A-123, 9th cross, dharawi, mumbai 560021', 'Aadhar', '[\"documents/documents_1699946182_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699946182_pan.jpg\"]', 1, 1, 5, '2023-11-14 12:46:20', 5, '2023-11-14 12:46:20', NULL),
(3, 'Franchise Owner 3', 'franchiseowner3@test.com', '9087123596', '$2b$12$O1whVb9hG77U6pgCdfE23uZKrUtgawAMhbeKooJSBiVc.Lj9JMZ8a', 'profile_pic/profile_pic_1699946182_hello.png', 0, '#A-123, 9th cross, dharawi, mumbai 560021', 'Aadhar', '[\"documents/documents_1699946182_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699946182_pan.jpg\"]', 1, 1, 5, '2023-11-14 12:46:20', 5, '2023-11-14 12:46:20', NULL),
(4, 'franchise optimetry 1', 'franchiseoptimetry1@test.com', '9812309736', '$2b$12$El6YZwCxYrpf3HjEwtlL7eXxrR5v.iTUZOQ4VwiQfK3PJwHLLkqC.', 'profile_pic/profile_pic_1699999233_optometry.jpg', 0, '#C-45, 3rd floor, NivasAppartment, HSR layout, Bangalore, Karnataka 560048', '1', '[\"documents/documents_1699999233_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699999233_pan.jpg\"]', 1, 2, 5, '2023-11-15 03:30:27', 5, '2023-11-15 03:30:27', '[\"certificates/certificates_1700000057_wed2.jpg\", \"certificates/certificates_1700000057_wed1.jpg\"]'),
(5, 'franchise optimetry 2', 'franchiseoptimetry2@test.com', '9812309737', '$2b$12$El6YZwCxYrpf3HjEwtlL7eXxrR5v.iTUZOQ4VwiQfK3PJwHLLkqC.', 'profile_pic/profile_pic_1699999233_optometry.jpg', 0, '#C-45, 3rd floor, NivasAppartment, HSR layout, Bangalore, Karnataka 560048', '1', '[\"documents/documents_1699999233_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699999233_pan.jpg\"]', 1, 2, 5, '2023-11-15 03:30:27', 5, '2023-11-15 03:30:27', '[\"certificates/certificates_1700000057_wed2.jpg\", \"certificates/certificates_1700000057_wed1.jpg\"]'),
(6, 'franchise optimetry 3', 'franchiseoptimetry3@test.com', '9808712345', '$2b$12$u31ReK3XXQhWzJW21rCZW.oaRZTD7MojMTs9g6jlKcWfGANDrxepa', 'profile_pic/profile_pic_1699999836_optometry.jpg', 0, '#C-45, 3rd floor, NivasAppartment, HSR layout, Bangalore, Karnataka 560048', '1', '[\"documents/documents_1699999836_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699999836_pan.jpg\"]', 0, 2, 5, '2023-11-15 03:38:51', 5, '2023-11-15 03:38:51', '[\"certificates/certificates_1700000057_wed2.jpg\", \"certificates/certificates_1700000057_wed1.jpg\"]'),
(7, 'franchise optimetry 4', 'franchiseoptimetry4@test.com', '9876345263', '$2b$12$JozpgEyZLEdpFXDEOUcMB.7TM2IFDRugR8EaOx9OJHJjwggqxmYZi', 'profile_pic/profile_pic_1700000057_optometry.jpg', 0, '#C-45, 3rd floor, NivasAppartment, HSR layout, Bangalore, Karnataka 560048', '1', '[\"documents/documents_1700000057_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700000057_pan.jpg\"]', 0, 2, 5, '2023-11-15 03:42:48', 5, '2023-11-15 03:42:48', '[\"certificates/certificates_1700000057_wed2.jpg\", \"certificates/certificates_1700000057_wed1.jpg\"]'),
(8, 'franchise Sales Executive 1', 'franchisesalesexecutive1@test.com', '9087123403', '$2b$12$IO7Zd3/kywk.ftld4ODHU..6Yk/q1OWF394MYDZgsMCNTi.nbfGYK', 'profile_pic/profile_pic_1700378125_sales_exec.jpg', 0, '#P-14, 3rd floor, 1st cross, 5th mail, Vijaynagar, Bangalore 560068', 'Aadhar', '[\"documents/documents_1700378125_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378125_pan.jpg\"]', 1, 3, 5, '2023-11-19 12:45:24', 5, '2023-11-19 12:45:24', NULL),
(9, 'franchise Sales Executive 2', 'franchisesalesexecutive2@test.com', '9087123404', '$2b$12$IO7Zd3/kywk.ftld4ODHU..6Yk/q1OWF394MYDZgsMCNTi.nbfGYK', 'profile_pic/profile_pic_1700378125_sales_exec.jpg', 0, '#P-14, 3rd floor, 1st cross, 5th mail, Vijaynagar, Bangalore 560068', 'Aadhar', '[\"documents/documents_1700378125_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378125_pan.jpg\"]', 1, 3, 5, '2023-11-19 12:45:24', 5, '2023-11-19 12:45:24', NULL),
(10, 'franchise Sales Executive 3', 'franchisesalesexecutive3@test.com', '9087123405', '$2b$12$IO7Zd3/kywk.ftld4ODHU..6Yk/q1OWF394MYDZgsMCNTi.nbfGYK', 'profile_pic/profile_pic_1700378125_sales_exec.jpg', 0, '#P-14, 3rd floor, 1st cross, 5th mail, Vijaynagar, Bangalore 560068', 'Aadhar', '[\"documents/documents_1700378125_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378125_pan.jpg\"]', 0, 3, 5, '2023-11-19 12:45:24', 5, '2023-11-19 12:45:24', NULL),
(11, 'franchise other emp 1', 'franchiseotheremp1@test.com', '9807123094', '$2b$12$R7JLHBwCImm0rLj.elJ52.K0NNnPscHO/AcDFVbmuqErgTR/QupCq', 'profile_pic/profile_pic_1700378448_other_employee.jpg', 0, '#A-23, 1st floor, 2nd main, 3cross, JP Nagar, Bangaore 560058', 'Aadhar', '[\"documents/documents_1700378448_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378448_pan.jpg\"]', 1, 4, 5, '2023-11-19 12:50:48', 5, '2023-11-19 12:50:48', NULL),
(12, 'franchise other emp 2', 'franchiseotheremp2@test.com', '9807123095', '$2b$12$avhtixlplgMxaiwLcfpv.OkKDkSk6FcJnuGisdM3uOismM8dH4Hh.', 'profile_pic/profile_pic_1700378468_other_employee.jpg', 0, '#A-23, 1st floor, 2nd main, 3cross, JP Nagar, Bangaore 560058', 'Aadhar', '[\"documents/documents_1700378468_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378468_pan.jpg\"]', 0, 4, 5, '2023-11-19 12:51:07', 5, '2023-11-19 12:51:07', NULL),
(13, 'franchise other emp 3', 'franchiseotheremp3@test.com', '9807123096', '$2b$12$k3xcui.fZ7OcMxiUCgugnuWKJ1AvY5nUr3LPkxC3UD.bGMNuRyDKu', 'profile_pic/profile_pic_1700378498_other_employee.jpg', 0, '#A-23, 1st floor, 2nd main, 3cross, JP Nagar, Bangaore 560058', 'Aadhar', '[\"documents/documents_1700378498_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700378498_pan.jpg\"]', 0, 4, 5, '2023-11-19 12:51:37', 5, '2023-11-19 12:51:37', NULL);

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

--
-- Dumping data for table `lab`
--

INSERT INTO `lab` (`lab_id`, `lab_name`, `lab_display_name`, `lab_phone`, `lab_gst`, `lab_email`, `lab_city`, `lab_state`, `lab_zip`, `lab_lat`, `lab_lng`, `lab_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Indolens lab 1', 'Indolens lab 1', 2147483647, 'GSTIN09876590', 'indolenslab1@test.com', 'Bangalore', 'Karnataka', '560058', 13.0978355, 77.39398600000001, 'indolense lab1, Nelamangala, near nelamangala bus stop, Bangalore 560098', 1, 5, '2023-11-22 12:44:31', 5, '2023-11-22 12:44:31'),
(2, 'Indolens lab 2', 'Indolens lab 1', 2147483647, 'GSTIN09876590', 'indolenslab2@test.com', 'Bangalore', 'Karnataka', '560058', 12.9662094, 77.5746429, 'Indolens lab2, chickpet, KR Market, Bangalore 560057', 1, 5, '2023-11-22 14:15:38', 5, '2023-11-22 14:15:38');

-- --------------------------------------------------------

--
-- Table structure for table `lab_technician`
--

CREATE TABLE `lab_technician` (
  `lab_technician_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
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

--
-- Dumping data for table `lab_technician`
--

INSERT INTO `lab_technician` (`lab_technician_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_lab_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Lab Tech 1', 'labtech1@test.com', '9816254314', '$2b$12$BIWIBfelWp2ojKr0Wg3CTeLqqmaNDp2hihAV5ABUfLUgJ6UR76HYO', 'profile_pic/profile_pic_1700637012_lab_tech.png', 0, '#A-01, ground floor, Shree Krishna Nivas, Hanumantha layout, Brindavana 470023', 'Aadhar', '[\"documents/documents_1700637012_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700637012_pan.jpg\"]', 0, 5, '2023-11-22 12:40:07', 5, '2023-11-22 12:40:07'),
(2, 'Lab Tech 2', 'labtech2@test.com', '9816254315', '$2b$12$BIWIBfelWp2ojKr0Wg3CTeLqqmaNDp2hihAV5ABUfLUgJ6UR76HYO', 'profile_pic/profile_pic_1700637012_lab_tech.png', 0, '#A-01, ground floor, Shree Krishna Nivas, Hanumantha layout, Brindavana 470023', 'Aadhar', '[\"documents/documents_1700637012_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700637012_pan.jpg\"]', 1, 5, '2023-11-22 12:40:07', 5, '2023-11-22 12:40:07'),
(3, 'Lab Tech 3', 'labtech3@test.com', '9816254316', '$2b$12$BIWIBfelWp2ojKr0Wg3CTeLqqmaNDp2hihAV5ABUfLUgJ6UR76HYO', 'profile_pic/profile_pic_1700637012_lab_tech.png', 0, '#A-01, ground floor, Shree Krishna Nivas, Hanumantha layout, Brindavana 470023', 'Aadhar', '[\"documents/documents_1700637012_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700637012_pan.jpg\"]', 1, 5, '2023-11-22 12:40:07', 5, '2023-11-22 12:40:07');

-- --------------------------------------------------------

--
-- Table structure for table `marketing_head`
--

CREATE TABLE `marketing_head` (
  `marketing_head_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_area_head` int(11) DEFAULT NULL,
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
-- Dumping data for table `marketing_head`
--

INSERT INTO `marketing_head` (`marketing_head_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_area_head`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Marketing Head 1', 'marketinghead1@test.com', '9080123748', '$2b$12$JU.7BBGv0LjF98UbbGhXJe324fqFaCOfxyl7aS8oZ2uE8lvHcL4ya', 'profile_pic/profile_pic_1700635284_marketing_head.jpg', NULL, '#A13, 4th floor, E block, golden city, yeshwanthapuram, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700635284_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635284_pan.jpg\"]', 1, 5, '2023-11-22 12:11:24', 5, '2023-11-22 12:11:24'),
(2, 'Marketing Head 2', 'marketinghead2@test.com', '9080123749', '$2b$12$JU.7BBGv0LjF98UbbGhXJe324fqFaCOfxyl7aS8oZ2uE8lvHcL4ya', 'profile_pic/profile_pic_1700635284_marketing_head.jpg', NULL, '#A13, 4th floor, E block, golden city, yeshwanthapuram, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700635284_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635284_pan.jpg\"]', 0, 5, '2023-11-22 12:11:24', 5, '2023-11-22 12:11:24'),
(3, 'Marketing Head 3', 'marketinghead3@test.com', '9080123750', '$2b$12$JU.7BBGv0LjF98UbbGhXJe324fqFaCOfxyl7aS8oZ2uE8lvHcL4ya', 'profile_pic/profile_pic_1700635284_marketing_head.jpg', NULL, '#A13, 4th floor, E block, golden city, yeshwanthapuram, Bangalore 560058', 'Aadhar', '[\"documents/documents_1700635284_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700635284_pan.jpg\"]', 1, 5, '2023-11-22 12:11:24', 5, '2023-11-22 12:11:24');

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
(1, 'Indolens Own Store 1', 'Indolense Mysore', '1235689784', 'GSTIN0211587546', 'indolensownstore1@gmail.com', 'Mysore', 'Karnataka', '560254', 12.2958104, 76.6393805, '5rd Cross\r\n#A228', 1, 5, '2023-11-13 19:43:36', 5, '2023-11-13 19:53:28'),
(2, 'Indolens Own Store 2', 'Indolense Mandya ', '9235689785', 'GSTIN0211587546', 'indolensownstore2@gmail.com', 'Mandya', 'Karnataka', '560253', 12.2958104, 76.6393805, '5rd Cross\r\n#A228', 1, 5, '2023-11-13 19:43:36', 5, '2023-11-13 19:53:28'),
(3, 'Indolens Own Store 3', 'Indolense Bangalore ', '9235689789', 'GSTIN0211587546', 'indolensownstore3@gmail.com', 'Bangalore', 'Karnataka', '560251', 12.2958104, 76.6393805, '5rd Cross\r\n#A228', 1, 5, '2023-11-13 19:43:36', 5, '2023-11-13 19:53:28');

-- --------------------------------------------------------

--
-- Table structure for table `own_store_employees`
--

CREATE TABLE `own_store_employees` (
  `employee_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `assigned_store_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `document_1_type` varchar(255) NOT NULL,
  `document_1_url` varchar(255) NOT NULL,
  `document_2_type` varchar(255) NOT NULL,
  `document_2_url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store_employees`
--

INSERT INTO `own_store_employees` (`employee_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `role`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`, `certificates`) VALUES
(1, 'Manager 1', 'manager1@test.com', '9078651239', '$2b$12$ybrqmeMwtV.DfExPvkE/uuBkcS8dBlkONPqzdydLesWOCI4.wCksy', 'profile_pic/profile_pic_1699901768_Users-Administrator-icon.png', 1, '#A-148, 3rd cross peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699901768_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699901768_pan.jpg\"]', 1, 1, 5, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', NULL),
(2, 'Manager 2', 'manager2@test.com', '9078651230', '$2b$12$ybrqmeMwtV.DfExPvkE/uuBkcS8dBlkONPqzdydLesWOCI4.wCksy', 'profile_pic/profile_pic_1699901768_Users-Administrator-icon.png', 2, '#A-148, 3rd cross peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699901768_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699901768_pan.jpg\"]', 1, 1, 5, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', NULL),
(3, 'Manager 3', 'manager3@test.com', '9078651231', '$2b$12$ybrqmeMwtV.DfExPvkE/uuBkcS8dBlkONPqzdydLesWOCI4.wCksy', 'profile_pic/profile_pic_1699901768_Users-Administrator-icon.png', 0, '#A-148, 3rd cross peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699901768_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699901768_pan.jpg\"]', 1, 1, 5, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', NULL),
(4, 'Own store optimetry 1', 'ownstoreoptimetry1@test.com', '9087134208', '$2b$12$oh5bKDm2Kmf9TwjC25SBIOiYyojShQbcH0A.KMAz3je.RgIq/02D2', 'profile_pic/profile_pic_1699903123_profile.png', 1, '#B-221, 4th cross, peenya 1stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903123_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903123_pan.jpg\"]', 1, 2, 5, '2023-11-14 00:48:39', 5, '2023-11-14 00:48:39', '[\"certificates/certificates_1700000213_wed2.jpg\", \"certificates/certificates_1700000214_wed1.jpg\"]'),
(5, 'Own store optimetry 2', 'ownstoreoptimetry2@test.com', '9087134207', '$2b$12$oh5bKDm2Kmf9TwjC25SBIOiYyojShQbcH0A.KMAz3je.RgIq/02D2', 'profile_pic/profile_pic_1699903123_profile.png', 2, '#B-221, 4th cross, peenya 1stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903123_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903123_pan.jpg\"]', 1, 2, 5, '2023-11-14 00:48:39', 5, '2023-11-14 00:48:39', '[\"certificates/certificates_1700000213_wed2.jpg\", \"certificates/certificates_1700000214_wed1.jpg\"]'),
(6, 'Own store optimetry 3', 'ownstoreoptimetry3@test.com', '9087134206', '$2b$12$oh5bKDm2Kmf9TwjC25SBIOiYyojShQbcH0A.KMAz3je.RgIq/02D2', 'profile_pic/profile_pic_1699903123_profile.png', 0, '#B-221, 4th cross, peenya 1stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903123_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903123_pan.jpg\"]', 1, 2, 5, '2023-11-14 00:48:39', 5, '2023-11-14 00:48:39', '[\"certificates/certificates_1700000213_wed2.jpg\", \"certificates/certificates_1700000214_wed1.jpg\"]'),
(7, 'Own store Sales Executive 1', 'ownstoresalesexecutive1@test.com', '9823075628', '$2b$12$QWn843HhstoBaC5U2ywwHuzueUV1wy58Mf/Pg3QfEX6IAFIdFbg2G', 'profile_pic/profile_pic_1699903535_user2-160x160.jpg', 1, '#A98, Agarwal enterprise, 2nd cross, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903535_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903535_pan.jpg\"]', 1, 3, 5, '2023-11-14 00:55:31', 5, '2023-11-14 00:55:31', NULL),
(8, 'Own store Sales Executive 2', 'ownstoresalesexecutive2@test.com', '9823075629', '$2b$12$QWn843HhstoBaC5U2ywwHuzueUV1wy58Mf/Pg3QfEX6IAFIdFbg2G', 'profile_pic/profile_pic_1699903535_user2-160x160.jpg', 0, '#A98, Agarwal enterprise, 2nd cross, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903535_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903535_pan.jpg\"]', 0, 3, 5, '2023-11-14 00:55:31', 5, '2023-11-14 00:55:31', NULL),
(9, 'Own store Sales Executive 3', 'ownstoresalesexecutive3@test.com', '9823075625', '$2b$12$QWn843HhstoBaC5U2ywwHuzueUV1wy58Mf/Pg3QfEX6IAFIdFbg2G', 'profile_pic/profile_pic_1699903535_user2-160x160.jpg', 2, '#A98, Agarwal enterprise, 2nd cross, peenya 1st stage, Bangalore 560058', 'Aadhar', '[\"documents/documents_1699903535_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699903535_pan.jpg\"]', 1, 3, 5, '2023-11-14 00:55:31', 5, '2023-11-14 00:55:31', NULL),
(10, 'Own store house keeping 1', 'ownstorehousekeeping1@test.com', '9081249836', '$2b$12$8bt8xRgKz9J59tVZ5PiTwOmiTVZmKcm6yXDfrv3aeExt8cNR5d8.C', 'profile_pic/profile_pic_1699904445_DSC_0167-removebg-preview (1).png', 0, 'VCNR hospital, 1st floor, nelmangala, Bangalore 56012', 'Aadhar', '[\"documents/documents_1699904445_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699904445_pan.jpg\"]', 1, 4, 5, '2023-11-14 01:09:22', 5, '2023-11-14 01:09:22', NULL),
(11, 'Own store house keeping 2', 'ownstorehousekeeping2@test.com', '9081249837', '$2b$12$8bt8xRgKz9J59tVZ5PiTwOmiTVZmKcm6yXDfrv3aeExt8cNR5d8.C', 'profile_pic/profile_pic_1699904445_DSC_0167-removebg-preview (1).png', 0, 'VCNR hospital, 1st floor, nelmangala, Bangalore 56012', 'Aadhar', '[\"documents/documents_1699904445_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699904445_pan.jpg\"]', 1, 4, 5, '2023-11-14 01:09:22', 5, '2023-11-14 01:09:22', NULL),
(12, 'Own store house keeping 3', 'ownstorehousekeeping3@test.com', '9081249838', '$2b$12$8bt8xRgKz9J59tVZ5PiTwOmiTVZmKcm6yXDfrv3aeExt8cNR5d8.C', 'profile_pic/profile_pic_1699904445_DSC_0167-removebg-preview (1).png', 0, 'VCNR hospital, 1st floor, nelmangala, Bangalore 56012', 'Aadhar', '[\"documents/documents_1699904445_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1699904445_pan.jpg\"]', 0, 4, 5, '2023-11-14 01:09:22', 5, '2023-11-14 01:09:22', NULL),
(13, 'Own store optimetry 4', 'ownstoreoptimetry4@test.com', '9809876735', '$2b$12$Ip2vLCF5ZkzuecgX/ue8quNqvjIPHDEbK1VoDkU6vCHnodPd1KOTm', 'profile_pic/profile_pic_1700000213_profile.png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1700000213_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1700000213_pan.jpg\"]', 0, 2, 5, '2023-11-15 03:42:48', 5, '2023-11-15 03:42:48', '[\"certificates/certificates_1700000213_wed2.jpg\", \"certificates/certificates_1700000214_wed1.jpg\"]');

-- --------------------------------------------------------

--
-- Table structure for table `product_categories`
--

CREATE TABLE `product_categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `category_prefix` varchar(255) NOT NULL,
  `category_description` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_categories`
--

INSERT INTO `product_categories` (`category_id`, `category_name`, `category_prefix`, `category_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Lens', 'IND', 'Indolens Lens', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Contact Lens', 'IND', 'Indolens Contact Lens', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(3, 'Frame', 'IND', 'Indolens Frame ', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(4, 'Lens Cover', 'IND', 'Indolens Lens Cover ', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

-- --------------------------------------------------------

--
-- Table structure for table `product_colors`
--

CREATE TABLE `product_colors` (
  `color_id` int(11) NOT NULL,
  `color_code` varchar(255) NOT NULL,
  `color_name` varchar(255) NOT NULL,
  `color_description` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_colors`
--

INSERT INTO `product_colors` (`color_id`, `color_code`, `color_name`, `color_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Red01', 'Red', 'Dark Red', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Brown02', 'Brown', 'Light Brown', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(3, 'Green 03', 'Green', 'Grass Green', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

-- --------------------------------------------------------

--
-- Table structure for table `product_materials`
--

CREATE TABLE `product_materials` (
  `material_id` int(11) NOT NULL,
  `material_name` varchar(255) NOT NULL,
  `material_description` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_materials`
--

INSERT INTO `product_materials` (`material_id`, `material_name`, `material_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Fiber', 'Fiber Material', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'Plastic', 'Plastic Material', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(3, 'Gold', 'Gold Material', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

-- --------------------------------------------------------

--
-- Table structure for table `request_products`
--

CREATE TABLE `request_products` (
  `request_products_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `store_type` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `product_quantity` int(11) NOT NULL,
  `unit_cost` int(11) NOT NULL,
  `request_status` int(11) NOT NULL,
  `delivery_status` int(11) NOT NULL,
  `is_requested` tinyint(1) NOT NULL,
  `request_to_store_id` int(11) NOT NULL,
  `payment_status` int(11) NOT NULL,
  `comment` varchar(255) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `request_products`
--

INSERT INTO `request_products` (`request_products_id`, `store_id`, `store_type`, `product_id`, `product_quantity`, `unit_cost`, `request_status`, `delivery_status`, `is_requested`, `request_to_store_id`, `payment_status`, `comment`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 1, 1, 1, 55, 0, 1, 0, 0, 0, 0, '', '2023-11-14 13:01:27', 5, '2023-11-14 13:01:27', 5),
(2, 1, 1, 1, 5, 0, 1, 0, 0, 0, 0, '', '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(3, 1, 1, 1, 10, 0, 1, 0, 0, 0, 0, '', '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(4, 1, 1, 2, 45, 0, 1, 0, 0, 0, 0, '', '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(5, 1, 1, 3, 85, 0, 1, 0, 0, 0, 0, '', '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(6, 1, 1, 1, 95, 0, 1, 0, 0, 0, 0, '', '2023-11-20 13:47:59', 5, '2023-11-20 13:47:59', 5),
(7, 1, 1, 1, 95, 0, 1, 0, 0, 0, 0, '', '2023-11-21 12:05:46', 5, '2023-11-21 12:05:46', 5),
(8, 3, 1, 1, 90, 0, 1, 0, 0, 0, 0, '', '2023-11-25 22:00:17', 5, '2023-11-25 22:00:17', 5),
(9, 1, 1, 1, 90, 0, 1, 0, 0, 0, 0, '', '2023-11-25 22:00:17', 5, '2023-11-25 22:00:17', 5),
(10, 1, 1, 1, 90, 0, 1, 0, 0, 0, 0, '', '2023-11-25 22:44:03', 5, '2023-11-25 22:44:03', 5),
(11, 1, 1, 1, 90, 0, 1, 0, 0, 0, 0, '', '2023-11-25 22:45:39', 5, '2023-11-25 22:45:39', 5),
(12, 1, 1, 1, 90, 0, 1, 0, 0, 0, 0, '', '2023-11-25 22:45:39', 5, '2023-11-25 22:45:39', 5),
(13, 1, 1, 1, 50, 0, 0, 0, 1, 2, 0, '', '2023-11-25 23:09:59', 1, '2023-11-25 23:09:59', 1),
(14, 2, 1, 2, 50, 0, 1, 0, 0, 0, 0, '', '2023-11-25 23:20:48', 5, '2023-11-25 23:20:48', 5),
(15, 2, 1, 2, 55, 0, 1, 0, 0, 0, 0, 'test comment section', '2023-11-25 23:26:36', 5, '2023-11-25 23:26:36', 5);

-- --------------------------------------------------------

--
-- Table structure for table `reset_password`
--

CREATE TABLE `reset_password` (
  `reset_password_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Table structure for table `store_expense`
--

CREATE TABLE `store_expense` (
  `store_expense_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `store_type` int(11) NOT NULL,
  `expense_amount` int(11) NOT NULL,
  `expense_reason` varchar(255) NOT NULL,
  `expense_date` datetime NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_inventory`
--

CREATE TABLE `store_inventory` (
  `store_inventory_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `store_type` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `product_quantity` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_inventory`
--

INSERT INTO `store_inventory` (`store_inventory_id`, `store_id`, `store_type`, `product_id`, `product_quantity`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 1, 1, 1, 675, '2023-11-14 13:13:54', 5, '2023-11-25 22:45:39', 5),
(3, 1, 1, 2, 10, '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(4, 1, 1, 3, 85, '2023-11-14 13:13:54', 5, '2023-11-14 13:13:54', 5),
(8, 3, 1, 1, 90, '2023-11-25 22:00:17', 5, '2023-11-25 22:00:17', 5),
(13, 2, 1, 2, 105, '2023-11-25 23:20:48', 5, '2023-11-25 23:26:36', 5);

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
-- Table structure for table `units`
--

CREATE TABLE `units` (
  `unit_id` int(11) NOT NULL,
  `unit_name` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `units`
--

INSERT INTO `units` (`unit_id`, `unit_name`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Premium', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5),
(2, 'standard', 1, '2023-11-13 20:00:12', 5, '2023-11-13 20:00:12', 5);

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
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`brand_id`);

--
-- Indexes for table `central_inventory`
--
ALTER TABLE `central_inventory`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  ADD PRIMARY KEY (`shape_id`);

--
-- Indexes for table `frame_types`
--
ALTER TABLE `frame_types`
  ADD PRIMARY KEY (`frame_id`);

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
-- Indexes for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  ADD PRIMARY KEY (`employee_id`);

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
-- Indexes for table `own_store_employees`
--
ALTER TABLE `own_store_employees`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `product_categories`
--
ALTER TABLE `product_categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `product_colors`
--
ALTER TABLE `product_colors`
  ADD PRIMARY KEY (`color_id`);

--
-- Indexes for table `product_materials`
--
ALTER TABLE `product_materials`
  ADD PRIMARY KEY (`material_id`);

--
-- Indexes for table `request_products`
--
ALTER TABLE `request_products`
  ADD PRIMARY KEY (`request_products_id`);

--
-- Indexes for table `reset_password`
--
ALTER TABLE `reset_password`
  ADD PRIMARY KEY (`reset_password_id`);

--
-- Indexes for table `sales_executive`
--
ALTER TABLE `sales_executive`
  ADD PRIMARY KEY (`sales_executive_id`);

--
-- Indexes for table `store_expense`
--
ALTER TABLE `store_expense`
  ADD PRIMARY KEY (`store_expense_id`);

--
-- Indexes for table `store_inventory`
--
ALTER TABLE `store_inventory`
  ADD PRIMARY KEY (`store_inventory_id`),
  ADD UNIQUE KEY `store_product_unique` (`store_id`,`store_type`,`product_id`);

--
-- Indexes for table `store_manager`
--
ALTER TABLE `store_manager`
  ADD PRIMARY KEY (`store_manager_id`);

--
-- Indexes for table `units`
--
ALTER TABLE `units`
  ADD PRIMARY KEY (`unit_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accountant`
--
ALTER TABLE `accountant`
  MODIFY `accountant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `area_head`
--
ALTER TABLE `area_head`
  MODIFY `area_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `central_inventory`
--
ALTER TABLE `central_inventory`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  MODIFY `shape_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `frame_types`
--
ALTER TABLE `frame_types`
  MODIFY `frame_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  MODIFY `franchise_owner_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `franchise_store`
--
ALTER TABLE `franchise_store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `lab`
--
ALTER TABLE `lab`
  MODIFY `lab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lab_technician`
--
ALTER TABLE `lab_technician`
  MODIFY `lab_technician_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `marketing_head`
--
ALTER TABLE `marketing_head`
  MODIFY `marketing_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `own_store_employees`
--
ALTER TABLE `own_store_employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `product_categories`
--
ALTER TABLE `product_categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product_colors`
--
ALTER TABLE `product_colors`
  MODIFY `color_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `product_materials`
--
ALTER TABLE `product_materials`
  MODIFY `material_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `request_products`
--
ALTER TABLE `request_products`
  MODIFY `request_products_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `reset_password`
--
ALTER TABLE `reset_password`
  MODIFY `reset_password_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_executive`
--
ALTER TABLE `sales_executive`
  MODIFY `sales_executive_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_expense`
--
ALTER TABLE `store_expense`
  MODIFY `store_expense_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_inventory`
--
ALTER TABLE `store_inventory`
  MODIFY `store_inventory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `store_manager`
--
ALTER TABLE `store_manager`
  MODIFY `store_manager_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `units`
--
ALTER TABLE `units`
  MODIFY `unit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
