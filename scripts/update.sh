ssh ${{ secrets.USERNAME }}@${{ secrets.HOST }}
cd /home/cd-example
pip install --upgrade pip
pip install -r requirements.txt
