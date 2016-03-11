mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
				 GRANT ALL ON qa.* TO 'qauser'@'localhost';"

sudo python /home/box/web/ask/manage.py syncdb