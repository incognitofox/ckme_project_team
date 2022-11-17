# CKME Address Validation

needs work

## Directory Structure

Our current directory looks like this. You can ignore everything here except for `validate.py`. In `validate.py` there is a function called `validate` that takes in a DataFrame, and modifies it inplace (ideally with cleaned addresses).

```
.
├── LICENSE
├── Procfile
├── README.md
├── __pycache__
│   ├── addr_search.cpython-38.pyc
│   ├── keys.cpython-38.pyc
│   └── validate.cpython-38.pyc
├── index.py
├── requirements.txt
├── templates
│   └── index.html
├── testing
│   ├── addr_search.py
│   ├── addresses.csv
│   ├── clean_addresses.py
│   ├── keys.py
│   ├── test.csv
│   ├── test_cleaned.csv
│   ├── test_removed.csv
│   └── validate_address.py
├── uploads
│   ├── EndoInnov_moments.csv
│   └── EndoInnov_results.csv
└── validate.py
```

Now, for those interested:

- `Procfile` is used by Heroku to host the server. It tells Heroku where our backend is so Heroku knows what to run and how to run it.
- `index.py` contains all of our endpoints. This is our server backend.
- `requirements.txt` contains a list of all the packages we are using, so Heroku knows what to install. You can also use this yourself by running `pip install requirements.txt`, which will install all the packages listed.
- `template/index.html` contains the html of our page. As of right now, all it does is allow you to upload a file, an download our output.
- `uploads` contains all the files users have uploaded. This is a huge security risk so we'll get rid of this eventually (ie don't save all the files users upload). The files in there right now are just files I've been testing with.
