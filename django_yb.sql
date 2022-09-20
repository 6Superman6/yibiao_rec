/*
 Navicat Premium Data Transfer

 Source Server         : sc
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : django_yb

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 19/09/2022 09:49:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 44 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add admin', 7, 'add_admin');
INSERT INTO `auth_permission` VALUES (26, 'Can change admin', 7, 'change_admin');
INSERT INTO `auth_permission` VALUES (27, 'Can delete admin', 7, 'delete_admin');
INSERT INTO `auth_permission` VALUES (28, 'Can view admin', 7, 'view_admin');
INSERT INTO `auth_permission` VALUES (29, 'Can add yibiao', 8, 'add_yibiao');
INSERT INTO `auth_permission` VALUES (30, 'Can change yibiao', 8, 'change_yibiao');
INSERT INTO `auth_permission` VALUES (31, 'Can delete yibiao', 8, 'delete_yibiao');
INSERT INTO `auth_permission` VALUES (32, 'Can view yibiao', 8, 'view_yibiao');
INSERT INTO `auth_permission` VALUES (33, 'Can add imgtemplate', 9, 'add_imgtemplate');
INSERT INTO `auth_permission` VALUES (34, 'Can change imgtemplate', 9, 'change_imgtemplate');
INSERT INTO `auth_permission` VALUES (35, 'Can delete imgtemplate', 9, 'delete_imgtemplate');
INSERT INTO `auth_permission` VALUES (36, 'Can view imgtemplate', 9, 'view_imgtemplate');
INSERT INTO `auth_permission` VALUES (37, 'Can add img ocr rec', 10, 'add_imgocrrec');
INSERT INTO `auth_permission` VALUES (38, 'Can change img ocr rec', 10, 'change_imgocrrec');
INSERT INTO `auth_permission` VALUES (39, 'Can delete img ocr rec', 10, 'delete_imgocrrec');
INSERT INTO `auth_permission` VALUES (40, 'Can view img ocr rec', 10, 'view_imgocrrec');
INSERT INTO `auth_permission` VALUES (41, 'Can add well danger', 11, 'add_welldanger');
INSERT INTO `auth_permission` VALUES (42, 'Can change well danger', 11, 'change_welldanger');
INSERT INTO `auth_permission` VALUES (43, 'Can delete well danger', 11, 'delete_welldanger');
INSERT INTO `auth_permission` VALUES (44, 'Can view well danger', 11, 'view_welldanger');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (7, 'my_app', 'admin');
INSERT INTO `django_content_type` VALUES (10, 'my_app', 'imgocrrec');
INSERT INTO `django_content_type` VALUES (9, 'my_app', 'imgtemplate');
INSERT INTO `django_content_type` VALUES (11, 'my_app', 'welldanger');
INSERT INTO `django_content_type` VALUES (8, 'my_app', 'yibiao');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-07-13 09:02:17.005849');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2022-07-13 09:02:17.891047');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2022-07-13 09:02:18.083092');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-07-13 09:02:18.100094');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-07-13 09:02:18.116099');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-07-13 09:02:18.252128');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-07-13 09:02:18.402160');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-07-13 09:02:18.517187');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-07-13 09:02:18.528189');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-07-13 09:02:18.627214');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-07-13 09:02:18.635214');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-07-13 09:02:18.645215');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-07-13 09:02:18.723234');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-07-13 09:02:18.820254');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-07-13 09:02:18.899272');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-07-13 09:02:18.914276');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-07-13 09:02:19.011297');
INSERT INTO `django_migrations` VALUES (18, 'my_app', '0001_initial', '2022-07-13 09:02:19.150330');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2022-07-13 09:02:19.201340');
INSERT INTO `django_migrations` VALUES (20, 'my_app', '0002_imgtemplate', '2022-07-14 06:47:51.990607');
INSERT INTO `django_migrations` VALUES (21, 'my_app', '0003_yibiao_img_name', '2022-07-14 06:49:27.117657');
INSERT INTO `django_migrations` VALUES (22, 'my_app', '0004_auto_20220715_0958', '2022-07-15 01:58:43.007925');
INSERT INTO `django_migrations` VALUES (23, 'my_app', '0005_admin_role', '2022-07-15 02:44:00.842479');
INSERT INTO `django_migrations` VALUES (24, 'my_app', '0006_auto_20220715_1140', '2022-07-15 03:41:03.678389');
INSERT INTO `django_migrations` VALUES (25, 'my_app', '0007_alter_admin_create_time', '2022-07-15 03:44:37.901376');
INSERT INTO `django_migrations` VALUES (26, 'my_app', '0008_alter_admin_create_time', '2022-07-16 07:51:40.710589');
INSERT INTO `django_migrations` VALUES (27, 'my_app', '0009_alter_admin_create_time', '2022-07-16 07:53:15.057814');
INSERT INTO `django_migrations` VALUES (28, 'my_app', '0010_auto_20220719_1645', '2022-07-19 08:45:23.123809');
INSERT INTO `django_migrations` VALUES (29, 'my_app', '0011_alter_admin_create_time', '2022-07-22 02:49:20.848882');
INSERT INTO `django_migrations` VALUES (30, 'my_app', '0012_auto_20220722_1114', '2022-07-22 03:15:01.531092');
INSERT INTO `django_migrations` VALUES (31, 'my_app', '0013_auto_20220722_1503', '2022-07-22 07:03:22.435051');
INSERT INTO `django_migrations` VALUES (32, 'my_app', '0014_auto_20220722_1556', '2022-07-22 07:57:04.663483');
INSERT INTO `django_migrations` VALUES (33, 'my_app', '0015_alter_admin_create_time', '2022-07-27 07:35:52.095534');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2l0bfmh1jjeqpqn3pbaa083cjdkkk0db', 'eyJpbWFnZV9jb2RlIjoiNzM4MjYiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDGhd:ttkQ8jScltBnGo4kULLDnmolLQsIbuaivokJGQ4_a8A', '2022-07-18 02:42:45.386225');
INSERT INTO `django_session` VALUES ('4fydv6zhmsz37lq50eofz44x7ozie05l', '.eJwti0EKwyAUBe_y1i60qDWeJSC2_hah8RetkBJy9xrSzYM3zGzIS3xSuHMieNhJmgkCoVFrmUug9Z3rF95K7aQUyOXB8BtyglcCvVEtcTnSyvwZ5f_N3VyUm7tLzgxa-XXS6y2qsVraYWjjsO8_fmQnzw:1oVXi5:Fpiw8sSEqBl3XMclDNCMEQwc9L9E0soRXV7ZhXC8T_A', '2022-09-13 12:29:45.954967');
INSERT INTO `django_session` VALUES ('8715vogcmh9clb5q6nh1h333aqbtfn8e', '.eJwti8EKAiEURf_lrl34SmcefsuAWFoIjS80YWKYf8-ozYV7OGdHXsM9-avEBAem-UxQ8C21lqX4tD1zfcNN2rDWCrncBG5HjnCk0FuqJazftIq8Rvl_S7cn4qVzZDtolcePzpdAY42ehmEs4zg-enAnxg:1oGbr7:1qsQ4WEf2iUrTsmO7mJBhD7hgLSjkPo54lDfSQCidoE', '2022-08-03 07:53:21.118514');
INSERT INTO `django_session` VALUES ('b7rl6g14fbbqzoif5xyczr7o9s08y3y7', 'eyJpbWFnZV9jb2RlIjoiNTI3NTAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oa5ka:d2Q6VIN1g2dmWiVI3NCnNEnKj8qYrGltjwegEW13jQg', '2022-09-19 01:40:08.866750');
INSERT INTO `django_session` VALUES ('b9ghzld486838b5gs80via9ciso0wv9k', 'eyJpbWFnZV9jb2RlIjoiOTkyNzIiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDGIZ:GGYWLa6mNJRsRsF8oQWHwIxnvtkQHDo5FBNZ6rHkWsQ', '2022-07-18 02:16:51.484684');
INSERT INTO `django_session` VALUES ('bdqa0do8v093uh06jciuj4uvwijq6mbe', 'eyJpbWFnZV9jb2RlIjoiNTk4NjAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDFIv:Ujrvu_pvToBRX4ZKkwMZk6J-pqQPp1_eP-NoGxdMzYc', '2022-07-18 01:13:09.930247');
INSERT INTO `django_session` VALUES ('jbcl8ul0jsqpyylg0pmpolrgr0zxmlqa', '.eJwti0EKwyAUBe_y1i40aBTPEhBbTfnQ-ItWaAi5ey3N5sEbZg7QFh853DlleGg5WQuB0HJrxCXkz4vqDj9L7aQUoLIy_AFK8Eqgt1xL3H5pZX6P8npLN5NyS3fJmUErP__U3qIaq-U8DG0czvMLelcnxg:1oLgNH:bVmm98rEc4AreMgMo-b1ESiuPUUWiTm4CZq7MpMwg9k', '2022-08-17 07:43:31.815794');
INSERT INTO `django_session` VALUES ('k4t5qr04fxzdth2fukanuv56ghnpqgjp', 'eyJpbWFnZV9jb2RlIjoiNTY3ODAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDFF3:U8NZJ9oBvRX4tEacU1raQLhFDZj6XOr17y-08VY0hKU', '2022-07-18 01:09:09.250504');
INSERT INTO `django_session` VALUES ('mp85hymiu16xeletmkjibta9xwnyzf5t', 'eyJpbWFnZV9jb2RlIjoiOTI1MDkiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDGfh:ZPSPyvWbPm3e4TcVHVol88qWe0jiJwsuqWvIksF0VvQ', '2022-07-18 02:40:45.033752');
INSERT INTO `django_session` VALUES ('ntke9j2rh25kkohr5hryw5e5c53s0cd5', '.eJwti8EKAiEURf_lrl08Q6c3fsuAWFoIjS80YWKYf8-ozYV7OGdHXsM9-avEBAc7E81Q8C21lqX4tD1zfcNNZJhIIZebwO3IEU4r9JZqCes3rSKvUf7f0u1J89I5sh20yuNHz5egxxqahmEs4zg-e7snyQ:1oDGpl:tuTSd4V4ZuXpcGP2AerARtNxZx09LygjvPTPzX_byRs', '2022-07-25 02:50:09.364141');
INSERT INTO `django_session` VALUES ('oqfngftw9jmq7ciseczbb0c8pi5ekbun', '.eJwti0EKwyAUBe_y1i6-qVrxLAGx1Rah8RetkBJy9xrSzYM3zGzIS3gmf-eY4EATmQsEfEutZS4-re9cv3CGlCUSyOXBcBtyhJMCvaVawnKklfkzyv-bu56knbuNVg9a-XXS6y3IsYrMMJS22PcfdlgnvQ:1oFrdL:vhq-mjhNrsCmQ44PITo8VgjjvaWGEDsx-lmqjyfAwUY', '2022-08-01 06:32:03.368778');
INSERT INTO `django_session` VALUES ('rmgnsnqk8yvxl9euctce1pk7g8t516mn', 'eyJpbWFnZV9jb2RlIjoiNDk4MzYiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDF2v:682asU6J8xxhnVDKaiEZ5O8ddwqY02GvQxYUJrv_zT4', '2022-07-18 00:56:37.240131');
INSERT INTO `django_session` VALUES ('t2es6888skmg7h80836v9l8lms6eabqb', 'eyJpbWFnZV9jb2RlIjoiMDg0OTciLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDG2d:o56ZoWTA27i_JNRfEuDp6HKKgaxDLbchb_bJ3Q76lxM', '2022-07-18 02:00:23.762295');
INSERT INTO `django_session` VALUES ('v74p2a1y1o2s8hk8g4yzt1087ppd1u8g', 'eyJpbWFnZV9jb2RlIjoiNzYyMjQiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oa5mt:jt-wKwQIWypmpaKXhm4rppGD42o7oQBiLqoGyvyuEPA', '2022-09-19 01:42:31.585467');
INSERT INTO `django_session` VALUES ('vff9lrrjvhwj973ywtszunj7q6q58bjh', 'eyJpbWFnZV9jb2RlIjoiOTcwMzgiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDFsc:ISluH8pPi_eZROJfDBH3LTQwtR-YAYQetVGmJbvwxVU', '2022-07-18 01:50:02.455064');
INSERT INTO `django_session` VALUES ('ygliiw4mfxjc9d60i22id091x1idiwoy', 'eyJpbWFnZV9jb2RlIjoiMTQwMDMiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDG6h:eIG2F4UgXs2-K5tkcVRNMu7cwt0X5WaaoY64IdqLw5U', '2022-07-18 02:04:35.377693');
INSERT INTO `django_session` VALUES ('yhetimgcr2d62027kfg534x9re15bayc', 'eyJpbWFnZV9jb2RlIjoiOTI2OTkiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDGaJ:bXJK_MbC90MLEqCbVp85kw1XUORnSETm7BN5vom3vkA', '2022-07-18 02:35:11.454681');
INSERT INTO `django_session` VALUES ('yy05up5vg6m0d1nexygg1uts1b984qpm', 'eyJpbWFnZV9jb2RlIjoiNDU5NTAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1oDGJt:cdZ1tOonIjOjrg2yWBclDRWsplq3qWFnISp-i8-B_Ww', '2022-07-18 02:18:13.042638');
INSERT INTO `django_session` VALUES ('z2agix9tgd61o9xhdgsap5ytmh7m95ef', '.eJwtjEEKwyAURO8yaxcaNBXPEhBbf8uHxl-0QkvI3WNoNwPzmDcbeE0PijfJhIDJuclAITZqjaVE-ry4fhFmbb3WClzugrCBM4JR6I1qSeupVpH3MP9t6ePIL91n7wat8vzRyzWZkVbPY2Gdx74feC8nwQ:1oa5po:eUy16Xgvx7B61c61AS2QzGBiTXGwdY1G6AHUyEA1hmk', '2022-09-26 01:44:32.595406');

-- ----------------------------
-- Table structure for my_app_admin
-- ----------------------------
DROP TABLE IF EXISTS `my_app_admin`;
CREATE TABLE `my_app_admin`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户名',
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `role` smallint(6) NOT NULL COMMENT '角色（1用户，2管理员）',
  `age` int(11) NOT NULL,
  `create_time` date NOT NULL,
  `gender` smallint(6) NOT NULL,
  `mobile` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of my_app_admin
-- ----------------------------
INSERT INTO `my_app_admin` VALUES (1, 'root', 'b2cb09feda40ad159c1a6c864363ae1f', 2, 23, '2022-07-15', 1, '15806409999', 'lc');
INSERT INTO `my_app_admin` VALUES (3, 'liu', 'b2cb09feda40ad159c1a6c864363ae1f', 1, 18, '2022-07-15', 2, '13654864023', 'ttg');
INSERT INTO `my_app_admin` VALUES (5, 'yyyy', 'fb25116ba878819ee1fdf362824742b3', 1, 23, '2022-07-15', 2, '15621153974', 'tg');
INSERT INTO `my_app_admin` VALUES (7, 'ag', 'b2cb09feda40ad159c1a6c864363ae1f', 1, 23, '2022-07-18', 2, '15621153988', 'AG');
INSERT INTO `my_app_admin` VALUES (13, 'tt', '59865caccf5621f835251ee857837541', 1, 5, '2022-07-19', 1, '15621153789', 'tt');
INSERT INTO `my_app_admin` VALUES (14, '888', '96be7378407fbdd9a5662aa8bc37bd89', 1, 8, '2022-07-22', 1, '15621153666', '888');
INSERT INTO `my_app_admin` VALUES (15, 'lccc', 'b2cb09feda40ad159c1a6c864363ae1f', 1, 23, '2022-07-27', 1, '15621153911', 'lc');

-- ----------------------------
-- Table structure for my_app_imgocrrec
-- ----------------------------
DROP TABLE IF EXISTS `my_app_imgocrrec`;
CREATE TABLE `my_app_imgocrrec`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `img` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img_result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `my_app_imgocrrec_admin_id_2b3935d7_fk_my_app_admin_id`(`admin_id`) USING BTREE,
  CONSTRAINT `my_app_imgocrrec_admin_id_2b3935d7_fk_my_app_admin_id` FOREIGN KEY (`admin_id`) REFERENCES `my_app_admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 64 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of my_app_imgocrrec
-- ----------------------------
INSERT INTO `my_app_imgocrrec` VALUES (35, 'rec/001.jpg', '300\n200\n400\nPFP SERIES\n100\n500\n19122651\n600\nu山u\nACC1.6\nWINERS\nkPa\nC3\nwww winters.com\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (36, 'rec/2.png', '温度\n25.7℃\nTemperature\n凯欣顺科技\n湿度\n479%\nHumidity\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (37, 'rec/6.jpg', 'LdN\nLAN\n/\nSVO\nREAD METER\nINSTRUCTIONS BEFORE WIRING\nPRESENT\n0\n。\n100\n490\n℃\nANALOG\n0\nARNING:DO NOT\nWHEN\nOPEN\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (41, 'rec/n001.jpg', '288-cth\n4.5\nDDRY\n44%\nAM\n3:10\nTHERMO/HYGRO/CLOCK\nYNGDO\nET\nMAY\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (42, 'rec/002.jpg', '80\n60\n100\nPFP SERIES\n40\n120\n二\n20\n140\n山\n19122643\n160\nA0C1.6\nWINIERS\npsi\n1963\nwww.winters.com\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (43, 'rec/002_TouNKcy.jpg', '80\n60\n100\nPFP SERIES\n40\n120\n二\n20\n140\n山\n19122643\n160\nA0C1.6\nWINIERS\npsi\n1963\nwww.winters.com\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (44, 'rec/004.jpg', '0.8\n0.4\n不锈钢压力表\n1.2\n2.5\nMPa\n鹤山\nMC\n浙制01830117号\n1.6\n杭州鹤山仪表有限公司\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (46, 'rec/012.jpg', 'Diaphrag ns and Wetted Parts\n1川1111179\nCE AISI316\n3000\n2000\n4000\nmmH2O\n1000\n000\nvax.static\npressure\n±100bar\n6000\n19047070\n0\n△p\nNo\n904701\n商效明\n定\nWw..com\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (47, 'rec/008.jpg', 'SWISS MOVEMENT\n0,10\n0.15\nEN837\n0.05\nPressure\nGauge\n0.20-\n316L\n0.25\n610090（）\n8600DMDA\nMPa\n10/16\nCL1.0\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (48, 'rec/temp013-2.jpg', '30000\n20000\n40000\n4000\n5000\n200\nEN837\n6000\n2000\n10000\n7000\n50000\n1000\n316SS\n8000\npsi\n8500\nkPa\nCETYPE2\n60000\n3385454\n09/108\nCL.1.6\nWIKA\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (49, 'rec/t1.png', '推荐\n热点视频\n娱乐\n国际财经科技懂车帝\n体育\n社会\n教育生活\n头一波酷生活\nilive.cn\n热搜\n热搜榜\n抖音\n微博\n知乎\n热视\n四川泳池事故遇难者高考606分，父亲：下\n音乐\n水一分钟就遇意外\n1成都将全面加强社会面疫情防控\n新闻联播微信公号·1小时前\nX\n要闻\n2山东7市将有大暴雨\n小说\n3终于等到录取通知书\n斯里兰卡继续在全国实施紧急状态\n游戏\n4哈士奇被蛇咬肿脸神似史努比\n新华社·1小时前\n5黄磊新剧人设是大冤种\nZR-V致在\n抢先试驾\n锁定年度重磅新车，抢先试驾广汽本田ZR-\n6习酒集团正式成立\nV致在\n7张小泉总经理道歉\nSUV大咖\n11:26\n2万次观看\n8起底偷拍黑色产业链\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (58, 'rec/c005.jpg', '.·2\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (59, 'rec/218003071099刘超.jpg', 'HD 046\nHD 2\nl\n4G\nQ\n3:29\n潮流\n等等我\n马上翻\n卷作起来了\n不可以一时之誉，断其为君子；不可以一时之谤，\n断其为小人。\n今天\n满分！我完成了“青年大学习”网上主\n6A000GL0400\n题团课2022年第17期，你也来试试吧\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (60, 'rec/218003071099刘超_0nWEQsB.jpg', 'HD 046\nHD 2\nl\n4G\nQ\n3:29\n潮流\n等等我\n马上翻\n卷作起来了\n不可以一时之誉，断其为君子；不可以一时之谤，\n断其为小人。\n今天\n满分！我完成了“青年大学习”网上主\n6A000GL0400\n题团课2022年第17期，你也来试试吧\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (61, 'rec/218003071099刘超_SGPpHw7.jpg', 'HD 046\nHD 2\nl\n4G\nQ\n3:29\n潮流\n等等我\n马上翻\n卷作起来了\n不可以一时之誉，断其为君子；不可以一时之谤，\n断其为小人。\n今天\n满分！我完成了“青年大学习”网上主\n6A000GL0400\n题团课2022年第17期，你也来试试吧\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (63, 'rec/218003071099刘超_kAc6loB.jpg', 'HD 0 46\n4G\nHD 2\nG0:\n3:01\n潮流\n等等我\n马上\n卷作起来了\n不可以一时之誉，断其为君子；不可以一时之谤，\n断其为小人。\n今天\n青\n满分！我完成了“青年大学习”网上主\n计\n题团课2022年第19期，你也来试试吧\n', 1);
INSERT INTO `my_app_imgocrrec` VALUES (64, 'rec/218003071099刘超_wMzLRep.jpg', 'HD 0 46\n4G\nHD 2\nG0:\n3:01\n潮流\n等等我\n马上\n卷作起来了\n不可以一时之誉，断其为君子；不可以一时之谤，\n断其为小人。\n今天\n青\n满分！我完成了“青年大学习”网上主\n计\n题团课2022年第19期，你也来试试吧\n', 1);

-- ----------------------------
-- Table structure for my_app_imgtemplate
-- ----------------------------
DROP TABLE IF EXISTS `my_app_imgtemplate`;
CREATE TABLE `my_app_imgtemplate`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '模板名称',
  `a` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '刻度及其对应像素坐标',
  `c_x` decimal(10, 2) NOT NULL COMMENT '圆心x像素坐标',
  `c_y` decimal(10, 2) NOT NULL COMMENT '圆心y像素坐标',
  `fir_d` decimal(10, 2) NOT NULL COMMENT '配置0刻度线参数1',
  `maxd` decimal(10, 2) NOT NULL COMMENT '最大刻度值',
  `scale` decimal(10, 2) NOT NULL COMMENT '配置0刻度线参数2',
  `sec_d` decimal(10, 2) NOT NULL COMMENT '刻度间隔',
  `img_template` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '模板图片',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of my_app_imgtemplate
-- ----------------------------
INSERT INTO `my_app_imgtemplate` VALUES (18, 'template.jpg', '{0.0: (61.5, 152.5), 0.1: (50.5, 109.5), 0.2: (77.5, 64.0), 0.3: (126.0, 46.0), 0.4: (169.0, 70.0), 0.5: (188.5, 122.0), 0.6: (164.0, 168.5)}', 120.00, 114.50, 0.50, 0.60, 0.10, 0.60, 'TemplateLib/template.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (19, 'temp001-1.jpg', '{0.0: (233.5, 657.5), 100.0: (209.5, 527.5), 200.0: (272.5, 384.0), 300.0: (404.5, 319.5), 400.0: (534.5, 386.5), 500.0: (595.0, 533.5), 600.0: (537.0, 674.0)}', 396.50, 531.00, 500.00, 600.00, 100.00, 600.00, 'TemplateLib/temp001-1.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (20, 'temp013-2.jpg', '{0: (90, 380), 10000:(45,270), 20000: (85,140), 30000: (220, 80),40000:(355,130), 50000: (400, 270),60000:(340,390)}', 228.00, 244.00, 50000.00, 60000.00, 10000.00, 60000.00, 'TemplateLib/temp013-2.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (21, '002.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/002.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (22, '003.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/003.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (23, '004.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/004.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (24, '005.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/005.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (25, '006.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/006.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (26, '007.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/007.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (27, '008.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/008.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (28, '009.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/009.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (29, '010.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/010.jpg');
INSERT INTO `my_app_imgtemplate` VALUES (30, '011.jpg', '0', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TemplateLib/011.jpg');

-- ----------------------------
-- Table structure for my_app_welldanger
-- ----------------------------
DROP TABLE IF EXISTS `my_app_welldanger`;
CREATE TABLE `my_app_welldanger`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `imgrec` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `imgresult` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `my_app_welldanger_admin_id_dd027e50_fk_my_app_admin_id`(`admin_id`) USING BTREE,
  CONSTRAINT `my_app_welldanger_admin_id_dd027e50_fk_my_app_admin_id` FOREIGN KEY (`admin_id`) REFERENCES `my_app_admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of my_app_welldanger
-- ----------------------------
INSERT INTO `my_app_welldanger` VALUES (55, 'yolov5_master/number/c026.jpg', 'yolov5_master/runs\\detect\\exp2\\c026.jpg', 1);
INSERT INTO `my_app_welldanger` VALUES (56, 'yolov5_master/number/c075.jpg', 'yolov5_master/runs\\detect\\exp3\\c075.jpg', 1);
INSERT INTO `my_app_welldanger` VALUES (57, 'yolov5_master/number/fu004.jpg', 'yolov5_master/runs\\detect\\exp4\\fu004.jpg', 1);
INSERT INTO `my_app_welldanger` VALUES (60, 'yolov5_master/number/fu004_ODyxMYW.jpg', 'yolov5_master/runs\\detect\\exp8\\fu004_ODyxMYW.jpg', 1);

-- ----------------------------
-- Table structure for my_app_yibiao
-- ----------------------------
DROP TABLE IF EXISTS `my_app_yibiao`;
CREATE TABLE `my_app_yibiao`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `img` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '仪表图片',
  `img_result` decimal(10, 2) NOT NULL COMMENT '识别结果',
  `admin_id` bigint(20) NOT NULL COMMENT '图片名称',
  `img_name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '所属用户',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `my_app_yibiao_admin_id_2082d4fe_fk_my_app_admin_id`(`admin_id`) USING BTREE,
  CONSTRAINT `my_app_yibiao_admin_id_2082d4fe_fk_my_app_admin_id` FOREIGN KEY (`admin_id`) REFERENCES `my_app_admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of my_app_yibiao
-- ----------------------------
INSERT INTO `my_app_yibiao` VALUES (16, 'img_test_2/001_kF3RmqA.jpg', 4.67, 1, '001_kF3RmqA.jpg');
INSERT INTO `my_app_yibiao` VALUES (19, 'img_test_2/001_e20X1GE.jpg', 4.67, 1, '001_e20X1GE.jpg');
INSERT INTO `my_app_yibiao` VALUES (30, 'img_test_2/15_dpLlP7t.jpg', 0.55, 1, '15_dpLlP7t.jpg');
INSERT INTO `my_app_yibiao` VALUES (31, 'img_test_2/8.jpg', 0.35, 1, '8.jpg');
INSERT INTO `my_app_yibiao` VALUES (32, 'img_test_2/7_7G5oJGk.jpg', 0.33, 15, '7_7G5oJGk.jpg');
INSERT INTO `my_app_yibiao` VALUES (33, 'img_test_2/9.jpg', 0.34, 1, '9.jpg');

SET FOREIGN_KEY_CHECKS = 1;
