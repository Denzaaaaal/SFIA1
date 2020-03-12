begin;

/* Creating dummy data for the income table */
insert into income (date_of_income, company, ammount, usr_id) values ('2020-03-11', 'Google','3000',1);
insert into income (date_of_income, company, ammount, usr_id) values ('2020-03-11', 'Amazon','9000',2);
insert into income (date_of_income, company, ammount, usr_id) values ('2020-03-11', 'Philips','5000',3);
insert into income (date_of_income, company, ammount, usr_id) values ('2020-03-11', 'HP','12000',4);

/* Creating dummy data for the user table*/
insert into user_details (username, passwd, first_name, last_name, dob) values ('jibarr','','Jessica','Ibarra','1960-01-26');
insert into user_details (username, passwd, first_name, last_name, dob) values ('sanja','','Sanjana','Brody','1999-11-12');
insert into user_details (username, passwd, first_name, last_name, dob) values ('Semaial','','Maialen','Seeger','2000-08-13');
insert into user_details (username, passwd, first_name, last_name, dob) values ('dalbus','','Buse','Dalca','1992-08-10');

/* Creating dummy data for investment table */
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479.94','24','0','0','9.48','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('BA','Boeing Co','8','178.00','1972.65','24','0','1','7.35','',1);
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');
insert into user_details (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) values ('SPCE','Virgin Galactic','4','16.47','2479','24','','','','','','');

/* Creating dummy data for expenses table */
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-06','Superdrug','Palmers Coco Butter Cream', 'Cosmetics','','5.35',1);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-06','Superdrug','Palmers Coco Butter Cream', 'Cosmetics','','5.35',1);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-02-22','Boots','Olay Complete Moisturiser', 'Cosmetics','','5.99',2);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco Express','Jaffer Cakes', 'Food','','1.00',3);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco Express','Sausage Roll', 'Food','','1.00',3);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco Express','Chicken Sandwich', 'Food','','2.75',3);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco','Bread Rolls', 'Food','','0.69',4);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco','Whole Milk', 'Drink','','0.50',2);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco','Cheese', 'Food','','2.30',4);
insert into expense (expense_date, company, description, catagory, account, amount, id) values ('2020-03-10','Tesco','Ham', 'Food','','3.00',4);

commit; 