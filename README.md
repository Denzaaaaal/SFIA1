# Your Money Or Your Life Personal Finance Manager

## Index
* [Brief](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#brief)
* * [Solution](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#solution)
* * [Trello Board](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Trello)
* [Architecture](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#architecture)
* *  [Entity Relationship Diagram](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md) # Needs Fixing
* [Testing](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Testing)
* [Deployment](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Deployment)
* * [Technologies Used](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Technologies)
* [Risk Assessment](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#br) # Needs Fixing
* [Front End Design](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md) # Needs Fixing
* * [Wireframes](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Wireframes)
* [Final appearence](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Final-appearence) # Needs Fixing
* [Author](https://github.com/Denzaaaaal/SFIA1/blob/developer/README.md#Author)

## Brief
To create an application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training. The application must manipulate two tables with full CRUD functionality.

### Solution
I have decided to create a online personal finance manager which allows the user to keep track of there income, expenses and investments based on the book called [Your Money or Your Life](https://www.amazon.co.uk/Transforming-Relationship-Achieving-Financial-Independence/dp/0143115766) written by Viki Robin and Joe Dominguez. Due to the ammount of data a individual would generate within all 3 catagories, a relational database would be extremely useful to drawing conclusions on where you are wasting money. 

### Trello Board



## Architecture

### Entity Relationship Diagram


## Testing
Testing wa. Urllib3 was used to determine if the pages can be called successfully by checking the code that is sent. The se

## Deployment

### Technologies Used
* Flask (Python based Web Application Framework)
* Python (Programming Language)
* HMTL (Programming language)
* CSS (Programming langauge)
* Git (Version Control System)
* Trello (Project Tracking Software)
* MySQL (Database)
* Bash (Shell Scripting lanugage)

## Risk Assessment
|Risk|Description|Hazard|Likelihood|Impact|Solution| 
|----|-----------|------|----------|------|--------|
|Project is not completed ontime|Due to poor time management, the project is not completed.|Worst case scenario, marks are lost due to lack of coverage of brief.|2|5|Make good use of Kanban to manage workflow, and efficient time use of office resources.|
|Being Hacked|Having your virtual machine being hacked|Will have to recreate program|1|5|Ensure that passwords have sufficient complexity and ports are closed off to the open internet|
|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|Worst case scenario, databases are unaccessable.|1|5|Continue monitoring GCP usage. Copy databases offline as final backup.|
|Database security: SQL|The GCP server is breached in some way, compromising data integrity.|Worst case scenario, data is lost, or user data is compromised.|3|5|Ensure user and personal data is encrypted, and passwords hashed, before being moved to the database.|
|Database security: SSH|Unmanaged connections cause data leak or damage, keys are lost or stolen.| Worst case scenario, GDPR noncompliance or total data compromisation.|2|5|Learn and make use of GCP's SSH key management role system, and implement it correctly.|
|Database security: SQL-I|Unsanitised user input allows SQL injection into the database.|Worst case scenario, database is maliciously destroyed.|2|5|Ensure any user accessible inputs are sanitised, and implement permission roles.|
|Flask password storage|Although Flask uses passwords fields, hashing isn't implemented natively.|Worst case scenario, hosted user data is found in contravension of GDPR regulation, incurring heavy fines.|4|4|Ensure hashing and data encryption is implemented before data is passed to the SQL server.|

## Front End Design

### Wireframes

### Final Appearence

## Improvements
* Create CSS for website
* Add Graph of account overview using D3

## Author
Denzel Douglas