-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 20, 2023 at 08:45 AM
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
(1, 'acc name', 'acc@gmail.com', '1111111111', 'accpassword', 'profile_pic/profile_pic_1695128877_profile.png', 'acc address ', 'Aadhar', '[\"documents/documents_1695128877_greeting_logo (2).png\", \"documents/documents_1695128877_greeting_logo (1).png\"]', 'Pan Card', '[\"documents/documents_1695128877_user2-160x160.jpg\", \"documents/documents_1695128877_user1-128x128.jpg\"]', 1, 1, '2023-09-19 18:36:45', 1, '2023-09-19 18:36:45'),
(2, 'test', 'test@gmail.com', '2147483647', 'password', 'profile_pic/profile_pic_1697004594_profile.png', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697004594_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697004594_pan.jpg\"]', 1, 5, '2023-10-11 11:35:18', 5, '2023-10-11 11:35:18'),
(3, 'Nikshep Thapa', 'nikshep@gmail.com', '9876789765', '1234test', 'profile_pic/profile_pic_1697455691_DSC_0179-removebg-preview (1).png', ' Mandya', 'Aadhar', '[\"documents/documents_1697455691_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697455691_pan.jpg\"]', 1, 5, '2023-10-16 16:11:27', 5, '2023-10-16 16:11:27');

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
(5, 'John Doe', 'admin@indolens.com', '1234567890', 'admin@#123', 1, 'profile_pic.jpg', '123 Main St, City, Country', 'Document 1 Type', '{\"key\": \"value1\"}', 'Document 2 Type', '{\"key\": \"value2\"}', 1, 1, '2023-09-21 12:18:10', 1, '2023-09-21 12:18:10'),
(10, 'sub admin', 'subadmin@gmail.com', '4455667788', 'testpwd', 2, 'profile_pic/profile_pic_1697002958_profile.png', '4th Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697002958_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697002958_pan.jpg\"]', 1, 0, '2023-10-11 11:02:38', 0, '2023-10-11 11:02:38'),
(11, 'sub admin', 'subadmin@gmail.com', '9090909090', 'pwd', 2, 'profile_pic/profile_pic_1697558262_profile.png', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697558262_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697558262_pan.jpg\"]', 1, 0, '2023-10-17 19:50:14', 0, '2023-10-17 19:50:14');

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
(1, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', '1234test', 'profile_pic/profile_pic_profile.png_1694343962', '2,4', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_wed2.jpg_1694343962\", \"documents/documents_wed1.jpg_1694343962\"]', 'Pan Card', '[\"documents/documents_greeting_logo (2).png_1694343962\", \"documents/documents_greeting_logo (1).png_1694343962\"]', 1, 1, '2023-09-10 16:34:46', 1, '2023-09-10 16:34:46'),
(2, 'Niraj Thapa', 'niraj@gmail.com', '2147483647', 'niraj', 'profile_pic/profile_pic_profile.png_1694349566', '2', 'peenya 1st stage bangalore 560058 ', 'Aadhar', '[\"documents/documents_greeting_logo (2).png_1694349566\"]', 'Pan Card', '[\"documents/documents_wed2.jpg_1694349566\", \"documents/documents_wed1.jpg_1694349566\"]', 1, 1, '2023-09-10 17:52:05', 1, '2023-09-10 17:52:05'),
(3, 'Darshan Bhandari', 'darshu@gmail.com', '2147483647', 'Darsh@123', 'profile_pic/profile_pic_DSC_0179-removebg-preview (1).png_1694700697', '', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694700697\", \"documents/documents_user1-128x128.jpg_1694700697\"]', 'Pan Card', '[\"documents/documents_user2-160x160.jpg_1694700697\", \"documents/documents_user1-128x128.jpg_1694700697\"]', 1, 1, '2023-09-14 19:39:46', 1, '2023-09-14 19:39:46'),
(4, 'Darshan Bhandari', 'darshu@gmail.com', '2147483647', 'Darsh@123', 'profile_pic/profile_pic_DSC_0179-removebg-preview (1).png_1694700793', '', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_user2-160x160.jpg_1694700793\", \"documents/documents_user1-128x128.jpg_1694700793\"]', 'Pan Card', '[\"documents/documents_user2-160x160.jpg_1694700793\", \"documents/documents_user1-128x128.jpg_1694700793\"]', 1, 1, '2023-09-14 19:43:10', 1, '2023-09-14 19:43:10'),
(5, 'Area Head', 'areahead@gmail.com', '2147483647', 'pwd', 'profile_pic/profile_pic_1697002797_profile.png', '', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697002797_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697002797_pan.jpg\"]', 1, 5, '2023-10-11 11:02:38', 5, '2023-10-11 11:02:38');

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
(1, 'brand name', 1, ' poiuytyuio', 1, '2023-10-03 19:59:48', 5, '2023-10-03 19:59:48', 5),
(2, 'test brand name', 2, ' test description', 1, '2023-10-03 19:59:48', 5, '2023-10-03 19:59:48', 5),
(3, 'xy', 1, ' dref', 1, '2023-10-04 11:46:21', 0, '2023-10-04 11:46:21', 0),
(4, 'xy', 1, ' dref', 0, '2023-10-04 12:16:13', 0, '2023-10-04 12:16:13', 0),
(5, 'test brand', 2, ' sdfghjkl;', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5);

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
  `origin` int(11) NOT NULL,
  `cost_price` int(11) NOT NULL,
  `sale_price` int(11) NOT NULL,
  `model_number` int(11) NOT NULL,
  `hsn` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_updated_on` datetime NOT NULL,
  `last_updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-18 12:43:10.634056'),
(2, 'auth', '0001_initial', '2023-10-18 12:43:10.972095'),
(3, 'admin', '0001_initial', '2023-10-18 12:43:11.050722'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-18 12:43:11.050722'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-18 12:43:11.066402'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-10-18 12:43:11.114915'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-10-18 12:43:11.145103'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-10-18 12:43:11.176317'),
(9, 'auth', '0004_alter_user_username_opts', '2023-10-18 12:43:11.183338'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-10-18 12:43:11.208036'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-10-18 12:43:11.223665'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-10-18 12:43:11.226102'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-10-18 12:43:11.245866'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-10-18 12:43:11.256537'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-10-18 12:43:11.283565'),
(16, 'auth', '0011_update_proxy_permissions', '2023-10-18 12:43:11.283565'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-10-18 12:43:11.298076');

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
('0jed5635znq4l49zqpjfyj5d4axhf98q', 'e30:1qlObf:IvX_sYeTbdAYwrJJu3vmDBrDiGQxnmTp3ejs5m-1RwE', '2023-10-11 07:05:11.763861'),
('0v7cyevx5tss0fb6qbfjlevh4588wj1w', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qerqO:HRW9I1yrUvVh55DBEUukNZH4bO34138uodYFEKwSogA', '2023-09-23 06:53:24.171838'),
('2j9z93h8w5h8tq39pwz3rxn1tjgn3enn', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qtNjb:FmvNFWeP3FzJpML36DYvd9o4obdp5S296QBQvAATFJQ', '2023-11-02 07:46:23.112930'),
('2vzor9et6mpngdgoj1cj7it4vudk45g7', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qmprb:qnxYuu1YL3YgPdyQHz_2SPayuNngLCL7qQV3B3KHGb8', '2023-10-15 06:23:35.075345'),
('4rppb7nmc32g3iac8jd3olhqkr7opxrc', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qirc2:BUYoY7ZfQDfPhO3unHF2fxaFQodzwKwAC96ZYIq4c_4', '2023-10-04 07:27:06.409238'),
('5gj03vrfwajgoqzq1o48jz7yp48m3dtl', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qh1cR:Id6-gP3ffaZ5flRk1d7HRzC7nL2SpELZFKmJI_dMrno', '2023-09-29 05:43:55.156342'),
('5hre8c1y1e4robl9ame8jgsqrbesrlzi', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qgjg3:bNwp2HesoyhwiQ02rhL9epSiu4UWe54rbjc6-QXmnT4', '2023-09-28 10:34:27.213659'),
('7cfcaq9blx91tgif8g4ihq4fzz557g4n', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qnvfo:-9AG_FRTzXE-FoJkDU_1CTxkicGrE9_jgWMbnz2ncqg', '2023-10-18 06:47:56.524022'),
('a4ruq9lnoyayz7vt8y1z12hi7cp0nc62', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qiwye:86VHjGGW5rklooE238vUy4ff9bF6Jmedl6PF0_l5HXk', '2023-10-04 13:10:48.607286'),
('b8l3vfkf2qtznvms7w09y1r6opo146ch', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qe8AS:AQWws2m8ssIEcc8FGwTvo-3kzJ0FO5JkIon0l_GqkRM', '2023-09-21 06:07:04.464787'),
('bjr4ob6u7uys32wsy97or5tpn0ljtyt2', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qiXGx:lgvNZidfxSsAH4GEQpsXSKwHiCAVQ71-oPOm3ZjPdlY', '2023-10-03 09:43:59.634363'),
('d7pwgjwjmmg7nxn8mlcqk7nkd4g5gd3e', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qi8fy:d6pSVptyxocRXCFIuK2tjAAQyGQ2OxYbI1y9k52UInQ', '2023-10-02 07:28:10.061111'),
('decowcqbg4va7ap2zwclyeo09w0q5k2b', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qt1oj:1khiYbGOZdLZXTrZ7Bda1gq0CREBxT1qofNwpxf2a18', '2023-11-01 08:22:13.387049'),
('dt8odvmao8glv0a0wejp76rar0xkuqhc', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qszkq:Bzxa5T9omCtAzP5v6_6E4g0sm7MbJUeLLg_0BiMm6q8', '2023-11-01 06:10:04.454607'),
('h5jij5pc8n2cp4xrscb633uksy1a0a5u', 'e30:1qk3Bl:jRhf2d9q2mw2hG7nZo4pTAK3Y_YW2fWg4Hi1VPbh7Ak', '2023-10-07 14:00:53.600132'),
('jru9de42wikyl59rdxaluu9fp116xjva', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qtM4V:3ZW3JhY8ADiZHB8JAfDUbSRtPIzTRI8EZ_tLRJNEleQ', '2023-11-02 05:59:51.644315'),
('kgtvl2wjz2x2iulz8d5pa54h1tsr9k54', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qmqt5:A6bCSvZfeFRI8FHOm2IRZqdxrzA1SicXYM_8dd9ZVEw', '2023-10-15 07:29:11.654938'),
('krb0pl7iamt3bieo36871hxapgssi2ui', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qjDUT:XBg-SCITwys-Iar_omYdA6s0xj8B1mquJB2Wc54bE14', '2023-10-05 06:48:45.057121'),
('kwfqssbraq7v9k0sge34r9d4v6imow36', '.eJxNi0EKgCAQRa8Ss5YO4KqWnUJEJxkYR9FaRXdvDIKW773_L6DufMwkjktKGB0J2KOdaACzJwYLb17SoDmUDAbEZ9SwSSyM0qd1LNQ3xe-gWFvZidFVCmr_dD_zTym7:1qdkJR:pH9aDyhztk66uZHOD2ZKfn1S51ppkQ2f2OmhickWkAI', '2023-09-06 12:38:45.368165'),
('l7em6036ivmr8rn0tbj0bvwig8e4trnn', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qmXKL:eo_lslptJUaxABXAFSuIvy-vToFslj-NGgJ1wU4uG5c', '2023-10-14 10:36:01.009354'),
('l7yxpbn3dd7vdm3lcj8bw8v7uwzt9k01', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qj0cR:WbZFe-0Fvy0UFnG7A1mbNm1xsAIWdeR70SGC6qpsLZk', '2023-10-04 17:04:07.190474'),
('m2qxvnyd9mzn0jwgtpdd7i8seoj9udd8', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qneYP:5QGa55pqNJXlYLi9QaRS3oMQFxQLlgf8yURgg1AaBBI', '2023-10-17 12:31:09.631484'),
('noag300cdjgsvlq9iyhgm43bom0tqp4d', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qneDT:X5CRyiGpuRqqEMWfYtGBi7Fklx8b0rE4aoaxl4sEprw', '2023-10-17 12:09:31.052153'),
('nxnsxhy0xnp6om110uebpnykwes3hvqe', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qi8XI:efTbMDgR1qtcuaz7stjO-AgGjXL9TK6zjbtS-Lgr6hc', '2023-10-02 07:19:12.333375'),
('p99wzi3peasn8a8tmlmu6rb6hao8kc1n', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qeUul:Weic5A0bPxB9kzKEzJLzeeLuMAmSNQD7_x1szm0lxgU', '2023-09-22 06:24:23.175906'),
('pqrct4iyk3ckecd92uiuwpuvxyaqu8dj', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qnddW:rzOg3CRNRAupGfbFPvFNHnsK5zqpOjvWynO6usLCkac', '2023-10-17 11:32:22.399625'),
('py3dib2fzu4w7dmu3q7oi1n43jz2uhoe', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qp1sx:-RMWNqaTCpJ8Wc5H5KVVHRjZO50e18o9AMW0dszK4Sw', '2023-10-21 07:38:03.142526'),
('qkxcztiz5cpg6qp700qmkogcyts2duqa', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qogz3:-5z0Mz9OH7bijT84DE0kxjYeIMbN0rxhIhhSvSDNvw4', '2023-10-20 09:18:57.760974'),
('rhcqz29b4fia5cbkwj834ebqdffse30x', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qt4tL:z7DITOtA-Dg9PQDWgrfaXJ0jaIK5_BWdbdBIOkHZFnY', '2023-11-01 11:39:11.415061'),
('s6644e25vtkrtk2ow8v9xvpo96bgngsx', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qt5u6:miPxcfezMO6wGgioc8PXlKy_87gnSlmfAHqn4OxONMU', '2023-11-01 12:44:02.888615'),
('v9d7nbfr1308z80nlos4jgy2teqh4ikv', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qmqcA:X0lYJEnMcjk5SIgVMgSidKaKTgstZwqUsa1Q02NPwJA', '2023-10-15 07:11:42.062320'),
('vpgtw0rzjkxqvg2ikj2mlhjej16u9qym', 'e30:1qm9oi:9p8SsJkdq79ma_xTr2DhWPdT8acgji2rSaeIvurnp9Y', '2023-10-13 09:29:48.047817'),
('wpxbtqq2pi94l2mjipx51rsnhypxovdc', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLVUcpLzE1VslLyys_IU3DJT1XSUSooyk_LzEmNL8hMBkog8fSyCtKVagHSfBz5:1qq92g:u4QpWKCkMF3IA7SDU-gFCfFttflovYWqPD8iYTOFI4E', '2023-10-24 09:28:42.114688'),
('xhpbnmkif52qgusnthxpqpnqes0a0we3', '.eJyrVsosjk9Myc3Mi8_JT09PTYnPzFOyKikqTdVRykxRsjLUUcpLzE1VslLyzEvJz0nNK1ZwBKlW0lEqKMpPy8xJjS_ITAZKI_NqARplHgQ:1qfDd2:zdkjUO4uKjRM8XdYkyu9YWVcd_VH6dCrbPOnBDCpBNU', '2023-09-24 06:09:04.816750');

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
(5, 'oval', ' oval description', 1, '2023-10-04 12:39:23', 5, '2023-10-04 12:39:23', 5),
(6, 'retro', ' wertyhjk', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5);

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
(2, 'frame type name', ' type desp', 1, '2023-10-04 13:04:18', 5, '2023-10-04 13:04:18', 5),
(3, 'frame type', ' sdfghjk', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5);

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
(1, 'franchise store 01', 'Santhosh lense store', 2147483647, 'GSTIN9087H', 'santhosh.lense.store@gmail.test', 'Madanayakahalli', 'Karnataka', '560058', 18.5204303, 73.8567437, '4rd Cross\r\n#A148  ', 0, 1, '2023-09-07 00:21:01', 1, '2023-09-07 11:58:51'),
(2, 'Indolens Franchise Store 04', 'Indolense 04  Mandya', 2147483647, 'GSTIN004', 'rooprajt@gmail.com', 'Mandya', 'Karnataka', '560058', 12.5218157, 76.89514880000002, '4th Cross\r\n#A148', 1, 5, '2023-10-19 11:42:49', 5, '2023-10-19 11:42:49');

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
(1, 'Niraj Thapa', 'niraj@gmail.com', '2147483647', 'niru@1', 'profile_pic/profile_pic_1696494830_profile.png', 1, 'bangalore', 'Aadhar', '[\"documents/documents_1696494830_314_9898989892.png\", \"documents/documents_1696494830_312_9898989892.png\"]', 'Pan Card', '[\"documents/documents_1696494830_circular_logo.png\"]', 1, 1, 5, '2023-10-05 14:02:44', 5, '2023-10-05 14:02:44', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(2, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', 'pwd', 'profile_pic/profile_pic_1696495050_profile.png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1696495050_greeting_card.jpg\"]', 'Pan Card', '[\"documents/documents_1696495050_pan.jpg\"]', 0, 1, 5, '2023-10-05 14:06:40', 5, '2023-10-05 14:06:40', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(3, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', 'password', 'profile_pic/profile_pic_1696501908_profile.png', 0, '4rd Cross\r\n#A148', 'Driving Licence', '[\"documents/documents_1696501908_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696501908_pan.jpg\"]', 0, 1, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(4, 'surabhi', 'surabhi@gmail.com', '8660225160', 'surabhi@1', 'profile_pic/profile_pic_1696505496_profile.png', 0, '4rd Cross\r\n#A148', 'Driving Licence', '[\"documents/documents_1696505496_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696505496_pan.jpg\"]', 1, 2, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(5, 'Santhosh', 'sushi@gmail.com', '9898989898', 'sushi', 'profile_pic/profile_pic_1696507380_profile.png', 1, '4rd Cross\r\n#A148', 'Driving Licence', '[\"documents/documents_1696507380_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696507380_pan.jpg\"]', 1, 3, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(6, 'franchise other emp', 'franchiseotheremp@gmail.com', '9089098789', 'pwd', 'profile_pic/profile_pic_1696670154_profile.png', 1, 'franchise other emp address ', 'Aadhar', '[\"documents/documents_1696670154_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696670154_pan.jpg\"]', 0, 4, 5, '2023-10-07 14:44:56', 5, '2023-10-07 14:44:56', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(7, 'franchise opti', 'franchiseopti@test.com', '9809875432', 'password', 'profile_pic/profile_pic_1697000439_profile.png', 0, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1697000439_aadhar.jpg\"]', 'None', '[\"documents/documents_1697000439_pan.jpg\"]', 0, 2, 0, '2023-10-11 10:29:33', 0, '2023-10-11 10:29:33', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(8, 'franchise opti', 'franchiseopti@test.com', '9809875432', 'password', 'profile_pic/profile_pic_1697000557_profile.png', 0, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1697000557_aadhar.jpg\"]', 'None', '[\"documents/documents_1697000557_pan.jpg\"]', 0, 2, 0, '2023-10-11 10:32:35', 0, '2023-10-11 10:32:35', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(9, 'None', 'testowner@gmail.com', '6677990065', 'pwd', 'profile_pic/profile_pic_1697006973_profile.png', 0, 'None', 'None', '[\"documents/documents_1697006973_aadhar.jpg\"]', 'None', '[\"documents/documents_1697006973_1690794699_wed2.png\"]', 1, 1, 5, '2023-10-11 12:19:20', 5, '2023-10-11 12:19:20', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(10, 'None', 'testowner@gmail.com', '6677990065', 'pwd', 'profile_pic/profile_pic_1697007106_profile.png', 0, 'None', 'None', '[\"documents/documents_1697007106_aadhar.jpg\"]', 'None', '[\"documents/documents_1697007106_1690794699_wed2.png\"]', 1, 1, 5, '2023-10-11 12:19:20', 5, '2023-10-11 12:19:20', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(11, 'Test Franchise Owner', 'testowner@gmail.com', '9620725475', 'pwd', 'profile_pic/profile_pic_1697007491_profile.png', 0, '4rd Cross\r\n#A148', 'Pan Card', '[\"documents/documents_1697007491_aadhar.jpg\"]', 'None', '[\"documents/documents_1697007491_pan.jpg\"]', 1, 1, 5, '2023-10-11 12:26:50', 5, '2023-10-11 12:26:50', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(12, 'test optimetry', 'testoptimetry@gmail.com', '9738450987', 'testpwd', 'profile_pic/profile_pic_1697007590_profile.png', 0, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1697007590_aadhar.jpg\"]', 'None', '[\"documents/documents_1697007590_pan.jpg\"]', 0, 2, 0, '2023-10-11 12:26:50', 0, '2023-10-11 12:26:50', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(13, 'Test certificate', 'certi@gmail.com', '9900350569', 'certi@1', 'profile_pic/profile_pic_1697443890_profile.png', 1, '4th Cross\r\n#A148', '1', '[\"documents/documents_1697443890_aadhar.jpg\"]', '1', '[\"documents/documents_1697443890_pan.jpg\"]', 0, 2, 0, '2023-10-16 13:41:17', 0, '2023-10-16 13:41:17', '[]'),
(14, 'Test Franchise Owner2', 'owner@gmail.com', '9988776655', 'pwd', 'profile_pic/profile_pic_1697559145_profile.png', 0, 'Mysore', 'Aadhar', '[\"documents/documents_1697559145_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697559145_pan.jpg\"]', 1, 1, 5, '2023-10-17 19:50:14', 5, '2023-10-17 19:50:14', NULL),
(15, 'test 18/10', 'rooprajt@gmail.com', '9738505213', 'pwd', 'profile_pic/profile_pic_1697609486_profile.png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697609486_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697609486_pan.jpg\"]', 1, 1, 5, '2023-10-18 11:37:25', 5, '2023-10-18 11:37:25', NULL);

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
(1, 'Nirmala Optics Lab', 'Nirmala Optics Centre', 2147483647, 'GSTIN09876590', 'rooprajt@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.3378762, 77.117325, '4rd Cross\r\n#A148', 1, 5, '2023-10-05 14:11:20', 5, '2023-10-05 14:11:20'),
(2, 'Nikshep optics', 'Nikshep Opticals', 2147483647, 'GSTIN09876780', 'nikshep@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.0345565, 77.52620089999999, '4th Cross\r\n#A148', 1, 5, '2023-10-16 13:54:57', 5, '2023-10-16 13:54:57');

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
(1, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', 'password', 'profile_pic/profile_pic_1696495774_profile.png', 1, '4rd Cross\r\n#A148', 'Driving Licence', '[\"documents/documents_1696495774_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696495774_pan.jpg\"]', 1, 5, '2023-10-05 14:14:30', 5, '2023-10-05 14:14:30'),
(2, 'lab tech', 'labtech@test.com', '9876543218', 'pwd', 'profile_pic/profile_pic_1697005278_profile.png', 0, '4rd Cross\r\n#A148', 'Driving Licence', '[\"documents/documents_1697005278_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697005278_greeting_card1.jpg\"]', 1, 5, '2023-10-11 11:49:49', 5, '2023-10-11 11:49:49'),
(3, 'Niraj Thapa', 'niraj@gmail.com', '9089097654', 'pwd', 'profile_pic/profile_pic_1697453420_DSC_0167-removebg-preview (1).png', 0, 'Brindhavana ', 'Aadhar', '[\"documents/documents_1697453420_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697453420_pan.jpg\"]', 1, 5, '2023-10-16 16:11:27', 5, '2023-10-16 16:11:27');

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
(0, 'Marketing Head', 'marketinghead@gmail.com', '7788665544', 'testpwd', 'profile_pic/profile_pic_1697002519_profile.png', NULL, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697002519_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697002519_pan.jpg\"]', 1, 5, '2023-10-11 11:02:38', 5, '2023-10-11 11:02:38'),
(3, 'Niraj Thapa', 'niraj@gmail.com', '9620725475', 'Niru@123', 'profile_pic/profile_pic_1695030354_profile.png', 1, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1695030354_pic.jpg\",\"documents/documents_1695030354_pic.jpg\"]', 'Pan Card', '[\"documents/documents_1695030354_pic.jpg\"]', 1, 1, '2023-09-18 15:13:31', 1, '2023-09-18 15:13:31'),
(4, 'Nirmala Bhandari', 'nimmi@gmail.com', '9620725475', 'nimmi', 'profile_pic/profile_pic_1695030560_profile.png', NULL, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1695030560_pic.jpg\"]', 'Pan Card', '[\"documents/documents_1695030560_pic.jpg\"]', 1, 1, '2023-09-18 15:17:46', 1, '2023-09-18 15:17:46');

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
(0, 'Indolens ownstore 04', 'Indolense Store 04 Nelmangala', '7788996655', 'GSTIN004', 'Store04@gmail.com', 'Nelmangala', 'Karnataka', '560058', 13.097301, 77.38563979999999, '4th Cross\r\n#A148', 0, 5, '2023-10-19 11:42:49', 5, '2023-10-19 11:42:49'),
(2, 'indolens ownstore 02', 'Indolense Mysore', '9890909090', 'GSTIN001', 'indolens.mysore@gmail.com', 'Mysore', 'Karnataka', '560058', 12.9532583, 77.5434616, ' 4rd Cross\r\n#A148', 1, 1, '2023-09-06 09:47:03', 1, '2023-09-07 11:40:07'),
(4, 'indolens ownstore 03', 'Indolense Mandya', '98765432345', 'GSTIN001', 'indolens.mandya@gmail.com', 'Mandya', 'Karnataka', '560058', 12.5218157, 76.89514880000002, '4rd Cross\r\n#A148', 1, 1, '2023-09-06 21:03:35', 1, '2023-09-06 21:03:35');

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
(1, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', 'password', 'profile_pic/profile_pic_1696493530_profile.png', 2, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]', 'Pan Card', '[\"documents/documents_1696493530_pan.jpg\"]', 1, 1, 5, '2023-10-05 13:41:34', 5, '2023-10-05 13:41:34', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(2, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '2147483647', 'password', 'profile_pic/profile_pic_1696493530_profile.png', 2, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]', 'Pan Card', '[\"documents/documents_1696493530_pan.jpg\"]', 0, 1, 5, '2023-10-05 13:41:34', 5, '2023-10-05 13:41:34', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(3, 'Nirmala Bhandari', 'nkbhandari95@gmail.com', '9620725475', 'nimmi@123', 'profile_pic/profile_pic_1696493896_profile.png', 2, ' Mandya', 'Driving Licence', '[\"documents/documents_1696493896_312_9898989892.png\", \"documents/documents_1696493896_313_9898989892.png\"]', 'Pan Card', '[\"documents/documents_1696493896_user2-160x160.jpg\", \"documents/documents_1696493896_user1-128x128.jpg\"]', 0, 1, 5, '2023-10-05 13:46:00', 5, '2023-10-05 13:46:00', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(4, 'Nirmala Bhandari', 'nkbhandari95@gmail.com', '9620725475', 'nimmi@123', 'profile_pic/profile_pic_1696493896_profile.png', 2, ' Mandya', 'Driving Licence', '[\"documents/documents_1696493896_312_9898989892.png\", \"documents/documents_1696493896_313_9898989892.png\"]', 'Pan Card', '[\"documents/documents_1696493896_user2-160x160.jpg\", \"documents/documents_1696493896_user1-128x128.jpg\"]', 0, 1, 5, '2023-10-05 13:46:00', 5, '2023-10-05 13:46:00', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(5, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '9898989898', 'testpwd', 'profile_pic/profile_pic_1696502372_profile.png', 2, '4rd Cross\r\n#A148', 'Ration Card', '[\"documents/documents_1696502372_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696502372_pan.jpg\"]', 1, 3, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(6, 'test name', 'testemail@test.com', '1111111111', 'testpwd', 'profile_pic/profile_pic_1696503141_profile.png', 2, '4rd Cross\r\n#A148', 'Voter Id', '[\"documents/documents_1696503141_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696503141_pan.jpg\"]', 1, 1, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(7, 'test name', 'testemail@test.com', '1111111111', 'testpwd', 'profile_pic/profile_pic_1696503141_profile.png', 2, '4rd Cross\r\n#A148', 'Voter Id', '[\"documents/documents_1696503141_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696503141_pan.jpg\"]', 1, 1, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(8, 'Ashish', 'ashu@gmail.com', '9900350569', 'ashu@1', 'profile_pic/profile_pic_1696505646_profile.png', 2, '4rd Cross\r\n#A148', 'Ration Card', '[\"documents/documents_1696505646_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696505646_pan.jpg\"]', 1, 1, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(9, 'Ashish', 'ashu@gmail.com', '9900350569', 'ashu@1', 'profile_pic/profile_pic_1696505646_profile.png', 2, '4rd Cross\r\n#A148', 'Ration Card', '[\"documents/documents_1696505646_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696505646_pan.jpg\"]', 1, 1, 5, '2023-10-05 16:01:01', 5, '2023-10-05 16:01:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(10, 'test store manager', 'test@test.com', '9090909090', 'test', 'profile_pic/profile_pic_1696507647_profile.png', 2, 'test address', 'Aadhar', '[\"documents/documents_1696507647_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696507647_pan.jpg\"]', 1, 1, 5, '2023-10-05 17:36:43', 5, '2023-10-05 17:36:43', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(12, 'test manager', 'testmanager@test.com', '9090989098', 'pwd', 'profile_pic/profile_pic_1696664337_profile.png', 2, 'test manager adress', 'Aadhar', '[\"documents/documents_1696664337_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696664337_pan.jpg\"]', 1, 1, 5, '2023-10-07 13:07:29', 5, '2023-10-07 13:07:29', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(13, 'test sales executive', 'testsalesexec@test.com', '9098789098', 'pwd', 'profile_pic/profile_pic_1696664417_profile.png', 2, 'tst sales executive address ', 'Aadhar', '[\"documents/documents_1696664417_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696664417_pan.jpg\"]', 0, 3, 5, '2023-10-07 13:07:29', 5, '2023-10-07 13:07:29', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(14, 'test sales executive', 'testsalesexec@test.com', '9098789098', 'pwd', 'profile_pic/profile_pic_1696664470_profile.png', 2, 'tst sales executive address ', 'Aadhar', '[\"documents/documents_1696664470_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696664470_pan.jpg\"]', 0, 3, 5, '2023-10-07 13:11:08', 5, '2023-10-07 13:11:08', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(15, 'Niraj Thapa', 'niraj@gmail.com', '9089098909', 'pwd', 'profile_pic/profile_pic_1696665713_profile.png', 2, ' niraj residential address', 'Aadhar', '[\"documents/documents_1696665713_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696665713_pan.jpg\"]', 1, 3, 5, '2023-10-07 13:30:01', 5, '2023-10-07 13:30:01', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(16, 'Niraj Thapa', 'niraj@gmail.com', '9089098909', 'pwd', 'profile_pic/profile_pic_1696665769_profile.png', 2, ' niraj residential address', 'Aadhar', '[\"documents/documents_1696665769_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696665769_pan.jpg\"]', 1, 3, 5, '2023-10-07 13:32:49', 5, '2023-10-07 13:32:49', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(17, 'test duplicate record', 'testduplicate@test.com', '9090909090', 'pwd', 'profile_pic/profile_pic_1696665817_profile.png', 0, 'duplicate record test ', 'Aadhar', '[\"documents/documents_1696665817_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696665817_pan.jpg\"]', 0, 3, 5, '2023-10-07 13:32:49', 5, '2023-10-07 13:32:49', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(18, 'other employee', 'otheremp@gmail.com', '9098909890', 'pwd', 'profile_pic/profile_pic_1696666636_profile.png', 2, 'other emp address ', 'Aadhar', '[\"documents/documents_1696666636_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696666636_pan.jpg\"]', 0, 4, 5, '2023-10-07 13:46:25', 5, '2023-10-07 13:46:25', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(19, 'other employee', 'otheremp@gmail.com', '9098909890', 'pwd', 'profile_pic/profile_pic_1696666676_profile.png', 2, 'other emp address ', 'Aadhar', '[\"documents/documents_1696666677_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696666677_pan.jpg\"]', 1, 4, 5, '2023-10-07 13:47:52', 5, '2023-10-07 13:47:52', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(20, 'Test sales exe', 'testemail@test.com', '9620725475', '1234e', 'profile_pic/profile_pic_1696667703_profile.png', 2, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1696667703_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1696667703_pan.jpg\"]', 0, 3, 5, '2023-10-07 14:03:17', 5, '2023-10-07 14:03:17', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(21, 'opti user', 'optiuser@gamil.com', '1111111111', 'pwd', 'profile_pic/profile_pic_1696676683_profile.png', 2, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1696676683_aadhar.jpg\"]', 'None', '[\"documents/documents_1696676683_pan.jpg\"]', 0, 2, 0, '2023-10-07 16:33:32', 0, '2023-10-07 16:33:32', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(22, 'franchise opti', 'optimetry@test.com', '9738505213', 'testpwd', 'profile_pic/profile_pic_1696935635_profile.png', 2, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1696935635_aadhar.jpg\"]', 'None', '[\"documents/documents_1696935635_pan.jpg\"]', 0, 2, 0, '2023-10-10 16:28:24', 0, '2023-10-10 16:28:24', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(23, 'franchise opti', 'optimetry@test.com', '9738505213', 'testpwd', 'profile_pic/profile_pic_1696937732_profile.png', 2, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1696937732_aadhar.jpg\"]', 'None', '[\"documents/documents_1696937732_pan.jpg\"]', 0, 2, 0, '2023-10-10 16:28:24', 0, '2023-10-10 16:28:24', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(24, 'None', 'testmanager@gmail.com', '8765434567', 'pwd', 'profile_pic/profile_pic_1697005477_profile.png', 2, 'None', 'None', '[\"documents/documents_1697005477_aadhar.jpg\"]', 'None', '[\"documents/documents_1697005477_pan.jpg\"]', 1, 1, 5, '2023-10-11 11:54:34', 5, '2023-10-11 11:54:34', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(25, 'test optimetry', 'optimetry@test.com', '9900350569', 'pwd', 'profile_pic/profile_pic_1697005722_profile.png', 2, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1697005722_aadhar.jpg\"]', 'None', '[\"documents/documents_1697005722_pan.jpg\"]', 1, 2, 0, '2023-10-11 11:54:34', 0, '2023-10-11 11:54:34', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(26, 'test optimetry', 'optimetry@test.com', '9900350569', 'pwd', 'profile_pic/profile_pic_1697005774_profile.png', 2, '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1697005774_aadhar.jpg\"]', 'None', '[\"documents/documents_1697005774_pan.jpg\"]', 0, 2, 0, '2023-10-11 11:59:32', 0, '2023-10-11 11:59:32', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(27, 'test executive ', 'test', '9591088997', 'pwd', 'profile_pic/profile_pic_1697006128_profile.png', 2, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1697006128_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697006128_pan.jpg\"]', 0, 3, 5, '2023-10-11 11:59:32', 5, '2023-10-11 11:59:32', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(28, 'other employee test', 'testemp@gmail.com', '9738505213', 'pwd', 'profile_pic/profile_pic_1697006294_profile.png', 0, '4rd Cross\r\n#A148', 'Ration Card', '[\"documents/documents_1697006294_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697006294_pan.jpg\"]', 0, 4, 5, '2023-10-11 11:59:32', 5, '2023-10-11 11:59:32', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(29, 'other employee test', 'testemp@gmail.com', '9738505213', 'pwd', 'profile_pic/profile_pic_1697006372_profile.png', 2, '4rd Cross\r\n#A148', 'Ration Card', '[\"documents/documents_1697006372_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697006372_pan.jpg\"]', 0, 4, 5, '2023-10-11 12:09:28', 5, '2023-10-11 12:09:28', '[\"documents/documents_1696493530_greeting_card1.jpg\", \"documents/documents_1696493530_greeting_card.jpg\"]'),
(30, 'new sale exec', 'newsale@gmail.com', '9988776655', '123', 'profile_pic/profile_pic_1697444314_profile.png', 2, ' ertyhj56', 'Aadhar', '[\"documents/documents_1697444314_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697444314_pan.jpg\"]', 0, 3, 5, '2023-10-16 13:41:57', 5, '2023-10-16 13:41:57', NULL),
(31, 'new sale exec', 'newsale@gmail.com', '9988776655', '123', 'profile_pic/profile_pic_1697444355_profile.png', 2, ' ertyhj56', 'Aadhar', '[\"documents/documents_1697444355_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697444355_pan.jpg\"]', 0, 3, 5, '2023-10-16 13:49:13', 5, '2023-10-16 13:49:13', NULL),
(32, 'test optimatry final', 'finalopti@test.com', '9890876569', 'pwd', 'profile_pic/profile_pic_1697552416_profile.png', 0, ' complete address of opti', 'Aadhar', '[\"documents/documents_1697552416_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1697552416_pan.jpg\"]', 0, 2, 0, '2023-10-17 19:50:14', 0, '2023-10-17 19:50:14', '[]');

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
(1, 'frame', 'prefix', ' description', 1, '0000-00-00 00:00:00', 5, '0000-00-00 00:00:00', 5),
(2, 'Lens', 'hello prefix', ' Hello description', 1, '0000-00-00 00:00:00', 5, '0000-00-00 00:00:00', 5),
(3, 'test name', 'test prefix', 'test description ', 0, '2023-10-03 18:49:25', 5, '2023-10-03 18:49:25', 5),
(4, 'cat1', 'cat prefix', ' esrdfghjkl,.', 0, '2023-10-16 12:44:38', 5, '2023-10-16 12:44:38', 5);

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
(1, 'rdfc', 'red', ' color description', 1, '2023-10-04 13:27:40', 5, '2023-10-04 13:27:40', 5),
(2, 'rbc', 'blue', ' sdfghjk', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5),
(3, 'grb', 'green', 'dfghjkl;', 0, '2023-10-19 16:28:00', 5, '2023-10-19 16:28:00', 5);

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
(1, 'Fiber', ' MAtrerial description', 1, '2023-10-04 13:39:20', 5, '2023-10-04 13:39:20', 5),
(2, 'glass', 'fghjkl; ', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5);

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
(1, 'vajra', 1, '2023-10-16 11:44:25', 5, '2023-10-16 11:44:25', 5),
(2, 'garuda', 0, '2023-10-16 12:47:31', 5, '2023-10-16 12:47:31', 5);

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
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `area_head`
--
ALTER TABLE `area_head`
  MODIFY `area_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
  MODIFY `brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `central_inventory`
--
ALTER TABLE `central_inventory`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  MODIFY `shape_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `frame_types`
--
ALTER TABLE `frame_types`
  MODIFY `frame_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `franchise_store`
--
ALTER TABLE `franchise_store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

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
-- AUTO_INCREMENT for table `own_store_employees`
--
ALTER TABLE `own_store_employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

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
  MODIFY `material_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
