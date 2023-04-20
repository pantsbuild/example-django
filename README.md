# example-django

An example repository to demonstrate Django support in Pants.

The demo consists of a set of services that implement an elaborate "Hello, World" site.
This repo shows how Pants can support multiple Django services in a single repo, with
minimal copypasta.

The layout in this repos enforces a strict distinction between Django apps (reusable units of
functionality such as models and related views), vs. services ("projects" in Django parlance) -
deployable services composed of multiple apps and typically attached to one or more database instances.

See [pantsbuild.org](https://www.pantsbuild.org/) for much more detailed documentation about Pants.

See [here](https://github.com/pantsbuild/example-python) for an example of basic Python support in Pants.

See [here](https://www.pantsbuild.org/docs/installation) for how to install the `pants` binary.

## Architecture

We utilize a flexible "database-first" architecture: Since migrating production databases
is significantly harder and riskier than modifying stateless services, our architecture treats
the databases as standalone logical entities not subservient to any app or service.
"Code is for now, data is forever."

- The models in each app map to one of the logical databases, via a custom
  [database router](helloworld/util/per_app_db_router.py).
- The settings for each server map the logical databases required by its apps to physical databases.

If it makes sense to do so, different services can reuse the same app in different databases, by
pointing the same logical database at different physical databases in each service.

The only constraint is that if a model in one app reference a model in another app via foreign key
then both apps must be mapped to the same logical db. You can see an example of this in
[helloworld/translate/models.py](helloworld/translate/models.py).

This architecture allows services to evolve in a flexible way as more apps and more functionality
are developed.

## Databases

In order to demonstrate multi-db configurations, there are two logical databases:

- `users`: User-related data.
- `greetings`: Greeting-related data.

Currently the services map these logical databases to sqlite dbs.
We plan to add examples of using PostgreSQL.

## Services

 There are four distinct services, defined under [`helloworld/service`](helloworld/service):

- `helloworld.services.admin`: Runs the Django admin UI.
- `helloworld.services.frontend`: Serves end user requests.
- `helloworld.services.user`: A backend service that provides user data.
- `helloworld.services.welcome`: A backend service that generates greetings.

Each service has its own `manage.py`, `gunicorn.py`, `urls.py` and `settings.py`.
The `settings.py` inherits most of its settings from [`helloworld/settings_base.py`](helloworld/settings_base.py)
and adds anything specific to that service.

Note that we make no argument for or against microservices vs. monolithic services as a deployment
architecture. We *do* make an argument in favor of a monorepo over multiple repos as a codebase architecture,
and this repo demonstrates the utility of a monorepo, especially if you deploy multiple services.

## Apps

The services are composed of four Django apps:

- `helloworld.greet`: Functionality related to selecting a greeting.
- `helloworld.person`: Functionality related to identifying the person to greet.
- `helloworld.translate`: Functionality related to translating greetings into various languages.
- `helloworld.ui`: Functionality related to rendering greetings to the end user.

## To view the frontend:

In three terminals run:
- `pants --concurrent run helloworld/service/frontend/manage.py -- runserver`
- `pants --concurrent run helloworld/service/user/manage.py -- runserver`
- `pants --concurrent run helloworld/service/welcome/manage.py -- runserver`

And visit this URL in a browser: [http://127.0.0.1:8000/?person=sherlock&lang=es]() .
You will have to first set up a database and run migrations, of course.

## Useful Pants commands

To run all tests:

```
pants test ::
```

To run formatters and linters:

```
pants fmt lint ::
```

To run typechecking:

```
pants check ::
```

To build deployable gunicorn .pex files for all services:

```
pants package ::
```

## manage.py

To run management commands for a service, use that service's `manage.py`, e.g.,

```
pants run helloworld/service/admin/manage.py -- runserver
```

 Note that for `runserver`, each dev server will run on its own port, see DEV_PORTS in
[`helloworld/util/discovery.py`](helloworld/util/discovery.py).

Also, with `runserver` we [turn off](helloworld/util/service.py#L40) Django's autoreloader.
Instead, we rely on Pants's own file-watching, by setting `restartable=True` on `manage.py`.
Pants will correctly restart servers in situations where Django cannot, such as changes to 
BUILD files, to `.proto` files, or to 3rdparty dependencies.

To run migrations, it's best to use the admin service's manage.py, as it has access to
all apps:

```
pants run helloworld/service/admin/manage.py -- migrate --database=users
pants run helloworld/service/admin/manage.py -- migrate --database=greetings
```
