sudo cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
