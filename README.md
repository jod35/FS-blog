# FS-Blog (Full Stack Blog)
This is a simple application I am building to teach myself Full Stack Web Development. It has its backend in Python (Flask) and I am planning to build its frontend using a Javascript client-side technology such as React or Angular. (Will see about that later.)

## The Backend 
The backend is a REST API that serves data as JSON to the client. It uses JSON Web Token Auhtentication as a security measure.

### Built With
- Flask
- Flask-SQLAlchemy (Object Relational mapper for Flask and relational Databases)
- Flask-Mashmallow (Object serialization and deserialization package)
- Flask-JWT-Extended (JSON Web Token Auth for Flask)
- PyMySQL (Database Drive for Python and MySQL)
- Flask-Migrate (Database Migration tool based on Alembic)
- MySQL (A relational database)

### API EndPoints
| ROUTE | METHOD  | DESCRIPTION | JWT TOKEN REQUIRED |
|-------|---------|-------------|----------------|
| /users/ | GET    | Get all users  | False
| /user/id | GET   | Get an user with an id | False |
| /users/signup | POST  | create a new user | False  |
| /user/id | PUT   | Update info for a user with an id | True |
| /user/id | DELETE | Delete a user with an id | True |
| /auth/signin | POST  | Sign In With a Username and Password to get a JWT Token | False |
| /posts/    | GET   | Get all the posts | True |
| /post/id   | GET   | Get a post with an id | True |
| /posts/    | POST  | Create a new post | True |
| /post/id   | PUT  | Update a post with a given id | True |
| /post/id   | DELETE | Delete a post with a given id | True |
| /posts/user_id | GET | Get posts for a given user using their id | True |

### How to run the API
#### 1. Get the project
### `$ git clone https://github.com/jod35/FS-Blog.git`

#### 2. Install all dependencies
### ` $ cd FS-Blog `
### ` $ pip3 install -r reuirements.txt `

#### 3. Set Up the Database
-  Use MySQL to create a database called 'mydb'
-  Edit ` main/config.py ` change your db credentials 
### ` SQLALCHEMY_DATABASE_URI='mysql+pymysql://jona:<mydbusername>@localhost/mydb ` 
where `mydb` is the database and `mydbusername` is your database username.
-  Expose your app by running 
### ` export FLASK_APP=run.py `
-  Create database tables 
### ` flask db upgrade `

#### 4. Start the App
### ` flask run ` 
or 
### `python3 run.py`


## Author
[Ssali Jonathan (Jod35)](https://github.com/jod35)

## Contributions
I welcome all contributions.