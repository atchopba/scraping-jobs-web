# scraping-jobs-web

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
docker build -t jobs-cli-web .
```

## Running the tests

Then to run that image and attach to it at the same time:
```
docker run -p 5000:5000 jobs-cli-web
```

Go to your web browser: http://localhost:5000/

#### Screenshots
1. When lauching page in your web browser. 

![Page index](static/images/01-search.png)

2. When you type four letters, the code goes to a json file for the city. That's what justifies the search time.

![Page index](static/images/02-search.png)

3. Then, many propositions display. Choose one.

![Page index](static/images/03-search.png)

4. When you validate your search, the code goes looking for jobs on apec.fr/Indeed.fr/monster.fr. So you have to wait for the search to be done.

![Page index](static/images/04-search.png)

5. Finally, you got the search results.

![Page index](static/images/05-search.png)

## License & copyright

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details
