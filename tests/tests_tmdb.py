import pytest
from unittest.mock import Mock
import requests
import sys
from main import app
sys.path.insert(0, 'C:\\Users\\User\\Desktop\\Projekty\\movies_project\\movies_catalogue') 
import tmdb_client
from tmdb_client import API_TOKEN
STATUS_CODE_OK = 200

def test_get_poster_url_uses_default_size():
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   assert expected_default_size in poster_url

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie_cast(monkeypatch):
   api_mock = Mock(return_value={'cast':['Actor 1','Actor 2']})
   movie_id = 10
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
   get_movie_cast = tmdb_client.get_single_movie_cast(movie_id=movie_id)
   assert get_movie_cast is not None 


def test_get_movies_returns_right_amount_of_movies(monkeypatch):
   api_mock = Mock(return_value={'results':['Movie 1','Movie 2', 'Movie 3', 'Movie 4', 'Movie 5']})
   how_many_movies = 3
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
   get_movies = tmdb_client.get_movies(how_many=how_many_movies)
   assert how_many_movies == len(get_movies)

def test_get_single_movie_cast_check_api_endpoint():
   movie_id = 20
   headers = {
      "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits", headers=headers)
   assert response.status_code == 200

def test_get_single_movie_check_api_endpoint():
   movie_id = 20
   headers = {
      "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers)
   assert response.status_code == 200

@pytest.mark.parametrize('list_type',[('popular'),('top_rated'),('upcoming'),('now_playing')])
def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
   with app.test_client() as client:
      response = client.get('/')
      assert response.status_code == STATUS_CODE_OK
      api_mock.assert_called_once_with('movie/popular') 
      response = client.get(f'/?list_type={list_type}')
      assert response.status_code == STATUS_CODE_OK
      api_mock.assert_called_with(f'movie/{list_type}')










