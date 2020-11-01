import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTY3ZDJjYTA5OWU0MjI1Yjg5MTcyOGFhYmY5NDRlZSIsInN1YiI6IjVmOTJmODEyYzFmZmJkMDAzN2E1ZTdiNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bL-8CnSflZX5QG6cbQq85dEkCfI66xdtfjbNCVGt7z4"

lists = ['popular', 'now_playing', 'top_rated', 'upcoming']

def get_movies_list(list_type):
    if list_type != lists[0] and list_type != lists[1] and list_type != lists[2] and list_type != lists[3]:
        list_type = "popular"
    else:
        list_type = list_type
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


