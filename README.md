# Log-Analysis
The log analysis is an internal reporting tool that uses information from a fictional news database to discover what kind of articles  the site's readers like using python and postgresSQL. 

The following is the kind of data that can be retrieved using this tool :

1. What are the most popular three articles of all time?

Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views


2.Who are the most popular article authors of all time?

Ursula La Multa - 507594
Rudolf von Treppenwitz - 423457
Anonymous Contributor - 170098
Markoff Chaney - 84557


3.On which days did more than 1% of requests lead to errors?

17 Jul 2016 - 2.26 % errors



# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Prerequisites
1. Virtual Box - https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
2. Vagrant - https://www.vagrantup.com/downloads.html
3. VM configuration -  You can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
4. newsdata.sql - You can find it in this repository. 

### Running
Copy the *.sql to the vagrant news folder. 
Execute the following in this order:
vagrant up
vagrant ssh 
cd /vagrant/news
python news.py

#### Versioning
Version 1.0 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


#### Authors
Suchita Kaundin 

#### Acknowledgments
Udacity and all the mentors 
