# auth_service

Этот сервис отвечает за проверку подлинности и идентификацию пользователей, которые хотят воспользоваться сервисом обмена сообщениями. Этот сервис может принимать запросы на регистрацию, вход в систему, выход из системы и сброс пароля от клиентов. Этот сервис может хранить данные о пользователях в базе данных *Azure Cosmos DB* и *генерировать токены* для доступа к другим сервисам.

## Цель 

Создать сервис аутентификации, который отвечает за проверку подлинности и идентификации пользователей, которые хотят воспользоваться сервисом обмена сообщениями. Сервис аутентификации должен быть разработан на *Python* с использованием *FastAPI*(асинхронный) и интегрирован с *Azure Cosmos DB* для хранения данных о пользователях.

## Функциональность 

Сервис аутентификации должен предоставлять следующие API для клиентов:
- *Регистрация*: позволяет пользователю создать учетную запись с логином, паролем и электронной почтой. Пароль должен быть захеширован перед сохранением в базе данных. Пользователь должен получить подтверждение о успешной регистрации.
- *Вход в систему*: позволяет пользователю войти в систему с логином и паролем. Пароль должен быть проверен с хешем из базы данных. Пользователь должен получить токен доступа, который дает ему право обращаться к другим сервисам.
- *Выход из системы*: позволяет пользователю выйти из системы и аннулировать свой токен доступа. Пользователь должен получить подтверждение о успешном выходе из системы.
- *Сброс пароля*: позволяет пользователю сбросить свой пароль, если он его забыл или потерял. Пользователь должен указать свою электронную почту, на которую будет отправлен *шестизначный* код, с пощьмю которого можно будет осуществить сброс. Новый пароль должен быть захеширован и сохранен в базе данных. Пользователь должен получить подтверждение о успешном сбросе пароля.

## Технологии 

Сервис аутентификации должен использовать следующие технологии для разработки и развертывания:
- *Python*: язык программирования, на котором будет написан код сервиса аутентификации.
- *FastAPI*: фреймворк для создания и тестирования API на Python с высокой производительностью и простотой использования.
- *Azure Cosmos DB*: облачная база данных, которая поддерживает разные модели данных, такие как документы, графы или ключ-значение. Будет использоваться для хранения данных о пользователях.
- ??? возможно можно использовать кэш хранилище для хранение ключей, и временных данных пользователя(информация о пользователе при регистрации, код потверждения)

## Требования 
asdadsad
Сервис аутентификации должен соответствовать следующим требованиям по качеству и безопасности:
- *Надежность*: сервис аутентификации должен быть доступен и работоспособен в любое время и при любых условиях. Сервис аутентификации должен обрабатывать ошибки и исключения и возвращать корректные ответы клиентам.
- *Производительность*: сервис аутентификации должен обеспечивать быстрый и эффективный обмен данными между клиентами и сервером. Сервис аутентификации должен масштабироваться и балансироваться по нагрузке в зависимости от количества и активности пользователей.
- *Безопасность*: сервис аутентификации должен защищать данные и личность пользователей от несанкционированного доступа и утечки. Сервис аутентификации должен использовать _шифрование_, _хеширование_ и _токены_ для обеспечения безопасности паролей и сессий пользователей. Сервис аутентификации должен соблюдать стандарты и нормативы по безопасности, такие как _OAuth 2.0_ и _OpenID Connect_.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m auth_service
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "auth_service"
auth_service
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "AUTH_SERVICE_" prefix.

For example if you see in your "auth_service/settings.py" a variable named like
`random_parameter`, you should provide the "AUTH_SERVICE_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `auth_service.settings.Settings.Config`.

An example of .env file:
```bash
AUTH_SERVICE_RELOAD="True"
AUTH_SERVICE_PORT="8000"
AUTH_SERVICE_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations until the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=auth_service" -e "POSTGRES_USER=auth_service" -e "POSTGRES_DB=auth_service" postgres:13.8-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```
