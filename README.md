# example-django

An example repository to demonstrate Django support in Pants.

The demo consists of a set of microservices that implement an elaborate "Hello, World" site.
This repo shows how Pants can support multiple Django services in a single repo, with
minimal copypasta.

The layout in this repos enforces a strict distinction between Django apps (reusable units of
functionality such as models and related views), vs. services ("projects" in Django parlance) -
deployable services composed of multiple apps and typically attached to one or more database instances.

See [pantsbuild.org](https://www.pantsbuild.org/) for much more detailed documentation about Pants.

See [here](https://github.com/pantsbuild/example-python) for an example of basic Python support in Pants.

## Services

 There are four distinct services, defined under [`helloworld/services`](helloworld/services):

- `helloworld.services.admin`: Runs the Django admin UI.
- `helloworld.services.frontend`: Serves end user requests.
- `helloworld.services.user`: A backend service that provides user data.
- `helloworld.services.welcome`: A backend service that generates greetings.

Each service has its own `manage.py`, `gunicorn.py`, `urls.py` and `settings.py`.
The `settings.py` inherits most of its settings from [`helloworld/settings_base.py`](helloworld/settings_base.py)
and adds anything specific to that service.

Note that we make no argument for or against microservices vs. monolithic services as a deployment
architecture. We *do* make an argument in favor of a monorepo over multiple repos as a codebase architecture,
and this repo demonstrates the utility of a monorepo even if (especially if!) you deploy microservices.

## Apps

The services are composed of four Django apps:

- `helloworld.greet`: Functionality related to selecting a greeting.
- `helloworld.person`: Functionality related to identifying the person to greet.
- `helloworld.translate`: Functionality related to translating greetings into various languages.
- `helloworld.ui`: Functionality related to rendering greetings to the end user.

## Databases

In order to demonstrate multi-db configurations, there are two databases:

- `users`: User-related data.
- `greetings`: Greeting-related data.

Each app is associated with exactly one database.

Currently these are sqlite. We plan to add examples of using PostgreSQL.

## Useful Pants commands

To run all tests:

```
./pants test ::
```

To run formatters and linters:

```
./pants fmt lint validate ::
```

To run typechecking:

```
./pants typecheck ::
```

To build deployable gunicorn .pex files for all services:

```
./pants package ::
```

## manage.py

To run management commands for a service, use that service's `manage.py`, e.g.,

```
./helloworld/service/admin/manage.py runserver
```

 Note that for `runserver`, each dev server will run on its own port, see DEV_PORTS in
[`settings_base.py`](helloworld/settings_base.py).

To run migrations, it's best to use the admin service's manage.py, as it has access to
all apps:

```
./helloworld/service/admin/manage.py migrate --database=users --database=greetings
```
