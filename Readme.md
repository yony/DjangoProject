# Django + PostgreSQL in Docker

A containerized Django application with a PostgreSQL database, designed for rapid development and easy deployment using Docker and Docker Compose.

---

## Features

- Django 4.x+ backend
- PostgreSQL as the primary database
- Docker & Docker Compose for isolated, reproducible environments
- `.env` file support for configuration
- Volume-mounted code for hot-reloading in development
- Persistent database storage
- Optional support for Django Debug Toolbar

---

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```


### 2. Create and configure your .env file

```bash
cp .env.example .env
```

Update values like:
```.env
DEBUG=1
SECRET_KEY=your-secret-key
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### 3. Build and run the containers

```bash
docker-compose up --build
```

This will:
- Build the Docker image for Django
- Spin up the PostgreSQL service
- Run migrations and start the development server on http://localhost:8000

## Project Structure

``` 
your-project/
├── app/                    # Django app source code
│   ├── manage.py
│   └── your_project/
│       └── settings.py
├── db/                     # PostgreSQL data volume (optional)
├── Dockerfile              # Docker build config for Django
├── docker-compose.yml      # Compose file to orchestrate services
├── .env                    # Environment variables
└── requirements.txt        # Python dependencies

```

## Database Access
- Host: localhost (inside containers: db)
- Port: 5432
- User/Password: Defined in .env

You can access the DB with tools like psql, DBeaver, or pgAdmin.

## 🧪 Run Management Commands

``` bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell
```

## Installing New Python Packages

To install a new package:

``` bash
docker-compose exec web pip install <package-name>
docker-compose exec web pip freeze > requirements.txt
```

## Useful Commands
| Task                            | Command                                                     |
| :-------------------------------|:------------------------------------------------------------|
| Run server                      | docker-compose up                                           |
| Run migrations                  | docker-compose exec web python manage.py migrate            | 
| Create superuser                | docker-compose exec web python manage.py createsuperuser    |
| Collect static files            | docker-compose exec web python manage.py collectstatic      |
| Access bash inside container    | docker-compose exec web bash                                |


## Security & Secrets
Never commit .env files with secrets to version control. Use .gitignore to exclude them.

## License

MIT © YAM

