pip install django
pip install gunicorn
rm /etc/nginx/sites-enabled/default
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
cp /home/box/web/etc/gunicorn-django.conf   /etc/gunicorn.d/
/etc/init.d/nginx restart
/etc/init.d/gunicorn restart