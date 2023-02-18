CREATE TABLE Clients (
  client_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR (255) NOT NULL,
  address VARCHAR (255) NOT NULL,
  PRIMARY KEY (client_id)
);

CREATE TABLE Nomenclature (
  nomenclature_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR (255) NOT NULL,
  quantity INT UNSIGNED NOT NULL,
  price DECIMAL (10,2) NOT NULL,
  PRIMARY KEY (nomenclature_id)
);

CREATE TABLE Nomenclature_Categories (
  category_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR (255) NOT NULL,
  parent_category_id INT UNSIGNED DEFAULT NULL,
  PRIMARY KEY (category_id)
);

CREATE TABLE Orders (
  order_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  client_id INT UNSIGNED NOT NULL,
  date_created DATE NOT NULL,
  PRIMARY KEY (order_id)
);

CREATE TABLE Order_Items (
  order_item_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  order_id INT UNSIGNED NOT NULL,
  nomenclature_id INT UNSIGNED NOT NULL,
  quantity INT UNSIGNED NOT NULL,
  price DECIMAL (10,2) NOT NULL,
  PRIMARY KEY (order_item_id)
);

ALTER TABLE Nomenclature_Categories
  ADD FOREIGN KEY (parent_category_id) REFERENCES Nomenclature_Categories (category_id);

ALTER TABLE Orders
  ADD FOREIGN KEY (client_id) REFERENCES Clients (client_id);

ALTER TABLE Order_Items
  ADD FOREIGN KEY (order_id) REFERENCES Orders (order_id),
  ADD FOREIGN KEY (nomenclature_id) REFERENCES Nomenclature (nomenclature_id);