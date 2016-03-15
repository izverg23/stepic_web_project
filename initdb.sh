sudo rm -r /etc/mysql/my.cnf
sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
				 GRANT ALL ON qa.* TO 'qauser'@'localhost';"

sudo python /home/box/web/ask/manage.py syncdb