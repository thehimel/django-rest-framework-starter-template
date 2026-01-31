echo "Upgrading pip..."
python3 -m pip install --upgrade pip setuptools

echo "Installing packages..."
pip3 install -r requirements.txt

echo "Installing pre-commit hooks..."
pre-commit install

echo "Migrating Database..."
python3 manage.py makemigrations
python3 manage.py migrate
