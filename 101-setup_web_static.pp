# Puppet for setup Redo the task #0 but by using Puppet:
exec { "Preparing_Server":
command => "sudo apt-get update && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && echo 'Holberton School' | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data/ && var='location /hbnb_static {\n\t\talias /data/web_static/current/;}' && sudo sed -i "44i$var" /etc/nginx/sites-available/default && sudo service nginx reload && sudo service nginx restart"
provider => "shell"
}
