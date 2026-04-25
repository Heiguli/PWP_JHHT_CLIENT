
from api_client import BeatifyClient 
import streamlit as st

client = BeatifyClient()

st.set_page_config(page_title="Beatify", page_icon=":🎵:")
st.sidebar.title(":🎵: Beatify API Client")
page = st.sidebar.selectbox("Navigate", ["Artists", "Albums", "Tracks", "Users", "Playlists"])

def show_artists():

    st.title("Artists")

    artists = client.get_artists()
    for artist in artists:
        st.write(f"- {artist['name']} (ID: {artist['id']})")

    st.divider()

    st.subheader("Create Artist")
    name = st.text_input("Artist name")
    if st.button("Create"):
        if name:
            response = client.create_artist(name)
            if response.status_code == 201:
                st.success(f"Artist {name} created successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please enter a name")

    st.divider()

    st.subheader("Update Artist")
    artist_options = {artist["name"]: artist["id"] for artist in artists}
    selected_artist = st.selectbox("Select artist to update", list(artist_options.keys()))
    updated_name = st.text_input("New artist name")
    if st.button("Update"):
        if updated_name:
            artist_id = artist_options[selected_artist]
            response = client.update_artist(artist_id, updated_name)
            if response.status_code == 200:
                st.success("Artist updated successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please enter a new name")

    st.divider()

    st.subheader("Delete Artist")
    selected_del = st.selectbox("Select artist to delete", list(artist_options.keys()), key="del")
    if st.button("Delete"):
        if selected_del:
            artist_id = artist_options[selected_del]
            response = client.delete_artist(artist_id)
            if response.status_code == 200:
                st.success("Artist deleted successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")

def show_albums():
    st.title("Albums")
    artists = client.get_artists()
    albums = client.get_albums()
    artist_lookup = {a["id"]: a["name"] for a in artists}
    for album in albums:
        artist_name = artist_lookup.get(album["artist_id"], "Unknown")
        st.write(f"- {album['name']} by {artist_name}")

    st.divider()

    st.subheader("Create Album")
    artist_options = {artist["name"]: artist["id"] for artist in artists}
    name = st.text_input("Album name")
    selected_artist = st.selectbox("Select artist", list(artist_options.keys()))
    if st.button("Create"):
        if name:
            artist_id = artist_options[selected_artist]
            if artist_id:
                response = client.create_album(name, artist_id)
                if response.status_code == 201:
                    st.success(f"Album {name} created successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please select an artist")
        else:
            st.warning("Please enter a name")
    
    st.divider()

    st.subheader("Update Album")
    album_options = {album["name"]: album["id"] for album in albums}
    selected_album = st.selectbox("Select album to update", list(album_options.keys()))
    updated_album_name = st.text_input("New album name")
    if st.button("Update Album"):
        if updated_album_name:
            album_id = album_options[selected_album]
            updated_artist_id = st.selectbox("Select new artist for album", list(artist_options.keys()), key="update_album_artist")
            if updated_artist_id:
                updated_artist_id = artist_options[updated_artist_id]
                response = client.update_album(album_id, updated_album_name, updated_artist_id)
                if response.status_code == 200:
                    st.success("Album updated successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please select an artist")
        else:
            st.warning("Please enter a new name")
    
    st.divider()

    st.subheader("Delete Album")
    selected_del = st.selectbox("Select album to delete", list(album_options.keys()), key="del_album")
    if st.button("Delete Album"):
        if selected_del:
            album_id = album_options[selected_del]
            response = client.delete_album(album_id)
            if response.status_code == 200:
                st.success("Album deleted successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please select an album to delete")

def show_tracks():
    st.title("Tracks")
    albums = client.get_albums()
    tracks = client.get_tracks()
    album_lookup = {a["id"]: a["name"] for a in albums}
    for track in tracks:
        album_name = album_lookup.get(track["album_id"], "Unknown")
        st.write(f"- {track['name']} from album {album_name}")
    
    st.divider()

    st.subheader("Create Track")
    album_options = {album["name"]: album["id"] for album in albums}
    name = st.text_input("Track name") 
    length = st.number_input("Length (seconds)", min_value=1, step=1)
    selected_album = st.selectbox("Select album", list(album_options.keys()), key="create_track_album")
    if st.button("Create Track"):
        if name and length:
            album_id = album_options[selected_album]
            if album_id:
                response = client.create_track(name, length, album_id)
                if response.status_code == 201:
                    st.success(f"Track {name} created successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please select an album")
        else:
            st.warning("Please enter a name")

    st.divider()

    st.subheader("Update Track")
    track_options = {track["name"]: track["id"] for track in tracks}
    selected_track = st.selectbox("Select track to update", list(track_options.keys()))
    updated_track_name = st.text_input("New track name")
    updated_track_length = st.number_input("New length (seconds)", min_value=1, step=1)
    selected_update_album = st.selectbox("Select album", list(album_options.keys()), key="update_track_album")
    if st.button("Update Track"):
        if updated_track_name and updated_track_length and selected_update_album:
            track_id = track_options[selected_track]
            album_id = album_options[selected_update_album]
            response = client.update_track(track_id, updated_track_name, updated_track_length, album_id)
            if response.status_code == 200:
                st.success("Track updated successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please enter a new name and length")

    st.divider()

    st.subheader("Delete Track")
    selected_del = st.selectbox("Select track to delete", list(track_options.keys()), key="del_track")
    if st.button("Delete Track"):
        if selected_del:
            track_id = track_options[selected_del]
            response = client.delete_track(track_id)
            if response.status_code == 200:
                st.success("Track deleted successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please select a track to delete")

def show_users():
    st.title("Users")
    users = client.get_users()
    for user in users:
        st.write(f"- {user['name']} (ID: {user['id']})")

    st.divider()

    st.subheader("Create User")
    name = st.text_input("Name") 
    if st.button("Create User"):
        if name:
            response = client.create_user(name)
            if response.status_code == 201:
                st.success(f"User {name} created successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please enter a name")

    st.divider()

    st.subheader("Update User")
    user_options = {user["name"]: user["id"] for user in users}
    selected_user = st.selectbox("Select user to update", list(user_options.keys()))
    updated_user_name = st.text_input("New user name")
    if st.button("Update User"):
        if updated_user_name:
            user_id = user_options[selected_user]
            response = client.update_user(user_id, updated_user_name)
            if response.status_code == 200:
                st.success("User updated successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please enter a new name")

    st.divider()

    st.subheader("Delete User")
    selected_del = st.selectbox("Select user to delete", list(user_options.keys()), key="del_user")
    if st.button("Delete User"):
        if selected_del:
            user_id = user_options[selected_del]
            response = client.delete_user(user_id)
            if response.status_code == 200:
                st.success("User deleted successfully!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
        else:
            st.warning("Please select a user to delete")

    def show_playlists():

        st.title("Playlists")
        playlists = client.get_playlists()
        for playlist in playlists:
            st.write(f"- name: {playlist['name']} (ID: {playlist['id']}) (Description: {playlist['description']})")

        st.divider()
        st.subheader("Create Playlist")
        name = st.text_input("Playlist name")
        description = st.text_input("Playlist description")
        if st.button("Create Playlist"):
            if name:
                response = client.create_playlist(name, description or "No description provided")
                if response.status_code == 201:
                    st.success(f"Playlist {name} created successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please enter a playlist name")
        
        st.divider()

        st.subheader("Update Playlist")
        playlist_options = {playlist["name"]: playlist["id"] for playlist in playlists}
        selected_playlist = st.selectbox("Select playlist to update", list(playlist_options.keys()))
        updated_playlist_name = st.text_input("New playlist name")
        updated_playlist_description = st.text_input("New playlist description")
        if st.button("Update Playlist"):
            if updated_playlist_name:
                playlist_id = playlist_options[selected_playlist]
                response = client.update_playlist(playlist_id, updated_playlist_name, updated_playlist_description)
                if response.status_code == 200:
                    st.success("Playlist updated successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please enter a new name")

        st.divider()

        st.subheader("Delete Playlist")
        selected_del = st.selectbox("Select playlist to delete", list(playlist_options.keys()), key="del_playlist")
        if st.button("Delete Playlist"):    
            if selected_del:
                playlist_id = playlist_options[selected_del]
                response = client.delete_playlist(playlist_id)
                if response.status_code == 200:
                    st.success("Playlist deleted successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.status_code}: {response.json().get('message')}")
            else:
                st.warning("Please select a playlist to delete")

        st.divider()
        st.subheader("Add Track to Playlist")
        tracks = client.get_tracks()
        track_options = {track["name"]: track["id"] for track in tracks}
        selected_playlist_for_track = st.selectbox("Select playlist", list(playlist_options.keys()), key="playlist_for_track")
        selected_track = st.selectbox("Select track to add", list(track_options.keys()))
        if st.button("Add Track"):
            playlist_id = playlist_options[selected_playlist_for_track]
            track_id = track_options[selected_track]
            response = client.add_track_to_playlist(playlist_id, track_id)
            if response.status_code == 200:
                st.success("Track added to playlist!")
                st.rerun()
            else:
                st.error(f"Error: {response.status_code}: {response.json().get('message')}")
