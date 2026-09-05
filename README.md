# Better Ships That Battle Better

A pirate-themed Django naval-combat project with player accounts and game-history features.

**Python · Django**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- Player registration and pirate profiles.
- Naval-combat views and game-state models.
- Battle statistics and dashboard templates.

> **Project notes:** The Django project is nested in better_ships_that_battle_better/. Historical Heroku links in the project record describe earlier deployments and are not a service-availability guarantee.

## Getting started

Requires Python, pip and a virtual environment. The repository records `3.11` in [.python-version](.python-version). Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better.git
cd Better-Ships-that-Battle-Better
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

After resolving the project notes and configuring the local environment, use:

```bash
cd better_ships_that_battle_better
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Configuration

Settings are defined in [better_ships_that_battle_better/better_ships_that_battle_better/settings.py](better_ships_that_battle_better/better_ships_that_battle_better/settings.py). Set the values used by your chosen local configuration before running Django. A `.env` file is only read when the project explicitly loads it; most of these projects read the process environment or an optional `env.py`.

| Variable | Purpose |
| --- | --- |
| `DEV` | Development-mode switch. Inspect whether the settings test its presence or its value. |
| `SECRET_KEY` | Django signing key. Use a locally generated value and keep it out of Git. |

Use a disposable development database for migrations and tests. Keep service credentials and local configuration out of commits.

## Repository guide

| Path | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [better_ships_that_battle_better/manage.py](better_ships_that_battle_better/manage.py) | Django management commands |
| [better_ships_that_battle_better/better_ships_that_battle_better/settings.py](better_ships_that_battle_better/better_ships_that_battle_better/settings.py) | Django configuration |
| [assets/](assets/) | Project styles, scripts, data and imagery |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Supporting notes: [USERNAME_VALIDATION_GUIDE.md](USERNAME_VALIDATION_GUIDE.md).

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

Hosting entry points are recorded in [Procfile](Procfile). Configure the runtime, database, allowed origins and static/media handling for the chosen host. Historical deployment records may describe services that are no longer available.

## Credits and reuse

Design decisions, original feature notes, historical testing evidence and detailed acknowledgements remain available in the preserved project record:

- [README.md · original project record](https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better/blob/5b5ad22513fd39e54b2692cc5e41bb4a5753bbea/README.md)

Learning resources and starter material: [Code Institute](https://codeinstitute.net/).

No repository-level licence file is present in this snapshot. This README does not grant additional reuse permissions. Check with the relevant rights holders before reusing code, written content or assets.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#better-ships-that-battle-better)
