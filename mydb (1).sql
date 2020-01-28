-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 28-Jan-2020 às 01:43
-- Versão do servidor: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `ar_condicionado`
--

CREATE TABLE `ar_condicionado` (
  `id_ar_condicionado` int(10) UNSIGNED NOT NULL,
  `id_casa_ar` int(11) NOT NULL,
  `temperatura` int(4) NOT NULL,
  `consumo` float NOT NULL,
  `humidade` int(11) NOT NULL,
  `data` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `descricao` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `casa`
--

CREATE TABLE `casa` (
  `id_casa` int(11) NOT NULL,
  `num_divisoes` int(11) NOT NULL,
  `garagem` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `casa`
--

INSERT INTO `casa` (`id_casa`, `num_divisoes`, `garagem`) VALUES
(2, 4, 1),
(3, 3, 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `contador`
--

CREATE TABLE `contador` (
  `id_contador` int(11) NOT NULL,
  `tipo_contador` varchar(100) NOT NULL,
  `descricao` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `contador`
--

INSERT INTO `contador` (`id_contador`, `tipo_contador`, `descricao`) VALUES
(1, 'b', 'lala');

-- --------------------------------------------------------

--
-- Estrutura da tabela `garagem`
--

CREATE TABLE `garagem` (
  `id_garagem` int(11) NOT NULL,
  `id_casa_garagem` int(11) NOT NULL,
  `data` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `garagem`
--

INSERT INTO `garagem` (`id_garagem`, `id_casa_garagem`, `data`) VALUES
(2, 2, '2020-01-28 00:41:51.209296');

-- --------------------------------------------------------

--
-- Estrutura da tabela `porta_principal`
--

CREATE TABLE `porta_principal` (
  `id_porta_principal` int(11) NOT NULL,
  `data` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `id_casa_porta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registo_consumo`
--

CREATE TABLE `registo_consumo` (
  `id_registo_consumo` int(11) NOT NULL,
  `id_contador` int(11) NOT NULL,
  `id_casa_registo` int(11) NOT NULL,
  `data` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `valor` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `registo_consumo`
--

INSERT INTO `registo_consumo` (`id_registo_consumo`, `id_contador`, `id_casa_registo`, `data`, `valor`) VALUES
(1, 1, 2, '2020-01-27 23:51:04.423506', 54.35);

-- --------------------------------------------------------

--
-- Estrutura da tabela `televisao`
--

CREATE TABLE `televisao` (
  `id_tv` int(11) NOT NULL,
  `id_casa_tv` int(11) NOT NULL,
  `data` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `consumo` int(11) NOT NULL,
  `descricao` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `televisao`
--

INSERT INTO `televisao` (`id_tv`, `id_casa_tv`, `data`, `consumo`, `descricao`) VALUES
(1, 2, '2020-01-27 23:22:58.846321', 17, 'sm');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ar_condicionado`
--
ALTER TABLE `ar_condicionado`
  ADD PRIMARY KEY (`id_ar_condicionado`),
  ADD KEY `id_casa_idx` (`id_casa_ar`);

--
-- Indexes for table `casa`
--
ALTER TABLE `casa`
  ADD PRIMARY KEY (`id_casa`);

--
-- Indexes for table `contador`
--
ALTER TABLE `contador`
  ADD PRIMARY KEY (`id_contador`);

--
-- Indexes for table `garagem`
--
ALTER TABLE `garagem`
  ADD PRIMARY KEY (`id_garagem`),
  ADD KEY `id_casa_idx` (`id_casa_garagem`);

--
-- Indexes for table `porta_principal`
--
ALTER TABLE `porta_principal`
  ADD PRIMARY KEY (`id_porta_principal`),
  ADD KEY `id_casa_idx` (`id_casa_porta`);

--
-- Indexes for table `registo_consumo`
--
ALTER TABLE `registo_consumo`
  ADD PRIMARY KEY (`id_registo_consumo`),
  ADD KEY `id_consumo_idx` (`id_contador`),
  ADD KEY `id_casa_idx` (`id_casa_registo`);

--
-- Indexes for table `televisao`
--
ALTER TABLE `televisao`
  ADD PRIMARY KEY (`id_tv`),
  ADD KEY `id_casa_idx` (`id_casa_tv`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ar_condicionado`
--
ALTER TABLE `ar_condicionado`
  MODIFY `id_ar_condicionado` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `casa`
--
ALTER TABLE `casa`
  MODIFY `id_casa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contador`
--
ALTER TABLE `contador`
  MODIFY `id_contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `garagem`
--
ALTER TABLE `garagem`
  MODIFY `id_garagem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `porta_principal`
--
ALTER TABLE `porta_principal`
  MODIFY `id_porta_principal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `registo_consumo`
--
ALTER TABLE `registo_consumo`
  MODIFY `id_registo_consumo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `televisao`
--
ALTER TABLE `televisao`
  MODIFY `id_tv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `ar_condicionado`
--
ALTER TABLE `ar_condicionado`
  ADD CONSTRAINT `id_casa_ar` FOREIGN KEY (`id_casa_ar`) REFERENCES `casa` (`id_casa`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `garagem`
--
ALTER TABLE `garagem`
  ADD CONSTRAINT `id_casa_garagem` FOREIGN KEY (`id_casa_garagem`) REFERENCES `casa` (`id_casa`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `porta_principal`
--
ALTER TABLE `porta_principal`
  ADD CONSTRAINT `id_casa_porta` FOREIGN KEY (`id_casa_porta`) REFERENCES `casa` (`id_casa`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `registo_consumo`
--
ALTER TABLE `registo_consumo`
  ADD CONSTRAINT `id_casa_reg` FOREIGN KEY (`id_casa_registo`) REFERENCES `casa` (`id_casa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_consumo_` FOREIGN KEY (`id_contador`) REFERENCES `contador` (`id_contador`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `televisao`
--
ALTER TABLE `televisao`
  ADD CONSTRAINT `id_casa_tv` FOREIGN KEY (`id_casa_tv`) REFERENCES `casa` (`id_casa`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
