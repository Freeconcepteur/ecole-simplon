-- SELECT DISTINCT Age_Group  FROM sales_data_csv
-- SELECT distinct State FROM sales_data_csv
-- SELECT distinct Country FROM sales_data_csv
-- SELECT distinct Sub_Category FROM sales_data_csv
-- SELECT distinct Product_Category FROM sales_data_csv


USE sales_data;

SET foreign_key_checks = 0; -- désactive la contrainte
TRUNCATE TABLE `Countries`;
TRUNCATE TABLE `age_group`;
TRUNCATE TABLE `Categories`;
TRUNCATE TABLE `Sub_categories`;
TRUNCATE TABLE `States`;
SET foreign_key_checks = 1; -- réactive la contrainte

-- Remplissage des tables (sans clé étrangère)
INSERT INTO Countries (name)
SELECT distinct Country FROM sales_data_csv;

INSERT INTO age_group (age_groupname)
SELECT distinct Age_Group FROM sales_data_csv;

INSERT INTO Categories (Category_name)
SELECT distinct Product_Category FROM sales_data_csv;


-- Remplissage des tables (clé étrangère)
INSERT INTO Sub_categories (Sub_category_name, Categories_idCategory)
SELECT DISTINCT a.Sub_Category, b.idCategory 
FROM sales_data_csv AS a 
INNER JOIN Categories AS b 
ON a.Product_Category = b.Category_name;

INSERT INTO States (name, Countries_idCountries1)
SELECT DISTINCT a.State, b.idCountries FROM sales_data_csv AS a 
INNER JOIN Countries AS b ON a.Country = b.name;

SELECT a.Customer_Age, a.Customer_Gender, c.Statesid
FROM sales_data_csv AS a
JOIN age_group AS b
	ON a.Age_Group = b.age_groupname
JOIN States AS c
	ON a.State = c.name
	
