python3 -m venv /tmp/venv

source /tmp/venv/bin/activate

pip show flask &> /dev/null || pip install flask && echo "flask installed."

pip show requests &> /dev/null || pip install requests && echo "requests installed."

pip show beautifulsoup4 &> /dev/null || pip install beautifulsoup4 && echo "beautifulsoup4 installed."

paver
