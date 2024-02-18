-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2024 at 07:35 AM
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
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accountant`
--

INSERT INTO `accountant` (`accountant_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Accountant ', 'accountant1@test.com', '9808780986', '$2b$12$iWNaaupawWdVbHYBMwnnXeCBj4N4wcEij4yboaH84nU0mAe8XNJcS', 'profile_pic/profile_pic_1705913339_document1_1703854570_profile_pic_1700635966_accountant.webp', '  Update the address to test  ', 'Aadhar', '[\"documents/document1_1707983211_aadhar.jpg\"]', 'Pan Card', '[\"documents/document2_1707983211_pan.jpg\"]', 1, 1, '2024-01-03 15:20:32', 1, '2024-02-16 17:33:21');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` int(12) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `name`, `email`, `phone`, `password`, `role`, `profile_pic`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Nirmala', 'nkbhandari95@gmail.com', '9620725475', '$2b$12$xPg1c0jgNRED/9fd7UtHHuGWLUznhbbUFl3pmhXoe371YIYG922kK', 1, 'profile_pic/profile_pic_1704272314_sub_admin.jpg', '123 Main St, City', 'Aadhar Card', NULL, 'Pan Card', NULL, 1, 1, '2024-01-03 11:46:04', 1, '2024-01-03 11:46:04'),
(2, 'sub Admin 01', 'subadmin01@gmail.com', '8899006655', '$2b$12$6W3VVm8Ap6T.2MGyP7gyaeZA.pa74ETNwIumRrj4uZXjKLVLBOq0K', 2, 'profile_pic/profile_pic_1704272314_sub_admin.jpg', '  mangalore', 'Aadhar', '[\"documents/documents_1704272314_aadhar.jpg\", \"documents/document1_1704275732_document1_1703854570_profile_pic_1700635966_accountant.webp\"]', 'Pan Card', '[\"documents/documents_1704272314_pan.jpg\", \"documents/document2_1704275775_eyeglass-png.png\", \"documents/document2_1704280922_marketing_head - Copy.jpg\"]', 1, 1, '2024-01-03 14:17:52', 1, '2024-01-03 16:55:46'),
(3, 'sub Admin 02', 'subadmin02@gmail.com', '9898989898', 'None', 2, 'profile_pic/profile_pic_1704281297_document1_1703854570_profile_pic_1700635966_accountant.webp', '  poiuytr lkjhgfdwertyuio oiuytre  kjhgf', 'Aadhar', '[\"documents/documents_1704281297_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704281297_pan.jpg\"]', 0, 1, '2024-01-03 16:57:16', 1, '2024-01-22 14:05:09'),
(4, 'sub Admin 02', 'subadmin03@gmail.com', '9898989898', 'None', 2, 'profile_pic/profile_pic_1705990730_marketing_head.jpg', '     poiuytr lkjhgfdwertyuio oiuytre  kjhgf', 'Aadhar', '[\"documents/documents_1704282195_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704282195_pan.jpg\"]', 0, 1, '2024-01-03 17:13:13', 1, '2024-01-23 11:48:35'),
(5, 'test name', 'testing@gmail.com', '8978675645', '$2b$12$Hape3FhcUpn1FYvSoXEAjehjxaijLNGrt4wyz7ocBxBMXHK0JeIZO', 2, 'profile_pic/profile_pic_1705990527_document1_1703854570_profile_pic_1700635966_accountant.webp', 'fzdxghcjkl/.', 'Aadhar', '[\"documents/documents_1705990527_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1705990527_pan.jpg\"]', 1, 1, '2024-01-23 11:33:31', 1, '2024-01-23 11:33:31'),
(6, 'test sub admin creation', 'devsandy12@gmail.com', '8660225160', '$2b$12$Ucu7v9TUKtkuA.KCOw8ZNu436JW8b9GUGy5SSi1PFagIo5iQVirqW', 2, 'profile_pic/profile_pic_1706344114_accountant.webp', 'madayanakanahalli, bangalore', 'Aadhar', '[\"documents/document1_1706354966_eyeglass-png.png\", \"documents/document1_1706880407_lab_tech.png\"]', 'Pan Card', '[\"documents/document2_1706354966_specs01.jpg\", \"documents/document2_1706880407_marketing_head.jpg\"]', 1, 1, '2024-01-27 13:52:26', 1, '2024-01-27 13:52:26'),
(7, 'Testing sub admin', 'testsub@gmail.com', '9999999999', '$2b$12$Lg4a8Xin5CWxROZDrP0mqO02sTIirgHQtd6hF/bPZZeFwl7Pa3u1i', 2, 'profile_pic/profile_pic_1707485106_document1_1703854570_profile_pic_1700635966_accountant.webp', 'VCN Arcade', 'Aadhar', '[\"documents/documents_1707485106_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/documents_1707485106_pan.jpg\"]', 1, 1, '2024-02-09 18:55:06', 1, '2024-02-09 18:55:06');

-- --------------------------------------------------------

--
-- Table structure for table `admin_setting`
--

CREATE TABLE `admin_setting` (
  `setting_id` int(11) NOT NULL,
  `emailjs_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`emailjs_attribute`)),
  `base_url` varchar(255) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `updated_by` int(11) NOT NULL,
  `updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_setting`
--

INSERT INTO `admin_setting` (`setting_id`, `emailjs_attribute`, `base_url`, `created_by`, `created_on`, `updated_by`, `updated_on`) VALUES
(1, '{\"emailjs_url\": \"https://api.emailjs.com/api/v1.0/email/send\", \"emailjs_service_id\": \"service_7eqv3fu\", \"emailjs_template_id\": \"template_1c47e6e\", \"emailjs_user_id\": \"qbWAgwqHOFbcgoJRF\", \"emailjs_recaptcha\": \"03AHJ_ASjnLA214KSNKFJAK12sfKASfehbmfd...\"}', 'http://127.0.0.1:8000/', 1, '2024-02-09 18:04:25', 1, '2024-02-09 18:47:09');

-- --------------------------------------------------------

--
-- Table structure for table `area_head`
--

CREATE TABLE `area_head` (
  `area_head_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_stores` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `area_head`
--

INSERT INTO `area_head` (`area_head_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_stores`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Area Head update', 'areahead@gmail.com', '9898989898', '$2b$12$TI3fApg72a0zQesoXTSZtO3r0oTBHHofZ26oOegTZsKHGwNcbOHnC', 'profile_pic/profile_pic_1704274433_area_head.png', '1,2', '    Nelamangala    ', 'None', '[\"documents/documents_1704274433_aadhar.jpg\", \"documents/document1_1704275178_313_9898989892.png\"]', 'None', '[\"documents/documents_1704274433_pan.jpg\", \"documents/document2_1704275161_greeting_card1.jpg\"]', 1, 1, '2024-01-03 14:17:52', 1, '2024-01-27 14:11:17'),
(2, 'Area Head 01', 'areahead01@test.com', '7788665544', '$2b$12$vBtLON6usb5gMC6PfTDFvef5pFKmir.zySwPStlXXvrzbD1MVCepa', 'profile_pic/profile_pic_1704274907_area_head - Copy.png', '1,2', 'Mysore', 'None', '[\"documents/documents_1704274907_aadhar.jpg\", \"documents/document1_1704280951_specs01.jpg\"]', 'None', '[\"documents/documents_1704274907_pan.jpg\"]', 1, 1, '2024-01-03 15:11:45', 1, '2024-01-03 15:11:45'),
(3, 'Area Head 02', 'areahead02@test.com', '6565090987', '$2b$12$kjJFJxxr1Am2ejAVthLAcuNMD3uygrfuPq7RGd8byF.a2ZOcuzZbO', 'profile_pic/profile_pic_1705913232_documents_1702293007_accountant.webp', '0', '   Mandya   ', 'Aadhar', '[\"documents/documents_1704275091_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704275091_pan.jpg\"]', 1, 1, '2024-01-03 15:13:24', 1, '2024-01-23 11:49:56'),
(4, 'test area head name on creation', 'devsandy12@gmail.com', '8660225160', '$2b$12$vPQ1rcg0mheVJcOk03xIiOLBThMtiY/uDzbrVTxob3eWqpB0Jx29S', 'profile_pic/profile_pic_1706346621_marketing_head.jpg', '0', 'poiuytre oiuytre poiuytre poiuytre ', 'Aadhar', '[\"documents/documents_1706346621_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1706346621_pan.jpg\"]', 1, 1, '2024-01-27 14:11:17', 1, '2024-01-27 14:11:17'),
(5, 'test ahead 001', 'rooprajt@gmail.com', '9738505213', '$2b$12$hD954qW820ndCNknFIYinuauBHudXt2V8rHjTXF6TwFM8HZiF8PlO', 'profile_pic/profile_pic_1706346832_marketing_head.jpg', '0', '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1706346832_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1706346832_pan.jpg\"]', 1, 1, '2024-01-27 14:42:58', 1, '2024-01-27 14:42:58'),
(6, 'lens area head', 'rooprajt96@gmail.com', '8660225160', '$2b$12$/i8333GjBenqsSNxYqJdl.acE.lMJxF7hCVwwPyB11inXlOhHuABq', 'profile_pic/profile_pic_1706346925_frame03.jpg', '0', '4rd Cross\r\n#A148', 'None', '[\"documents/documents_1706346925_aadhar.jpg\"]', 'None', '[\"documents/documents_1706346925_pan.jpg\"]', 1, 1, '2024-01-27 14:44:23', 1, '2024-01-27 14:44:23');

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `brand_id` int(11) NOT NULL,
  `brand_name` varchar(255) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `brand_description` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`brand_id`, `brand_name`, `category_id`, `brand_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Lens Guru', 0, 'lens guru brand', 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1),
(2, 'Indolens', 0, 'indolens brand', 0, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1);

-- --------------------------------------------------------

--
-- Table structure for table `central_inventory`
--

CREATE TABLE `central_inventory` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `product_description` longtext DEFAULT NULL,
  `product_images` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`product_images`)),
  `product_qr_code` varchar(255) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `material_id` int(11) DEFAULT NULL,
  `frame_type_id` int(11) DEFAULT NULL,
  `frame_shape_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `origin` varchar(255) DEFAULT NULL,
  `cost_price` int(11) DEFAULT NULL,
  `sale_price` int(11) DEFAULT NULL,
  `model_number` varchar(255) DEFAULT NULL,
  `hsn` varchar(255) DEFAULT NULL,
  `power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`power_attribute`)),
  `franchise_sale_price` double DEFAULT NULL,
  `product_quantity` int(11) DEFAULT NULL,
  `product_gst` float DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `central_inventory`
--

INSERT INTO `central_inventory` (`product_id`, `product_name`, `product_description`, `product_images`, `product_qr_code`, `category_id`, `brand_id`, `material_id`, `frame_type_id`, `frame_shape_id`, `color_id`, `unit_id`, `origin`, `cost_price`, `sale_price`, `model_number`, `hsn`, `power_attribute`, `franchise_sale_price`, `product_quantity`, `product_gst`, `status`, `discount`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'INDOLENSE frame_01', '<p>fframe desc</p>', '[\"products/products_1707302289_specs01.jpg\", \"products/products_1707302289_eyeglass-png.png\"]', 'product_qr_codes/9.png', 1, 1, 1, 1, 1, 1, 1, 'Indian', 999, 1499, 'MN no01', 'HSN no 01', '{}', 1999, 29, 10, 1, 5, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1),
(2, 'Lens Stock 01', '<p>lens stock</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 2, 1, 1, 0, 0, 1, 1, 'Indian', 999, 1499, 'MN no 01', 'HSN No 01', '{\"vision_type\": \"single_vision\", \"stock_type\": \"stock\", \"index\": \"0.2\"}', 1999, 123, 10, 1, 5, '2024-01-03 11:55:48', 1, '2024-01-04 02:47:25', 1),
(3, 'Contact lens rx01', '<p>contact lens rx</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 3, 1, 1, 0, 0, 2, 0, 'Foreign', 1999, 1599, 'MN no 01', 'HSN 02', '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Soft\", \"contact_lens_disposability\": \"6 Month\"}', 1999, 138, 10, 1, 5, '2024-01-03 11:55:48', 1, '2024-01-04 02:47:25', 1),
(4, 'Contact lens rx02', '<p>Contactlens rx</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\", \"products/products_1707303233_eyeglass-png.png\", \"products/products_1707303367_specs01.jpg\"]', 'product_qr_codes/9.png', 3, 1, 1, 0, 0, 1, 1, 'Indian', 8765, 9000, 'MN no01', 'HSN no 01', '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Semi Soft\", \"contact_lens_disposability\": \"Yearly\"}', 9500, 118, 10, 1, 5, '2024-01-03 19:10:22', 1, '2024-01-03 19:10:22', 1),
(5, 'Contact lens stock 01', '<p>Contact lens stock</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 3, 2, 1, 0, 0, 2, 1, 'Domestic', 999, 1500, 'MN no01', 'HSN123', '{\"stock_type\": \"stock\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"Daily\"}', 2000, 1, 10, 1, 5, '2024-01-03 19:10:22', 1, '2024-01-04 02:47:25', 1),
(6, 'Metalic Red Oval Frame', '<p>fframe desc</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 1, 1, 1, 1, 1, 1, 1, 'Indian', 999, 1499, 'INDL9876', 'HSN no 01', '{}', 1999, 18, 10, 1, 5, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1),
(7, 'Crystal white glacier frame', '<p>this frame has been edited to test the flow to redirect t view page</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 1, 1, 1, 1, 1, 1, 1, 'Indian', 2000, 2600, 'INDL9876', 'HSN no 01', '{}', 1999, 165, 10, 1, 0, '2024-01-03 11:55:48', 1, '2024-02-01 19:32:31', 1),
(8, 'Lens uat test 1', '<p>Lens uat test 1</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 2, 1, 1, 0, 0, 1, 1, 'Indian', 499, 1000, 'IND9876', 'IND876KJHG', '{\"vision_type\": \"single_vision\", \"stock_type\": \"stock\", \"index\": \"0.1\"}', 650, 250, 0, 0, 5, '2024-01-20 12:14:48', 1, '2024-01-20 12:14:48', 1),
(9, 'Lens uat test 1', '<p>Lens uat test 1</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 2, 1, 1, 0, 0, 1, 1, 'Indian', 499, 1000, 'IND9876', 'IND876KJHG', '{\"vision_type\": \"single_vision\", \"stock_type\": \"stock\", \"index\": \"0.2\"}', 650, 250, 0, 0, 5, '2024-01-20 12:16:42', 1, '2024-01-26 17:59:21', 1),
(10, 'oiuytfd', '<p>oiuyt</p>', '[\"products/products_1705733111_specs01.jpg\", \"products/products_1705733111_eyeglass-png.png\"]', 'product_qr_codes/9.png', 4, 1, 1, 0, 0, 2, 1, 'Indian', 444, 666, 'oiuyt9876', 'lkjhgf87654', '{}', 600, 65, 0, 0, 0, '2024-01-20 12:26:21', 1, '2024-02-01 19:39:55', 1),
(11, 'test lens rx', '<p><strong><a title=\"Lens Image here\" href=\"https://tse3.mm.bing.net/th?id=OIP.NuPp6jqjJweFRXqo8DD_nwHaHi&amp;pid=Api&amp;P=0&amp;h=180\" target=\"_blank\" rel=\"noopener\">Lens Image here</a>Test lens index value as 0.2 </strong></p>\r\n<p>The test lens serves as an advanced diagnostic instrument, empowering users with the ability to assess and evaluate a myriad of factors within a specific context. Through its customizable parameters and intricate design, this versatile tool provides a focused and comprehensive perspective, allowing for in-depth scrutiny and understanding of complex details. With features for fine-tuned examinations, researchers, analysts, and professionals can leverage its adaptability for data-driven decision-making. Its rich text capabilities enhance the user experience, enabling the inclusion of formatted content, images, and diverse data types for a more immersive and informative analysis</p>\r\n<p><strong>Lense feature</strong></p>\r\n<ol>\r\n<li>point1</li>\r\n<li>pounr2</li>\r\n<li>point3</li>\r\n</ol>\r\n<p><strong>Lense Specification</strong></p>\r\n<ul>\r\n<li>Spec1</li>\r\n<li>Spec2</li>\r\n<li>Spec3</li>\r\n</ul>\r\n<p><img src=\"blob:http://127.0.0.1:8000/0d021f31-3b55-4785-a76f-16bbd012fc30\"></p>\r\n<p>&nbsp;</p>\r\n<p>https://tse3.mm.bing.net/th?id=OIP.NuPp6jqjJweFRXqo8DD_nwHaHi&amp;pid=Api&amp;P=0&amp;h=180</p>', '[\"products/products_1706877526_specs01.jpg\"]', 'product_qr_codes/11.png', 2, 1, 1, 0, 0, 1, 1, 'Indian', 200, 300, 'POIUYT8765', 'POIUYT7654', '{\"vision_type\": \"bifocal\", \"stock_type\": \"rx\", \"index\": \"0.2\"}', 125, 123, 0, 1, 0, '2024-01-26 17:59:21', 1, '2024-02-14 17:25:45', 1),
(12, 'test restock log', '<p>test restock log</p>', '[\"products/products_1708003676_accountant.webp\", \"products/products_1708031295_eyeglass-png.png\", \"products/products_1708031344_specs01.jpg\", \"products/products_1708032021_specs01.jpg\", \"products/products_1708032021_eyeglass-png.png\"]', 'product_qr_codes/12.png', 1, 1, 1, 1, 2, 1, 1, 'Foreign', 200, 400, 'MJHGF98765r', 'HJKJHGFD8765', '{}', 300, 0, 1, 0, 0, '2024-02-06 15:22:58', 1, '2024-02-16 18:46:49', 1);

-- --------------------------------------------------------

--
-- Table structure for table `central_inventory_restock_log`
--

CREATE TABLE `central_inventory_restock_log` (
  `restock_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `central_inventory_restock_log`
--

INSERT INTO `central_inventory_restock_log` (`restock_id`, `product_id`, `quantity`, `created_by`, `created_on`) VALUES
(1, 5, 2, 1, '2024-02-05 15:55:26'),
(2, 11, 11, 1, '2024-02-05 15:55:58'),
(3, 11, 2, 1, '2024-02-05 22:08:58'),
(4, 11, 3, 1, '2024-02-05 22:09:05'),
(5, 11, 5, 1, '2024-02-05 22:09:11'),
(6, 5, -4, 1, '2024-02-06 12:00:29'),
(7, 5, -12, 1, '2024-02-06 12:00:41'),
(8, 5, 14, 1, '2024-02-06 12:04:13'),
(9, 11, 2, 1, '2024-02-06 12:04:59'),
(10, 12, 200, 1, '2024-02-06 15:22:58'),
(11, 1, 100, 1, '2024-02-12 14:34:01'),
(12, 1, 900, 1, '2024-02-12 14:34:25');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `created_by_employee_id` int(11) DEFAULT NULL,
  `created_by_store_id` int(11) DEFAULT NULL,
  `created_by_store_type` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_by_employee_id` int(11) DEFAULT NULL,
  `updated_by_store_id` int(11) DEFAULT NULL,
  `updated_by_store_type` int(11) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `gender`, `age`, `phone`, `email`, `language`, `city`, `address`, `created_by_employee_id`, `created_by_store_id`, `created_by_store_type`, `created_on`, `updated_by_employee_id`, `updated_by_store_id`, `updated_by_store_type`, `updated_on`) VALUES
(1, 'Niraj Thapa', 'M', 4, '9089765423', 'nirajthapa@gmail.com', 'Hindi', 'Bangalore', '4rd Cross #A148', 17, 1, 1, '2024-01-03 17:14:12', 17, 1, 1, '2024-02-01 16:28:59'),
(10, 'Nikshep Thapa', 'M', 18, '9620725475', 'nikshepthapa@gmail.com', 'Hindi', 'Bangalore', '4rd Cross #A148', 17, 1, 1, '2024-01-03 17:46:50', 2, 2, 2, '2024-02-08 12:05:19'),
(11, 'Darshan Bhandari', 'M', 27, '9738505213', 'darshan@test.com', 'Kannada', 'Mandya', '#A-13, Water quarters, abc nagara, def layout, Mandya, Karnataka 569-034', 17, 1, 1, '2024-01-03 17:46:50', 17, 1, 1, '2024-02-09 13:16:52'),
(12, 'Nirmala', 'F', 28, '9620725457', 'nimmi@gmail.com', 'English', 'mandya', 'Mandya', 17, 1, 2, '2024-01-03 17:46:50', 17, 1, 1, '2024-02-08 11:59:57'),
(13, 'Alok', 'M', 25, '9900350569', 'alok@gamil.com', 'Hindi', 'Bangalore', '4rd Cross\n#A148', 17, 1, 1, '2024-01-03 17:46:50', 17, 1, 1, '2024-01-03 17:46:50'),
(14, 'Anil', 'M', 35, '9728765678', 'ani@gmail.com', 'English', 'Bangalore', '4rd Cross\n#A148', 17, 1, 1, '2024-01-03 17:46:50', 17, 1, 1, '2024-01-03 17:46:50'),
(15, 'Shwetha', 'F', 29, '9876543219', 'shwe@gmail.com', 'Kannada', 'Mysore', 'Mysore', 17, 1, 1, '2024-01-03 17:46:50', 17, 1, 1, '2024-02-09 13:10:10'),
(16, 'Nidhi', 'F', 21, '9591088997', 'nidhi@gmail.com', 'Tamil', 'Nelmangala', 'Nelmangala', 17, 1, 1, '2024-01-03 17:46:50', 17, 1, 1, '2024-01-03 17:46:50'),
(17, 'ROOP RAJ THAPA', 'M', 24, '90897654213', 'rooprajt@gmail.com', 'Hindi', 'Bangalore', '4rd Cross\n#A148', 17, 1, 1, '2024-01-03 18:29:15', 17, 1, 1, '2024-01-03 18:29:15'),
(25, 'Rj Thapa', 'M', 28, '7411865276', 'rjthapa@gmail.com', 'Hindi', 'Bangalore', '#A-148, 3rd cross, Peenya 1st stage, Bangalore 560058', 17, 1, 1, '2024-01-07 14:16:44', 17, 1, 1, '2024-02-09 13:00:43'),
(27, 'Santhosk Kumar', 'M', 18, '9089765431', 'devsandy12@gmail.com', 'Hindi', 'Bangalore', '23, 1st floor, Appannna building, krishna layout, 3rd cross, 1st stage, Bangalore 560058, Karnataka', 17, 1, 1, '2024-01-07 17:37:34', 17, 1, 1, '2024-02-02 19:15:06'),
(45, 'Test eye', 'M', 35, '9988776655', 'testeye@gmail.com', 'Tamil', 'Bangalore', '4rd Cross\r\n#A148', 17, 1, 1, '2024-01-09 17:16:55', 17, 1, 1, '2024-01-09 18:00:52'),
(49, 'test user for eye test', 'M', 29, '9089878765', 'testuserforeye@test.com', 'Kannada', 'Bangalore city north', 'new customer to test the eye test module', 2, 1, 1, '2024-01-11 11:15:12', 17, 1, 1, '2024-01-20 14:18:53');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext DEFAULT NULL,
  `expire_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1rzzhr9dw884jqiy2ravfcg41je9oebc', '.eJxNjVEOgyAQRK9i9ptYsTZYv3qBnoFQ2BoSWAxgTNP07kVtGv923szOvMEmmXKIKF0YRzTSEgw5zsjAGhi4YEDKIwxwV6RGjBUHBuiVdYX5nfFbxpRrHXzx9rbfkyUTHFKqwkKbUTXtP5Nf05pZC1VKdqQyvzvbNIMphqd1KCerS-6gTodbctF0or92_UWaoGePlNMK2_Z6bhohldZhpqwo1ws-Jvh8ASKXU6Y:1rSwEv:g8sPKuU46n4JxKd_xGBa_pmI5HGr_qUHxvIGTYvBcJk', '2024-02-08 09:41:41.733597'),
('2oikzv7m8ljmji6vb0pi13if06g5fdqv', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rVB5r:ceVskALa6iJDJGGM5L_WeXWIU9c-8h0gknMQHrLVQIU', '2024-02-14 13:57:35.980435'),
('3j9n3lw4jtv2y049o5lpkrqamhpuxhfs', 'e30:1rNtxz:D_IpIMVlqRUf8Ep0W7OK-B9xjs1cGCkTwnGG9rYmKLI', '2024-01-25 12:15:23.480164'),
('3qu2dpekfmolf8zfoja6zf2xz5h71lvl', '.eJxNjssKwjAQRX8lzDpWGy1qVoJbceU-pOmYDuZFExci_rspiHQ3d86cy7yBsnK6VwXNqFy0FgdFAWSZnsiBBpCCQ9AeQcJF9-xW75gADug1ubqs8uyKU8FcGhN9ZXPhz7nSI4-YWEyFTK4sTfFODlUiU_EirRezaveb7thud93h_x1bsXNMryYFC58vdyQ-KA:1rY1YQ:8rv0_b220GUOqXm8eBeQOC-10opSKxXJ2yr0TLJCL20', '2024-02-22 10:22:50.979584'),
('4i0txivlwfmqdzxjyzo84xq95e86r3in', 'e30:1rQjFu:K1aga-aYVqUQFamJvHX1mzLbL44qkfyelaocHRj2Ch4', '2024-02-02 07:25:34.594104'),
('4ki69wo0j8eqshx8y6z37mpj6zpq73e9', '.eJxlj8sKgzAQRX9FZq3WWKHgqqtu-wkh1TEO5EWSKqX03xsrFcHdPM7MvfcNFLjoNRmurJTYczLQRv_EHKiHts7BCI3Qws0L040UMLvPBn1WQw7O24EUckddInbdaVdzdqma-sKqc8NHVMoWHrWd8CEL53EinEtnZPqWnAx_ER6i9Xj0hFqQSlobaBcz9TViiGVndXqzXh5c_8ZZxbINiS-3IEsQEQJJk5TWzZKcfb6Zi2PJ:1rMN5k:RnjLwMFqgdX7Ym31Zv8EyKFcZctHYoHeK4wMAgwO6VU', '2024-01-21 06:57:04.105260'),
('588rvtm74cph6jn8pex5y48q713ph13y', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1rV8Rb:TV5r5gQeQw53nu9EhR2q6PebR5V1LG20WvACbIYPNnA', '2024-02-14 11:07:51.791239'),
('5bnubh6w0ich3rnmn99xj6bsu33jsoti', '.eJxNjVEOgyAQRK9i9ptYsTZYv3qBnoFQ2BoSWAxgTNP07kVtGv923szOvMEmmXKIKF0YRzTSEgw5zsjAGhi4YEDKIwxwV6RGjBUHBuiVdYX5nfFbxpRrHXzx9rbfkyUTHFKqwkKbUTXtP5Nf05pZC1VKdqQyvzvbNIMphqd1KCerS-6gTodbctF0or92_UWaoGePlNMK2_Z6bhohldZhpqwo1ws-Jvh8ASKXU6Y:1rRq98:mIEIB4WpG96z6JHyiPgV2DjQwGG5PhkB8WGxM8WWJnA', '2024-02-05 08:59:10.505599'),
('6bubfkwco0gxbque6z9c2d82soaiiv14', '.eJxNjs0KAiEUhV9F7tomlQHJVTGb3iFCZLzZhRkVtUVE756zanbnj4_zAarWFXT2ic7bJYWA3lIE08oLOZAHozi4WinE3tSWClYwN8nVnUN0K4KBSwewawcwIYEDro6WHm_cDSvkuWFtw5zW3uaSHrSgzTT3zc4dd9pKLUalx5PQ_3vswKaU30OOAb4_BZM-gQ:1rXKt1:kL-ZstG0uYvm2Mdbf2z10Ke2qc8AXhh2qVSmWZTjIbE', '2024-02-20 12:49:15.845162'),
('6ceia4ydxileycxaqfl6rbls9tkjcs5z', 'e30:1rRoMS:06e5vVfgIBXdi4ZvzuQywfboVlfOUM3c-NE4hujdiDM', '2024-02-05 07:04:48.485082'),
('7dk4nqsrhrxodakxndx1slsja4w1ai0h', '.eJxNj80OgjAQhF-F7JkgIIafk3ePPkBT2xWa0F1Ci4QY390CxnDbnW92M_MG44TzPKLouW1RC0PQ-HHCGIyGJitjIGkRGrhL8h27LrpNVo4QA1pp-gA0vpwkvWT5tV2lRLENeP_6OzakuUdyEc-0gSjN_x6_DKsnC4J0zrQUYuxkixDDMPLT9CgGo4LvsJ0Os8jKtCiruqguQrOaLJJ3q5jn9TlNSyGV4ol8qJHM-Bjg8wVIhFcB:1rat6v:6_7ZwvbslFhuqQ4x60MnczeKMjlw7eJnNsPEGIjfXM0', '2024-03-01 07:58:17.752523'),
('7pcs6ki8sngt0ngtk8iahu68tmwh2icl', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rTcmY:M-FxaxyGWmzSyN2DJthH1qc6ZAqgBpB5xRV5P7eBjEA', '2024-02-10 07:07:14.194724'),
('8suit0n58dey5xoumoabqea0ot0cj5c7', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rRSNC:TT143BQgYya6nWqOtfPf_Grs8uW-8Rc-qqw7vyF2Z0w', '2024-02-04 07:36:06.780200'),
('8v3gcgq2anjuua228zs5p5a28kbx9sj8', 'e30:1rUmCv:oowoZTWW4fqinlfVgwlXF5rdDQXbSF2O2nIs74z3Ukk', '2024-02-13 11:23:13.417979'),
('agaturw2lrpwm2ka2lw2ibxdevriv511', '.eJxNjVsOgjAQRbdC5rsgNUoTvtyAa2gqjHWSvtJWiDHu3QLG8Ddz7pm5b6AkU_YRpfFa4yjJQZ_jExnQCD0XDJyyCD1clVMaY8WBAVpFpjC7MX7JmHIzeFuy7dvviNzoDbpU-dmtQdXyv5NfYXEWoFIi7Ur9lqzVDEL0dzIoAw3F222H3Sy5aE_HTojuLB9ojK8jWj_hTdch4kQ4N8Fp-HwBAMJRPA:1rKzlm:6x7bg690OqjKQBlp4kQ60fxKsqOgqvT5BDPNaIhXLJQ', '2024-01-17 11:50:46.746966'),
('ajeazvpuzqggugbgjap1opn75cxj6agl', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1rZRzQ:Wlk5d6DKZeBON_0sNue6HFYG4d_kPClhMtOKhq8FVUA', '2024-02-26 08:48:36.145925'),
('ajmu4ifjmolp7e8osgjbm0qm7bez5l1f', '.eJxNj80OgjAQhF-F7JkgIIafk3ePPkBT2xWa0F1Ci4QY390CxnDbnW92M_MG44TzPKLouW1RC0PQ-HHCGIyGJitjIGkRGrhL8h27LrpNVo4QA1pp-gA0vpwkvWT5tV2lRLENeP_6OzakuUdyEc-0gSjN_x6_DKsnC4J0zrQUYuxkixDDMPLT9CgGo4LvsJ0Os8jKtCiruqguQrOaLJJ3q5jn9TlNSyGV4ol8qJHM-Bjg8wVIhFcB:1rYKVd:nb3NhrGZgFgdQUEXmDHuUgzu3TrquY52rYs49g0gFB8', '2024-02-23 06:37:13.320832'),
('dvat2g80aermbg8dnxqq07elu2bi8ho2', '.eJxNjssKwjAQRX8lzDpWGy1qVoJbceU-pOmYDuZFExci_rspiHQ3d86cy7yBsnK6VwXNqFy0FgdFAWSZnsiBBpCCQ9AeQcJF9-xW75gADug1ubqs8uyKU8FcGhN9ZXPhz7nSI4-YWEyFTK4sTfFODlUiU_EirRezaveb7thud93h_x1bsXNMryYFC58vdyQ-KA:1rYKXZ:ogq8zKTKY8mVP-B78HI4rNlPiOTRbG7PxbzRHb8hlok', '2024-02-23 06:39:13.722055'),
('ere4g8nys6yqvcsiggm1rkiu9xzx5072', '.eJxNjssKwjAQRX8lzLrUGoVgVn6AdOU-pOmYDuZFE1fivzsFke7mzplzmTdQNcFOpqFbTMje42wogW7rCzugGbTsINmIoOFmJ3HnOyGhA4yWAi9Z3lx5bVhb73JkthX-nJGedcEicmnkKrOy5gcFNIUc41067GZzVMNZKjWcLv_v-pI8fL7N9Twd:1rQLqL:545U2webnYjtryu3U27-43mrn-9N9c2clpp6rPTslKE', '2024-02-01 06:25:37.407050'),
('eygaws270lkh7tel831dxhdvqow1kelh', '.eJxNjVsOgjAQRbdC5rsgNUoTvtyAa2gqjHWSvtJWiDHu3QLG8Ddz7pm5b6AkU_YRpfFa4yjJQZ_jExnQCD0XDJyyCD1clVMaY8WBAVpFpjC7MX7JmHIzeFuy7dvviNzoDbpU-dmtQdXyv5NfYXEWoFIi7Ur9lqzVDEL0dzIoAw3F222H3Sy5aE_HTojuLB9ojK8jWj_hTdch4kQ4N8Fp-HwBAMJRPA:1rL8na:iit0SUmHS5olybHZz23Ekuw5Ry5YDrG80ebXUqjzPeM', '2024-01-17 21:29:14.734951'),
('fc0f5f8mnclwwhzyuju4rirrzz7m7yia', 'e30:1rOY60:OAiBcFb-VG8Qwhm8S4H4fjLid66q2xOEyDvgM7Hih7s', '2024-01-27 07:06:20.523697'),
('fq0wmahwfbuw1qaxt89vlnvxx78ej1gj', '.eJxNjs0KAiEUhV9F7tomlQHJVTGb3iFCZLzZhRkVtUVE756zanbnj4_zAarWFXT2ic7bJYWA3lIE08oLOZAHozi4WinE3tSWClYwN8nVnUN0K4KBSwewawcwIYEDro6WHm_cDSvkuWFtw5zW3uaSHrSgzTT3zc4dd9pKLUalx5PQ_3vswKaU30OOAb4_BZM-gQ:1rUmsR:Xlq-uNnfmdZ6S77WKvdmwugZhe81gUXtR43MhsSwYqA', '2024-02-13 12:06:07.550268'),
('frjttrsq07do5f74eiidjyowbapzmtdk', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1ratjH:Hq352kwBduTRa9anwtNwXouOc8FUnAqE_KtDTBZaGJ4', '2024-03-01 08:37:55.793976'),
('fuscsxcvkje6ter29l7x6pwisystayw9', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rV5C0:WE-UHwrmFzsWzwm9wiAFXW83z6HgrUJmeZGMaQ3AIdQ', '2024-02-14 07:39:32.615639'),
('i8y4cnaivn3zlukq8horfw5wm9r1nn8s', '.eJxNyDsOgCAQRdG9vJr4K_xQW7uFCZGRTAIjQa2Me9fS7p57Qw5yPolS3ENgT6KwZ7nYQDxsa6AuMSwWKclFB4Nc9k0iU5b1-z_Vv6a2n4ZuaMa-oZkPCVplDXhewc8m1w:1rN7Pw:AhwWG1Ik_lIZWbvO3KDNGUev6Cv1yLyOkjLOxS4mLRg', '2024-01-23 08:25:00.417872'),
('j20n0rh2olmr30fufobrflboee4oxjy8', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rR64v:KX4fBpsUGmCtYqeY3h0JGlMDmLv435uB3N7U8LSUnJk', '2024-02-03 07:47:45.304418'),
('k1hjjmzz3l0g79y0q1xzpwemueu2czit', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1ratjj:UoYbhzWtwpnJ0Auu8TEaggVv2gzz2UeoQqC6OlSRNEw', '2024-03-01 08:38:23.360309'),
('kwl70ju6i41ow9bj8vbjdluciefi0fmy', '.eJxNjVEOgyAQRK9i9ptYsTZYv3qBnoFQ2BoSWAxgTNP07kVtGv923szOvMEmmXKIKF0YRzTSEgw5zsjAGhi4YEDKIwxwV6RGjBUHBuiVdYX5nfFbxpRrHXzx9rbfkyUTHFKqwkKbUTXtP5Nf05pZC1VKdqQyvzvbNIMphqd1KCerS-6gTodbctF0or92_UWaoGePlNMK2_Z6bhohldZhpqwo1ws-Jvh8ASKXU6Y:1rR6sv:scJS8VjmPrexNDX0T0x0CHlPkl4tLLtsa1GDPrsHut8', '2024-02-03 08:39:25.571192'),
('mdrbam0g4qni5nd43ce05spt2zr5by80', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rVskw:CW5m-8bR6KrhHbX5GVU7pFOc5KNCNziqSDhzHJvbHYA', '2024-02-16 12:34:54.265068'),
('n33vqbvm4lq0pm6xyyysd5483oxcomnl', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1raEJ5:WTK3Zqm8r5J5a9CDsihgp-G1qZ7kKl72MriJbYTHawA', '2024-02-28 12:24:07.506685'),
('obheryspugi28ovw7er4fu0wdodmupd8', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1rXhE7:C_KrTFleIth4RX0aFx8nqqxhcHE2Iq4vL-kTMz6jKcY', '2024-02-21 12:40:31.492254'),
('q6rz2j0md4t3xrggxj7szze0aq3y3x5x', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1rXbtz:JOqx852v4oKGIlnwJOj5x1ukzOarVkBuamUBXqi-NOE', '2024-02-21 06:59:23.690267'),
('ql071ailg8jru7782ny64thlt6a9t0xp', '.eJxNjssKwjAQRX8lzDpWGy1qVoJbceU-pOmYDuZFExci_rspiHQ3d86cy7yBsnK6VwXNqFy0FgdFAWSZnsiBBpCCQ9AeQcJF9-xW75gADug1ubqs8uyKU8FcGhN9ZXPhz7nSI4-YWEyFTK4sTfFODlUiU_EirRezaveb7thud93h_x1bsXNMryYFC58vdyQ-KA:1raiMv:4zE8yFl75pyeIw2xiaCrIo1dmkgdAWbiwcgQ8zuf2v0', '2024-02-29 20:30:05.911696'),
('rk38axwclk8k2p76umjj9umoktvt4u2s', 'e30:1rXJ8q:KvPfjZPhnG6PAZwY7CnAXMylfQViHiac3_BUBrnLbKI', '2024-02-20 10:57:28.658820'),
('sb4o278cb5curq6rhlrau6p6j1my6qee', '.eJxNjssKwjAQRX8lzDpWGy1qVoJbceU-pOmYDuZFExci_rspiHQ3d86cy7yBsnK6VwXNqFy0FgdFAWSZnsiBBpCCQ9AeQcJF9-xW75gADug1ubqs8uyKU8FcGhN9ZXPhz7nSI4-YWEyFTK4sTfFODlUiU_EirRezaveb7thud93h_x1bsXNMryYFC58vdyQ-KA:1raxZi:El4n_jWD-1O3obtFdjsuO0e8jD9SzlCnRs17n9KALuc', '2024-03-01 12:44:18.121085'),
('ujrore6bup0nu0boqaccdpckk5hsv78q', '.eJxNj80OgjAQhF-F7JkgIIafk3ePPkBT2xWa0F1Ci4QY390CxnDbnW92M_MG44TzPKLouW1RC0PQ-HHCGIyGJitjIGkRGrhL8h27LrpNVo4QA1pp-gA0vpwkvWT5tV2lRLENeP_6OzakuUdyEc-0gSjN_x6_DKsnC4J0zrQUYuxkixDDMPLT9CgGo4LvsJ0Os8jKtCiruqguQrOaLJJ3q5jn9TlNSyGV4ol8qJHM-Bjg8wVIhFcB:1rVRot:NR3N0FPwuICqecLAllMB7_2BjD5XkAkq7r62g87rCd0', '2024-02-15 07:49:11.124038'),
('vm0uxi07xcrwdxgj4o073tqzo4kuvv6c', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rSFiZ:eivM9w-pPVQj7zZ_y3Cb89s-cMCuPqmaJcZS8qC5Seo', '2024-02-06 12:17:27.597396'),
('wzpo0ybq0y55hfcrlnzjju0kh06iqx60', '.eJxdjssOgjAQRX-lmZUmREt5KKxcufUTJrWM2ARa0pYQY_x3QZAYdzP3nNzcJ2iPNyeNumtP6IN1hI2ta6pQGyiD6ykCXUEpIjCyJSjh_NXZZTDkmIAIqJW6GdlaZSckToF82CnbjsrcvXSsHvvEjIvVCI9uMqZAeq9rM06ZyTKjc_amG8JOq9H7-fY_N8YHnhWxyNMUK6v6lkyIpzA5Zml24Pjn8jzJijxHqZTtTZAmsE283Q107eD1BgE9ZD8:1rXyQt:laisrnQXz59Wa_a8jp1kVmOv2zzjaKauybmKsYuJtEM', '2024-02-22 07:02:51.127181'),
('y2kwhhao0srltzp4aq759h0fjrqhls0p', '.eJxNyDsOgCAQRdG9vJr4K_xQW7uFCZGRTAIjQa2Me9fS7p57Qw5yPolS3ENgT6KwZ7nYQDxsa6AuMSwWKclFB4Nc9k0iU5b1-z_Vv6a2n4ZuaMa-oZkPCVplDXhewc8m1w:1rLiTy:qhTqY5vMDxZdfpR3tnr8NXGhBDX5WvLW_YuxTYv0ENI', '2024-01-19 11:35:22.285971'),
('yl0cccp2ckomfwo0ecoqmefb59xndf6n', '.eJxNjU0KgCAUBu_yraWygsBDdIWHpckL_9BaRXcvaNNuZjZzgStpEziST85ZQxyhjnJaATZQUiDqYKEwcwnaawjkkjb2ljKvb_9Z-2OSUzf2Uz_Ikeq5fI9mzw73AzqLKBw:1rYMD8:_Pz2KgaFVCBonondilCig7KAehcSkOZk-7zkH9IZW5A', '2024-02-23 08:26:14.774575');

-- --------------------------------------------------------

--
-- Table structure for table `eye_test`
--

CREATE TABLE `eye_test` (
  `eye_test_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `power_attributes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`power_attributes`)),
  `created_by_store_id` int(11) NOT NULL,
  `created_by_store_type` int(11) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `updated_by` int(11) NOT NULL,
  `updated_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `eye_test`
--

INSERT INTO `eye_test` (`eye_test_id`, `customer_id`, `power_attributes`, `created_by_store_id`, `created_by_store_type`, `created_by`, `created_on`, `updated_by`, `updated_on`) VALUES
(1, 25, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"10\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 17:06:30', 17, '2024-01-09 17:06:30'),
(2, 27, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"10\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 17:16:55', 17, '2024-01-09 17:16:55'),
(3, 45, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"12\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 17:16:55', 17, '2024-01-09 17:16:55'),
(4, 45, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"12\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 18:00:52', 17, '2024-01-09 18:00:52'),
(5, 27, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"12\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 18:00:52', 17, '2024-01-09 18:00:52'),
(6, 45, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"12\", \"pdl\": \"15\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"1\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 17, '2024-01-09 18:00:52', 17, '2024-01-09 18:00:52'),
(7, 49, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"2\", \"RightDvAxis\": \"3\", \"RightDvVision\": \"4\", \"RightNvSph\": \"5\", \"RightNvCyl\": \"6\", \"RightNvAxis\": \"7\", \"RightNvVision\": \"8\", \"LeftDvSph\": \"8\", \"LeftDvCyl\": \"7\", \"LeftDvAxis\": \"6\", \"LeftDvVision\": \"5\", \"LeftNvSph\": \"4\", \"LeftNvCyl\": \"3\", \"LeftNvAxis\": \"2\", \"LeftNvVision\": \"1\", \"unifocal\": \"\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"1\", \"arc\": \"\", \"pdr\": \"12\", \"pdl\": \"21\", \"glass\": \"\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"1\", \"near\": \"\"}', 1, 2, 2, '2024-01-11 11:15:12', 2, '2024-01-11 11:15:12'),
(8, 27, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"2\", \"RightDvAxis\": \"3\", \"RightDvVision\": \"4\", \"RightNvSph\": \"5\", \"RightNvCyl\": \"6\", \"RightNvAxis\": \"7\", \"RightNvVision\": \"8\", \"LeftDvSph\": \"8\", \"LeftDvCyl\": \"7\", \"LeftDvAxis\": \"6\", \"LeftDvVision\": \"5\", \"LeftNvSph\": \"4\", \"LeftNvCyl\": \"3\", \"LeftNvAxis\": \"2\", \"LeftNvVision\": \"1\", \"unifocal\": \"\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"11\", \"pdl\": \"22\", \"glass\": \"\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"1\", \"near\": \"1\"}', 1, 2, 2, '2024-01-11 11:18:15', 2, '2024-01-11 11:18:15'),
(9, 49, '{\"RightDvSph\": \"909\", \"RightDvCyl\": \"2\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"2\", \"RightNvSph\": \"2\", \"RightNvCyl\": \"23\", \"RightNvAxis\": \"4\", \"RightNvVision\": \"4\", \"LeftDvSph\": \"4\", \"LeftDvCyl\": \"5\", \"LeftDvAxis\": \"3\", \"LeftDvVision\": \"5\", \"LeftNvSph\": \"3\", \"LeftNvCyl\": \"6\", \"LeftNvAxis\": \"8\", \"LeftNvVision\": \"6\", \"unifocal\": \"\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"123\", \"pdl\": \"456\", \"glass\": \"\", \"highIndex\": \"1\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"\"}', 1, 2, 2, '2024-01-11 11:18:15', 2, '2024-01-11 11:18:15'),
(10, 25, '{\"RightDvSph\": \"1111\", \"RightDvCyl\": \"1\", \"RightDvAxis\": \"1\", \"RightDvVision\": \"1\", \"RightNvSph\": \"1\", \"RightNvCyl\": \"1\", \"RightNvAxis\": \"1\", \"RightNvVision\": \"1\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"1\", \"LeftDvAxis\": \"1\", \"LeftDvVision\": \"1\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"1\", \"LeftNvAxis\": \"1\", \"LeftNvVision\": \"1\", \"unifocal\": \"\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"9738\", \"pdl\": \"9738\", \"glass\": \"\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"1\", \"distance\": \"\", \"near\": \"\"}', 1, 1, 17, '2024-01-11 11:18:15', 17, '2024-01-11 11:18:15');

-- --------------------------------------------------------

--
-- Table structure for table `frame_shapes`
--

CREATE TABLE `frame_shapes` (
  `shape_id` int(11) NOT NULL,
  `shape_name` varchar(255) DEFAULT NULL,
  `shape_description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_shapes`
--

INSERT INTO `frame_shapes` (`shape_id`, `shape_name`, `shape_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Square', 'square frame shape', 0, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1),
(2, 'Oval', 'oval frame shape', 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1);

-- --------------------------------------------------------

--
-- Table structure for table `frame_types`
--

CREATE TABLE `frame_types` (
  `frame_id` int(11) NOT NULL,
  `frame_type_name` varchar(255) DEFAULT NULL,
  `frame_type_description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_types`
--

INSERT INTO `frame_types` (`frame_id`, `frame_type_name`, `frame_type_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Fiber', 'fiber frame type', 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1);

-- --------------------------------------------------------

--
-- Table structure for table `franchise_owner`
--

CREATE TABLE `franchise_owner` (
  `franchise_owner_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `franchise_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store`
--

CREATE TABLE `franchise_store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(255) DEFAULT NULL,
  `store_display_name` varchar(255) DEFAULT NULL,
  `store_phone` int(11) DEFAULT NULL,
  `store_gst` varchar(255) DEFAULT NULL,
  `store_email` varchar(255) DEFAULT NULL,
  `store_city` varchar(255) DEFAULT NULL,
  `store_state` varchar(255) DEFAULT NULL,
  `store_zip` varchar(255) DEFAULT NULL,
  `store_lat` double DEFAULT NULL,
  `store_lng` double DEFAULT NULL,
  `store_address` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store`
--

INSERT INTO `franchise_store` (`store_id`, `store_name`, `store_display_name`, `store_phone`, `store_gst`, `store_email`, `store_city`, `store_state`, `store_zip`, `store_lat`, `store_lng`, `store_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Franchise store 01 ', 'Franchise Store 01', 2147483647, 'GSTIN00112345672', 'franshiseStore@gmail.com', 'Nelmangala', 'Karnataka', '560064', 13.1006804, 77.39045519999999, 'Indolens, Indolens Solutions Pvt Ltd, BH Road, Jyothi Nagar, Nelamangala Town, Karnataka, India    ', 1, 1, '2024-01-03 11:55:48', 1, '2024-01-22 14:05:09'),
(2, 'franchise store 02', 'Franchise Store 01', 2147483647, 'GSTIN0011234567', 'rooprajt@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.097301, 77.38563979999999, '4rd Cross\r\n#A148 ', 1, 1, '2024-01-03 15:45:43', 1, '2024-02-16 17:42:04'),
(3, 'indolens franchise test store', 'indolens franchise test store', 2147483647, 'GST98IN76gbgui8', 'indolens.test@gmail.com', 'mysore', 'Karnataka', '571402', 12.2958104, 76.6393805, '#143 Thapa Mansion  ', 1, 1, '2024-01-31 13:32:23', 1, '2024-01-31 13:32:23'),
(4, 'test123', 'test123', 2147483647, 'GSTIN772yyg6788', 'rooprajt@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.097301, 77.38563979999999, '4rd Cross\r\n#A148', 1, 1, '2024-01-31 13:32:23', 1, '2024-01-31 13:32:23');

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store_employees`
--

CREATE TABLE `franchise_store_employees` (
  `employee_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store_employees`
--

INSERT INTO `franchise_store_employees` (`employee_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `role`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`, `certificates`) VALUES
(2, 'Franchise Owner 2', 'franchiseowner2@test.com', '9090909090', '$2b$12$7e7BVDojltZ6P6AKAcwRTOabpOn1zkxxDtFTChCdP2teR/jAjgoky', 'profile_pic/profile_pic_1705912644_document1_1703854570_profile_pic_1700635966_accountant (1).webp', 2, '   hubli', 'Aadhar', '[\"documents/documents_1704271034_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704271034_pan.jpg\", \"documents/document2_1707984096_eyeglass-png.png\"]', 1, 1, 1, '2024-01-03 14:05:39', 1, '2024-01-22 14:05:09', NULL),
(8, 'Niroop', 'niroop@gmail.com', '09987877665', '$2b$12$sezJsEe3HgLeBsHCUsxE8OxQjJxOn7TpFSVKm.HLcERxM4teFGrXq', 'profile_pic/profile_pic_1705912662_optometry.jpg', 0, '     fghjkl', 'Driving Licence', '[\"documents/document1_1706355158_eyeglass-png.png\"]', 'Pan Card', '[\"documents/document2_1706355158_specs01.jpg\"]', 0, 2, 2, '2024-01-19 13:02:20', 1, '2024-01-22 14:05:09', '[\"certificates/certificates_1706355158_square_logo.jpg\"]'),
(10, 'Sales exective testing', 'testemail89@test.com', '9090909090', '$2b$12$shbm1vs6lW2c6R3n56X2ae46t4L82q8QEUSGvGBWuBmfk4vOvEc5a', 'profile_pic/profile_pic_1705912860_accountant - Copy.webp', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1705912755_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/documents_1705912755_pan.jpg\"]', 0, 3, 1, '2024-01-22 14:05:09', 1, '2024-01-22 14:05:09', NULL),
(12, 'ROOP RAJ THAPA', 'rooprajt1996@gmail.com', '9898989898', '$2b$12$LZ2UREp16AjNyeqQDpLEruJ3QkKqPsbbSMzlTzOH7Qi6se8Z.uIXW', 'profile_pic/profile_pic_1705920137_other_employee.jpg', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1705912826_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/documents_1705912826_pan.jpg\"]', 1, 3, 1, '2024-01-22 14:05:09', 1, '2024-01-22 14:05:09', NULL),
(14, 'other employee test123', 'otheremp123@gmail.com', '9898989898', '$2b$12$tq24B2ZRcMiEgiO0R3NUlu4l4voHldRaZDoQA0WNKCWcn7i1fX1M2', 'profile_pic/profile_pic_1705912958_lab_tech.png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1705912958_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/documents_1705912958_pan.jpg\"]', 1, 4, 1, '2024-01-22 14:05:09', 1, '2024-01-22 14:05:09', NULL),
(15, 'testing 123', 'testing123@gmail.com', '1111111111', '$2b$12$LZ93mCRIHb.P46xwyqxMGOLhNgw4x2FrI30g7E/oJZ5aEQU2ZduXS', 'profile_pic/profile_pic_1705990868_lab_tech - Copy.png', 0, 'vhbjknljhgcvbn', 'Aadhar', '[\"documents/documents_1705990868_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/documents_1705990868_pan.jpg\"]', 0, 3, 1, '2024-01-23 11:49:56', 1, '2024-01-23 11:49:56', NULL),
(17, 'test franchise owner ', 'testfranchiseowner@test.com', '9809890987', '$2b$12$jR1SIDA0TVqMHkZ4rYnJx.YZLNPUq9fitWoPSOcfqGl4sTfwe0qOW', 'profile_pic/profile_pic_1706354281_marketing_head - Copy.jpg', 0, ' oiuytre', 'Aadhar', '[\"documents/documents_1706354281_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1706354281_pan.jpg\"]', 1, 1, 1, '2024-01-27 15:02:44', 1, '2024-02-16 17:39:41', NULL),
(18, 'test franchise optimetry', 'testfranchiseopt@test.com', '9098989786', '$2b$12$bSezWrNGSyPAzGfcBQBAtetzscSvlm9aIdQxi7FsD3aTr1ghgOFom', 'profile_pic/profile_pic_1706354362_marketing_head.jpg', 0, 'oiuytre', 'Aadhar', '[\"documents/document1_1707982900_aadhar.jpg\"]', 'Pan Card', '[\"documents/document2_1707982900_pan.jpg\"]', 0, 2, 1, '2024-01-27 15:02:44', 1, '2024-01-27 15:02:44', '[\"certificates/certificates_1707982900_lab_tech.png\"]');

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `invoice_id` int(11) NOT NULL,
  `invoice_number` varchar(255) NOT NULL,
  `order_id` varchar(255) NOT NULL,
  `store_id` int(11) NOT NULL,
  `store_type` int(11) NOT NULL,
  `invoice_status` int(11) NOT NULL,
  `invoice_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`invoice_id`, `invoice_number`, `order_id`, `store_id`, `store_type`, `invoice_status`, `invoice_date`) VALUES
(1, 'OS-1-11022024-00000001', 'ORDER17073737929383526', 1, 1, 1, '2024-02-11'),
(2, 'OS-1-11022024-00000002', 'ORDER17074648096094236', 1, 1, 1, '2024-02-16');

-- --------------------------------------------------------

--
-- Table structure for table `lab`
--

CREATE TABLE `lab` (
  `lab_id` int(11) NOT NULL,
  `lab_name` varchar(255) DEFAULT NULL,
  `lab_display_name` varchar(255) DEFAULT NULL,
  `lab_phone` int(11) DEFAULT NULL,
  `lab_gst` varchar(255) DEFAULT NULL,
  `lab_email` varchar(255) DEFAULT NULL,
  `lab_city` varchar(255) DEFAULT NULL,
  `lab_state` varchar(255) DEFAULT NULL,
  `lab_zip` varchar(255) DEFAULT NULL,
  `lab_lat` double DEFAULT NULL,
  `lab_lng` double DEFAULT NULL,
  `lab_address` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lab`
--

INSERT INTO `lab` (`lab_id`, `lab_name`, `lab_display_name`, `lab_phone`, `lab_gst`, `lab_email`, `lab_city`, `lab_state`, `lab_zip`, `lab_lat`, `lab_lng`, `lab_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Nirmala Optics Lab', 'Nirmala Optics Centre', 2147483647, 'GSTIN09876590', 'nirmalaoptics@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.0285133, 77.5196763, '4rd Cross\r\n#A148', 1, 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48'),
(2, 'Nikshep optics', 'Nirmala Optics Centre', 1111111111, 'GsT786543467890', 'nikshep@gmail.com', 'mysore', 'Karnataka', '571409', 12.2958104, 76.6393805, '   vv puram', 1, 1, '2024-01-03 11:55:48', 1, '2024-01-30 12:07:16');

-- --------------------------------------------------------

--
-- Table structure for table `lab_technician`
--

CREATE TABLE `lab_technician` (
  `lab_technician_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_lab_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lab_technician`
--

INSERT INTO `lab_technician` (`lab_technician_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_lab_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Lab Tech 1', 'labtech1@test.com', '9738505213', '$2b$12$XuOME7xnh0.Q8VRkg9HHI.lNbkopNZZxEC3hZWVAMvIYQV7Bf4Jhe', 'profile_pic/profile_pic_1704276838_lab_tech.png', 0, 'MANDYA', 'Aadhar', '[\"documents/documents_1704276838_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704276838_pan.jpg\"]', 1, 1, '2024-01-03 15:20:32', 1, '2024-01-03 15:20:32'),
(2, 'Lab Tech 2', 'labtech2@test.com', '9738505213', '$2b$12$xPg1c0jgNRED/9fd7UtHHuGWLUznhbbUFl3pmhXoe371YIYG922kK', 'profile_pic/profile_pic_1705913458_lab_tech - Copy.png', 2, '   MANDYA', 'Aadhar', '[\"documents/documents_1704277039_aadhar.jpg\", \"documents/document1_1704280983_specs01.jpg\"]', 'Pan Card', '[\"documents/documents_1704277039_pan.jpg\"]', 1, 1, '2024-01-03 15:45:43', 1, '2024-01-22 14:05:09');

-- --------------------------------------------------------

--
-- Table structure for table `marketing_head`
--

CREATE TABLE `marketing_head` (
  `marketing_head_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_area_head` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `marketing_head`
--

INSERT INTO `marketing_head` (`marketing_head_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_area_head`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'Marketing Head', 'marketinghead@gmail.com', '7788665544', '$2b$12$9OGHNlrId5AyUu34W.5WQuhAQ3Blol7Ib92ZNiAS3LwZye.tVTSZy', 'profile_pic/profile_pic_1704275507_marketing_head.jpg', 0, 'Hassan ', 'None', '[\"documents/documents_1704275507_aadhar.jpg\", \"documents/document1_1704275674_document1_1703854570_profile_pic_1700635966_accountant.webp\"]', 'None', '[\"documents/documents_1704275507_pan.jpg\", \"documents/document2_1704280938_document1_1703854570_profile_pic_1700635966_accountant.webp\"]', 1, 1, '2024-01-03 15:20:32', 1, '2024-01-19 18:04:21');

-- --------------------------------------------------------

--
-- Table structure for table `optimetry`
--

CREATE TABLE `optimetry` (
  `optimetry_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_track`
--

CREATE TABLE `order_track` (
  `track_id` int(11) NOT NULL,
  `order_id` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_track`
--

INSERT INTO `order_track` (`track_id`, `order_id`, `status`, `created_on`) VALUES
(1, 'ORDER17073741114443533', 2, '2024-02-08 16:59:23'),
(2, 'ORDER17073741114443533', 3, '2024-02-08 16:59:42'),
(3, 'ORDER17073737929383526', 2, '2024-02-09 12:18:24'),
(4, 'ORDER17073737929383526', 3, '2024-02-11 14:13:10'),
(5, 'ORDER17073737929383526', 4, '2024-02-11 14:13:14'),
(6, 'ORDER17073737929383526', 5, '2024-02-11 15:10:28'),
(7, 'ORDER17073737929383526', 6, '2024-02-11 15:10:49'),
(8, 'ORDER17074648096094236', 7, '2024-02-15 20:24:35'),
(9, 'ORDER17074648096094236', 7, '2024-02-15 20:24:49'),
(10, 'ORDER17074648096094236', 5, '2024-02-15 20:37:40'),
(11, 'ORDER17074648096094236', 2, '2024-02-15 20:41:18'),
(12, 'ORDER17074648096094236', 5, '2024-02-16 01:45:16'),
(13, 'ORDER17074648096094236', 6, '2024-02-16 01:46:07'),
(14, 'ORDER17074648096094236', 5, '2024-02-16 01:55:39'),
(15, 'ORDER17074648096094236', 6, '2024-02-16 01:55:54'),
(16, 'ORDER17074648096094236', 2, '2024-02-16 01:58:55'),
(17, 'ORDER17074644055219809', 2, '2024-02-16 02:03:46'),
(18, 'ORDER17074644055219809', 3, '2024-02-16 02:03:53'),
(19, 'ORDER17074644055219809', 4, '2024-02-16 02:03:57');

-- --------------------------------------------------------

--
-- Table structure for table `other_employees`
--

CREATE TABLE `other_employees` (
  `other_employee_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `own_store`
--

CREATE TABLE `own_store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(255) DEFAULT NULL,
  `store_display_name` varchar(255) DEFAULT NULL,
  `store_phone` varchar(255) DEFAULT NULL,
  `store_gst` varchar(255) DEFAULT NULL,
  `store_email` varchar(255) DEFAULT NULL,
  `store_city` varchar(255) DEFAULT NULL,
  `store_state` varchar(255) DEFAULT NULL,
  `store_zip` varchar(255) DEFAULT NULL,
  `store_lat` double DEFAULT NULL,
  `store_lng` double DEFAULT NULL,
  `store_address` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store`
--

INSERT INTO `own_store` (`store_id`, `store_name`, `store_display_name`, `store_phone`, `store_gst`, `store_email`, `store_city`, `store_state`, `store_zip`, `store_lat`, `store_lng`, `store_address`, `status`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`) VALUES
(1, 'indolens ownstore 02', 'Indolense Nelmangla', '9876543233', 'GSTIN00', 'indolens.nelmangala@gmail.com', 'Nelmangala', 'Karnataka', '560065', 13.2957137, 77.53639079999999, 'RANGAPPA CIRCLE, opposite to Sai Baba Temple, Shanthinagar, Doddaballapura, Karnataka 561203', 1, 1, '2024-01-03 11:55:48', 1, '2024-02-01 12:20:31'),
(2, 'indolens ownstore 03', 'Indolense Nelmangla test', '989898', 'GSTIN001', 'rooprajt@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.097301, 77.38563979999999, 'RANGAPPA CIRCLE, opposite to Sai Baba Temple, Shanthinagar, Doddaballapura, Karnataka 561203', 0, 1, '2024-01-03 15:45:43', 1, '2024-01-19 18:04:21');

-- --------------------------------------------------------

--
-- Table structure for table `own_store_employees`
--

CREATE TABLE `own_store_employees` (
  `employee_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_1_url`)),
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`document_2_url`)),
  `status` int(11) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store_employees`
--

INSERT INTO `own_store_employees` (`employee_id`, `name`, `email`, `phone`, `password`, `profile_pic`, `assigned_store_id`, `address`, `document_1_type`, `document_1_url`, `document_2_type`, `document_2_url`, `status`, `role`, `created_by`, `created_on`, `last_updated_by`, `last_updated_on`, `certificates`) VALUES
(17, 'Santhosh Kumar', 'devsandy12@gmail.com', '9808780986', '$2b$12$lHPZHWoAw8DyIUGu5q05muEaZVNQMOBW/tgyNMqvU/BsmMxbHEzDO', 'profile_pic/profile_pic_1704789485_documents_1702293007_accountant.webp', 1, 'tumkur    ', 'Aadhar', '[\"documents/document1_1704267624_aadhar.jpg\", \"documents/document1_1707984694_eyeglass-png.png\"]', 'Pan Card', '[\"documents/document2_1704267624_pan.jpg\", \"documents/document2_1707985757_Indolens Invoice.pdf\", \"documents/document2_1707985757_specs01.jpg\"]', 1, 1, 1, '2024-01-03 11:55:48', 1, '2024-01-25 19:51:37', NULL),
(18, 'optimetry 01', 'optimetry@test.com', '8660225160', '$2b$12$j1n.bZJ3MLGdS8lgkdcp6eVPVQgnAfEM/lqNbpwWrU3auULfi/j5y', 'profile_pic/profile_pic_1704267921_optometry.jpg', 0, 'Nelmangala', 'Aadhar', '[\"documents/documents_1704267921_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704267921_pan.jpg\"]', 1, 2, 1, '2024-01-03 11:55:48', 3, '2024-01-03 11:55:48', '[\"certificates/certificates_1704267921_wed1.jpg\"]'),
(19, 'optimetry 02', 'optimetry02@test.com', '8660225160', '$2b$12$nlrwN1bz1tuNLTPS2bYxjOi77D9OZaXDwr/yE2xTM4Gam5DFfIlNm', 'profile_pic/profile_pic_1705912580_documents_1702293007_accountant.webp', 1, 'Nelmangala', 'Aadhar', '[\"documents/document1_1706355018_eyeglass-png.png\"]', 'Pan Card', '[\"documents/document2_1706355018_pan.jpg\"]', 1, 2, 1, '2024-01-03 11:55:48', 1, '2024-01-22 14:05:09', '[\"certificates/certificates_1706355018_square_logo.jpg\"]'),
(20, 'Sales exective 01', 'salesecx@gmail.com', '9808780986', '$2b$12$AnqNLwdakIIYOk94MrbVMuugY8saLCbNgvjZbAdp6m3CgvkJ4o0nG', 'profile_pic/profile_pic_1704268734_sales_exec.jpg', 1, 'Bangalore', 'Aadhar', '[\"documents/documents_1704268734_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704268734_pan.jpg\"]', 1, 3, 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', NULL),
(21, 'Sales exective 02', 'salesexc@gmail.com', '9900350569', '$2b$12$eh/3Y4qpIp48K1ndysJVmOH99D8djRgCey0ZgpE.BiiFB7QKxjIw2', 'profile_pic/profile_pic_1704269673_hello-removebg-preview.png', 0, 'Mandya', 'Aadhar', '[\"documents/documents_1704269673_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704269673_pan.jpg\"]', 0, 3, 1, '2024-01-03 13:43:17', 1, '2024-01-03 13:43:17', NULL),
(22, 'ROOP RAJ THAPA', 'rooprajt@gmail.com', '8660225160', '$2b$12$H7jrXlV/x0Fp5IFChQ2Uju8M/CiUPxTm0QF..jkvRgSBFOlqpYduW', 'profile_pic/profile_pic_1705912607_document1_1703854570_profile_pic_1700635966_accountant.webp', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1704270039_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704270039_pan.jpg\"]', 0, 3, 1, '2024-01-03 13:43:17', 1, '2024-01-22 14:05:09', NULL),
(23, 'other employee', 'otheremp@gmail.com', '9898989898', '$2b$12$vn4TTjCsBd5ml1Qrx.EOfeSBiiyDuEqBIRc30GV0RmafbkxUobOSa', 'profile_pic/profile_pic_1704270159_other_employee.jpg', 1, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1704270159_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704270159_pan.jpg\"]', 1, 4, 1, '2024-01-03 13:43:17', 1, '2024-01-03 13:43:17', NULL),
(24, 'other employee 02', 'otheremp2@gmail.com', '8660225160', '$2b$12$Ehh2N1ocXVoT7jmVwEFtlOrPZbZ6ot7yPPMQRBEzUBmg9HxQ.eUie', 'profile_pic/profile_pic_1705912624_document1_1703854570_profile_pic_1700635966_accountant.webp', 1, '                                                                                                4rd Cross\r\n#A148\r\n                            \r\n                            \r\n                            ', 'Aadhar', '[\"documents/documents_1704270443_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1704270443_pan.jpg\"]', 1, 4, 1, '2024-01-03 13:54:37', 1, '2024-01-22 14:05:09', NULL),
(25, 'TEST manager', 'testmanager@gmail.com', '9620725475', '$2b$12$yj64PSjUoi4M4qViwJ4zpeIlEUDiVBOgjS/k9Nx155mKnTtT87/H.', 'profile_pic/profile_pic_1704788744_DSC_0179-removebg-preview.png', 0, '4rd Cross\r\n#A148 ', 'Aadhar', '[\"documents/document1_1704697830_aadhar.jpg\"]', 'Pan Card', '[\"documents/document2_1704697830_pan.jpg\"]', 1, 1, 2, '2024-01-07 17:37:34', 1, '2024-01-09 13:51:56', NULL),
(26, 'Testing1', 'testing1@gmail.com', '9876543214', '$2b$12$0HzcGGGbXi7NVYMnApIPLea.jP/45DASYxQ4bR4fUE93H01t0WORe', 'profile_pic/profilePic_1704788842_DSC_0167-removebg-preview (1).png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/document1_1704788842_aadhar.jpg\"]', 'Pan Card', '[\"documents/document2_1704788842_pan.jpg\"]', 1, 1, 1, '2024-01-09 13:51:56', 1, '2024-01-09 13:51:56', NULL),
(27, 'Niraj Thapa', 'nimmiallatthebest@gmail.com', '9620725476', '$2b$12$OCIe8zntOyvHDotbFUE9X.X7vOZ1HtKlxl2E8rYqIaTwxBSuXtaQC', 'profile_pic/profile_pic_1705912555_accountant.webp', 0, '#A-148, 3rd cross, peeenya 1st stage, Industrial estate, Bangalore North, 560058, Karnataka, India   ppppppppppppp  ', 'Aadhar', '[\"documents/document1_1705044693_aadhar.jpg\", \"documents/document1_1706879963_AADHAAR.jpeg\"]', 'Pan Card', '[\"documents/document2_1705044693_pan.jpg\", \"documents/document2_1706879971_pan.jpg\"]', 1, 1, 1, '2024-01-12 12:59:15', 1, '2024-01-23 19:35:08', NULL),
(35, 'Roop', 'nkbhandari95@gmail.com', '8660225160', '$2b$12$Aa/Aw1049kBE5W1swRKizO1DJ5adB4I7LJXAiAmRcw3sYwCAMYBaK', 'profile_pic/profile_pic_1705906056_hello-removebg-preview.png', 0, '4rd Cross\r\n#A148', 'Aadhar', '[\"documents/documents_1705906056_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1705906056_pan.jpg\"]', 0, 2, 1, '2024-01-22 11:44:01', 1, '2024-01-22 11:44:01', '[\"certificates/certificates_1705906056_Screenshot 2023-04-29 220515.png\"]');

-- --------------------------------------------------------

--
-- Table structure for table `product_categories`
--

CREATE TABLE `product_categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `category_prefix` varchar(255) DEFAULT NULL,
  `category_description` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_categories`
--

INSERT INTO `product_categories` (`category_id`, `category_name`, `category_prefix`, `category_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'Frames', 'IND-FR', 'description for frames goes here', 1, '2024-01-03 11:46:04', 1, '2024-01-03 11:46:04', 1),
(2, 'Lens', 'IND-LENS', 'description for lens goes here', 1, '2024-01-03 11:46:04', 1, '2024-01-03 11:46:04', 1),
(3, 'Contact Lens', 'IND-CL', 'description for lens goes here', 1, '2024-01-03 11:46:04', 1, '2024-01-03 11:46:04', 1),
(4, 'lens cover', 'lens cover', 'lens cover', 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1),
(5, 'customised contact lens', 'xyz', 'customers customised contact lens', 0, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_colors`
--

CREATE TABLE `product_colors` (
  `color_id` int(11) NOT NULL,
  `color_code` varchar(255) DEFAULT NULL,
  `color_name` varchar(255) DEFAULT NULL,
  `color_description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_colors`
--

INSERT INTO `product_colors` (`color_id`, `color_code`, `color_name`, `color_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'rbc', 'Red', 'red color', 1, '2024-01-03 11:55:48', 1, '2024-02-01 17:50:45', 1),
(2, 'clr1', 'clr 01', 'green color', 1, '2024-01-03 11:55:48', 1, '2024-01-03 15:45:43', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_materials`
--

CREATE TABLE `product_materials` (
  `material_id` int(11) NOT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `material_description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_materials`
--

INSERT INTO `product_materials` (`material_id`, `material_name`, `material_description`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'glasse', 'materials', 1, '2024-01-03 11:55:48', 1, '2024-01-03 15:45:43', 1);

-- --------------------------------------------------------

--
-- Table structure for table `request_products`
--

CREATE TABLE `request_products` (
  `request_products_id` int(11) NOT NULL,
  `store_id` int(11) DEFAULT NULL,
  `store_type` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `product_quantity` int(11) DEFAULT NULL,
  `unit_cost` int(11) DEFAULT NULL,
  `request_status` int(11) DEFAULT NULL,
  `delivery_status` int(11) DEFAULT NULL,
  `is_requested` tinyint(1) DEFAULT NULL,
  `request_to_store_id` int(11) DEFAULT NULL,
  `payment_status` int(11) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `request_products`
--

INSERT INTO `request_products` (`request_products_id`, `store_id`, `store_type`, `product_id`, `product_quantity`, `unit_cost`, `request_status`, `delivery_status`, `is_requested`, `request_to_store_id`, `payment_status`, `comment`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(9, 1, 1, 1, 10, 1555, 1, 2, 0, 0, 0, 'test comment section', '2024-01-03 11:55:48', 1, '0000-00-00 00:00:00', 17),
(11, 1, 1, 1, 3, 1999, 1, 2, 1, 0, 0, NULL, '2024-01-03 17:22:01', 17, '0000-00-00 00:00:00', 17),
(12, 1, 1, 1, 15, 1999, 2, 3, 1, 0, 0, NULL, '2024-01-03 17:24:19', 17, '2024-01-03 17:14:12', 1),
(13, 1, 1, 1, 5, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-03 17:25:38', 17, '2024-01-03 17:25:38', 17),
(14, 1, 1, 1, 2, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-04 13:15:00', 17, '2024-01-04 13:15:00', 17),
(15, 1, 1, 1, 1, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-04 13:15:16', 17, '2024-01-04 13:15:16', 17),
(16, 1, 1, 1, 5, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-04 13:15:33', 17, '2024-01-04 13:15:33', 17),
(17, 1, 1, 1, 13, 1999, 2, 3, 1, 0, 0, NULL, '2024-01-04 13:30:15', 17, '2024-01-17 13:10:07', 1),
(20, 1, 2, 7, 5, 1555, 1, 2, 0, 0, 0, 'enjoy', '2024-01-05 17:06:57', 1, '0000-00-00 00:00:00', 2),
(21, 1, 2, 6, 9, 1555, 1, 2, 1, 1, 0, NULL, '2024-01-05 17:09:06', 2, '0000-00-00 00:00:00', 2),
(22, 1, 2, 7, 3, NULL, 1, 1, 0, 0, 0, 'test', '2024-01-07 12:05:30', 1, '2024-01-07 12:05:30', 1),
(23, 1, 2, 6, 2, NULL, 1, 1, 0, 0, 0, 'test', '2024-01-07 12:05:30', 1, '2024-01-07 12:05:30', 1),
(24, 1, 2, 1, 2, NULL, 1, 1, 0, 0, 0, 'tets', '2024-01-07 12:05:30', 1, '2024-01-07 12:05:30', 1),
(25, 1, 1, 7, 1, NULL, 1, 1, 0, 0, 0, 'test', '2024-01-07 12:05:30', 2, '2024-01-07 12:05:30', 2),
(26, 1, 1, 1, 1, NULL, 1, 2, 0, 0, 0, 'test', '2024-01-07 12:05:30', 2, '0000-00-00 00:00:00', 17),
(27, 1, 1, 6, 1, NULL, 1, 2, 0, 0, 0, 'tets', '2024-01-07 12:05:30', 2, '0000-00-00 00:00:00', 17),
(28, 1, 1, 6, 1555, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-07 12:30:17', 17, '2024-01-07 12:30:17', 17),
(29, 1, 1, 6, 10000, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-07 12:32:57', 17, '2024-01-07 12:32:57', 17),
(30, 1, 1, 6, 1, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-07 12:38:38', 17, '2024-01-07 12:38:38', 17),
(31, 1, 1, 6, 2, 1999, 1, 1, 1, 0, 0, NULL, '2024-01-07 12:39:24', 17, '2024-02-08 13:12:30', 1),
(32, 1, 1, 6, 2, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-07 12:39:34', 17, '2024-01-07 12:39:34', 17),
(33, 1, 1, 6, 2, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-07 12:39:55', 17, '2024-01-07 12:39:55', 17),
(34, 1, 2, 7, 555, NULL, 0, 0, 1, 0, 0, NULL, '2024-01-08 16:57:42', 2, '2024-01-08 16:57:42', 2),
(35, 1, 2, 7, 2, NULL, 0, 0, 1, 0, 0, NULL, '2024-01-08 17:07:22', 2, '2024-01-08 17:07:22', 2),
(36, 1, 1, 6, 2, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-09 16:46:22', 17, '2024-01-09 16:46:22', 17),
(37, 1, 1, 1, 1, NULL, 1, 1, 0, 0, 0, 'kjhgfd', '2024-01-13 12:57:02', 1, '2024-01-13 12:57:02', 1),
(38, 1, 1, 7, 1122, 1999, 0, 0, 1, 0, 0, NULL, '2024-01-20 19:13:15', 17, '2024-01-20 19:13:15', 17),
(39, 1, 1, 7, 1, 1999, 2, 3, 1, 0, 0, NULL, '2024-01-22 14:05:09', 17, '2024-01-30 13:42:58', 1),
(40, 0, 2, 7, 1, NULL, 1, 1, 0, 0, 0, 'kjuhgfd', '2024-01-30 13:42:58', 1, '2024-01-30 13:42:58', 1),
(41, 2, 2, 7, 1, NULL, 0, 0, 1, 0, 0, NULL, '2024-01-30 15:46:25', 2, '2024-01-30 15:46:25', 2),
(42, 2, 2, 7, 2, NULL, 1, 1, 0, 0, 0, 'test', '2024-01-30 15:46:25', 1, '2024-01-30 15:46:25', 1),
(43, 2, 2, 6, 1, NULL, 0, 0, 1, 0, 0, NULL, '2024-01-30 15:46:25', 2, '2024-01-30 15:46:25', 2),
(44, 2, 2, 6, 1, NULL, 2, 3, 1, 0, 0, NULL, '2024-01-30 15:46:25', 2, '2024-02-08 13:02:37', 1),
(45, 1, 1, 1, -5, NULL, 1, 2, 0, 0, 0, 'test', '2024-02-02 13:37:20', 1, '2024-02-06 13:44:46', 17),
(46, 1, 1, 1, 1000, NULL, 1, 1, 0, 0, 0, 'test', '2024-02-12 14:22:25', 1, '2024-02-12 14:22:25', 1);

-- --------------------------------------------------------

--
-- Table structure for table `reset_password`
--

CREATE TABLE `reset_password` (
  `reset_password_id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reset_password`
--

INSERT INTO `reset_password` (`reset_password_id`, `email`, `code`, `status`, `created_on`) VALUES
(1, 'nkbhandari95@gmail.com', 'FF5LaYCnVkFbmk8j', 1, '2024-01-19 02:35:55'),
(2, 'nkbhandari95@gmail.com', 'vNb0awBpWyJPoajL', 1, '2024-01-19 02:35:55'),
(3, 'nkbhandari95@gmail.com', 'viVVC8xyCrSe05Zr', 1, '2024-01-19 13:02:20'),
(4, 'nkbhandari95@gmail.com', 'QBRdNKjkF8QvqMtc', 1, '2024-01-19 13:32:20'),
(5, 'nkbhandari95@gmail.com', 'jxqSXg6CRUrwWFAt', 1, '2024-01-19 13:37:03'),
(6, 'nkbhandari95@gmail.com', 'fImavDzqjfT8cg6D', 1, '2024-01-19 13:43:24'),
(7, 'nkbhandari95@gmail.com', 'nFCq6xmabp3Pt77r', 1, '2024-01-21 12:57:22'),
(8, 'nkbhandari95@gmail.com', 'PI4NTlBXKOEyAbVZ', 1, '2024-01-21 13:01:49'),
(9, 'nkbhandari95@gmail.com', 'brZDYcW17U2el0CO', 1, '2024-01-22 11:51:37'),
(10, 'nkbhandari95@gmail.com', 'HOqDnwSWLFp2ZIDN', 1, '2024-01-22 11:51:42'),
(11, 'nkbhandari95@gmail.com', 'R8BSw2yOXKRkNM6z', 1, '2024-01-22 11:56:09'),
(12, 'labtech2@test.com', '619yEbgVmvaO3o4V', 1, '2024-01-26 16:51:08'),
(13, 'labtech2@test.com', '4VqY6jSeZ2MwB0KB', 1, '2024-01-26 16:55:56'),
(14, 'labtech2@test.com', 'Wz5QK8Bgjl3wdtcf', 1, '2024-01-26 16:56:37'),
(15, 'labtech2@test.com', '4Ppachyvp5BB2YXe', 1, '2024-01-26 17:48:31'),
(16, 'labtech2@test.com', 'ttn7geIQEuEMmCUX', 1, '2024-01-26 17:50:22'),
(17, 'labtech2@test.com', 'KGyi4XWOei0WrRmi', 1, '2024-01-26 17:55:27'),
(18, 'labtech2@test.com', 'AT3Vao2YERn2877W', 1, '2024-01-26 17:58:27'),
(19, 'nimmiallatthebest@gmail.com', 'fxHzU7l8Qj6j0bui', 0, '2024-02-01 12:48:58'),
(20, 'nimmiallatthebest@gmail.com', 'bLSIw2BiKGGJBrhK', 0, '2024-02-01 12:52:01'),
(21, 'nimmiallatthebest@gmail.com', 'TBnJd90J008gvmEh', 0, '2024-02-01 12:53:46');

-- --------------------------------------------------------

--
-- Table structure for table `sales_executive`
--

CREATE TABLE `sales_executive` (
  `sales_executive_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sales_order`
--

CREATE TABLE `sales_order` (
  `sale_item_id` int(11) NOT NULL,
  `order_id` varchar(255) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `hsn` varchar(255) DEFAULT NULL,
  `unit_sale_price` int(11) DEFAULT NULL,
  `unit_type` varchar(255) DEFAULT NULL,
  `purchase_quantity` int(11) DEFAULT NULL,
  `product_total_cost` int(11) DEFAULT NULL,
  `discount_percentage` int(11) DEFAULT NULL,
  `is_discount_applied` int(11) DEFAULT NULL,
  `power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`power_attribute`)),
  `assigned_lab` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `order_status` int(11) DEFAULT NULL,
  `payment_status` int(11) DEFAULT NULL,
  `delivery_status` int(11) DEFAULT NULL,
  `payment_mode` int(11) DEFAULT NULL,
  `amount_paid` int(11) DEFAULT NULL,
  `estimated_delivery_date` date DEFAULT NULL,
  `linked_item` int(11) DEFAULT NULL,
  `sales_note` longtext NOT NULL,
  `created_by_store` int(11) DEFAULT NULL,
  `created_by_store_type` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales_order`
--

INSERT INTO `sales_order` (`sale_item_id`, `order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`, `purchase_quantity`, `product_total_cost`, `discount_percentage`, `is_discount_applied`, `power_attribute`, `assigned_lab`, `customer_id`, `order_status`, `payment_status`, `delivery_status`, `payment_mode`, `amount_paid`, `estimated_delivery_date`, `linked_item`, `sales_note`, `created_by_store`, `created_by_store_type`, `created_by`, `created_on`, `updated_by`, `updated_on`) VALUES
(1, 'ORDER17073737929383526', 2, 'HSN No 01', 1499, 'xyz unit', 2, 2848, 5, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"\", \"leftLensCylStock\": \"\", \"leftLensAxisStock\": \"\", \"leftLensAddStock\": \"\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"1\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 2, 12, 7, 1, 1, 1, 10000, '2024-02-11', NULL, 'Checking all', 1, 1, 20, '2024-02-08 11:59:57', 20, '2024-02-08 11:59:57'),
(2, 'ORDER17073737929383526', 4, 'HSN no 01', 9000, 'xyz unit', 2, 17100, 5, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"\", \"contact_lens_disposability\": \"\", \"power\": \"\", \"bc\": \"\", \"dia\": \"\", \"cyl\": \"\", \"axis\": \"\"}', 2, 12, 5, 1, 1, 1, 10000, '2024-02-11', NULL, 'Checking all', 1, 1, 20, '2024-02-08 11:59:57', 20, '2024-02-08 11:59:57'),
(3, 'ORDER17073737929383526', 1, 'HSN no 01', 1499, 'xyz unit', 1, 1424, 5, 1, '{}', 2, 12, 5, 1, 1, 1, 10000, '2024-02-11', NULL, 'Checking all', 1, 1, 20, '2024-02-08 11:59:57', 20, '2024-02-08 11:59:57'),
(4, 'ORDER17073741114443533', 2, 'HSN No 01', 1499, 'xyz unit', 12, 17089, 5, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"\", \"leftLensCylStock\": \"\", \"leftLensAxisStock\": \"\", \"leftLensAddStock\": \"\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"2\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 2, 10, 7, 1, 1, 1, 10000, '2024-02-11', NULL, 'checking all', 2, 2, 2, '2024-02-08 12:05:19', 2, '2024-02-08 12:05:19'),
(5, 'ORDER17073741114443533', 3, 'HSN 02', 1599, '', 10, 15191, 5, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"\", \"contact_lens_disposability\": \"\", \"power\": \"\", \"bc\": \"\", \"dia\": \"\", \"cyl\": \"\", \"axis\": \"\"}', 2, 10, 3, 1, 1, 1, 10000, '2024-02-11', NULL, 'checking all', 2, 2, 2, '2024-02-08 12:05:19', 2, '2024-02-08 12:05:19'),
(6, 'ORDER17073741114443533', 6, 'HSN no 01', 1499, 'xyz unit', 1, 1424, 5, 1, '{}', 2, 10, 3, 1, 1, 1, 10000, '2024-02-11', NULL, 'checking all', 2, 2, 2, '2024-02-08 12:05:19', 2, '2024-02-08 12:05:19'),
(7, 'ORDER17074638411939129', 2, 'HSN No 01', 1499, 'xyz unit', 1, 1424, 5, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"\", \"leftLensCylStock\": \"\", \"leftLensAxisStock\": \"\", \"leftLensAddStock\": \"\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"1\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 2, 25, 1, 1, 1, 1, 200, '2024-02-12', NULL, 'Both lense are independent', 1, 1, 19, '2024-02-09 13:00:43', 19, '2024-02-09 13:00:43'),
(8, 'ORDER17074638411939129', 3, 'HSN 02', 1599, '', 1, 1519, 5, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"\", \"contact_lens_disposability\": \"\", \"power\": \"\", \"bc\": \"\", \"dia\": \"\", \"cyl\": \"\", \"axis\": \"\"}', 2, 25, 1, 1, 1, 1, 200, '2024-02-12', NULL, 'Both lense are independent', 1, 1, 19, '2024-02-09 13:00:43', 19, '2024-02-09 13:00:43'),
(9, 'ORDER17074644055219809', 2, 'HSN No 01', 1499, 'xyz unit', 2, 2848, 5, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"\", \"leftLensCylStock\": \"\", \"leftLensAxisStock\": \"\", \"leftLensAddStock\": \"\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"2\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 2, 15, 4, 1, 1, 1, 1000, '2024-02-12', NULL, 'Checkkkkkkkkkk', 1, 1, 20, '2024-02-09 13:10:10', 20, '2024-02-09 13:10:10'),
(10, 'ORDER17074648096094236', 2, 'HSN No 01', 1499, 'xyz unit', 1, 1424, 1, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"1\", \"leftLensCylStock\": \"1\", \"leftLensAxisStock\": \"1\", \"leftLensAddStock\": \"1\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"1\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 0, 11, 2, 2, 1, 1, 500, '2024-02-12', NULL, 'lens', 1, 1, 24, '2024-02-09 13:16:52', 24, '2024-02-09 13:16:52');

-- --------------------------------------------------------

--
-- Table structure for table `store_expense`
--

CREATE TABLE `store_expense` (
  `store_expense_id` int(11) NOT NULL,
  `store_id` int(11) DEFAULT NULL,
  `store_type` int(11) DEFAULT NULL,
  `expense_amount` int(11) DEFAULT NULL,
  `expense_reason` varchar(255) DEFAULT NULL,
  `expense_date` datetime DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_expense`
--

INSERT INTO `store_expense` (`store_expense_id`, `store_id`, `store_type`, `expense_amount`, `expense_reason`, `expense_date`, `created_on`, `created_by`) VALUES
(1, 1, 1, 5000, 'import materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport materialsimport material', '2024-01-04 12:07:47', '2024-01-04 12:07:47', 17),
(2, 1, 1, 50000, 'export ', '2024-01-05 12:07:47', '2024-01-10 00:00:00', 17),
(3, 1, 1, 5000, 'materials', '2024-01-05 13:02:23', '2024-01-05 13:02:23', 17),
(4, 1, 1, 10000, 'transport', '2024-01-05 13:02:23', '2024-01-05 13:02:23', 17),
(5, 1, 1, 45000, 'import', '2024-01-05 13:02:23', '2024-01-05 13:02:23', 17),
(6, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(7, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(8, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(9, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(10, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(11, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(12, 1, 1, 50000, 'materials', '2024-01-23 15:36:18', '2024-01-23 15:36:18', 17),
(13, 2, 2, 5000, 'raw', '2024-02-07 12:34:57', '2024-02-07 12:34:57', 2);

-- --------------------------------------------------------

--
-- Table structure for table `store_inventory`
--

CREATE TABLE `store_inventory` (
  `store_inventory_id` int(11) NOT NULL,
  `store_id` int(11) DEFAULT NULL,
  `store_type` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `product_quantity` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_inventory`
--

INSERT INTO `store_inventory` (`store_inventory_id`, `store_id`, `store_type`, `product_id`, `product_quantity`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(6, 1, 1, 1, 0, '2024-01-03 11:55:48', 1, '2024-02-06 13:44:46', 17),
(9, 2, 2, 7, 7, '2024-01-05 17:06:57', 1, '2024-01-07 12:05:30', 1),
(10, 2, 2, 6, 10, '2024-01-05 17:06:57', 1, '2024-01-07 12:05:30', 1),
(13, 1, 2, 1, 2, '2024-01-07 12:05:30', 1, '2024-01-07 12:05:30', 1),
(14, 1, 1, 7, -3, '2024-01-07 12:05:30', 2, '2024-01-07 12:05:30', 2),
(16, 1, 1, 6, -7, '2024-01-07 12:05:30', 2, '2024-01-07 12:05:30', 2);

-- --------------------------------------------------------

--
-- Table structure for table `store_manager`
--

CREATE TABLE `store_manager` (
  `store_manager_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `assigned_store_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document_1_type` varchar(255) DEFAULT NULL,
  `document_1_url` varchar(255) DEFAULT NULL,
  `document_2_type` varchar(255) DEFAULT NULL,
  `document_2_url` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `units`
--

CREATE TABLE `units` (
  `unit_id` int(11) NOT NULL,
  `unit_name` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `units`
--

INSERT INTO `units` (`unit_id`, `unit_name`, `status`, `created_on`, `created_by`, `last_updated_on`, `last_updated_by`) VALUES
(1, 'xyz unit', 1, '2024-01-03 11:55:48', 1, '2024-01-03 11:55:48', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accountant`
--
ALTER TABLE `accountant`
  ADD PRIMARY KEY (`accountant_id`),
  ADD UNIQUE KEY `unique_email_accountant` (`email`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `unique_email_admin` (`email`);

--
-- Indexes for table `admin_setting`
--
ALTER TABLE `admin_setting`
  ADD PRIMARY KEY (`setting_id`);

--
-- Indexes for table `area_head`
--
ALTER TABLE `area_head`
  ADD PRIMARY KEY (`area_head_id`),
  ADD UNIQUE KEY `unique_email_area_head` (`email`);

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
-- Indexes for table `central_inventory_restock_log`
--
ALTER TABLE `central_inventory_restock_log`
  ADD PRIMARY KEY (`restock_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `unique_phone` (`phone`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `eye_test`
--
ALTER TABLE `eye_test`
  ADD PRIMARY KEY (`eye_test_id`);

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
  ADD PRIMARY KEY (`employee_id`),
  ADD UNIQUE KEY `unique_email` (`email`),
  ADD UNIQUE KEY `unique_email_franchise` (`email`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoice_id`),
  ADD UNIQUE KEY `unique_order_id` (`order_id`);

--
-- Indexes for table `lab`
--
ALTER TABLE `lab`
  ADD PRIMARY KEY (`lab_id`);

--
-- Indexes for table `lab_technician`
--
ALTER TABLE `lab_technician`
  ADD PRIMARY KEY (`lab_technician_id`),
  ADD UNIQUE KEY `unique_email_lab_technician` (`email`);

--
-- Indexes for table `marketing_head`
--
ALTER TABLE `marketing_head`
  ADD PRIMARY KEY (`marketing_head_id`),
  ADD UNIQUE KEY `unique_email_marketing_head` (`email`);

--
-- Indexes for table `optimetry`
--
ALTER TABLE `optimetry`
  ADD PRIMARY KEY (`optimetry_id`);

--
-- Indexes for table `order_track`
--
ALTER TABLE `order_track`
  ADD PRIMARY KEY (`track_id`);

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
  ADD PRIMARY KEY (`employee_id`),
  ADD UNIQUE KEY `unique_email` (`email`);

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
-- Indexes for table `sales_order`
--
ALTER TABLE `sales_order`
  ADD PRIMARY KEY (`sale_item_id`);

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
  ADD PRIMARY KEY (`store_manager_id`),
  ADD UNIQUE KEY `email` (`email`);

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
  MODIFY `accountant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `admin_setting`
--
ALTER TABLE `admin_setting`
  MODIFY `setting_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `area_head`
--
ALTER TABLE `area_head`
  MODIFY `area_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `central_inventory`
--
ALTER TABLE `central_inventory`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `central_inventory_restock_log`
--
ALTER TABLE `central_inventory_restock_log`
  MODIFY `restock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT for table `eye_test`
--
ALTER TABLE `eye_test`
  MODIFY `eye_test_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  MODIFY `shape_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `frame_types`
--
ALTER TABLE `frame_types`
  MODIFY `frame_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  MODIFY `franchise_owner_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `franchise_store`
--
ALTER TABLE `franchise_store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `lab`
--
ALTER TABLE `lab`
  MODIFY `lab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lab_technician`
--
ALTER TABLE `lab_technician`
  MODIFY `lab_technician_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `marketing_head`
--
ALTER TABLE `marketing_head`
  MODIFY `marketing_head_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `optimetry`
--
ALTER TABLE `optimetry`
  MODIFY `optimetry_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_track`
--
ALTER TABLE `order_track`
  MODIFY `track_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

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
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `product_categories`
--
ALTER TABLE `product_categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `product_colors`
--
ALTER TABLE `product_colors`
  MODIFY `color_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `product_materials`
--
ALTER TABLE `product_materials`
  MODIFY `material_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `request_products`
--
ALTER TABLE `request_products`
  MODIFY `request_products_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `reset_password`
--
ALTER TABLE `reset_password`
  MODIFY `reset_password_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `sales_executive`
--
ALTER TABLE `sales_executive`
  MODIFY `sales_executive_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_order`
--
ALTER TABLE `sales_order`
  MODIFY `sale_item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `store_expense`
--
ALTER TABLE `store_expense`
  MODIFY `store_expense_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `store_inventory`
--
ALTER TABLE `store_inventory`
  MODIFY `store_inventory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `store_manager`
--
ALTER TABLE `store_manager`
  MODIFY `store_manager_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `units`
--
ALTER TABLE `units`
  MODIFY `unit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
