ssh $USER@$HOST
cd /home/cd-example
pip install --upgrade pip
pip install -U -r requirements.txt
systemctl -H $USER@$HOST restart cd-example