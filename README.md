Hi there,
In order to start project you need to either execute first or second below:

Unix platform:
- pip3 install -r requirements.txt
- python3 manage.py migrate
- python3 main.py

Windows:
- pip install -r requirements.txt
- python manage.py migrate
- python main.py

or just run:
- python main.py

Meanwhile, I have completed with testing cases coverage, there was 76% percentage coveraged.
You can use following commands:
- pip install coverage
- coverage run --source='.' manage.py test
- coverage report

