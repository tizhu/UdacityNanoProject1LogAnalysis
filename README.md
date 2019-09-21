Los Analysis Internal Reporting Tool
There are three functions written in python in the los analysis tool help us find What are the most popular three articles of all time,Who are the most popular article authors of all time and On which days did more than 1% of requests lead to errors

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

Prerequisites
We need vagrant, virtualbox to bring virtual machine. We also need to import log data to run the reports.

Installing
Download vagrant: https://www.vagrantup.com/downloads.html
Download VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
Download VM configuration files: https://github.com/udacity/fullstack-nanodegree-vm
Import the data from the newsdata.sql file: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Save the newsdata.sql in the the folder /fullstack-nanodegree-vm-master/vagrant/(previously downloaded)
After installed Vagrant and VirtualBox, we cd into /fullstack-nanodegree-vm-master/vagrant/, run vagrant up, then run vagrant ssh, then cd /vagrant.
After connected with virtual machine, we run "psql -d news -f newsdata.sql" to import data.
Run "python LogAnalysis.py", we will see our reports printing in the terminal.

Authors
Tingting Zhu - Initial work
