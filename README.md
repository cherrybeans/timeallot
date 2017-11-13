# timeallot

Backend in Django REST for the focus timer timeallot.


## Setup virtualenv

### Setup virtualenvwrapper
Requires installed virtualenv. Google it.
Used this for guide: http://railslide.io/virtualenvwrapper-python3.html

To setup virtualenvwrapper, put this in some file somewhere that depends on your computer
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

