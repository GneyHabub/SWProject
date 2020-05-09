# SWProject
##### You can check out our project now at http://34.65.251.9/polls/login_student/ 
Innopolis University, Spring semester 2020.\
Staff assesment and ranking system for Innopolis University.\
Software project by Alexander Krivonosov, Polina Turishcheva, Rufina Sirgalina, Vladislav Kalmyikov

### Dependencies
Python dependencies are listed in requirements.txt, so you can run 
____$ python3 -m pip install -r requirements.txt____
to install all the necessary python requirements

Additionaly SQLite 3.8.3+ is required to support the database

### Running the project
just go to __SWProject/mysite__ and run
____$ python3 manage.py runserver____
to run a server that is available at localhost:8000
alternatively, if you want the app to be available to everyone on the network, run
____$ python3 manage.py runserver 0:<port>____
where <port> is your favorite port number,
this way anyone in your subnet will be able to access the application at _http://<your_ip>:<port>/polls/login_student_