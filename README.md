<h1>Online store made using Django</h1>
<hr>
It's a Django project of online bedding store with a shopping cart, user profile, async order processing which i implemented using Celery and RabbitMQ. For the front end I used bootstrap.
<h2>Launching</h2>
<hr>
1. Clone the repository or download the code in a ZIP archive and extract it to your computer
2. Create a virtual environment and activate it
<code>python -m venv venv</code><br>
<code>source venv/bin/activate</code><br>
3. Install requirements
<code>pip install -r requirements.txt</code><br>
4. Create and fill ".env" file with a template ".env.example"
5. Make migrations and init the db
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code><br>
6. Create superuser for admin page
<code>python manage.py createsuperuser</code>
7. Install RabbitMQ
You can find installing guide here: https://www.rabbitmq.com/docs/download
8. Open terminal and run Celery and RabbitMQ
<code>rabbitmq-server</code><br>
<code>celery -A mashop worker -l info</code><br>
<code>celery -A mashop flower</code><br>
9. Run the server
<code>python manage.py runserver</code>
10. Now you can open http://127.0.0.1:8000/ and see the store working
