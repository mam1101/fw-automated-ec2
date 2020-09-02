sudo apt update
sudo apt install -y nginx
sudo ufw allow 'Nginx HTTP'
python3 -V
python3 -m venv ~/venv
source ~/venv/bin/activate
pip install Django==3.1.1
