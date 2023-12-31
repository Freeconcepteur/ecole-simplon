-- MySQL Script generated by MySQL Workbench
-- Thu Sep 28 14:00:47 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sales_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sales_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sales_data` DEFAULT CHARACTER SET utf8 ;
USE `sales_data` ;

-- -----------------------------------------------------
-- Table `sales_data`.`Countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`Countries` (
  `idCountries` INT(3) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idCountries`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`States`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`States` (
  `name` VARCHAR(45) NULL,
  `Countries_idCountries1` INT NOT NULL,
  `Statesid` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Statesid`),
  INDEX `fk_States_Countries1_idx` (`Countries_idCountries1` ASC) VISIBLE,
  CONSTRAINT `fk_States_Countries1`
    FOREIGN KEY (`Countries_idCountries1`)
    REFERENCES `sales_data`.`Countries` (`idCountries`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`age_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`age_group` (
  `idage_group` TINYINT(2) NOT NULL AUTO_INCREMENT,
  `age_groupname` VARCHAR(45) NULL,
  PRIMARY KEY (`idage_group`),
  UNIQUE INDEX `age_groupname_UNIQUE` (`age_groupname` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`Customers` (
  `idCustomers` INT NOT NULL AUTO_INCREMENT,
  `age` TINYINT(3) NULL,
  `genre` VARCHAR(1) NULL,
  `age_group_idage_group` TINYINT(2) NOT NULL,
  `States_Statesid` INT NOT NULL,
  PRIMARY KEY (`idCustomers`, `age_group_idage_group`, `States_Statesid`),
  INDEX `fk_Customers_age_group1_idx` (`age_group_idage_group` ASC) VISIBLE,
  INDEX `fk_Customers_States1_idx` (`States_Statesid` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_age_group1`
    FOREIGN KEY (`age_group_idage_group`)
    REFERENCES `sales_data`.`age_group` (`idage_group`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_States1`
    FOREIGN KEY (`States_Statesid`)
    REFERENCES `sales_data`.`States` (`Statesid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`Categories` (
  `idCategory` INT NOT NULL AUTO_INCREMENT,
  `Category_name` VARCHAR(45) NULL,
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`Sub_categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`Sub_categories` (
  `idSub_category` INT NOT NULL,
  `Sub_category_name` VARCHAR(45) NULL,
  `Categories_idCategory` INT NOT NULL,
  PRIMARY KEY (`idSub_category`),
  INDEX `fk_Sub_categories_Categories1_idx` (`Categories_idCategory` ASC) VISIBLE,
  CONSTRAINT `fk_Sub_categories_Categories1`
    FOREIGN KEY (`Categories_idCategory`)
    REFERENCES `sales_data`.`Categories` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`products` (
  `idproducts` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(45) NULL,
  `Unit_Price` DECIMAL(6,2) NULL,
  `Unit_Cost` DECIMAL(6,2) NULL,
  `Sub_categories_idSub_category` INT NOT NULL,
  PRIMARY KEY (`idproducts`),
  INDEX `fk_products_Sub_categories1_idx` (`Sub_categories_idSub_category` ASC) VISIBLE,
  CONSTRAINT `fk_products_Sub_categories1`
    FOREIGN KEY (`Sub_categories_idSub_category`)
    REFERENCES `sales_data`.`Sub_categories` (`idSub_category`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sales_data`.`Sales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sales_data`.`Sales` (
  `idSales` INT NOT NULL AUTO_INCREMENT,
  `Order_Quantity` VARCHAR(45) NULL,
  `Profit` VARCHAR(45) NULL,
  `Cost` VARCHAR(45) NULL,
  `Revenue` VARCHAR(45) NULL,
  `Customers_idCustomers` INT NOT NULL,
  `products_idproducts` INT NOT NULL,
  `date_order` DATE NULL,
  PRIMARY KEY (`idSales`, `Customers_idCustomers`),
  INDEX `fk_Sales_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  INDEX `fk_Sales_products1_idx` (`products_idproducts` ASC) VISIBLE,
  CONSTRAINT `fk_Sales_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `sales_data`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sales_products1`
    FOREIGN KEY (`products_idproducts`)
    REFERENCES `sales_data`.`products` (`idproducts`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
