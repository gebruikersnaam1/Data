-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 22 jan 2020 om 13:49
-- Serverversie: 10.4.11-MariaDB
-- PHP-versie: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jeugdfonds`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `highscore`
--

CREATE TABLE `highscore` (
  `username` varchar(15) NOT NULL,
  `insert_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `highscore`
--

INSERT INTO `highscore` (`username`, `insert_date`, `score`) VALUES
('abv', '2020-01-19 11:15:50', 4000),
('deford', '2020-01-19 11:16:54', 5600),
('gebruikersnaam', '2020-01-19 11:15:25', 1000),
('gmaas', '2020-01-19 11:16:42', 6000),
('hemsworth', '2020-01-19 11:19:16', 4000),
('koos', '2020-01-19 11:18:48', 10291),
('lotte', '2020-01-19 11:16:34', 8899),
('ouwefonds', '2020-01-19 11:15:36', 1500),
('plugm', '2020-01-19 11:12:29', 999999),
('ubert', '2020-01-19 11:12:17', 999999);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `possibleanswers`
--

CREATE TABLE `possibleanswers` (
  `id` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `content` text NOT NULL,
  `correct` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `possibleanswers`
--

INSERT INTO `possibleanswers` (`id`, `questionID`, `content`, `correct`) VALUES
(1, 1, 'Information about the intermediairs', 0),
(2, 1, 'Information about the applicants and intermediairs', 0),
(3, 1, 'Information about the intermediairs, applicants and which intermediair helps an applicants', 1),
(4, 2, 'Intermediaries', 1),
(5, 2, 'Parents', 0),
(6, 2, 'Intermediaries and parents', 0),
(7, 3, 'You need to know which operations you can execute on the data', 1),
(8, 3, 'It gives meaning to the data', 1),
(9, 3, 'More analytic processing can be done', 1),
(10, 4, 'The data is used to measure the amount of children in an area', 1),
(11, 4, 'Because the data type used is ‘integer’', 0),
(12, 4, 'It would be a problem if the exact ZIP code was stored, because of GDPR laws', 0),
(13, 5, 'Documenting is an important part of developing', 0),
(14, 5, 'Columns can be understood differently by different people', 1),
(15, 5, 'It is compulsory to document according to laws', 1),
(16, 6, 'To ensure that the quality of the data does not decrease. Otherwise it becomes impossible to compare rows with each other.', 1),
(17, 6, 'To ensure that all fields have been filled in', 1),
(18, 6, 'To check for any attempts of hacking', 1),
(19, 7, 'Complete, Accurate and User Friendly', 0),
(20, 7, 'Unambiguous, Confidential and Efficient', 0),
(21, 7, 'Complete, Consistent and Accurate', 1),
(22, 8, 'Your data will start to be clean when the data information be accurate because there are no duplicates', 1),
(23, 8, 'Make data as consistent as possible in terms of labels, categories, time stamps and other types of structures', 1),
(24, 8, 'When data is without risks and problems including the loss of important information or valid data', 1),
(25, 9, 'A dropdown with fixed options could be used', 1),
(26, 9, 'The user can write down the disease themselves', 0),
(27, 9, 'A dropdown with also an option to write down the disease themselves', 0),
(28, 10, 'No, when data complies to an ISO standard it does not automatically mean that it also complies to another ISO standard about data quality', 0),
(29, 10, 'Yes, because ISO 8000 is met when the data is made portable and this is also one of the characteristics in the data quality model of ISO 25012', 1),
(30, 10, 'Yes, when data meets all of ISO 25012 the quality of the data is at its best and the quality cannot be made better.', 0),
(31, 11, 'True. Different companies can use different software.', 0),
(32, 11, 'False. Your data should not be locked into the software. The software needs to be ISO 8000 compliant.', 1),
(33, 11, 'False. If the data is made in a portable way (e.g. JSON, XML etc.) that is enough. You can use whichever software you like.', 0),
(34, 12, 'Yes, the most important characteristics are met.', 0),
(35, 12, 'No, not all data characteristics are met.', 1),
(36, 12, 'It depends on the situation. In the case of Jeugdfonds, because of GDPR laws the data complies to ISO 25012 when having these characteristics.', 0);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `questions`
--

CREATE TABLE `questions` (
  `ID` int(11) NOT NULL,
  `question` text NOT NULL,
  `difficult` tinyint(1) NOT NULL DEFAULT 1,
  `extraInfo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `questions`
--

INSERT INTO `questions` (`ID`, `question`, `difficult`, `extraInfo`) VALUES
(1, 'If you want to know how many applicants an intermediair helps out. What information is needed?', 0, ''),
(2, 'Who can sign up an applicant?', 0, ''),
(3, 'Why are data types important?', 1, ''),
(4, 'Why is it not a problem that only the 4 digits of the ZIP codes are saved and not the exact ZIP code?', 1, ''),
(5, 'Why is it important to document the design decisions of the database?', 1, ''),
(6, 'Why is it important to check the insertion of data?', 1, ''),
(7, 'What are some of the characteristics of good data quality according to ISO 25012?', 1, ''),
(8, 'When are you in the right direction of getting your data clean?', 1, ''),
(9, 'If additional information about an applicant is needed (e.g. a disease/mental issue) what would be the optimal way of asking that question?', 1, ''),
(10, 'Does data also comply to ISO 8000 when all characteristics of the data quality model of ISO 25012 is met?', 1, ''),
(11, 'The software used to make data ISO 8000 compliant is not of importance.', 1, ''),
(12, 'Does data comply to ISO 25012 when it is accurate, complete, consistent, portable and credible?', 1, '');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `user`
--

CREATE TABLE `user` (
  `username` varchar(15) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `affix` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `user`
--

INSERT INTO `user` (`username`, `password`, `firstname`, `affix`, `lastname`) VALUES
('abv', '$2y$10$MR57k7QBWnWhDKQNICzkp.oewvAJFV6/AkQgfh3tvvG5sWc/HnBpe', 'Abdulvahid', '', 'Kilic'),
('deford', '$2y$10$kcQKGQUdY16pUCe4RCkbX.37v71gdq6kjhEVi3MIqOJi4BMQ8SXRy', 'Devon', '', 'Crawford'),
('dujaa', '$2y$10$xlaEEiJwT2DnNtXI40/5puoGNp77iUA./Oanyetszzr8aQvBdlW3a', 'anouk', '', 'Dujardin'),
('gebruikersnaam', '$2y$10$.A1iY9MyszgXcVvY5M7do.X8k63LtuljSmxlBdGOrsJyjCmK1l/Gm', 'Chris', '', 'Achternaam'),
('gmaas', '$2y$10$ziw/jQsge6Li2mCry1HEM.XeI27GEJhNHPQxzqif2h33cBYV0UB9q', 'Gwen', '', 'Maas'),
('hemsworth', '$2y$10$USYF/8Uum4ajrd6I9dUx7eN2bReUO8RqBhsaQoLsyLVFp1ym1adJS', 'Sara', 'der', 'Bennik'),
('koos', '$2y$10$ZWEcPgqs855vAy/bEFNGt.ZMoGs5MFIzudSzE9p6G5wBfoz5kJqmK', 'Roos', 'de', 'Kole'),
('lotte', '$2y$10$bEB/T3dNoxyXCRGB6mos4uOklqTwbsP3NeBce6g.d8wIlCv52exkC', 'Lotte', '', 'Muilwijk'),
('ouwefonds', '$2y$10$eNR7UwwX7BDJr33wlrN5yuKhHbNk7ntwhLcNIH7Ummkt8JuKPPCr6', 'Jaap', '', 'Emtec'),
('plugm', '$2y$10$29OmCD5F8i54RlwNYqzHue7ROZoTk8uNuJOJINy.NBusSQkKrs/92', 'George', '', 'Pluimakers'),
('ubert', '$2y$10$edcV6d.vQmSiFf3Er9OvJOglOOioOZpPuThQF7U3wu4ru.LQ3WX3G', 'Tanja', '', 'Ubert');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `highscore`
--
ALTER TABLE `highscore`
  ADD PRIMARY KEY (`username`,`insert_date`);

--
-- Indexen voor tabel `possibleanswers`
--
ALTER TABLE `possibleanswers`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`ID`);

--
-- Indexen voor tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `possibleanswers`
--
ALTER TABLE `possibleanswers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT voor een tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
