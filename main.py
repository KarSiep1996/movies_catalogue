from flask import Flask, render_template
import tmdb_client
from flask import request
from tmdb_client import lists

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    if selected_list == 'top_rated':
        template="homepage_top_rated.html"
    elif selected_list == 'upcoming':
        template="homepage_upcoming.html"
    elif selected_list == 'now_playing':
        template="homepage_now_playing.html"
    else:
        template="homepage.html"
    return render_template(template, movies=movies, current_list=selected_list, lists=lists)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)

@app.route('/search')
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)