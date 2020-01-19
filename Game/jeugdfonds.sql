-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 19 jan 2020 om 09:29
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
(24, 8, 'When data is without risks and problems including the loss of important information or valid data', 1);

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
(8, 'When are you in the right direction of getting your data clean?', 1, '');

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
('ouwefonds', '$2y$10$eNR7UwwX7BDJr33wlrN5yuKhHbNk7ntwhLcNIH7Ummkt8JuKPPCr6', 'Jaap', '', 'Emtec');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT voor een tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
