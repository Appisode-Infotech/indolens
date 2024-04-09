-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 06, 2024 at 02:31 PM
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
-- Database: `2_indolens_db`
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
(1, 'Roop', 'raja@dm.com', '1111111111', '$2b$12$OE6eJi1G2.unoANUMZHdOuS10U89OpiLTl61irW4EudmRULHmExnm', 'profile_pic/profile_pic_1709295472_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg', 'gvhjk', 'Aadhar', '[\"documents/documents_1709295472_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\"]', 'Pan Card', '[\"documents/documents_1709295472_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\"]', 1, 1, '2024-03-01 17:47:52', 1, '2024-03-01 17:47:52');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_admin_id` int(11) NOT NULL,
  `admin_name` varchar(255) DEFAULT NULL,
  `admin_email` varchar(255) DEFAULT NULL,
  `admin_phone` varchar(12) DEFAULT NULL,
  `admin_password` varchar(255) DEFAULT NULL,
  `admin_role` int(12) DEFAULT NULL,
  `admin_profile_pic` varchar(255) DEFAULT NULL,
  `admin_address` varchar(255) DEFAULT NULL,
  `admin_document_1_type` varchar(255) DEFAULT NULL,
  `admin_document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `admin_document_2_type` varchar(255) DEFAULT NULL,
  `admin_document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `admin_status` int(11) DEFAULT NULL,
  `admin_created_by` int(11) DEFAULT NULL,
  `admin_created_on` datetime DEFAULT NULL,
  `admin_last_updated_by` int(11) DEFAULT NULL,
  `admin_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_admin_id`, `admin_name`, `admin_email`, `admin_phone`, `admin_password`, `admin_role`, `admin_profile_pic`, `admin_address`, `admin_document_1_type`, `admin_document_1_url`, `admin_document_2_type`, `admin_document_2_url`, `admin_status`, `admin_created_by`, `admin_created_on`, `admin_last_updated_by`, `admin_last_updated_on`) VALUES
(1, 'Accelstack', 'accelstack@gmail.com', '8660225610', '$2b$12$L7AxukKyeRLxXq8E3TNMbuo7sRZ37U76bG6eVFehSETQoeIOo2eyC', 1, 'logo/admin.png', '123 Main St, City', 'Aadhar Card', NULL, 'Pan Card', NULL, 1, 1, '2024-02-29 12:49:37', 1, '2024-02-29 12:49:37'),
(2, 'Santhosh', 'devsandy12@gmail.com', '9876554322', '$2b$12$KUSGu9KOrCV5MFzf4DjZGOZIvy5zS5DR9t9RaJh50bCUy7VLpV/2i', 2, 'profile_pic/profile_pic_1709194045_sandyf.png', 'address', 'Aadhar', '[\"documents/documents_1709194045_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\"]', 'Pan Card', '[\"documents/documents_1709194045_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\"]', 1, 1, '2024-02-29 13:37:25', 1, '2024-02-29 13:37:25');

-- --------------------------------------------------------

--
-- Table structure for table `admin_setting`
--

CREATE TABLE `admin_setting` (
  `setting_id` int(11) NOT NULL,
  `emailjs_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`emailjs_attribute`)),
  `base_url` varchar(255) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `support_attributes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`support_attributes`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_setting`
--

INSERT INTO `admin_setting` (`setting_id`, `emailjs_attribute`, `base_url`, `created_by`, `created_on`, `updated_by`, `updated_on`, `support_attributes`) VALUES
(1, '{\"emailjs_url\": \"https://api.emailjs.com/api/v1.0/email/send\", \"emailjs_service_id\": \"service_7eqv3fu\", \"emailjs_template_id\": \"template_1c47e6b\", \"emailjs_user_id\": \"qbWAgwqHOFbcgoJRF\"}', 'http://127.0.0.1:8000', 1, '2024-03-31 12:59:27', 1, '2024-03-31 13:00:06', '{\"support_email\": \"support@indolens.com\", \"support_phone\": \"8660225160\", \"support_hour\": \"09 AM - 06 PM \"}');

-- --------------------------------------------------------

--
-- Table structure for table `area_head`
--

CREATE TABLE `area_head` (
  `ah_area_head_id` int(11) NOT NULL,
  `ah_name` varchar(255) DEFAULT NULL,
  `ah_email` varchar(255) DEFAULT NULL,
  `ah_phone` varchar(255) DEFAULT NULL,
  `ah_password` varchar(255) DEFAULT NULL,
  `ah_profile_pic` varchar(255) DEFAULT NULL,
  `ah_assigned_stores` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ah_address` varchar(255) DEFAULT NULL,
  `ah_document_1_type` varchar(255) DEFAULT NULL,
  `ah_document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ah_document_2_type` varchar(255) DEFAULT NULL,
  `ah_document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ah_status` int(11) DEFAULT NULL,
  `ah_created_by` int(11) DEFAULT NULL,
  `ah_created_on` datetime DEFAULT NULL,
  `ah_last_updated_by` int(11) DEFAULT NULL,
  `ah_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `brand_brand_id` int(11) NOT NULL,
  `brand_name` varchar(255) DEFAULT NULL,
  `brand_category_id` int(11) DEFAULT NULL,
  `brand_description` varchar(255) DEFAULT NULL,
  `brand_status` tinyint(1) DEFAULT NULL,
  `brand_created_on` datetime DEFAULT NULL,
  `brand_created_by` int(11) DEFAULT NULL,
  `brand_last_updated_on` datetime DEFAULT NULL,
  `brand_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`brand_brand_id`, `brand_name`, `brand_category_id`, `brand_description`, `brand_status`, `brand_created_on`, `brand_created_by`, `brand_last_updated_on`, `brand_last_updated_by`) VALUES
(1, 'Rayban', 0, 'Description for rayban', 1, '2024-02-29 12:59:09', 1, '2024-02-29 12:59:09', 1),
(2, 'Vincent Chase', 0, 'Description for vincent chase', 0, '2024-02-29 12:59:22', 1, '2024-02-29 12:59:22', 1),
(5, 'test dict', 0, 'test dict update', 0, '2024-03-28 13:31:49', 1, '2024-03-28 13:33:26', 1);

-- --------------------------------------------------------

--
-- Table structure for table `central_inventory`
--

CREATE TABLE `central_inventory` (
  `ci_product_id` int(11) NOT NULL,
  `ci_product_name` varchar(255) DEFAULT NULL,
  `ci_product_description` longtext DEFAULT NULL,
  `ci_product_images` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ci_product_qr_code` varchar(255) DEFAULT NULL,
  `ci_category_id` int(11) DEFAULT NULL,
  `ci_brand_id` int(11) DEFAULT NULL,
  `ci_material_id` int(11) DEFAULT NULL,
  `ci_frame_type_id` int(11) DEFAULT NULL,
  `ci_frame_shape_id` int(11) DEFAULT NULL,
  `ci_color_id` int(11) DEFAULT NULL,
  `ci_unit_id` int(11) DEFAULT NULL,
  `ci_origin` varchar(255) DEFAULT NULL,
  `ci_cost_price` int(11) DEFAULT NULL,
  `ci_sale_price` int(11) DEFAULT NULL,
  `ci_model_number` varchar(255) DEFAULT NULL,
  `ci_hsn` varchar(255) DEFAULT NULL,
  `ci_power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ci_franchise_sale_price` int(11) DEFAULT NULL,
  `ci_product_quantity` int(11) DEFAULT NULL,
  `ci_product_gst` float DEFAULT NULL,
  `ci_status` tinyint(1) DEFAULT NULL,
  `ci_discount` float DEFAULT NULL,
  `ci_created_on` datetime DEFAULT NULL,
  `ci_created_by` int(11) DEFAULT NULL,
  `ci_last_updated_on` datetime DEFAULT NULL,
  `ci_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `central_inventory`
--

INSERT INTO `central_inventory` (`ci_product_id`, `ci_product_name`, `ci_product_description`, `ci_product_images`, `ci_product_qr_code`, `ci_category_id`, `ci_brand_id`, `ci_material_id`, `ci_frame_type_id`, `ci_frame_shape_id`, `ci_color_id`, `ci_unit_id`, `ci_origin`, `ci_cost_price`, `ci_sale_price`, `ci_model_number`, `ci_hsn`, `ci_power_attribute`, `ci_franchise_sale_price`, `ci_product_quantity`, `ci_product_gst`, `ci_status`, `ci_discount`, `ci_created_on`, `ci_created_by`, `ci_last_updated_on`, `ci_last_updated_by`) VALUES
(1, 'Indolens  Full shell frame BLACK', '<p>Hello</p>', '[\"products/products_1709192184_Design.png\", \"products/products_1709192184_sandyf.png\"]', 'product_qr_codes/1.png', 1, 1, 1, 1, 1, 1, 1, 'Indian', 1000, 1400, '01', '01', '{}', 1100, 13, 12, 1, 50, '2024-02-29 13:06:24', 1, '2024-02-29 13:08:56', 1),
(2, 'Indolens  Full shell frame BLACK  No discount', '', '[\"products/products_1709192495_Gemini_Generated_Image.jpeg\", \"products/products_1709192495_Design.png\"]', 'product_qr_codes/2.png', 1, 2, 1, 1, 1, 1, 1, 'Indian', 600, 1200, '09', '09', '{}', 900, 88, 5, 1, 25, '2024-02-29 13:11:35', 1, '2024-02-29 13:11:35', 1),
(3, 'Indolens Lens HMC  Stock', '<p>Description for lens</p>', '[\"products/products_1709192687_Design.png\", \"products/products_1709192687_sandyf.png\"]', 'product_qr_codes/3.png', 2, 1, 2, 0, 0, 1, 2, 'Indian', 100, 250, '07', '07', '{\"vision_type\": \"single_vision\", \"stock_type\": \"stock\", \"index\": \"0.1\"}', 150, 82, 5, 1, 10, '2024-02-29 13:14:47', 1, '2024-02-29 13:14:47', 1),
(4, 'Indolens Lens HMC  RX', '<p>updated</p>', '[\"products/products_1709192744_Design.png\", \"products/products_1709192744_sandyf.png\"]', 'product_qr_codes/4.png', 2, 1, 1, 0, 0, 1, 1, 'Indian', 400, 600, '04', '04', '{\"vision_type\": \"bifocal\", \"stock_type\": \"rx\", \"index\": \"1.49\"}', 500, 76, 5, 1, 10, '2024-02-29 13:15:44', 1, '2024-03-22 19:24:53', 1),
(5, 'Indolens Contact Lens Stock BL three month soft', '<p>Desdc</p>', '[\"products/products_1709192845_Design.png\"]', 'product_qr_codes/5.png', 3, 1, 1, 0, 0, 1, 2, 'Indian', 900, 2000, '012', '12', '{\"stock_type\": \"stock\", \"contact_lens_type\": \"Soft\", \"contact_lens_disposability\": \"3 Month\"}', 1400, 1000, 12, 1, 25, '2024-02-29 13:17:25', 1, '2024-02-29 13:17:25', 1),
(6, 'Indolens Contact Lens Rx BL  three month hard', '<p>descpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp ooooooooooooooooooooooooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyoooooooooooooooooooooooooooooooooooooooossssssssssssssssssssbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbppppppppppppppppppppppppppiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiieeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeennnnnnnnnnnnnnnnnnn</p>', '[\"products/products_1709192909_Design.png\", \"products/products_1709192909_sandyf.png\", \"products/products_1711961894_profile_pic_1700635966_accountant.webp\"]', 'product_qr_codes/6.png', 3, 1, 1, 0, 0, 1, 1, 'Indian', 1000, 2000, '097', '097', '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"3 Month\"}', 1100, 81, 12, 1, 9, '2024-02-29 13:18:29', 1, '2024-04-01 14:28:14', 1);

-- --------------------------------------------------------

--
-- Table structure for table `central_inventory_restock_log`
--

CREATE TABLE `central_inventory_restock_log` (
  `cirl_restock_id` int(11) NOT NULL,
  `cirl_product_id` int(11) DEFAULT NULL,
  `cirl_quantity` int(11) DEFAULT NULL,
  `cirl_created_by` int(11) DEFAULT NULL,
  `cirl_created_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `central_inventory_restock_log`
--

INSERT INTO `central_inventory_restock_log` (`cirl_restock_id`, `cirl_product_id`, `cirl_quantity`, `cirl_created_by`, `cirl_created_on`) VALUES
(1, 1, 100, 1, '2024-02-29 13:06:24'),
(2, 2, 120, 1, '2024-02-29 13:11:35'),
(3, 3, 90, 1, '2024-02-29 13:14:47'),
(4, 4, 90, 1, '2024-02-29 13:15:44'),
(5, 5, 1000, 1, '2024-02-29 13:17:25'),
(6, 6, 90, 1, '2024-02-29 13:18:29'),
(7, 1, 100, 1, '2024-03-20 01:20:35');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_customer_id` int(11) NOT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `customer_gender` varchar(255) DEFAULT NULL,
  `customer_age` int(11) DEFAULT NULL,
  `customer_phone` varchar(255) DEFAULT NULL,
  `customer_email` varchar(255) DEFAULT NULL,
  `customer_language` varchar(255) DEFAULT NULL,
  `customer_city` varchar(255) DEFAULT NULL,
  `customer_address` varchar(255) DEFAULT NULL,
  `customer_created_by_employee_id` int(11) DEFAULT NULL,
  `customer_created_by_store_id` int(11) DEFAULT NULL,
  `customer_created_by_store_type` int(11) DEFAULT NULL,
  `customer_created_on` datetime DEFAULT NULL,
  `customer_updated_by_employee_id` int(11) DEFAULT NULL,
  `customer_updated_by_store_id` int(11) DEFAULT NULL,
  `customer_updated_by_store_type` int(11) DEFAULT NULL,
  `customer_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_customer_id`, `customer_name`, `customer_gender`, `customer_age`, `customer_phone`, `customer_email`, `customer_language`, `customer_city`, `customer_address`, `customer_created_by_employee_id`, `customer_created_by_store_id`, `customer_created_by_store_type`, `customer_created_on`, `customer_updated_by_employee_id`, `customer_updated_by_store_id`, `customer_updated_by_store_type`, `customer_updated_on`) VALUES
(1, 'Deeraj', 'M', 23, '08792103813', 'smitharaj0703@gmail.com', 'Kannada', 'banglore', 'Rajajinagar, Banglore', 2, 1, 1, '2024-02-29 13:51:34', 2, 1, 1, '2024-03-05 13:12:42'),
(8, 'Santhosh', 'M', 23, '8660225160', 'devsandy12@gmail.com', 'English', 'Bangalore', 'Hello', 2, 1, 1, '2024-03-05 15:35:10', 2, 1, 1, '2024-03-23 13:02:52');

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
('0zshlruhgofd07wmmegmadjvlmgyzcyo', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnHgB:4O4miMEhHnnx4dSjuUVQbVozycGtv0EJBRAV5axucB4', '2024-03-21 13:07:55.396097'),
('125ub48wmuej7gcgr90i7zwovntlqa07', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rkrW6:T_kV4QK0GIsxTtPPEBGG4PJ3lo56t9E5tYwh8C1JlIE', '2024-03-14 20:47:30.275458'),
('27elhiqfs3oc95n1wlv5reu9oy376joq', '.eJxNjDsOwjAQRK8SbR0FHAqIK0SbkgOslnhjW_JPdoKEEHfHQRTpZuZp3htsQUcPXHgy6KLWrNAGkEteuQWrQIoWAnkGCXcKi4nFNOPqKUML7Mm6ChQ_CwX1Ev1Vb1M3RV_x5v1fbxQ0ucxN3SpJOc7WMSY7Vbhrh11GcT4OYjhdRI8__dyloOHzBerVPcA:1rhRvg:tJN55zU6ukPH2zmb6pxIjrfd0WOOpInpGN17B8UkApo', '2024-03-19 10:21:48.707967'),
('4umdvly9pcpu7knux5kqbkrlr98v8grs', '.eJxNjTEOwjAMRe_iOSpNK4TaiYmJjQNYUeumhjSJkjAgxN1JKKBu9vv2-0_giFNQdpg5EsbkAqFxWtOIbKFP4U4CeIR-L8CqhaCHM984zSCAFsUmA_MBR13WanBLjlbR9-H0818Klf84PXyJmwxUjKxtLl2TUigF-OAmNoSeh3y32XabGeWh7mTXdm2NnkJ0tqmuXmdpcCb75esNEslPEw:1rndXg:qb11etxvsChGMs7b6f66BxM_vFHRnoA_b0u1GUVPsFc', '2024-03-22 12:28:36.130255'),
('52xzuyf8wdzha5eve41t0mj3vu98kf5m', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rm7MZ:6MjX6nVY3R-UN7jDi3x4D8-zrr1nHmWtDN6_gRUF66c', '2024-03-18 07:54:51.815148'),
('67lmy95h6ky9k028ewzr1o5eeicy94ej', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rfcCa:slj5PG7zCwDvltNr-TZqL6FtVcl-hlLeruqGYUvjLFc', '2024-03-14 08:55:40.905909'),
('6l0ntnnk35jwp1b5i5ahjn2a7ex9c3n8', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rmeR2:auxQ46AaA3RqWrN_o3ANvx5gMANU6uRLtAmberDctaI', '2024-03-19 19:13:40.280372'),
('72ntj59hpql0msiftpdmjkmx0sahlaa0', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rndgu:7-LRqSltkqlYBFB_WNE3ZOEXnLCxLzgr9FfdFD8SUYE', '2024-03-22 12:38:08.268156'),
('86xo57ujk267yjspqf6z6lxeb8baazti', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rpmfC:FYOOO9RPDGz1WfrEghl3mQqixOu9iEiaA6T5PHfRM08', '2024-04-11 10:07:14.997645'),
('879cxpqeo0hxvlimsyxlpjqiul0ap8en', 'e30:1rkrHG:41pQF2wpZelQwxR2Bd0YZrRajFcAejHsxKDbBFDF-B4', '2024-03-14 20:32:10.415083'),
('ar2lijrpeb9dqrte3go6xu9uc99fikpw', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnIwL:QqmwswSkUSkIcYEH58xpxOhBfuwG5niK-gUrc5v9KxI', '2024-03-21 14:28:41.300189'),
('avrvdhd94tzy3kg7ewumuys9o3de59q9', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rfdgp:JqVGDtg3nudYK9LpuLDpusbjnihmlVssW2W3aOEo-7Y', '2024-03-14 10:30:59.724899'),
('cssneroui9tg3nllokrxdjjs9jp1pxtm', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnw04:mj7IX40o0FnQuCdo8gNkCwTgVYH-bh1NReBF_v4tKj4', '2024-03-23 08:11:08.081066'),
('d2dtis94dd53pbn81udn8dtgo7nfiftz', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rpBze:EKyQZMJyrKDyo-OYuDqeXoGfLuHy-RcM9N5WlFGTDz4', '2024-04-09 18:57:54.951428'),
('dq0lp424ceduruoou1aknghby5qsmmki', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rm9FR:TG6ilrddJjxUOieoykUR9jodQ-smDI8HxbyChHsIirc', '2024-03-18 09:55:37.824112'),
('etqfoaklxmqocc0ztqltv93ukhew6d8f', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rnwjY:u0MU9t9xQrwcm-THeeu3zOthuD2hP6mFMbxxkX41G0k', '2024-03-23 08:58:08.422060'),
('fdz2b4ecifx63mockcx5ny7zb14gwgoi', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rkra6:YoCeX52__K9-0DyoDng-G2THh3S-rNZkuoPSFqShm1A', '2024-03-14 20:51:38.189562'),
('fm6szmit23oht40xxb0hxpyrlw37nwfi', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rp7BB:HFGMb0z4Pv5XCuxzkd7rJpd89p6BDretufsw5aIKWeo', '2024-03-26 14:19:29.846725'),
('fzk9xrlff8fcmdwxrtnfbi7iqiuluizz', '.eJxNyUsKgCAURuG9_GPpRRG5jRZwkTS7UFdRG0S09xo2Ox_nBmcy9mChPXjvLLFAl3Q6BbbQnYKYw0FjNlK2kDcoxBRW3h1FXr7xU_1rasdmaqe-6QfKRuy1VlE8nhf2KieB:1rnfU4:M7CizYALKEjtPrO8ysrCqWjOvjdoLM7b2YFN7AxnvBM', '2024-03-22 14:33:00.452062'),
('g218tj5eu45zi5q6dhwbqf07dr3i22vc', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rlkg0:kgLGj3WkOv_I5RFjy43lzwaS-2jicyyCtJ3hA3ufkdc', '2024-03-17 07:41:24.229476'),
('g9xr5wcodyf5jbumlhtrvvbzejolzbjy', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnzzW:75LMJqGk7OpJsx9WD7gH2uuPFDz6ZzYQyXK0SLEYKtk', '2024-03-23 12:26:50.192915'),
('gvwujj41573enx74v9thw7t3kfnqzm97', 'e30:1rjDYJ:CjDxOBdOnHPJw5kyzCyoTxyvDMuzKI0pSJOc9e-EPbc', '2024-03-10 07:54:59.363316'),
('hrv4trlkkjryqyhtsd6re2ljlc2l1d0h', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rpTri:3o0Ns1G0uShF-bPGzLzYmEzm-X9rJ3Q9esyhi0cFYkk', '2024-04-10 14:02:54.074808'),
('igx6g9oor88aagsetdjwa4pxp6qewfms', '.eJxNjDsOwjAQRK8SbR0FHAqIK0SbkgOslnhjW_JPdoKEEHfHQRTpZuZp3htsQUcPXHgy6KLWrNAGkEteuQWrQIoWAnkGCXcKi4nFNOPqKUML7Mm6ChQ_CwX1Ev1Vb1M3RV_x5v1fbxQ0ucxN3SpJOc7WMSY7Vbhrh11GcT4OYjhdRI8__dyloOHzBerVPcA:1rfc9s:YD6C31xjPfb1ZZZ94tLpce7_hmrJFF1GIIkU3_X4RiI', '2024-03-14 08:52:52.957157'),
('itbv36zt883p3f4x3z8qc4fys6yd8230', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rjDcK:W80yykmuxNB5n_eUrp8ObC-NmzkixiI2yjm3tUGHCfU', '2024-03-10 07:59:08.146380'),
('j9sk0ymbvcgbr0xeqfj7na6euyylqus2', 'e30:1rjCxx:OYhA0_FlvqP2abDciJfmT5u4Ry_U78Q31r9jM3QiYP0', '2024-03-10 07:17:25.938712'),
('jzkjg3znggtyqas93beptmj8xwdj0hg2', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rfaib:HTFpM9NrpQJhMU5DMqmHwC6u81B4ufd9xbDitKz7OZ0', '2024-03-14 07:20:37.065133'),
('k0y6jtobx66b9p13bdu7r4qt4nvr0bav', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rpTq0:wOmf8q1BrrUF2-dVXjTKVLpyVF_MbtVgyL4kZ5AjlEM', '2024-04-10 14:01:08.812468'),
('ktz82ziwkxauvcq2t4o4wraipezty48c', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rkIYv:p1lIH17-UyJ1UwUV7Fok1QEinN_F1F9oOrfp7XCEfww', '2024-03-13 07:28:05.045552'),
('l0gpyg3zds620221c60myn7z2o6gj02l', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnvQu:RLs9-2_rnG6h1q_sTJ21Th9GQYhmu9APCvXsbAaNMZ4', '2024-03-23 07:34:48.775005'),
('l1ivb1euk9ji87wsxg8x8juihcp233dr', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rkgOU:RIwoM2lSRjTQS51ZVjmNhPdpRZ4yX11nWs20jRfdvZk', '2024-03-14 08:54:54.187020'),
('lc9gybh3ypyt4cukieajyts8hvittowf', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rm9AM:3cWkBJC75qSh0MXtC2iDQoi2BHSBLV5KWd_9gIDRoks', '2024-03-18 09:50:22.940473'),
('lk2b653gavuncl6yzwn4sv21obfb1qqm', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rkocQ:qLGYmO9N6SfAY3gLgUDLwefbWciZcsEiN9tufDGU-Lo', '2024-03-14 17:41:50.849355'),
('m59ruxiq67psx9q9g78bssti6c63ow08', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rjxXC:C5y_X3Hj1XKrKDy5RQwd_NXCosRGxF64ghsdTtg7zRM', '2024-03-12 09:00:54.025286'),
('m5dfpbx2tnxngh71jy6uvifilaieq2ij', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rmfTn:QvAoIQMzWCSE3t3qEvH3iOPHZqEFbYgn9kZ7YoBWdS8', '2024-03-19 20:20:35.761843'),
('ndxj26zj7f0e7uekxjupmzbpnbmcvkci', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rndOi:tw3SNL7bw8p9oYq2lSfs2YopEcTLCQWgdLhK2qlXCpw', '2024-03-22 12:19:20.784030'),
('nuhl8e3v9xdse65595yo0ri2c5u0cqfm', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rm6r3:34gQiqoH5eLVByLQliWkewMnUyvWQhsAmzNF1R9qR-A', '2024-03-18 07:22:17.648493'),
('p6sujixl6teix9k2yenxnaes4d6y60w7', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rhNJy:hVOypzrzDVl3Cok92pKgiyNquyb5m4fd8WKj1OOnJIc', '2024-03-19 05:26:34.651290'),
('pdh20d543nj1zr08e0624vvkqtimnw5w', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnxWy:18sjkSvBkapMgeDg3F-cT1kBTavieQGyyG418evVkX4', '2024-03-23 09:49:12.115016'),
('qvyalruhn1c61lzpg4jlm2coe32dpuw5', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rkh1G:8mO2SOZ4eRUlL4_VqnMyGzNMCOeypADrJp328m47V8U', '2024-03-14 09:34:58.108121'),
('rz8jw2475u42oeeuxry9lcyfbf1b3e48', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rgKPr:JLakNKVEdxdO59QoAghD-MHI5WjchV7785mC5tHc9FE', '2024-03-16 08:08:19.507573'),
('so0d2bc44v4hi2kjhp3823nxfad8cdap', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rnfAX:LAb66eefUk9sO7pfFcISbCAYgbHrWN1FACJwa9S_gpY', '2024-03-22 14:12:49.697066'),
('sz3hgtd399q6kte6lieyf4t5nhxjniy8', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rg1sg:sWU_mCSrLzj3-YYBWFbYUW_WBiE3irwNo3fWvjMmkII', '2024-03-15 12:20:50.301463'),
('tlbku1liano7xad5hdkee1lk4wu6jpuc', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rjDcY:HfheLObFFOKcVA8ta2ED8W6WDjnGRC4BjPf5FrfUDXk', '2024-03-10 07:59:22.327939'),
('tm3ewscrf1nimyd8jcerzune62b7rb1f', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rkrC7:AV6OqixcJ8wt2dEiVGDdyh-ZTDfR1ZgVBMJ1drinNIA', '2024-03-14 20:26:51.405912'),
('u9qbabqi5ysvru7401icimpyukudmb18', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rngqs:8dlKTSOd6bzQh7Z51TJWTdW_czaczAm_oFh5r0dbQ6U', '2024-03-22 16:00:38.116173'),
('u9xvr221nzcawkz1u7wrnp77kigsv1f3', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rngmK:foILiLp-2rdttc4L1E23Z3JZgdiCbm1r3joj_DfjmY0', '2024-03-22 15:55:56.744304'),
('ukjcauzhkmhppswbv0vo605qd7spnq74', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rghO9:HMgLNxA0ZKrwLlbSmYJNMGmQxyAMnVlr_pSBUrT28Zk', '2024-03-17 08:40:05.234203'),
('urm123ngakabi56jaaht688dvcbxmtu7', 'e30:1rmcs9:N8deC84t0QKhlb4fAnvH6lIzmQDvdDvL7jzRlgeLe3U', '2024-03-19 17:33:33.148887'),
('w50xyz1otuamtrt2vm1hz1zky6t6dlyp', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rkgOj:YQ5n3lZeMsvGLVOcsc7PsvOe66QIO8ZZYhUoIOQ5wJk', '2024-03-14 08:55:09.924577'),
('wetwzd8ysug3splrfyfmjhc0x7710jl0', '.eJwdzDsOgCAQRdG9vJpoaOlcCSHDSCbyC2Bl3LsT65tzH8j0IRapPreUOHqpcGvcbCARzhrUUBgOBxHnuQJdMOijnZLZdyFNKtv-T7Zek-bRshL7fhCRIAo:1rp6G1:UM-L0aovyuXdj27wZ07H5FIk2cJE50wF7FvWrDjFHxk', '2024-03-26 13:20:25.960223'),
('xwqcgvo5qx2ynm2dyu4sfsqcb19agl9d', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rnHjR:GlJOnqVKs6kIG2pip6R_YKpaJEuyM5zP1D0E8V3YRUo', '2024-03-21 13:11:17.837899'),
('z10c1qnnwx79hdzk844sxgznno9sar6e', '.eJxNjc0KwjAQhN9lz6E2FSntyYN3BR8ghHaNW_JHEhER390NLeJt55vZmTdQVrmEhMoGY3BW5GEs6YECaIaxE-C1QxjhhJj0AgLQabIMsqNy18zavt0fTaXNFBwn1r7t7_z016rlzyivWI0KdM5kPK-uTl2UAmIKN7KoIk2c-1O77b7QpGTfDnLo-oNUEVMOvmuWaLgzBcv18vMFCtZKDQ:1rmcNq:htcmp5tLuhXCPEz4fVLxVal6J0pWWrkrqMK04BSUWvo', '2024-03-19 17:02:14.929835'),
('zyztd2mx1tyj7yvc6lejulwe1kq22bs5', 'eyJpc19hZG1pbl9sb2dnZWRfaW4iOnRydWUsImlkIjoxLCJuYW1lIjoiQWNjZWxzdGFjayIsInByb2ZpbGVfcGljIjoibG9nby9hZG1pbi5wbmcifQ:1rm79l:pHrsVgmbOi8l4OfPe4WcdikOPNgGrfmUuD1Ai48mlOk', '2024-03-18 07:41:37.623194');

-- --------------------------------------------------------

--
-- Table structure for table `eye_test`
--

CREATE TABLE `eye_test` (
  `et_eye_test_id` int(11) NOT NULL,
  `et_customer_id` int(11) DEFAULT NULL,
  `et_power_attributes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `et_created_by_store_id` int(11) DEFAULT NULL,
  `et_created_by_store_type` int(11) DEFAULT NULL,
  `et_created_by` int(11) DEFAULT NULL,
  `et_created_on` datetime DEFAULT NULL,
  `et_updated_by` int(11) DEFAULT NULL,
  `et_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `eye_test`
--

INSERT INTO `eye_test` (`et_eye_test_id`, `et_customer_id`, `et_power_attributes`, `et_created_by_store_id`, `et_created_by_store_type`, `et_created_by`, `et_created_on`, `et_updated_by`, `et_updated_on`) VALUES
(1, 1, '{\"RightDvSph\": \"2\", \"RightDvCyl\": \"3\", \"RightDvAxis\": \"4\", \"RightDvVision\": \"4\", \"RightNvSph\": \"4\", \"RightNvCyl\": \"4\", \"RightNvAxis\": \"4\", \"RightNvVision\": \"4\", \"LeftDvSph\": \"7\", \"LeftDvCyl\": \"7\", \"LeftDvAxis\": \"7\", \"LeftDvVision\": \"7\", \"LeftNvSph\": \"7\", \"LeftNvCyl\": \"7\", \"LeftNvAxis\": \"7\", \"LeftNvVision\": \"7\", \"unifocal\": \"1\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"6\", \"pdl\": \"6\", \"glass\": \"1\", \"highIndex\": \"1\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 2, '2024-02-29 13:51:34', 2, '2024-02-29 13:51:34'),
(2, 8, '{\"RightDvSph\": \"1\", \"RightDvCyl\": \"\", \"RightDvAxis\": \"\", \"RightDvVision\": \"\", \"RightNvSph\": \"\", \"RightNvCyl\": \"\", \"RightNvAxis\": \"2\", \"RightNvVision\": \"\", \"LeftDvSph\": \"\", \"LeftDvCyl\": \"\", \"LeftDvAxis\": \"\", \"LeftDvVision\": \"\", \"LeftNvSph\": \"\", \"LeftNvCyl\": \"\", \"LeftNvAxis\": \"7.9\", \"LeftNvVision\": \"\", \"unifocal\": \"\", \"bifocal\": \"\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"\", \"pdl\": \"\", \"glass\": \"\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"\"}', 1, 1, 2, '2024-03-22 20:42:20', 2, '2024-03-22 20:42:20'),
(3, 8, '{\"test_type\": \"\", \"RightDvSph\": \"1\", \"RightDvCyl\": \"\", \"RightDvAxis\": \"3\", \"RightDvVision\": \"1\", \"RightNvSph\": \"6\", \"RightNvCyl\": \"\", \"RightNvAxis\": \"6\", \"RightNvVision\": \"\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"\", \"LeftDvAxis\": \"6\", \"LeftDvVision\": \"\", \"LeftNvSph\": \"1\", \"LeftNvCyl\": \"2\", \"LeftNvAxis\": \"\", \"LeftNvVision\": \"4\", \"unifocal\": \"1\", \"bifocal\": \"\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"1\", \"pdr\": \"1.2\", \"pdl\": \"\", \"glass\": \"\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"\"}', 1, 1, 2, '2024-03-23 12:56:58', 2, '2024-03-23 12:56:58'),
(4, 8, '{\"test_type\": \"Specticale\", \"RightDvSph\": \"1\", \"RightDvCyl\": \"\", \"RightDvAxis\": \"3\", \"RightDvVision\": \"\", \"RightNvSph\": \"5\", \"RightNvCyl\": \"\", \"RightNvAxis\": \"7\", \"RightNvVision\": \"8\", \"LeftDvSph\": \"1\", \"LeftDvCyl\": \"2\", \"LeftDvAxis\": \"\", \"LeftDvVision\": \"\", \"LeftNvSph\": \"5\", \"LeftNvCyl\": \"\", \"LeftNvAxis\": \"7\", \"LeftNvVision\": \"8\", \"unifocal\": \"\", \"bifocal\": \"1\", \"progressive\": \"\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"1.1\", \"pdl\": \"\", \"glass\": \"1\", \"highIndex\": \"\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"\"}', 1, 1, 2, '2024-03-23 13:01:24', 2, '2024-03-23 13:01:24'),
(5, 8, '{\"test_type\": \"Contact Lens\", \"RightDvSph\": \"1\", \"RightDvCyl\": \"2\", \"RightDvAxis\": \"\", \"RightDvVision\": \"\", \"RightNvSph\": \"5\", \"RightNvCyl\": \"6\", \"RightNvAxis\": \"\", \"RightNvVision\": \"\", \"LeftDvSph\": \"\", \"LeftDvCyl\": \"\", \"LeftDvAxis\": \"3\", \"LeftDvVision\": \"4\", \"LeftNvSph\": \"\", \"LeftNvCyl\": \"\", \"LeftNvAxis\": \"7\", \"LeftNvVision\": \"8\", \"unifocal\": \"\", \"bifocal\": \"\", \"progressive\": \"1\", \"cr39\": \"\", \"arc\": \"\", \"pdr\": \"\", \"pdl\": \"1.5\", \"glass\": \"\", \"highIndex\": \"1\", \"pg\": \"\", \"constant\": \"\", \"distance\": \"\", \"near\": \"1\"}', 1, 1, 2, '2024-03-23 13:02:52', 2, '2024-03-23 13:02:52');

-- --------------------------------------------------------

--
-- Table structure for table `frame_shapes`
--

CREATE TABLE `frame_shapes` (
  `fshape_shape_id` int(11) NOT NULL,
  `fshape_name` varchar(255) DEFAULT NULL,
  `fshape_description` varchar(255) DEFAULT NULL,
  `fshape_status` int(11) DEFAULT NULL,
  `fshape_created_on` datetime DEFAULT NULL,
  `fshape_created_by` int(11) DEFAULT NULL,
  `fshape_last_updated_on` datetime DEFAULT NULL,
  `fshape_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_shapes`
--

INSERT INTO `frame_shapes` (`fshape_shape_id`, `fshape_name`, `fshape_description`, `fshape_status`, `fshape_created_on`, `fshape_created_by`, `fshape_last_updated_on`, `fshape_last_updated_by`) VALUES
(1, 'Round', 'Description for round\r\n', 1, '2024-02-29 12:59:43', 1, '2024-02-29 12:59:43', 1),
(2, 'Hexa', 'rtdf', 0, '2024-02-29 12:59:48', 1, '2024-02-29 12:59:48', 1),
(3, 'test dict update', 'test dict update', 1, '2024-03-28 13:35:40', 1, '2024-03-28 13:43:33', 1);

-- --------------------------------------------------------

--
-- Table structure for table `frame_types`
--

CREATE TABLE `frame_types` (
  `ftype_frame_id` int(11) NOT NULL,
  `ftype_name` varchar(255) DEFAULT NULL,
  `ftype_description` varchar(255) DEFAULT NULL,
  `ftype_status` int(11) DEFAULT NULL,
  `ftype_created_on` datetime DEFAULT NULL,
  `ftype_created_by` int(11) DEFAULT NULL,
  `ftype_last_updated_on` datetime DEFAULT NULL,
  `ftype_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frame_types`
--

INSERT INTO `frame_types` (`ftype_frame_id`, `ftype_name`, `ftype_description`, `ftype_status`, `ftype_created_on`, `ftype_created_by`, `ftype_last_updated_on`, `ftype_last_updated_by`) VALUES
(1, 'Full Frame', 'gh', 1, '2024-02-29 12:59:57', 1, '2024-02-29 12:59:57', 1),
(2, 'Half Frame', 'gcvh', 0, '2024-02-29 13:00:01', 1, '2024-02-29 13:00:01', 1),
(3, 'dict test update', 'dict test update', 0, '2024-03-28 13:45:46', 1, '2024-03-28 13:48:12', 1);

-- --------------------------------------------------------

--
-- Table structure for table `franchise_owner`
--

CREATE TABLE `franchise_owner` (
  `franchise_owner_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
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
  `fs_store_id` int(11) NOT NULL,
  `fs_store_name` varchar(255) DEFAULT NULL,
  `fs_store_display_name` varchar(255) DEFAULT NULL,
  `fs_store_phone` varchar(255) DEFAULT NULL,
  `fs_store_gst` varchar(255) DEFAULT NULL,
  `fs_store_email` varchar(255) DEFAULT NULL,
  `fs_store_city` varchar(255) DEFAULT NULL,
  `fs_store_state` varchar(255) DEFAULT NULL,
  `fs_store_zip` varchar(255) DEFAULT NULL,
  `fs_store_lat` double DEFAULT NULL,
  `fs_store_lng` double DEFAULT NULL,
  `fs_store_address` varchar(255) DEFAULT NULL,
  `fs_status` int(11) DEFAULT NULL,
  `fs_created_by` int(11) DEFAULT NULL,
  `fs_created_on` datetime DEFAULT NULL,
  `fs_last_updated_by` int(11) DEFAULT NULL,
  `fs_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store`
--

INSERT INTO `franchise_store` (`fs_store_id`, `fs_store_name`, `fs_store_display_name`, `fs_store_phone`, `fs_store_gst`, `fs_store_email`, `fs_store_city`, `fs_store_state`, `fs_store_zip`, `fs_store_lat`, `fs_store_lng`, `fs_store_address`, `fs_status`, `fs_created_by`, `fs_created_on`, `fs_last_updated_by`, `fs_last_updated_on`) VALUES
(1, 'FranchiseStore1', 'FranchiseStore1', '8792103816', '26AATCA501G1Z67', 'franchise1@gmail.com', 'banglore', 'karnataka', '111112', 13.0285133, 77.5196763, 'Peenya, Banglore', 1, 1, '2024-02-29 13:05:05', 1, '2024-02-29 13:05:05'),
(2, 'FranchiseStore2', 'FranchiseStore2', '8792103817', '26AATCA501G1Z89', 'franchise12@gmail.com', 'chennai', 'tamilnadu', '111112', 13.0826802, 80.2707184, 'Chennai,Tamilnadu', 1, 1, '2024-02-29 13:06:27', 1, '2024-02-29 13:06:27'),
(3, 'FranchiseStore3', 'FranchiseStore3', '08792103818', '26AATCA501G1Z19', 'smitharaj0703@gmail.com', 'Hyderabad', 'Telangana', '123456', 17.406498, 78.47724389999999, 'Hyderabad,Telangana', 1, 1, '2024-02-29 13:07:40', 1, '2024-02-29 13:07:40'),
(4, 'test dict franchise store updated', 'test dict display name', '9809890989', 'GSTIN00124FR', 'testdictfranchise@test.com', 'Bangalore', 'Karnataka', '560058', 12.9111314, 77.6487393, 'Bescom Office, Parangi Palaya, Sector 2, HSR Layout, Bengaluru, Karnataka, India ', 1, 1, '2024-04-06 14:08:35', 1, '2024-04-06 15:07:57');

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store_employees`
--

CREATE TABLE `franchise_store_employees` (
  `fse_employee_id` int(11) NOT NULL,
  `fse_name` varchar(255) DEFAULT NULL,
  `fse_email` varchar(255) DEFAULT NULL,
  `fse_phone` varchar(255) DEFAULT NULL,
  `fse_password` varchar(255) DEFAULT NULL,
  `fse_profile_pic` varchar(255) DEFAULT NULL,
  `fse_assigned_store_id` int(11) DEFAULT NULL,
  `fse_address` varchar(255) DEFAULT NULL,
  `fse_document_1_type` varchar(255) DEFAULT NULL,
  `fse_document_1_url` varchar(255) DEFAULT NULL,
  `fse_document_2_type` varchar(255) DEFAULT NULL,
  `fse_document_2_url` varchar(255) DEFAULT NULL,
  `fse_status` int(11) DEFAULT NULL,
  `fse_role` int(11) DEFAULT NULL,
  `fse_created_by` int(11) DEFAULT NULL,
  `fse_created_on` datetime DEFAULT NULL,
  `fse_last_updated_by` int(11) DEFAULT NULL,
  `fse_last_updated_on` datetime DEFAULT NULL,
  `fse_certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `franchise_store_employees`
--

INSERT INTO `franchise_store_employees` (`fse_employee_id`, `fse_name`, `fse_email`, `fse_phone`, `fse_password`, `fse_profile_pic`, `fse_assigned_store_id`, `fse_address`, `fse_document_1_type`, `fse_document_1_url`, `fse_document_2_type`, `fse_document_2_url`, `fse_status`, `fse_role`, `fse_created_by`, `fse_created_on`, `fse_last_updated_by`, `fse_last_updated_on`, `fse_certificates`) VALUES
(1, 'Bharat', 'bharat123@gmail.com', '8792103812', '$2b$12$loClKR3Z3phcuBFF5I6dT.ai4ZSPP2koNAwxTwr4yv0Jm.yQLzThq', 'profile_pic/profile_pic_1709193655_person1.jpg', 0, 'Chennai, Tamil nadu', 'Aadhar', '[\"documents/documents_1709193655_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193655_pan.png\"]', 1, 1, 1, '2024-02-29 13:30:56', 1, '2024-02-29 13:30:56', NULL),
(2, 'Puneeth', 'puneeth@gmail.com', '8792103815', '$2b$12$nwxjLSgVgIOfPORlziIe6eb6KbTUL43Mx.YkQOORp2.Ktp4Nl1X7C', 'profile_pic/profile_pic_1709193744_person2.jpg', 0, 'Rajajinagar, Banglore', 'Aadhar', '[\"documents/documents_1709193744_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193744_pan.png\"]', 0, 2, 1, '2024-02-29 13:32:24', 1, '2024-02-29 13:32:24', '[\"certificates/certificates_1709193744_pan.png\"]'),
(3, 'Harshitha', 'harshitha@gmail.com', '8792103815', '$2b$12$ybFjU1LaAjSmpfXV66DjD.gyqqiJueBh2MIEGqLmnZaDAKeiUiXtq', 'profile_pic/profile_pic_1709193813_person3.jpg', 0, 'Delhi', 'Aadhar', '[\"documents/documents_1709193813_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193813_pan.png\"]', 0, 3, 1, '2024-02-29 13:33:34', 1, '2024-02-29 13:33:34', NULL),
(4, 'Bindu', 'bindu123@gmail.com', '08792103819', '$2b$12$Pky.SXb90zkLYO3C2i/.KOp2B.68ziB/6wmuFrJJokWEafSOtJ.ue', 'profile_pic/profile_pic_1709193887_person4.jpg', 0, 'Peenya, Banglore', 'Aadhar', '[\"documents/documents_1709193887_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193887_pan.png\"]', 0, 4, 1, '2024-02-29 13:34:48', 1, '2024-02-29 13:34:48', NULL),
(5, 'Likith', 'likith@gmail.com', '08792103817', '$2b$12$sIm6fPDaAxB6C0BTVD1CAu.mWVV9Ff7mXEeU3wp6CTyuDf6CvMCAa', 'profile_pic/profile_pic_1709193930_person2.jpg', 1, 'Chennai, Tamil nadu', 'Aadhar', '[\"documents/documents_1709193930_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193930_pan.png\"]', 1, 1, 1, '2024-02-29 13:35:31', 1, '2024-02-29 13:35:31', NULL),
(6, 'Vinitha', 'smitharaj0703@gmail.com', '08792103818', '$2b$12$Ue9S26GpWQUaW8EXzhKBUeZg82/.mYlG3KypF6cIs9bRIJ4Ifzre6', 'profile_pic/profile_pic_1709193983_person3.jpg', 0, 'Hyderabad, Telangana', 'Aadhar', '[\"documents/documents_1709193983_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193983_pan.png\"]', 0, 2, 1, '2024-02-29 13:36:24', 1, '2024-02-29 13:36:24', '[\"certificates/certificates_1709193983_aadhar.jpg\"]'),
(7, 'Divya', 'devsandy123@gmail.com', '08792103817', '$2b$12$6HlV1BJA5aqEByujYqHyzu/YfnJXDjR7wjC8yGLiKPMhZJBn.X7j2', 'profile_pic/profile_pic_1709194028_person4.jpg', 0, 'Chennai, Tamil nadu', 'Aadhar', '[\"documents/documents_1709194028_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709194028_pan.png\"]', 0, 3, 1, '2024-02-29 13:37:09', 1, '2024-02-29 13:37:09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `invoice_invoice_id` int(11) NOT NULL,
  `invoice_invoice_number` varchar(255) DEFAULT NULL,
  `invoice_order_id` varchar(255) DEFAULT NULL,
  `invoice_store_id` int(11) DEFAULT NULL,
  `invoice_store_type` int(11) DEFAULT NULL,
  `invoice_invoice_status` int(11) DEFAULT NULL,
  `invoice_invoice_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`invoice_invoice_id`, `invoice_invoice_number`, `invoice_order_id`, `invoice_store_id`, `invoice_store_type`, `invoice_invoice_status`, `invoice_invoice_date`) VALUES
(1, 'OS-1-29022024-00000001', 'OS_1_1709196147', 1, 1, 1, '2024-02-29'),
(2, 'OS_1_29022024_00000002', 'OS_1_1709195417', 1, 1, 1, '2024-02-29'),
(3, 'OS_1_29022024_00000003', 'OS_1_1709197165', 1, 1, 1, '2024-02-29'),
(4, 'OS_1_29022024_00000004', 'OS_1_1709633304', 1, 1, 1, '2024-03-05'),
(5, 'OS_1_29022024_00000005', 'OS_1_1709633110', 1, 1, 1, '2024-03-05'),
(6, 'OS_1_29022024_00000006', 'OS_1_1710225616', 1, 1, 1, '2024-03-12'),
(7, 'OS_1_29022024_00000007', 'OS_1_1710446969', 1, 1, 1, '2024-03-15');

-- --------------------------------------------------------

--
-- Table structure for table `lab`
--

CREATE TABLE `lab` (
  `lab_lab_id` int(11) NOT NULL,
  `lab_name` varchar(255) DEFAULT NULL,
  `lab_display_name` varchar(255) DEFAULT NULL,
  `lab_phone` varchar(255) DEFAULT NULL,
  `lab_gst` varchar(255) DEFAULT NULL,
  `lab_email` varchar(255) DEFAULT NULL,
  `lab_city` varchar(255) DEFAULT NULL,
  `lab_state` varchar(255) DEFAULT NULL,
  `lab_zip` varchar(255) DEFAULT NULL,
  `lab_lat` double DEFAULT NULL,
  `lab_lng` double DEFAULT NULL,
  `lab_address` varchar(255) DEFAULT NULL,
  `lab_status` int(11) DEFAULT NULL,
  `lab_created_by` int(11) DEFAULT NULL,
  `lab_created_on` datetime DEFAULT NULL,
  `lab_last_updated_by` int(11) DEFAULT NULL,
  `lab_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lab`
--

INSERT INTO `lab` (`lab_lab_id`, `lab_name`, `lab_display_name`, `lab_phone`, `lab_gst`, `lab_email`, `lab_city`, `lab_state`, `lab_zip`, `lab_lat`, `lab_lng`, `lab_address`, `lab_status`, `lab_created_by`, `lab_created_on`, `lab_last_updated_by`, `lab_last_updated_on`) VALUES
(1, 'Bangalre lab', 'Bangalore lab', '8660225160', 'GSTIN09876543', 'lab.bangalore@gmail.com', 'Bangalore', 'Karnataka', '562123', 13.1006804, 77.39045519999999, ' Indolens, Indolens Solutions Pvt Ltd, BH Road, Jyothi Nagar, Nelamangala Town, Karnataka, India', 1, 1, '2024-02-29 13:31:41', 1, '2024-02-29 14:21:53'),
(2, 'Tumkur lab Updated', 'Tumkur lab', '8660225160', 'GSTIN09876543', 'lab.tumkur@gmail.com', 'Bangalore', 'Karnataka', '111111', 12.9853859, 77.5352348, ' Tumkur, Stage 1, KHB Colony, Basaveshwar Nagar, Bengaluru, Karnataka, India', 1, 1, '2024-02-29 13:32:29', 1, '2024-04-06 17:52:04');

-- --------------------------------------------------------

--
-- Table structure for table `lab_technician`
--

CREATE TABLE `lab_technician` (
  `lt_lab_technician_id` int(11) NOT NULL,
  `lt_name` varchar(255) DEFAULT NULL,
  `lt_email` varchar(255) DEFAULT NULL,
  `lt_phone` varchar(255) DEFAULT NULL,
  `lt_password` varchar(255) DEFAULT NULL,
  `lt_profile_pic` varchar(255) DEFAULT NULL,
  `lt_assigned_lab_id` int(11) DEFAULT NULL,
  `lt_address` varchar(255) DEFAULT NULL,
  `lt_document_1_type` varchar(255) DEFAULT NULL,
  `lt_document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `lt_document_2_type` varchar(255) DEFAULT NULL,
  `lt_document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `lt_status` int(11) DEFAULT NULL,
  `lt_created_by` int(11) DEFAULT NULL,
  `lt_created_on` datetime DEFAULT NULL,
  `lt_last_updated_by` int(11) DEFAULT NULL,
  `lt_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lab_technician`
--

INSERT INTO `lab_technician` (`lt_lab_technician_id`, `lt_name`, `lt_email`, `lt_phone`, `lt_password`, `lt_profile_pic`, `lt_assigned_lab_id`, `lt_address`, `lt_document_1_type`, `lt_document_1_url`, `lt_document_2_type`, `lt_document_2_url`, `lt_status`, `lt_created_by`, `lt_created_on`, `lt_last_updated_by`, `lt_last_updated_on`) VALUES
(1, 'Santhosh Kumar', 'devsandy12@gmail.com', '8660225160', '$2b$12$jRbmzj.REjfZWB2Qyfnfe.SLvmgbFwyBZ1TFl2w70EoNjob0NE71m', 'profile_pic/profile_pic_1709193812_sandyf.png', 1, 'Address of technician', 'Aadhar', '[\"documents/documents_1709193812_sandyf.png\"]', 'Pan Card', '[\"documents/documents_1709193812_sandyf.png\"]', 1, 1, '2024-02-29 13:33:33', 1, '2024-02-29 13:33:33'),
(2, 'Roop Raj Thapa', 'accelstack@gmail.com', '09876543210', '$2b$12$Agz9c3IVn.zt59sNr5q0Z.hNtYwfuDmAMLGF3ZMvqraREx0wO8Ace', 'profile_pic/profile_pic_1709193883_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg', 2, 'Address here', 'Aadhar', '[\"documents/documents_1709193883_sandyf.png\"]', 'Pan Card', '[\"documents/documents_1709193883_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\"]', 1, 1, '2024-02-29 13:34:44', 1, '2024-02-29 13:34:44');

-- --------------------------------------------------------

--
-- Table structure for table `marketing_head`
--

CREATE TABLE `marketing_head` (
  `mh_marketing_head_id` int(11) NOT NULL,
  `mh_name` varchar(255) DEFAULT NULL,
  `mh_email` varchar(255) DEFAULT NULL,
  `mh_phone` varchar(255) DEFAULT NULL,
  `mh_password` varchar(255) DEFAULT NULL,
  `mh_profile_pic` varchar(255) DEFAULT NULL,
  `mh_assigned_area_head` int(11) DEFAULT NULL,
  `mh_address` varchar(255) DEFAULT NULL,
  `mh_document_1_type` varchar(255) DEFAULT NULL,
  `mh_document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `mh_document_2_type` varchar(255) DEFAULT NULL,
  `mh_document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `mh_status` int(11) DEFAULT NULL,
  `mh_created_by` int(11) DEFAULT NULL,
  `mh_created_on` datetime DEFAULT NULL,
  `mh_last_updated_by` int(11) DEFAULT NULL,
  `mh_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `optimetry`
--

CREATE TABLE `optimetry` (
  `optimetry_id` int(11) NOT NULL,
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
  `order_id` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_track`
--

INSERT INTO `order_track` (`track_id`, `order_id`, `status`, `created_on`) VALUES
(1, 'OS_1_1709195417', 1, '2024-02-29 14:00:17'),
(2, 'OS_1_1709196147', 1, '2024-02-29 14:12:27'),
(3, 'OS_1_1709196147', 5, '2024-02-29 14:14:21'),
(4, 'OS_1_1709196147', 6, '2024-02-29 14:14:53'),
(5, 'OS_1_1709195417', 2, '2024-02-29 14:24:52'),
(6, 'OS_1_1709195417', 3, '2024-02-29 14:25:02'),
(7, 'OS_1_1709195417', 4, '2024-02-29 14:25:07'),
(8, 'OS_1_1709195417', 5, '2024-02-29 14:26:19'),
(9, 'OS_1_1709195417', 6, '2024-02-29 14:26:26'),
(10, 'OS_1_1709197165', 1, '2024-02-29 14:29:25'),
(11, 'OS_1_1709197165', 5, '2024-02-29 14:30:17'),
(12, 'OS_1_1709197165', 6, '2024-02-29 14:30:25'),
(13, 'OS_1_1709197165', 6, '2024-02-29 16:13:13'),
(14, 'OS_1_1709197165', 6, '2024-02-29 16:15:54'),
(15, 'OS_1_1709197165', 6, '2024-02-29 16:20:08'),
(16, 'OS_1_1709197165', 6, '2024-02-29 16:24:55'),
(17, 'OS_1_1709382890', 1, '2024-03-02 18:04:50'),
(18, 'OS_1_1709455633', 1, '2024-03-03 14:17:13'),
(19, 'OS_1_1709382890', 7, '2024-03-04 16:45:23'),
(20, 'OS_1_1709624562', 1, '2024-03-05 13:12:42'),
(21, 'OS_1_1709633110', 1, '2024-03-05 15:35:10'),
(22, 'OS_1_1709633304', 1, '2024-03-05 15:38:24'),
(23, 'OS_1_1709633304', 5, '2024-03-05 15:40:10'),
(24, 'OS_1_1709633304', 6, '2024-03-05 15:40:41'),
(25, 'OS_1_1709633110', 2, '2024-03-05 15:52:40'),
(26, 'OS_1_1709633110', 3, '2024-03-05 15:53:30'),
(27, 'OS_1_1709633110', 4, '2024-03-05 15:57:24'),
(28, 'OS_1_1709633110', 5, '2024-03-05 15:59:20'),
(29, 'OS_1_1709633110', 6, '2024-03-05 15:59:43'),
(30, 'OS_1_1710225250', 1, '2024-03-12 12:04:10'),
(31, 'OS_1_1710225582', 1, '2024-03-12 12:09:42'),
(32, 'OS_1_1710225616', 1, '2024-03-12 12:10:16'),
(33, 'OS_1_1710225616', 5, '2024-03-12 12:10:23'),
(34, 'OS_1_1710225616', 6, '2024-03-12 12:10:48'),
(35, 'OS_1_1710446587', 1, '2024-03-15 01:33:07'),
(36, 'OS_1_1710446715', 1, '2024-03-15 01:35:15'),
(37, 'OS_1_1710446969', 1, '2024-03-15 01:39:29'),
(38, 'OS_1_1710446969', 5, '2024-03-15 01:39:42'),
(39, 'OS_1_1710446969', 6, '2024-03-15 01:40:06'),
(40, 'OS_1_1710447298', 1, '2024-03-15 01:44:58'),
(41, 'OS_1_1710447484', 1, '2024-03-15 01:48:04'),
(42, 'OS_1_1710447484', 5, '2024-03-15 01:49:50'),
(43, 'OS_1_1710447651', 1, '2024-03-15 01:50:51'),
(44, 'OS_1_1710447651', 5, '2024-03-15 01:51:35'),
(45, 'OS_1_1710865113', 1, '2024-03-19 21:48:33'),
(46, 'OS_1_1711023482', 1, '2024-03-21 17:48:02'),
(47, 'OS_1_1711177991', 1, '2024-03-23 12:43:11');

-- --------------------------------------------------------

--
-- Table structure for table `other_employees`
--

CREATE TABLE `other_employees` (
  `other_employee_id` int(11) NOT NULL,
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
  `os_store_id` int(11) NOT NULL,
  `os_store_name` varchar(255) DEFAULT NULL,
  `os_store_display_name` varchar(255) DEFAULT NULL,
  `os_store_phone` varchar(255) DEFAULT NULL,
  `os_store_gst` varchar(255) DEFAULT NULL,
  `os_store_email` varchar(255) DEFAULT NULL,
  `os_store_city` varchar(255) DEFAULT NULL,
  `os_store_state` varchar(255) DEFAULT NULL,
  `os_store_zip` varchar(255) DEFAULT NULL,
  `os_store_lat` double DEFAULT NULL,
  `os_store_lng` double DEFAULT NULL,
  `os_store_address` varchar(255) DEFAULT NULL,
  `os_status` int(11) DEFAULT NULL,
  `os_created_by` int(11) DEFAULT NULL,
  `os_created_on` datetime DEFAULT NULL,
  `os_last_updated_by` int(11) DEFAULT NULL,
  `os_last_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store`
--

INSERT INTO `own_store` (`os_store_id`, `os_store_name`, `os_store_display_name`, `os_store_phone`, `os_store_gst`, `os_store_email`, `os_store_city`, `os_store_state`, `os_store_zip`, `os_store_lat`, `os_store_lng`, `os_store_address`, `os_status`, `os_created_by`, `os_created_on`, `os_last_updated_by`, `os_last_updated_on`) VALUES
(1, 'OwnStore1', 'OwnStore1', '08792103812', '26AATCA501G1Z11', 'ownstore123@gmail.com', 'banglore', 'karnataka', '111111', 13.1006804, 77.39045519999999, 'Indolens, Indolens Solutions Pvt Ltd, BH Road, Jyothi Nagar, Nelamangala Town, Karnataka, India', 1, 1, '2024-02-29 13:00:32', 1, '2024-03-23 13:11:07'),
(2, 'OwnStore2', 'OwnStore2', '8792103814', '26AATCA501G1Z12', 'ownstore124@gmail.com', 'chennai', 'tamil nadu', '111234', 13.0826802, 80.2707184, 'Chennai, Tamil Nadu', 1, 1, '2024-02-29 13:02:11', 1, '2024-02-29 13:02:11'),
(3, 'OwnStore3', 'OwnStore3', '8792103815', '26AATCA501G1Z14', 'ownstore125@gmail.com', 'Shivmogga', 'Karnataka', '123456', 14.1670402, 75.0403, 'Sagara, Shivmogga', 1, 1, '2024-02-29 13:03:45', 1, '2024-02-29 13:03:45'),
(4, 'INDOLENS OWN STORE 01', 'INDOLENS OWN STORE 01', '3456788874', 'tfjghjkfcghbggg', 'devsandy12@gmail.com', 'bangalore', 'Karnataka', '560057', 13.0524556, 77.4697055, 'No.23, Hessargatta road ,AGBG layout,chikkasandra bengaluru', 1, 1, '2024-03-15 01:26:47', 1, '2024-03-15 01:26:47'),
(5, 'indolens ownstore 09', 'xxxx store', '9089098789', 'GSTIN00124FR', 'rooprajt@gmail.com', 'Bangalore', 'Karnataka', '560058', 13.097301, 77.38563979999999, '4rd Cross\r\n#A148', 1, 1, '2024-03-23 17:26:34', 1, '2024-03-23 17:26:34');

-- --------------------------------------------------------

--
-- Table structure for table `own_store_employees`
--

CREATE TABLE `own_store_employees` (
  `ose_employee_id` int(11) NOT NULL,
  `ose_name` varchar(255) DEFAULT NULL,
  `ose_email` varchar(255) DEFAULT NULL,
  `ose_phone` varchar(255) DEFAULT NULL,
  `ose_password` varchar(255) DEFAULT NULL,
  `ose_profile_pic` varchar(255) DEFAULT NULL,
  `ose_assigned_store_id` int(11) DEFAULT NULL,
  `ose_address` varchar(255) DEFAULT NULL,
  `ose_document_1_type` varchar(255) DEFAULT NULL,
  `ose_document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ose_document_2_type` varchar(255) DEFAULT NULL,
  `ose_document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `ose_status` int(11) DEFAULT NULL,
  `ose_role` int(11) DEFAULT NULL,
  `ose_created_by` int(11) DEFAULT NULL,
  `ose_created_on` datetime DEFAULT NULL,
  `ose_last_updated_by` int(11) DEFAULT NULL,
  `ose_last_updated_on` datetime DEFAULT NULL,
  `ose_certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `own_store_employees`
--

INSERT INTO `own_store_employees` (`ose_employee_id`, `ose_name`, `ose_email`, `ose_phone`, `ose_password`, `ose_profile_pic`, `ose_assigned_store_id`, `ose_address`, `ose_document_1_type`, `ose_document_1_url`, `ose_document_2_type`, `ose_document_2_url`, `ose_status`, `ose_role`, `ose_created_by`, `ose_created_on`, `ose_last_updated_by`, `ose_last_updated_on`, `ose_certificates`) VALUES
(1, 'Tom Cruze', 'devsandy12@gmail.com', '8792103813', '$2b$12$BS2wyKae3o5tOMGekjCSRu69oiYikRWBhFV8PFO51o16q0znwbFi6', 'profile_pic/profilePic_1709192662_person1.jpg', 3, 'Peenya, Banglore', 'Aadhar', '[\"documents/document1_1709192662_aadhar.jpg\"]', 'Pan Card', '[\"documents/document2_1709192662_pan.png\"]', 1, 1, 1, '2024-02-29 13:14:22', 1, '2024-02-29 13:14:22', NULL),
(2, 'Deeraj', 'smitharaj0703@gmail.com', '08792103813', '$2b$12$yx9BIHlrrADjED6MC2590.Cr2c8rmU7r5OmyDR.pOnY9tzpXDtU0q', 'profile_pic/profilePic_1709192751_person2.jpg', 1, 'Rajajinagar, Banglore', 'Aadhar', '[\"documents/document1_1709192751_aadhar.jpg\", \"documents/document1_1709193948_dsrhfghjfdxfghxgdxghgjfxfgyfxcfgygfcvgjhcvghcxvfgcvfgcvfcv.jpeg\", \"documents/document1_1709198239_Design.png\"]', 'Pan Card', '[\"documents/document2_1709192751_pan.png\"]', 1, 1, 1, '2024-02-29 13:15:51', 1, '2024-02-29 14:47:19', NULL),
(3, 'Mary ', 'ownstore123@gmail.com', '08792103814', '$2b$12$b4l24LnzcPAMN9A8/wfhE.RQk5gZuSg9INPCrFKMBnXQRk7ttd/Hq', 'profile_pic/profile_pic_1709192849_person3.jpg', 0, 'Hyderabad, Telangana', 'Aadhar', '[\"documents/documents_1709192849_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709192849_pan.png\"]', 0, 2, 1, '2024-02-29 13:17:30', 1, '2024-02-29 13:17:30', '[\"certificates/certificates_1709192849_pan.png\"]'),
(4, 'Shehanaz', 'rajsmitha723@gmail.com', '8792103815', '$2b$12$QWbHhgMWPe0aGtGtG3wPle0GwEa.jWKmNOu.aZyn9CQfZAcxtoXmO', 'profile_pic/profile_pic_1709192986_person4.jpg', 0, 'Peenya, Banglore', 'Aadhar', '[\"documents/documents_1709192986_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709192986_pan.png\"]', 0, 2, 1, '2024-02-29 13:19:46', 1, '2024-02-29 13:19:46', '[\"certificates/certificates_1709192986_pan.png\"]'),
(5, 'Riyaz', 'devsandy123@gmail.com', '08792103817', '$2b$12$pkd.47aAIVQXWx9gRnWqaukMeHUe7g4E9cADgv.9Pt01sRrgi8qpC', 'profile_pic/profile_pic_1709193071_person1.jpg', 0, 'Chennai, Tamil nadu', 'Aadhar', '[\"documents/documents_1709193071_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193071_pan.png\"]', 0, 3, 1, '2024-02-29 13:21:11', 1, '2024-02-29 13:21:11', NULL),
(7, 'Kavya', 'kavya123@gmail.com', '08792103819', '$2b$12$cZFMW5ncRrBh0Pm8yQHYZef8K5Xi2cY9QgEKxzQ6lxdGdh6SMBClS', 'profile_pic/profile_pic_1709193268_person3.jpg', 0, 'Delhi', 'Aadhar', '[\"documents/documents_1709193268_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193268_pan.png\"]', 0, 3, 1, '2024-02-29 13:24:29', 1, '2024-02-29 13:24:29', NULL),
(8, 'Teresa', 'teresa123@gmail.com', '8792103815', '$2b$12$sPegsH/YnB71sq7hiEtemusZxc7JTVOlpeDyiGH3hZWUV3Ib7y8x6', 'profile_pic/profile_pic_1709193370_person4.jpg', 0, 'Chennai, Tamil nadu', 'Aadhar', '[\"documents/documents_1709193370_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193370_pan.png\"]', 0, 4, 1, '2024-02-29 13:26:11', 1, '2024-02-29 13:26:11', NULL),
(9, 'Ankit Sharma', 'ankit123@gmail.com', '08792103815', '$2b$12$eHYEoT5i8TH7WrrFYmJ.1ORl.MwSRW7z6vFH/FOvilPgdSHJVHd6S', 'profile_pic/profile_pic_1709193454_person2.jpg', 0, 'Peenya, Banglore', 'Aadhar', '[\"documents/documents_1709193454_aadhar.jpg\"]', 'Pan Card', '[\"documents/documents_1709193454_pan.png\"]', 0, 4, 1, '2024-02-29 13:27:35', 1, '2024-02-29 13:27:35', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `product_categories`
--

CREATE TABLE `product_categories` (
  `pc_category_id` int(11) NOT NULL,
  `pc_category_name` varchar(255) DEFAULT NULL,
  `pc_category_prefix` varchar(255) DEFAULT NULL,
  `pc_category_description` varchar(255) DEFAULT NULL,
  `pc_status` tinyint(1) DEFAULT NULL,
  `pc_created_on` datetime DEFAULT NULL,
  `pc_created_by` int(11) DEFAULT NULL,
  `pc_last_updated_on` datetime DEFAULT NULL,
  `pc_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_categories`
--

INSERT INTO `product_categories` (`pc_category_id`, `pc_category_name`, `pc_category_prefix`, `pc_category_description`, `pc_status`, `pc_created_on`, `pc_created_by`, `pc_last_updated_on`, `pc_last_updated_by`) VALUES
(1, 'Frames', 'IND-FR', 'description for frames goes here', 1, '2024-02-29 12:49:37', 1, '2024-02-29 12:49:37', 1),
(2, 'Lens', 'IND-LENS', 'description for lens goes here', 1, '2024-02-29 12:49:37', 1, '2024-02-29 12:49:37', 1),
(3, 'Contact Lens', 'IND-CL', 'description for lens goes here', 1, '2024-02-29 12:49:37', 1, '2024-02-29 12:49:37', 1),
(4, 'Accessories', 'IND-ACC', 'Description for accessories goes here', 0, '2024-02-29 12:58:50', 1, '2024-02-29 12:58:50', 1),
(5, 'ContactLens', 'ContactLens', 'ContactLens', 0, '2024-03-21 18:59:07', 1, '2024-03-21 18:59:07', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_colors`
--

CREATE TABLE `product_colors` (
  `pcol_color_id` int(11) NOT NULL,
  `pcol_color_code` varchar(255) DEFAULT NULL,
  `pcol_color_name` varchar(255) DEFAULT NULL,
  `pcol_color_description` varchar(255) DEFAULT NULL,
  `pcol_status` int(11) DEFAULT NULL,
  `pcol_created_on` datetime DEFAULT NULL,
  `pcol_created_by` int(11) DEFAULT NULL,
  `pcol_last_updated_on` datetime DEFAULT NULL,
  `pcol_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_colors`
--

INSERT INTO `product_colors` (`pcol_color_id`, `pcol_color_code`, `pcol_color_name`, `pcol_color_description`, `pcol_status`, `pcol_created_on`, `pcol_created_by`, `pcol_last_updated_on`, `pcol_last_updated_by`) VALUES
(1, 'C1', 'Metallic grey', 'h', 1, '2024-02-29 13:00:08', 1, '2024-02-29 13:00:08', 1),
(2, 'C2', 'Black', 'fghj', 0, '2024-02-29 13:00:16', 1, '2024-02-29 13:00:16', 1),
(3, 'test dict update', 'test dict update', 'test dict update', 0, '2024-03-28 13:52:18', 1, '2024-03-28 13:53:26', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_materials`
--

CREATE TABLE `product_materials` (
  `pm_material_id` int(11) NOT NULL,
  `pm_material_name` varchar(255) DEFAULT NULL,
  `pm_material_description` varchar(255) DEFAULT NULL,
  `pm_status` int(11) DEFAULT NULL,
  `pm_created_on` datetime DEFAULT NULL,
  `pm_created_by` int(11) DEFAULT NULL,
  `pm_last_updated_on` datetime DEFAULT NULL,
  `pm_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_materials`
--

INSERT INTO `product_materials` (`pm_material_id`, `pm_material_name`, `pm_material_description`, `pm_status`, `pm_created_on`, `pm_created_by`, `pm_last_updated_on`, `pm_last_updated_by`) VALUES
(1, 'Metal', 'gh', 0, '2024-02-29 13:00:23', 1, '2024-02-29 13:00:23', 1),
(2, 'Shell', 'ghj', 1, '2024-02-29 13:00:34', 1, '2024-02-29 13:00:34', 1),
(4, 'test dict update', 'test dict update', 0, '2024-03-28 19:04:52', 1, '2024-03-28 19:11:15', 1);

-- --------------------------------------------------------

--
-- Table structure for table `request_products`
--

CREATE TABLE `request_products` (
  `pr_request_products_id` int(11) NOT NULL,
  `pr_store_id` int(11) DEFAULT NULL,
  `pr_store_type` int(11) DEFAULT NULL,
  `pr_product_id` int(11) DEFAULT NULL,
  `pr_product_quantity` int(11) DEFAULT NULL,
  `pr_unit_cost` int(11) DEFAULT NULL,
  `pr_request_status` int(11) DEFAULT NULL,
  `pr_delivery_status` int(11) DEFAULT NULL,
  `pr_is_requested` tinyint(1) DEFAULT NULL,
  `pr_request_to_store_id` int(11) DEFAULT NULL,
  `pr_payment_status` int(11) DEFAULT NULL,
  `pr_comment` varchar(255) DEFAULT NULL,
  `pr_created_on` datetime DEFAULT NULL,
  `pr_created_by` int(11) DEFAULT NULL,
  `pr_last_updated_on` datetime DEFAULT NULL,
  `pr_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `request_products`
--

INSERT INTO `request_products` (`pr_request_products_id`, `pr_store_id`, `pr_store_type`, `pr_product_id`, `pr_product_quantity`, `pr_unit_cost`, `pr_request_status`, `pr_delivery_status`, `pr_is_requested`, `pr_request_to_store_id`, `pr_payment_status`, `pr_comment`, `pr_created_on`, `pr_created_by`, `pr_last_updated_on`, `pr_last_updated_by`) VALUES
(1, 1, 1, 1, 10, 900, 1, 2, 0, 0, 0, 'Enjoy', '2024-02-29 13:38:19', 1, '2024-02-29 13:38:19', 1),
(2, 1, 1, 2, 10, 900, 1, 2, 0, 0, 0, 'enjoy', '2024-02-29 13:40:44', 1, '2024-02-29 13:40:44', 1),
(3, 1, 1, 2, -4, 900, 2, 3, 1, 0, 0, 'invalid qty\r\n', '2024-02-29 13:42:28', 2, '2024-02-29 13:45:38', 1),
(4, 1, 1, 2, -5, 900, 2, 3, 1, 0, 0, 'This is to test the rejection comment on the table view', '2024-02-29 13:43:51', 2, '2024-02-29 13:45:48', 1),
(5, 1, 1, 2, 2, 900, 1, 2, 1, 0, 0, NULL, '2024-02-29 13:45:26', 2, '2024-02-29 13:45:53', 1),
(6, 2, 1, 1, 3, 900, 1, 1, 0, 0, 0, 'gfh', '2024-03-05 10:57:06', 1, '2024-03-05 10:57:06', 1),
(7, 3, 1, 1, 4, 900, 1, 2, 0, 0, 0, 'DFGHJ\r\n', '2024-03-05 10:57:19', 1, '2024-03-05 10:57:19', 1),
(8, 3, 1, 1, 10, 900, 1, 2, 0, 0, 0, 'hg', '2024-03-05 13:46:39', 1, '2024-03-05 13:46:39', 1),
(9, 3, 1, 2, 10, 900, 1, 2, 0, 0, 0, 'ghjj', '2024-03-05 13:49:24', 1, '2024-03-05 13:49:24', 1),
(10, 1, 1, 2, 10, 900, 1, 2, 0, 0, 0, 'o', '2024-03-05 14:13:53', 1, '2024-03-05 14:13:53', 1),
(11, 1, 1, 2, 5, 900, 2, 3, 1, 0, 0, 'lol', '2024-03-14 13:53:07', 2, '2024-03-14 13:53:21', 1),
(12, 1, 1, 2, 2, 900, 2, 3, 1, 0, 0, 'werf', '2024-03-14 13:53:44', 2, '2024-03-14 13:53:52', 1),
(13, 1, 1, 2, 3, 900, 2, 3, 1, 0, 0, 'edfv', '2024-03-14 13:54:53', 2, '2024-03-14 13:55:09', 1),
(14, 4, 1, 1, 10, 900, 1, 1, 0, 0, 0, 'hg', '2024-03-20 01:08:07', 1, '2024-03-20 01:08:07', 1),
(15, 4, 1, 1, 63, 900, 1, 1, 0, 0, 0, 'gf', '2024-03-20 01:20:21', 1, '2024-03-20 01:20:21', 1),
(16, 1, 1, 1, 85, 900, 1, 2, 0, 0, 0, 'test', '2024-03-21 17:58:22', 1, '2024-03-21 17:58:22', 1),
(17, 1, 2, 1, 2, 900, 1, 2, 0, 0, 0, 'test invoice', '2024-03-22 17:11:41', 1, '2024-03-22 17:11:41', 1);

-- --------------------------------------------------------

--
-- Table structure for table `reset_password`
--

CREATE TABLE `reset_password` (
  `rpwd_reset_password_id` int(11) NOT NULL,
  `rpwd_email` varchar(255) DEFAULT NULL,
  `rpwd_code` varchar(255) DEFAULT NULL,
  `rpwd_status` int(11) DEFAULT NULL,
  `rpwd_created_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reset_password`
--

INSERT INTO `reset_password` (`rpwd_reset_password_id`, `rpwd_email`, `rpwd_code`, `rpwd_status`, `rpwd_created_on`) VALUES
(1, 'smitharaj0703@gmail.com', 'gt2HXpadCeAhtSt0', 1, '2024-03-04 16:03:11'),
(2, 'accelstack@gmail.com', 'OkQFUjMkZ3NfY97J', 1, '2024-03-04 16:03:29'),
(3, 'devsandy12@gmail.com', 'NFDjSDaKgC9xSWcI', 0, '2024-03-04 16:04:15'),
(4, 'smitharaj0703@gmail.com', 'avQrDQPF7h6noweL', 1, '2024-03-04 16:05:34'),
(5, 'smitharaj0703@gmail.com', 'DkaiyRVjJFlw5NTz', 1, '2024-03-04 16:13:19'),
(6, 'accelstack@gmail.com', '8FkPCkdLY6qpeUCb', 1, '2024-03-04 16:14:24'),
(7, 'smitharaj0703@gmail.com', 'VCa8qabIRyYYuhJi', 1, '2024-03-04 16:17:22'),
(8, 'accelstack@gmail.com', 'fT3m3qJHxAPreGVD', 0, '2024-03-23 14:18:21'),
(9, 'accelstack@gmail.com', 'AQbP97b8fBgIfFVE', 0, '2024-03-23 14:19:31'),
(10, 'accelstack@gmail.com', 'wgejzlTOcHdkBUEy', 0, '2024-03-23 14:21:19');

-- --------------------------------------------------------

--
-- Table structure for table `sales_executive`
--

CREATE TABLE `sales_executive` (
  `sales_executive_id` int(11) NOT NULL,
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
  `so_sale_item_id` int(11) NOT NULL,
  `so_order_id` varchar(255) DEFAULT NULL,
  `so_product_id` int(11) DEFAULT NULL,
  `so_hsn` varchar(255) DEFAULT NULL,
  `so_unit_sale_price` int(11) DEFAULT NULL,
  `so_unit_type` varchar(255) DEFAULT NULL,
  `so_purchase_quantity` int(11) DEFAULT NULL,
  `so_product_total_cost` int(11) DEFAULT NULL,
  `so_discount_percentage` int(11) DEFAULT NULL,
  `so_is_discount_applied` int(11) DEFAULT NULL,
  `so_power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `so_assigned_lab` int(11) DEFAULT NULL,
  `so_customer_id` int(11) DEFAULT NULL,
  `so_order_status` int(11) DEFAULT NULL,
  `so_payment_status` int(11) DEFAULT NULL,
  `so_delivery_status` int(11) DEFAULT NULL,
  `so_payment_mode` int(11) DEFAULT NULL,
  `so_amount_paid` int(11) DEFAULT NULL,
  `so_estimated_delivery_date` date DEFAULT NULL,
  `so_linked_item` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `so_sales_note` longtext DEFAULT NULL,
  `so_created_by_store` int(11) DEFAULT NULL,
  `so_created_by_store_type` int(11) DEFAULT NULL,
  `so_created_by` int(11) DEFAULT NULL,
  `so_created_on` datetime DEFAULT NULL,
  `so_updated_by` int(11) DEFAULT NULL,
  `so_updated_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales_order`
--

INSERT INTO `sales_order` (`so_sale_item_id`, `so_order_id`, `so_product_id`, `so_hsn`, `so_unit_sale_price`, `so_unit_type`, `so_purchase_quantity`, `so_product_total_cost`, `so_discount_percentage`, `so_is_discount_applied`, `so_power_attribute`, `so_assigned_lab`, `so_customer_id`, `so_order_status`, `so_payment_status`, `so_delivery_status`, `so_payment_mode`, `so_amount_paid`, `so_estimated_delivery_date`, `so_linked_item`, `so_sales_note`, `so_created_by_store`, `so_created_by_store_type`, `so_created_by`, `so_created_on`, `so_updated_by`, `so_updated_on`) VALUES
(1, 'OS_1_1709195417', 1, '01', 1400, 'Pair', 1, 700, 50, 1, '{}', 1, 1, 6, 1, 1, 1, 1, '2024-03-03', NULL, 'test', 1, 1, 2, '2024-02-29 14:00:17', 2, '2024-02-29 14:00:17'),
(2, 'OS_1_1709195417', 4, '04', 600, 'Pair', 1, 540, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"2\", \"leftLensCylRx\": \"2\", \"leftLensAxisRx\": \"2\", \"leftLensAddRx\": \"2\", \"leftLensPdRx\": \"2\", \"rightLensSphRx\": \"2\", \"rightLensCylRx\": \"22\", \"rightLensAxisRx\": \"2\", \"rightLensAddRx\": \"2\", \"rightLensPdRx\": \"2\"}', 1, 1, 6, 1, 1, 1, 1, '2024-03-03', NULL, 'test', 1, 1, 2, '2024-02-29 14:00:17', 2, '2024-02-29 14:00:17'),
(3, 'OS_1_1709195417', 3, '07', 250, 'Single', 1, 225, 10, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"1\", \"leftLensCylStock\": \"1\", \"leftLensAxisStock\": \"1\", \"leftLensAddStock\": \"1\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"1\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 1, 1, 6, 1, 1, 1, 1, '2024-03-03', NULL, 'test', 1, 1, 2, '2024-02-29 14:00:17', 2, '2024-02-29 14:00:17'),
(4, 'OS_1_1709195417', 6, '097', 2000, 'Pair', 1, 1820, 9, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"\", \"contact_lens_disposability\": \"\", \"power\": \"\", \"bc\": \"\", \"dia\": \"\", \"cyl\": \"\", \"axis\": \"\"}', 1, 1, 6, 1, 1, 1, 1, '2024-03-03', NULL, 'test', 1, 1, 2, '2024-02-29 14:00:17', 2, '2024-02-29 14:00:17'),
(5, 'OS_1_1709196147', 1, '01', 1400, 'Pair', 1, 700, 50, 1, '{}', 0, 1, 6, 2, 1, 1, 700, '2024-03-03', NULL, 'nice', 1, 1, 2, '2024-02-29 14:12:27', 2, '2024-02-29 14:12:27'),
(6, 'OS_1_1709197165', 1, '01', 1400, 'Pair', 1, 700, 50, 1, '{}', 0, 1, 6, 2, 1, 1, 1240, '2024-03-03', NULL, 'test', 1, 2, 2, '2024-02-29 14:29:25', 2, '2024-02-29 14:29:25'),
(7, 'OS_1_1709197165', 4, '04', 600, 'Pair', 1, 540, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"2\", \"leftLensCylRx\": \"2\", \"leftLensAxisRx\": \"2\", \"leftLensAddRx\": \"2\", \"leftLensPdRx\": \"2\", \"rightLensSphRx\": \"2\", \"rightLensCylRx\": \"2\", \"rightLensAxisRx\": \"2\", \"rightLensAddRx\": \"2\", \"rightLensPdRx\": \"2\"}', 0, 1, 6, 2, 1, 1, 1240, '2024-03-03', NULL, 'test', 1, 2, 2, '2024-02-29 14:29:25', 2, '2024-02-29 14:29:25'),
(8, 'OS_1_1709382890', 1, '01', 1400, 'Pair', 3, 4200, 50, 1, '{}', 1, 1, 7, 2, 1, 1, 5400, '2024-03-05', NULL, 'hello', 1, 1, 2, '2024-03-02 18:04:50', 2, '2024-03-02 18:04:50'),
(9, 'OS_1_1709382890', 4, '04', 600, 'Pair', 2, 1200, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"2\", \"leftLensCylRx\": \"2\", \"leftLensAxisRx\": \"2\", \"leftLensAddRx\": \"2\", \"leftLensPdRx\": \"2\", \"rightLensSphRx\": \"2\", \"rightLensCylRx\": \"2\", \"rightLensAxisRx\": \"2\", \"rightLensAddRx\": \"2\", \"rightLensPdRx\": \"2\"}', 1, 1, 7, 2, 1, 1, 5400, '2024-03-05', NULL, 'hello', 1, 1, 2, '2024-03-02 18:04:50', 2, '2024-03-02 18:04:50'),
(10, 'OS_1_1709455633', 4, '04', 600, 'Pair', 1, 600, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"2\", \"leftLensCylRx\": \"2\", \"leftLensAxisRx\": \"2\", \"leftLensAddRx\": \"2\", \"leftLensPdRx\": \"2\", \"rightLensSphRx\": \"2\", \"rightLensCylRx\": \"2\", \"rightLensAxisRx\": \"2\", \"rightLensAddRx\": \"2\", \"rightLensPdRx\": \"2\"}', 1, 1, 7, 3, 1, 1, 0, '2024-03-06', '[1]', 'test', 1, 1, 2, '2024-03-03 14:17:13', 2, '2024-03-03 14:17:13'),
(11, 'OS_1_1709455633', 6, '097', 2000, 'Pair', 1, 2000, 9, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"3 Month\", \"power\": \"6\", \"bc\": \"6\", \"dia\": \"6\", \"cyl\": \"6\", \"axis\": \"6\"}', 1, 1, 7, 3, 1, 1, 0, '2024-03-06', NULL, 'test', 1, 1, 2, '2024-03-03 14:17:13', 2, '2024-03-03 14:17:13'),
(12, 'OS_1_1709455633', 1, '01', 1400, 'Pair', 1, 700, 50, 1, '{}', 1, 1, 7, 3, 1, 1, 0, '2024-03-06', NULL, 'test', 1, 1, 2, '2024-03-03 14:17:13', 2, '2024-03-03 14:17:13'),
(13, 'OS_1_1709624562', 3, '07', 250, 'Single', 5, 1125, 10, 1, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"1\", \"leftLensCylStock\": \"1\", \"leftLensAxisStock\": \"1\", \"leftLensAddStock\": \"1\", \"leftLensPdStock\": \"1\", \"rightLensSphStock\": \"1\", \"rightLensCylStock\": \"1\", \"rightLensAxisStock\": \"1\", \"rightLensAddStock\": \"1\", \"rightLensPdStock\": \"1\"}', 2, 1, 7, 3, 1, 1, 0, '2024-03-08', '[1, 1, 1]', 'ok', 1, 1, 2, '2024-03-05 13:12:42', 2, '2024-03-05 13:12:42'),
(14, 'OS_1_1709624562', 6, '097', 2000, 'Pair', 2, 3640, 9, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"3 Month\", \"power\": \"2\", \"bc\": \"2\", \"dia\": \"2\", \"cyl\": \"2\", \"axis\": \"2\"}', 2, 1, 7, 3, 1, 1, 0, '2024-03-08', NULL, 'ok', 1, 1, 2, '2024-03-05 13:12:42', 2, '2024-03-05 13:12:42'),
(15, 'OS_1_1709624562', 1, '01', 1400, 'Pair', 3, 2100, 50, 1, '{}', 2, 1, 7, 3, 1, 1, 0, '2024-03-08', NULL, 'ok', 1, 1, 2, '2024-03-05 13:12:42', 2, '2024-03-05 13:12:42'),
(16, 'OS_1_1709633110', 4, '04', 600, 'Pair', 2, 1200, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"4\", \"leftLensCylRx\": \"4\", \"leftLensAxisRx\": \"4\", \"leftLensAddRx\": \"3\", \"leftLensPdRx\": \"4\", \"rightLensSphRx\": \"65\", \"rightLensCylRx\": \"5\", \"rightLensAxisRx\": \"3\", \"rightLensAddRx\": \"3\", \"rightLensPdRx\": \"3\"}', 1, 8, 6, 1, 1, 1, 100, '2024-03-08', '[2, 2]', 'nothingf', 1, 1, 2, '2024-03-05 15:35:10', 2, '2024-03-05 15:35:10'),
(17, 'OS_1_1709633110', 2, '09', 1200, 'Pair', 2, 2400, 25, 1, '{}', 1, 8, 6, 1, 1, 1, 100, '2024-03-08', NULL, 'nothingf', 1, 1, 2, '2024-03-05 15:35:10', 2, '2024-03-05 15:35:10'),
(18, 'OS_1_1709633304', 2, '09', 1200, 'Pair', 2, 2400, 25, 1, '{}', 0, 8, 6, 1, 1, 1, 0, '2024-03-08', NULL, 'hgjj', 1, 1, 2, '2024-03-05 15:38:24', 2, '2024-03-05 15:38:24'),
(19, 'OS_1_1710225250', 6, '097', 2000, 'Pair', 1, 2000, 9, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"3 Month\", \"power\": \"1\", \"bc\": \"1\", \"dia\": \"1\", \"cyl\": \"1\", \"axis\": \"1\", \"eye\": \"Right\"}', 1, 8, 1, 1, 1, 1, 0, '2024-03-15', NULL, 'sdf', 1, 1, 2, '2024-03-12 12:04:10', 2, '2024-03-12 12:04:10'),
(20, 'OS_1_1710225582', 2, '09', 1200, 'Pair', 1, 1200, 25, 1, '{}', 1, 8, 1, 1, 1, 1, 0, '2024-03-15', NULL, 'r', 1, 1, 2, '2024-03-12 12:09:42', 2, '2024-03-12 12:09:42'),
(21, 'OS_1_1710225616', 2, '09', 1200, 'Pair', 1, 1200, 25, 1, '{}', 0, 8, 6, 2, 1, 1, 1200, '2024-03-15', NULL, 'df', 1, 1, 2, '2024-03-12 12:10:16', 2, '2024-03-12 12:10:16'),
(22, 'OS_1_1710446587', 4, '04', 600, 'Pair', 1, 600, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"56\", \"leftLensCylRx\": \"6\", \"leftLensAxisRx\": \"7\", \"leftLensAddRx\": \"897\", \"leftLensPdRx\": \"90\", \"rightLensSphRx\": \"86434\", \"rightLensCylRx\": \"6\", \"rightLensAxisRx\": \"7\", \"rightLensAddRx\": \"9\", \"rightLensPdRx\": \"764\"}', 1, 8, 1, 1, 1, 1, 0, '2024-03-18', '[]', 'werfg', 1, 1, 2, '2024-03-15 01:33:07', 2, '2024-03-15 01:33:07'),
(23, 'OS_1_1710446715', 4, '04', 600, 'Pair', 2, 1200, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"6\", \"leftLensCylRx\": \"5\", \"leftLensAxisRx\": \"6\", \"leftLensAddRx\": \"89\", \"leftLensPdRx\": \"6\", \"rightLensSphRx\": \"0\", \"rightLensCylRx\": \"7\", \"rightLensAxisRx\": \"5\", \"rightLensAddRx\": \"7\", \"rightLensPdRx\": \"8\"}', 1, 8, 1, 1, 1, 1, 10, '2024-03-18', '[2, 2]', 'fgchj', 1, 1, 2, '2024-03-15 01:35:15', 2, '2024-03-15 01:35:15'),
(24, 'OS_1_1710446715', 2, '09', 1200, 'Pair', 2, 2400, 25, 1, '{}', 1, 8, 1, 1, 1, 1, 10, '2024-03-18', NULL, 'fgchj', 1, 1, 2, '2024-03-15 01:35:15', 2, '2024-03-15 01:35:15'),
(25, 'OS_1_1710446969', 2, '09', 1200, 'Pair', 1, 1200, 25, 1, '{}', 0, 8, 6, 2, 1, 1, 1200, '2024-03-18', NULL, 'wdf', 1, 1, 2, '2024-03-15 01:39:29', 2, '2024-03-15 01:39:29'),
(26, 'OS_1_1710447298', 2, '09', 1200, 'Pair', 1, 1200, 25, 1, '{}', 0, 8, 1, 1, 1, 1, 0, '2024-03-18', NULL, 'dfg', 1, 1, 2, '2024-03-15 01:44:58', 2, '2024-03-15 01:44:58'),
(27, 'OS_1_1710447484', 4, '04', 600, 'Pair', 1, 600, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"7\", \"leftLensCylRx\": \"7\", \"leftLensAxisRx\": \"7\", \"leftLensAddRx\": \"7\", \"leftLensPdRx\": \"7\", \"rightLensSphRx\": \"77\", \"rightLensCylRx\": \"7\", \"rightLensAxisRx\": \"7\", \"rightLensAddRx\": \"7\", \"rightLensPdRx\": \"7\"}', 0, 8, 5, 1, 1, 1, 0, '2024-03-18', '[]', 'fchg', 1, 1, 2, '2024-03-15 01:48:04', 2, '2024-03-15 01:48:04'),
(28, 'OS_1_1710447651', 4, '04', 600, 'Pair', 1, 600, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"4\", \"leftLensCylRx\": \"4\", \"leftLensAxisRx\": \"4\", \"leftLensAddRx\": \"4\", \"leftLensPdRx\": \"4\", \"rightLensSphRx\": \"4\", \"rightLensCylRx\": \"4\", \"rightLensAxisRx\": \"4\", \"rightLensAddRx\": \"4\", \"rightLensPdRx\": \"4\"}', 0, 8, 5, 1, 1, 1, 0, '2024-03-18', '[]', 'fdgg', 1, 1, 2, '2024-03-15 01:50:51', 2, '2024-03-15 01:50:51'),
(29, 'OS_1_1710865113', 2, '09', 1200, 'Pair', 1, 1200, 25, 0, '{}', 0, 8, 1, 1, 1, 1, 0, '2024-03-22', NULL, 'df', 1, 1, 2, '2024-03-19 21:48:33', 2, '2024-03-19 21:48:33'),
(30, 'OS_1_1711023482', 2, '09', 1200, 'Pair', 2, 1800, 25, 1, '{}', 0, 8, 2, 1, 1, 1, 0, '2024-03-24', NULL, 'one with discount and another without discount', 1, 1, 2, '2024-03-21 17:48:02', 2, '2024-03-21 17:48:02'),
(31, 'OS_1_1711023482', 2, '09', 1200, 'Pair', 2, 2400, 0, 0, '{}', 0, 8, 2, 1, 1, 1, 0, '2024-03-24', NULL, 'one with discount and another without discount', 1, 1, 2, '2024-03-21 17:48:02', 2, '2024-03-21 17:48:02'),
(32, 'OS_1_1711177991', 4, '04', 600, 'Pair', 2, 1080, 10, 1, '{\"lens_type\": \"bifocal\", \"stock_type\": \"rx\", \"leftLensSphRx\": \"\", \"leftLensCylRx\": \"3\", \"leftLensAxisRx\": \"8\", \"leftLensAddRx\": \"\", \"leftLensPdRx\": \"1\", \"rightLensSphRx\": \"1.1\", \"rightLensCylRx\": \"\", \"rightLensAxisRx\": \"2\", \"rightLensAddRx\": \"\", \"rightLensPdRx\": \"7\"}', 0, 8, 1, 1, 1, 1, 0, '2024-03-26', '[]', 'test power fields', 1, 1, 2, '2024-03-23 12:43:11', 2, '2024-03-23 12:43:11'),
(33, 'OS_1_1711177991', 3, '07', 250, 'Single', 2, 500, 0, 0, '{\"lens_type\": \"single_vision\", \"stock_type\": \"stock\", \"leftLensSphStock\": \"\", \"leftLensCylStock\": \"\", \"leftLensAxisStock\": \"55\", \"leftLensAddStock\": \"\", \"leftLensPdStock\": \"55\", \"rightLensSphStock\": \"-20.00\", \"rightLensCylStock\": \"\", \"rightLensAxisStock\": \"85\", \"rightLensAddStock\": \"+1.25\", \"rightLensPdStock\": \"\"}', 0, 8, 1, 1, 1, 1, 0, '2024-03-26', '[]', 'test power fields', 1, 1, 2, '2024-03-23 12:43:11', 2, '2024-03-23 12:43:11'),
(34, 'OS_1_1711177991', 6, '097', 2000, 'Pair', 4, 7280, 9, 1, '{\"stock_type\": \"rx\", \"contact_lens_type\": \"Hard\", \"contact_lens_disposability\": \"3 Month\", \"power\": \"1\", \"bc\": \"\", \"dia\": \"2\", \"cyl\": \"\", \"axis\": \"3\", \"eye\": \"Both\"}', 0, 8, 1, 1, 1, 1, 0, '2024-03-26', NULL, 'test power fields', 1, 1, 2, '2024-03-23 12:43:11', 2, '2024-03-23 12:43:11');

-- --------------------------------------------------------

--
-- Table structure for table `sales_order_payment_track`
--

CREATE TABLE `sales_order_payment_track` (
  `sopt_id` int(11) NOT NULL,
  `sopt_order_id` varchar(255) DEFAULT NULL,
  `sopt_payment_amount` int(11) DEFAULT NULL,
  `sopt_payment_mode` int(11) DEFAULT NULL,
  `sopt_payment_type` int(11) DEFAULT NULL,
  `sopt_created_by_store` int(11) DEFAULT NULL,
  `sopt_created_by_store_type` int(11) DEFAULT NULL,
  `sopt_created_by_id` int(11) DEFAULT NULL,
  `sopt_created_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales_order_payment_track`
--

INSERT INTO `sales_order_payment_track` (`sopt_id`, `sopt_order_id`, `sopt_payment_amount`, `sopt_payment_mode`, `sopt_payment_type`, `sopt_created_by_store`, `sopt_created_by_store_type`, `sopt_created_by_id`, `sopt_created_on`) VALUES
(1, 'OS_1_1709195417', 1, 1, 1, 1, 1, 2, '2024-02-29 14:00:17'),
(2, 'OS_1_1709196147', 700, 2, 2, 1, 1, 2, '2024-02-29 14:14:49'),
(3, 'OS_1_1709197165', 1240, 1, 2, 1, 1, 2, '2024-02-29 14:29:59'),
(4, 'OS_1_1709382890', 100, 2, 1, 1, 1, 2, '2024-03-02 18:04:50'),
(5, 'OS_1_1709455633', 1, 2, 1, 1, 1, 2, '2024-03-03 14:17:13'),
(6, 'OS_1_1709455633', 1, 2, 3, 1, 1, 2, '2024-03-04 16:40:08'),
(7, 'OS_1_1709382890', 5300, 1, 2, 1, 1, 2, '2024-03-04 16:46:07'),
(8, 'OS_1_1709624562', 100, 2, 1, 1, 1, 2, '2024-03-05 13:12:42'),
(9, 'OS_1_1709624562', 6765, 2, 2, 1, 1, 2, '2024-03-05 13:16:23'),
(10, 'OS_1_1709624562', 6865, 3, 3, 1, 1, 2, '2024-03-05 13:16:55'),
(11, 'OS_1_1709633110', 100, 2, 1, 1, 1, 2, '2024-03-05 15:35:10'),
(12, 'OS_1_1710225616', 1200, 1, 2, 1, 1, 2, '2024-03-12 12:10:46'),
(13, 'OS_1_1710446715', 10, 3, 1, 1, 1, 2, '2024-03-15 01:35:15'),
(14, 'OS_1_1710446969', 1200, 3, 2, 1, 1, 2, '2024-03-15 01:40:03');

-- --------------------------------------------------------

--
-- Table structure for table `store_expense`
--

CREATE TABLE `store_expense` (
  `se_store_expense_id` int(11) NOT NULL,
  `se_store_id` int(11) DEFAULT NULL,
  `se_store_type` int(11) DEFAULT NULL,
  `se_expense_amount` int(11) DEFAULT NULL,
  `se_expense_reason` varchar(255) DEFAULT NULL,
  `se_expense_date` datetime DEFAULT NULL,
  `se_created_on` datetime DEFAULT NULL,
  `se_created_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_expense`
--

INSERT INTO `store_expense` (`se_store_expense_id`, `se_store_id`, `se_store_type`, `se_expense_amount`, `se_expense_reason`, `se_expense_date`, `se_created_on`, `se_created_by`) VALUES
(1, 1, 2, 1200, 'i dont know', '2024-02-29 13:53:42', '2024-02-29 13:53:42', 2),
(2, 1, 1, 100, 'hgh', '2024-03-20 01:03:25', '2024-03-20 01:03:25', 2),
(3, 1, 1, 100, '89', '2024-03-20 01:03:54', '2024-03-20 01:03:54', 2),
(4, 1, 1, 100, 'ljhv', '2024-03-20 01:04:46', '2024-03-20 01:04:46', 2);

-- --------------------------------------------------------

--
-- Table structure for table `store_inventory`
--

CREATE TABLE `store_inventory` (
  `si_store_inventory_id` int(11) NOT NULL,
  `si_store_id` int(11) DEFAULT NULL,
  `si_store_type` int(11) DEFAULT NULL,
  `si_product_id` int(11) DEFAULT NULL,
  `si_product_quantity` int(11) DEFAULT NULL,
  `si_created_on` datetime DEFAULT NULL,
  `si_created_by` int(11) DEFAULT NULL,
  `si_last_updated_on` datetime DEFAULT NULL,
  `si_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_inventory`
--

INSERT INTO `store_inventory` (`si_store_inventory_id`, `si_store_id`, `si_store_type`, `si_product_id`, `si_product_quantity`, `si_created_on`, `si_created_by`, `si_last_updated_on`, `si_last_updated_by`) VALUES
(1, 2, 1, 1, 10, '2024-02-29 13:40:11', 2, '2024-02-29 13:40:11', 2),
(2, 2, 1, 2, 12, '2024-02-29 13:41:00', 2, '2024-02-29 13:46:27', 2),
(4, 3, 1, 1, 14, '2024-03-05 13:47:46', 1, '2024-03-05 13:47:48', 1),
(6, 3, 1, 2, 10, '2024-03-05 13:49:34', 1, '2024-03-05 13:49:34', 1),
(7, 1, 1, 2, 5, '2024-03-05 14:14:07', 2, '2024-03-05 14:14:07', 2),
(8, 1, 1, 1, 85, '2024-03-21 17:58:40', 2, '2024-03-21 17:58:40', 2),
(9, 1, 2, 1, 2, '2024-03-22 17:11:52', 5, '2024-03-22 17:11:52', 5);

-- --------------------------------------------------------

--
-- Table structure for table `store_manager`
--

CREATE TABLE `store_manager` (
  `store_manager_id` int(11) NOT NULL,
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
  `unit_unit_id` int(11) NOT NULL,
  `unit_name` varchar(255) DEFAULT NULL,
  `unit_status` int(11) DEFAULT NULL,
  `unit_created_on` datetime DEFAULT NULL,
  `unit_created_by` int(11) DEFAULT NULL,
  `unit_last_updated_on` datetime DEFAULT NULL,
  `unit_last_updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `units`
--

INSERT INTO `units` (`unit_unit_id`, `unit_name`, `unit_status`, `unit_created_on`, `unit_created_by`, `unit_last_updated_on`, `unit_last_updated_by`) VALUES
(1, 'Pair', 1, '2024-02-29 13:00:42', 1, '2024-02-29 13:00:42', 1),
(2, 'Single', 0, '2024-02-29 13:00:46', 1, '2024-02-29 13:00:46', 1),
(3, 'Pack', 1, '2024-02-29 13:01:07', 1, '2024-02-29 13:01:07', 1),
(8, 'dict test update', 0, '2024-03-28 19:13:58', 1, '2024-03-28 19:14:12', 1);

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
  ADD PRIMARY KEY (`admin_admin_id`),
  ADD UNIQUE KEY `unique_email_admin` (`admin_email`);

--
-- Indexes for table `admin_setting`
--
ALTER TABLE `admin_setting`
  ADD PRIMARY KEY (`setting_id`);

--
-- Indexes for table `area_head`
--
ALTER TABLE `area_head`
  ADD PRIMARY KEY (`ah_area_head_id`),
  ADD UNIQUE KEY `unique_email_area_head` (`ah_email`);

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`brand_brand_id`),
  ADD UNIQUE KEY `unique_brand_name` (`brand_name`);

--
-- Indexes for table `central_inventory`
--
ALTER TABLE `central_inventory`
  ADD PRIMARY KEY (`ci_product_id`);

--
-- Indexes for table `central_inventory_restock_log`
--
ALTER TABLE `central_inventory_restock_log`
  ADD PRIMARY KEY (`cirl_restock_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_customer_id`),
  ADD UNIQUE KEY `unique_phone` (`customer_phone`);

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
  ADD PRIMARY KEY (`et_eye_test_id`);

--
-- Indexes for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  ADD PRIMARY KEY (`fshape_shape_id`),
  ADD UNIQUE KEY `unique_shape_name` (`fshape_name`);

--
-- Indexes for table `frame_types`
--
ALTER TABLE `frame_types`
  ADD PRIMARY KEY (`ftype_frame_id`),
  ADD UNIQUE KEY `unique_frame_type_name` (`ftype_name`);

--
-- Indexes for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  ADD PRIMARY KEY (`franchise_owner_id`);

--
-- Indexes for table `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD PRIMARY KEY (`fs_store_id`);

--
-- Indexes for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  ADD PRIMARY KEY (`fse_employee_id`),
  ADD UNIQUE KEY `unique_email` (`fse_email`),
  ADD UNIQUE KEY `unique_email_franchise` (`fse_email`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoice_invoice_id`),
  ADD UNIQUE KEY `unique_order_id` (`invoice_order_id`);

--
-- Indexes for table `lab`
--
ALTER TABLE `lab`
  ADD PRIMARY KEY (`lab_lab_id`);

--
-- Indexes for table `lab_technician`
--
ALTER TABLE `lab_technician`
  ADD PRIMARY KEY (`lt_lab_technician_id`),
  ADD UNIQUE KEY `unique_email_lab_technician` (`lt_email`);

--
-- Indexes for table `marketing_head`
--
ALTER TABLE `marketing_head`
  ADD PRIMARY KEY (`mh_marketing_head_id`),
  ADD UNIQUE KEY `unique_email_marketing_head` (`mh_email`);

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
  ADD PRIMARY KEY (`os_store_id`);

--
-- Indexes for table `own_store_employees`
--
ALTER TABLE `own_store_employees`
  ADD PRIMARY KEY (`ose_employee_id`),
  ADD UNIQUE KEY `unique_email` (`ose_email`);

--
-- Indexes for table `product_categories`
--
ALTER TABLE `product_categories`
  ADD PRIMARY KEY (`pc_category_id`),
  ADD UNIQUE KEY `unique_category_name_prefix` (`pc_category_name`,`pc_category_prefix`);

--
-- Indexes for table `product_colors`
--
ALTER TABLE `product_colors`
  ADD PRIMARY KEY (`pcol_color_id`),
  ADD UNIQUE KEY `unique_color_code_name` (`pcol_color_code`,`pcol_color_name`);

--
-- Indexes for table `product_materials`
--
ALTER TABLE `product_materials`
  ADD PRIMARY KEY (`pm_material_id`),
  ADD UNIQUE KEY `unique_material_name` (`pm_material_name`);

--
-- Indexes for table `request_products`
--
ALTER TABLE `request_products`
  ADD PRIMARY KEY (`pr_request_products_id`);

--
-- Indexes for table `reset_password`
--
ALTER TABLE `reset_password`
  ADD PRIMARY KEY (`rpwd_reset_password_id`);

--
-- Indexes for table `sales_executive`
--
ALTER TABLE `sales_executive`
  ADD PRIMARY KEY (`sales_executive_id`);

--
-- Indexes for table `sales_order`
--
ALTER TABLE `sales_order`
  ADD PRIMARY KEY (`so_sale_item_id`);

--
-- Indexes for table `sales_order_payment_track`
--
ALTER TABLE `sales_order_payment_track`
  ADD PRIMARY KEY (`sopt_id`);

--
-- Indexes for table `store_expense`
--
ALTER TABLE `store_expense`
  ADD PRIMARY KEY (`se_store_expense_id`);

--
-- Indexes for table `store_inventory`
--
ALTER TABLE `store_inventory`
  ADD PRIMARY KEY (`si_store_inventory_id`),
  ADD UNIQUE KEY `store_product_unique` (`si_store_id`,`si_store_type`,`si_product_id`);

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
  ADD PRIMARY KEY (`unit_unit_id`),
  ADD UNIQUE KEY `unique_unit_name` (`unit_name`);

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
  MODIFY `admin_admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `admin_setting`
--
ALTER TABLE `admin_setting`
  MODIFY `setting_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `area_head`
--
ALTER TABLE `area_head`
  MODIFY `ah_area_head_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `brand_brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `central_inventory`
--
ALTER TABLE `central_inventory`
  MODIFY `ci_product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `central_inventory_restock_log`
--
ALTER TABLE `central_inventory_restock_log`
  MODIFY `cirl_restock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `eye_test`
--
ALTER TABLE `eye_test`
  MODIFY `et_eye_test_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `frame_shapes`
--
ALTER TABLE `frame_shapes`
  MODIFY `fshape_shape_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `frame_types`
--
ALTER TABLE `frame_types`
  MODIFY `ftype_frame_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `franchise_owner`
--
ALTER TABLE `franchise_owner`
  MODIFY `franchise_owner_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `franchise_store`
--
ALTER TABLE `franchise_store`
  MODIFY `fs_store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `franchise_store_employees`
--
ALTER TABLE `franchise_store_employees`
  MODIFY `fse_employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoice_invoice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `lab`
--
ALTER TABLE `lab`
  MODIFY `lab_lab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lab_technician`
--
ALTER TABLE `lab_technician`
  MODIFY `lt_lab_technician_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `marketing_head`
--
ALTER TABLE `marketing_head`
  MODIFY `mh_marketing_head_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `optimetry`
--
ALTER TABLE `optimetry`
  MODIFY `optimetry_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_track`
--
ALTER TABLE `order_track`
  MODIFY `track_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `other_employees`
--
ALTER TABLE `other_employees`
  MODIFY `other_employee_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `own_store`
--
ALTER TABLE `own_store`
  MODIFY `os_store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `own_store_employees`
--
ALTER TABLE `own_store_employees`
  MODIFY `ose_employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `product_categories`
--
ALTER TABLE `product_categories`
  MODIFY `pc_category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `product_colors`
--
ALTER TABLE `product_colors`
  MODIFY `pcol_color_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `product_materials`
--
ALTER TABLE `product_materials`
  MODIFY `pm_material_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `request_products`
--
ALTER TABLE `request_products`
  MODIFY `pr_request_products_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `reset_password`
--
ALTER TABLE `reset_password`
  MODIFY `rpwd_reset_password_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `sales_executive`
--
ALTER TABLE `sales_executive`
  MODIFY `sales_executive_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_order`
--
ALTER TABLE `sales_order`
  MODIFY `so_sale_item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `sales_order_payment_track`
--
ALTER TABLE `sales_order_payment_track`
  MODIFY `sopt_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `store_expense`
--
ALTER TABLE `store_expense`
  MODIFY `se_store_expense_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `store_inventory`
--
ALTER TABLE `store_inventory`
  MODIFY `si_store_inventory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `store_manager`
--
ALTER TABLE `store_manager`
  MODIFY `store_manager_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `units`
--
ALTER TABLE `units`
  MODIFY `unit_unit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
