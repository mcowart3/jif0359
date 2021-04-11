# Application Setup

## Installing Dependencies

### Packages

To run this project, you'll need the following applications:

- MongoDB
- Python3
- Docker

The easiest way to install these is to use [Homebrew](https://brew.sh/#install). Once Homebrew is installed, run the following:

#### Docker

`brew cask install docker`

#### Python3

`brew install python3`

#### MongoDB

`brew tap mongodb/brew`
`brew install mongodb-community@4.4`

### Installing Packages

Next, install the packages for the python application. To do that,
run the following (assuming you're in the `backEnd` folder):

`pip3 install -r requirements.txt`

... I think this will go away with docker, but IDK.

## Running Application

### Running MongoDB Server

`brew services start mongodb/brew/mongodb-community`

### Running Flask

`python3 -m flask run`

## API Usage

`http://localhost:5000/documents`
`http://localhost:5000/documents/<id>`
`http://localhost:5000/search/<term>` (doesn't work?)
`http://localhost:5000/sort/title/ascending`

## Initial set up:

### Windows:

Install the Community Version with the UI\
Open the application

#### Linux:

Install the shell version
run "sudo service mongod start" in your shell

### Working with the DB:

MongoDB essentially works by keeping a big collection of dicts, each of which will represent a document for us. You can see the (currently) basic set up actions we take with the Database by looking at database.py. There are also two example documents
so you can see the form a document takes. There is also an example query to find documents.

---

## Conda (WILL REMOVE)

Activate the environment after you create the environment: `conda activate lms`
Create an environment from the .yaml `conda env create --file environment.yaml`
Install new dependencies: `conda env update --file environment.yaml`
Add a new dependency: `conda install packageName`
You've gotta update the environment.yaml by hand though.

Note for windows users: Conda will not work with powershell :(
