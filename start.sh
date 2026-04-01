root_password="12345678"

echo $root_password | su -c "

dnf install python3-pip -y
pip3 install playwright
playwright install chromium

python main.py

shutdown

"
