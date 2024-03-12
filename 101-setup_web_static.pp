#Puppet execution.
exec {'web_static':
command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && echo "<!DOCTYPE html> <html> <head> </head> <body> Holberton School </body> </html>" | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data/ && sudo sed -i "51i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;}" /etc/nginx/sites-available/default && sudo service nginx reload && sudo service nginx restart',
provider => shell,
}
