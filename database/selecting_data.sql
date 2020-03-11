/* Selecting all income amounts for a user  */
select username, first_name, last_name, amount from user_details, income_1 where user_details.id = usr_id and usr_id = 1;

/* Selecting all expense amount for a user*/
select username, first_name, last_name, amount from user_details, expense where user_details.id = user_id and user_id = 1;

/* Selecting all investments for a user */
select username, first_name, last_name, amount from user_details, investment where userdetails.id = user_id and userid = 1;