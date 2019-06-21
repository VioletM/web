sudo cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application