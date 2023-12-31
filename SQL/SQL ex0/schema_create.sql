-- MySQL Script generated by MySQL Workbench
-- Tue Sep 26 10:03:24 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema csv_prdts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema csv_prdts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `csv_prdts` DEFAULT CHARACTER SET utf8 ;
USE `csv_prdts` ;

-- -----------------------------------------------------
-- Table `csv_prdts`.`famille`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csv_prdts`.`famille` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csv_prdts`.`conditionnementnement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csv_prdts`.`conditionnement` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csv_prdts`.`produits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csv_prdts`.`produits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `libelle` VARCHAR(100) NOT NULL,
  `prix` DECIMAL(4,2) NOT NULL,
  `code_art` VARCHAR(45) NOT NULL,
  `famille_id1` INT NOT NULL,
  `conditionnement_id1` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_produits_famille1_idx` (`famille_id1` ASC) VISIBLE,
  INDEX `fk_produits_conditionnement1_idx` (`conditionnement_id1` ASC) VISIBLE,
  CONSTRAINT `fk_produits_famille1`
    FOREIGN KEY (`famille_id1`)
    REFERENCES `csv_prdts`.`famille` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_produits_conditionnement1`
    FOREIGN KEY (`conditionnement_id1`)
    REFERENCES `csv_prdts`.`conditionnement` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
