ssh $USER@$HOST
cd /home/cd-example
pip install --upgrade pip
pip install -U -r requirements.txt
ssh $USER@$HOST -t systemctl restart cd-example