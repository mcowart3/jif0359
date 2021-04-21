## Conda

Activate the environment after you create the environment: `conda activate lms`
Create an environment from the .yaml `conda env create --file environment.yaml`
Install new dependencies: `conda env update --file environment.yaml`
Add a new dependency: `conda install packageName`
You've gotta update the environment.yaml by hand though.

Note for windows users: Conda will not work with powershell :(

## Serving with Flask

In the /frontEnd directory, run `npm run build`.
After this command, you should notice that the static and templates folders are populated.
Now, in the /backEnd directory, run `python3 app.py`.
The application should be available at the IP and port specified in the app.py.


## DB Stuff

### Initial set up:
#### Windows:
Install the Community Version with the UI\
Open the application

#### Linux:
Install the shell version
run "sudo service mongod start" in your shell

#### Populate your local DB:
In the /scripts directory, run the following command: `python3 driver.py`


### Working with the DB:
MongoDB essentially works by keeping a big collection of dicts, each of which will
represent a document for us. You can see the (currently) basic set up actions we take
with the Database by looking at database.py. There are also two example documents
so you can see the form a document takes. There is also an example query to find documents.
