import requests

url = "https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNmY2YjNjZDE5MjRmZjYyZjk4ZmFiOWEyNmM3MWNhNCIsInN1YiI6IjY0ZTNhOGQyMDZmOTg0MDBhZTQ2YWI0YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.L3gox5NNe9ryma5DXmOrAGo1srOEDjgucauzJFBcJc0"
}

response = requests.get(url, headers=headers)

print(response.text)