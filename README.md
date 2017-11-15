# timeallot

Backend in Django REST for the focus timer timeallot.


## Setup virtualenv

### Setup virtualenvwrapper
Requires installed virtualenv. Google it.
Used this for guide: http://railslide.io/virtualenvwrapper-python3.html

To setup virtualenvwrapper, put this in some file somewhere that depends on your computer xD
```
vim ~/.zshrc
```

```
export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
export PROJECT_HOME=$HOME/code
source ~/.local/bin/virtualenvwrapper.sh
```

### Create virtualenv with virtualenvwrapper:
```
mkvirtualenv timeallot
```

#### Adding/Upgrading packages
To install packages
```
pip install -r requirements.txt
```

Update ```requirements.in``` with new packages then run the following command to update ```requirements.txt```
```
pip-compile > requirements.txt
```


## Loading fixtures
### One by one
```
python manage.py loaddata <nameoffixture>.yaml
```
### All at once
Added a custom management command for loading all fixtures at once.
```
python manage.py load_fixtures
```
This only loads fixtures that have been added in the command, so to add
new fixtures, add it in ```utils/management/commands/load_fixtures.py```.