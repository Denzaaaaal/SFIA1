Begin;

/*Creating the user details table*/
create table user_details (
    id int(4) Primary key auto_increment,
    username varchar(100) not null,
    passwd varchar(100) not null,
    first_name varchar (100) not null,
    last_name varchar (100) not null,
    dob date not null
    );

/*Creating the income table*/
    create table income (
        id int(4) primary key not null auto_increment,
        date_of_income date not null,
        company varchar(100) not null,
        amount int(7) not null,
        usr_id int(4), 
        foreign key(usr_id) references user_details(id)
        );

/*Creating the expenses table*/
CREATE TABLE expense (
    id int(4) Primary Key not null auto_increment,
    expense_date date not null,
    company varchar(100) not null,
    description varchar(100) not null,
    catagory varchar(50) not null,
    account varchar(17) not null,
    amount int(5) not null,
    usr_id int(4), 
    foreign key(usr_id) references user_details(id)
    );

/*Creating the Investment table*/
create table investment (
    id int(4) primary key not null auto_increment,
    ticker varchar(5) not null,
    description varchar(100) not null,
    quantity int(4) not null,
    price int(3) not null,
    value int(7) not null,
    cost int(3) not null,
    regular_investment tinyint(1) not null,
    dividend_reinvestment tinyint(1) not null,
    dividend_amount float(4) not null,
    usr_id int(4), 
    foreign key(usr_id) references user_details(id)
    );

Commit;