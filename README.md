# Introduction : 
* This is a Python 3 script which when scheduled to run every 10 minutes on a system (using cronjob on linux), checks for new announcements on my college website and if there are any new announcements, it will send emails to given addresses contaning link for announcements.

# Working :
* This program creates two file in Home directory named as :  
**.notification**  
**log.txt**  
* ".notification" is a hidden file use to store the data of last announcement.  
* "log.txt" is a log file get appended with Execution status (Success or Failed) alongwith the time and date of execution of program.  
* When program is executed, it first compares the current announcements on website with the last announcements in ".notification" file.  
If both are different then it will send the new notifications to registered addresses and then updates the ".notificaton" to current data for future use and updates log file and exits.  
If both are same then program just log into log file and exits.

**Python Libraries Used :**  
* **smtplib, ssl** : To send email
* **requests, bs4** : To fetch data from website
