root_password="12345678"

echo $root_password | su -c "

pip3 install playwright
playwright install chromium

python main.py
"
