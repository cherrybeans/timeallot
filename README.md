# timeallot

Backend in Django REST framework for the focus timer timeallot.


## Setup virtualenv

### Setup virtualenvwrapper
Requires installed [virtualenv](https://virtualenv.pypa.io/en/stable/) and Python 3.6.1. <br>
Used this for guide: http://railslide.io/virtualenvwrapper-python3.html

To setup [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), put this in some file somewhere that
might be located differently on different systems.
In my case on Ubuntu this file is found by the following command (I use the zsh shell, hence the different than usual file).
```sh
$ vim ~/.zshrc
```
Put this in at the bottom of the file.
```
export WORKON_HOME=~=$HOME/virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
export PROJECT_HOME=$HOME/code
source ~/.local/bin/virtualenvwrapper.sh
```

### Create virtualenv with virtualenvwrapper:
```sh
$ mkproject -p python3.6 timeallot
```
There is a `mkvirtualenv` command as well that worked for me before, but it does not move me into the project folder after jumping into the project with `workon` anymore, and only activates the virtual environment, which is strange. At least this works.

#### Adding/Upgrading packages
To install packages
```sh
$ pip install -r requirements.txt
```

I use [pip-tools](https://github.com/jazzband/pip-tools) to make the requirement files easy to understand.
Update ```requirements.in``` with new packages then run the following command to update ```requirements.txt```
```sh
$ pip-compile > requirements.txt
```

To sync your virtual environment with the generated `.txt` files, 
use `pip-sync`. If given no argument, it syncs based on `requirements.txt`. 
It can take several files as input, like this:
```
pip-sync development.txt requirements.txt
```

### Upgrade Python version in virtual environment
To do this you have to remove the old virtual environment and create a new one
and reinstall all dependencies. (https://stackoverflow.com/a/44477446)


1. Deactivate and remove the old virtual environment (assuming you have used ```workon timeallot``` beforehand):
```sh
$ deactivate
$ rmvirtualenv timeallot
```
2. Stash the real project in a temp directory:
```sh
$ cd ..
$ mv timeallot timeallot-tmp
```
3. Create the new virtual environment (and project dir) and activate:
```
$ mkproject -p python3.6 timeallot
```
4. Replace the empty generated dir with real dir, and change back into project dir:
```sh
$ cd ..
$ mv -f timeallot-tmp/.* timeallot
$ cd timeallot
```
5. Confirm new Python version and re-install dependencies:
```sh
$ python --version
$ pip install -r requirements.txt
```

## Virtualenvwrapper commands
Enter the virtualenvironment from anywhere. This navigates you to the
project folder and activates the virtual environment.
```sh
$ workon timeallot
```

## Loading fixtures
### One by one
```sh
$ python manage.py loaddata <nameoffixture>.yaml
```
### All at once
Made a custom management command for loading all fixtures at once.
```sh
$ python manage.py load_fixtures
```
This only loads fixtures that have been added in the command, so to add
new fixtures, add them in ```utils/management/commands/load_fixtures.py```.
