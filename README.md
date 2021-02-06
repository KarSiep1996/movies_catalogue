# Movies catalogue
>Web application created to find information about movies stored in The Movie Database API (TNDb).

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Structure](#structure)
* [Status](#status)
* [Contact](#contact)

## General info
Web application created to find information about movies stored in The Movie Database API (TNDb). List of required packages can be found in requirements.txt. It was deployed using Heroku (link to heroku app: https://my-movies-library.herokuapp.com/).

## Technologies
* Python3 
* Flask
* HTML
* CSS
* Bootstrap

## Structure

| Endpoint          | HTTP method        | Result                                         |
| ----------------  | :----------------: | :---------------------------------------------:| 
| /                 | GET                | Get 8 movies of chosen category                |
| /movie/<movie_id> | GET                | Get details of movie with certain id           |
| /search           | GET                | Get list of movies that match the search       |
| /today            | GET                | Get list of movies that are on TV today        |
| /favorites        | GET                | Get list of movies that were add to favourites |
| /favorites/add    | POST               | Add certain position to favourites             |


## Status
Project is: _in progress_

## Contact
Feel free to contact me :)
E-mail: karsiep1996@gmail.com
