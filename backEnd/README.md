# Application Setup

## Installing Dependencies

### Packages

To run this project, you'll need the following applications:

- Docker

The easiest way to install these is to use [Homebrew](https://brew.sh/#install). Once Homebrew is installed, run the following:

#### Docker

`brew cask install docker`

## Running Application

Run this application by running `docker-compose up` in the main folder. The container for the back-end app will spin up, along with the client and database.

## API Usage

`http://localhost:5000/documents`
`http://localhost:5000/documents/<id>`
`http://localhost:5000/search/<term>` (doesn't work?)
`http://localhost:5000/sort/title/ascending`

### Working with the DB:

MongoDB essentially works by keeping a big collection of dicts, each of which will represent a document for us. You can see the (currently) basic set up actions we take with the Database by looking at database.py. There are also two example documents so you can see the form a document takes. There is also an example query to find documents.
