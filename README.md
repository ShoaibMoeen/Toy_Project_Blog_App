# Toy Project Blog App for Link Graph

The blog app is developed using django and deployed to the following heroku link using docker:

https://toyproject-linkgraph.herokuapp.com/

Requirement needed to run the project:
1. Python
2. Django
3. Anaconda Prompt
4. PostgreSQL
5. pgAdmin4
6. Docker

Code can be exectued using following steps:

1. Clone the git project
2. Create a virtual environment using conda and run the requirements.txt to install the requirements
3. Open pgAdmin and create a local PostgreSQL database
4. Update the database in the settings.py file to the local database just created
5. Execute 'docker-compose build' command on the terminal
6. Execute 'docker-compose up' command on the terminal
7. The server should start and you can reach it via localhost:8000


Screenshots:

Login Screen
![Alt text](https://github.com/ShoaibMoeen/Toy_Project_Blog_App/blob/main/Screenshots/Login_screen.JPG "Login")

Home Screen
![Alt text](https://github.com/ShoaibMoeen/Toy_Project_Blog_App/blob/main/Screenshots/home_screen.JPG "Home")

Edited Screen
![Alt text](https://github.com/ShoaibMoeen/Toy_Project_Blog_App/blob/main/Screenshots/edited_articles.JPG "edited")

Create Article Screen
![Alt text](https://github.com/ShoaibMoeen/Toy_Project_Blog_App/blob/main/Screenshots/create_article.JPG "Create")

Article Approval Screen
![Alt text](https://github.com/ShoaibMoeen/Toy_Project_Blog_App/blob/main/Screenshots/article_approval.JPG "Approve")

