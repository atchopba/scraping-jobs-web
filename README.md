python -m flask run

# Project Title

Extraction of job offers from indeed.fr, apec.fr, monster.fr... in an IHM.

## What is this repository for? 

Scraping jobs is the extraction of key information about jobs through a search on a site. Here, there are: apec.fr, indeed.fr, monster.fr

## Benefices 

* Make it easier to find a job

* Gather information from several sites.

* Provide an IHM

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Windows 7+ or Linux kernel version 3.10 or higher
* 2.00 GB of RAM
* 3.00 GB of available disk space

Use with Docker http://www.docker.io

### Installation

To build an image with docker is pretty simple:
```
docker build -t jobs-cli .
```

## Running the tests

Then to run that image and attach to it at the same time:
```
docker run jobs-cli 
```

Go to your web navigator: http://127.0.0.1:5000/

## License & copyright

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details