import requests 

class BeatifyClient:

    # Artist resource request methods via requests.Session()
    def __init__(self):
        self.base_url = "http://130.162.240.153:5000"
        self.session = requests.Session()

    def get_artists(self):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/artists")
        json_response = response.json()
        return json_response
    
    def get_artist(self, id):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/artists/{id}")
        json_response = response.json()
        return json_response
    
    def create_artist(self, name):
        data = {
            "name": name
        }
        response = self.session.post(f"{self.base_url}/Beatify/api/v1/artists", json=data)
        return response
    
    def update_artist(self, id, name):
        data = {
            "name": name
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/artists/{id}", json=data)
        return response
    
    def delete_artist(self, id):
        response = self.session.delete(f"{self.base_url}/Beatify/api/v1/artists/{id}")
        return response
    
    # Album resource request methods via requests.Session()

    def get_albums(self):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/albums")
        json_response = response.json()
        return json_response
    
    def get_album(self, id):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/albums/{id}")
        json_response = response.json()
        return json_response
    
    def create_album(self, name, artist_id):
        data = {
            "name": name,
            "artist_id": artist_id
        }
        response = self.session.post(f"{self.base_url}/Beatify/api/v1/albums", json=data)
        return response
    
    def update_album(self, id, name, artist_id):
        data = {
            "name": name,
            "artist_id": artist_id
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/albums/{id}", json=data)
        return response
    
    def delete_album(self, id):
        response = self.session.delete(f"{self.base_url}/Beatify/api/v1/albums/{id}")
        return response
    
    # Track resource request methods via requests.Session()

    def get_tracks(self):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/tracks")
        json_response = response.json()
        return json_response
    
    def get_track(self, id):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/tracks/{id}")
        json_response = response.json()
        return json_response
    
    def create_track(self, name, length, album_id):
        data = {
            "name": name,
            "length": length,
            "album_id": album_id
        }
        response = self.session.post(f"{self.base_url}/Beatify/api/v1/tracks", json=data)
        return response
    
    def update_track(self, id, name, length, album_id):
        data = {
            "name": name,
            "length": length,
            "album_id": album_id
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/tracks/{id}", json=data)
        return response    
    
    def delete_track(self, id):
        response = self.session.delete(f"{self.base_url}/Beatify/api/v1/tracks/{id}")
        return response    
    
    # Playlist resource request methods via requests.Session()

    def get_playlists(self):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/playlists")
        json_response = response.json()
        return json_response
    
    def get_playlist(self, id):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/playlists/{id}")
        json_response = response.json()
        return json_response
    
    def create_playlist(self, name, description):
        data = {
            "name": name,
            "description": description
        }
        response = self.session.post(f"{self.base_url}/Beatify/api/v1/playlists", json=data)
        return response
    
    def update_playlist(self, id, name, description):
        data = {
            "name": name,
            "description": description
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/playlists/{id}", json=data)
        return response    
    
    def delete_playlist(self, id):
        response = self.session.delete(f"{self.base_url}/Beatify/api/v1/playlists/{id}")
        return response 
    
    def add_track_to_playlist(self, playlist_id, track_id):
        data = {
            "track_id": track_id
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/playlists/{playlist_id}", json=data)
        return response
    
    def add_user_to_playlist(self, playlist_id, user_id):
        data = {
            "user_id": user_id
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/playlists/{playlist_id}", json=data)
        return response
    
    # User resource request methods via requests.Session()

    def get_users(self):
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/users")
        json_response = response.json()
        return json_response
    
    def get_user(self, id): 
        response = self.session.get(f"{self.base_url}/Beatify/api/v1/users/{id}")
        json_response = response.json()
        return json_response
    
    def create_user(self, name):
        data = {
            "name": name
        }
        response = self.session.post(f"{self.base_url}/Beatify/api/v1/users", json=data)
        return response    
    
    def update_user(self, id, name):
        data = {
            "name": name
        }
        response = self.session.put(f"{self.base_url}/Beatify/api/v1/users/{id}", json=data)
        return response
    
    def delete_user(self, id):
        response = self.session.delete(f"{self.base_url}/Beatify/api/v1/users/{id}")
        return response
    
 
    

