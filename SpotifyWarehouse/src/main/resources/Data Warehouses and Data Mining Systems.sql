Data Warehouses and Data Mining Systems



Report no. 4

Exercise topic: 
Physical Modelling

Project topic:
Popular Spotify songs




Section members:
Magdalena Rąpała
Miłosz Liniewiecki



Gliwice, 20.04.26
Task 1
	In this exercise we developed a physical model of the Data Warehouse and wrote DDL SQL queries. So far we decided to use the Hibernate database system with PostgreSQL as the main driver of our database.
	Note: The model provided on figure 1 needs to be rearranged. We will provide the changes shortly.  
Task 2
 
Figure 1 – Physical model of the database.

Task 3

Below we provide DDL SQL queries which should create the database.
CREATE TABLE track (
    track_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    artist_id bigint REFERENCES artist (artist_id) ON DELETE CASCADE NOT NULL,
    youtube_id bigint REFERENCES youtube (youtube_id) ON DELETE CASCADE NOT NULL,
    spotify_id bigint REFERENCES spotify (spotify_id) ON DELETE CASCADE NOT NULL,
    streams_spotify_range bigint REFERENCES streams_range (streams_range_id) NOT NULL,
    views_youtube_range bigint REFERENCES views_range (views_range_id) NOT NULL,
    likes_youtube_range bigint REFERENCES likes_range (likes_range_id) NOT NULL,
    streams_spotify bigint NOT NULL,
    views_youtube bigint NOT NULL,
    likes_youtube bigint NOT NULL,
    tempo float4 NOT NULL,
    duration_mn int4 NOT NULL,
    most_playedon TEXT CONSTRAINT played_on_constr CHECK (most_playedon IN ('youtube','spotify')) NOT NULL,
    licensed BOOL NOT NULL,
    official_video BOOL NOT NULL,
    title_youtube TEXT CHECK (char_length(title_youtube) >= 1) NOT NULL
 
); 

CREATE TABLE artist (
    artist_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    artist TEXT CONSTRAINT art_constr CHECK ((char_length(artist) >=1) AND (char_length(artist) < 100)) NOT NULL
);

CREATE TABLE album (
    album_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    artist_id bigint REFERENCES artist (artist_id) ON DELETE CASCADE NOT NULL,
    album TEXT CONSTRAINT album_constr CHECK ((char_length(album) >=1) AND (char_length(album) < 255)) NOT NULL,
    album_type TEXT CONSTRAINT al_type_constr CHECK (album_type IN ('single', 'compilation', 'album')) NOT NULL
);

CREATE TABLE youtube_channel (
    youtube_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    channel TEXT CONSTRAINT ch_constr CHECK ((char_length(channel) >=1) AND (char_length(channel) < 255)) NOT NULL
);

CREATE TABLE streams_range (
    streams_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    range int8range NOT NULL
);

CREATE TABLE views_range (
    views_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    range int8range NOT NULL
);

CREATE TABLE likes_range (
    likes_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    range int8range NOT NULL
);

CREATE TABLE spotify (
    spotify_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    track_id bigint REFERENCES track (track_id) ON DELETE CASCADE NOT NULL,
    track TEXT CONSTRAINT text_constr CHECK ((char_length(track) >= 1) AND (char_length(track) < 100)) NOT NULL,
    danceability_id bigint REFERENCES danceability_range (danceability_id) ON DELETE CASCADE NOT NULL,
    energy_id bigint REFERENCES energy_range (energy_id) ON DELETE CASCADE NOT NULL,
    loudness_id bigint REFERENCES loudness_range (loudness_id) ON DELETE CASCADE NOT NULL,
    speechiness_id bigint REFERENCES speechiness_range (speechiness_id) ON DELETE CASCADE NOT NULL,
    acousticness_id bigint REFERENCES acousticness_range (acousticness_id) ON DELETE CASCADE NOT NULL,
    liveness_id bigint REFERENCES liveness_range (liveness_id) ON DELETE CASCADE NOT NULL,
    valence_id bigint REFERENCES valence_range (valence_id) ON DELETE CASCADE NOT NULL,
    tempo_id bigint REFERENCES tempo_range (tempo_id) ON DELETE CASCADE NOT NULL,
    acousticness_range_id bigint REFERENCES acousticness_range (acousticness_range_id) ON DELETE CASCADE NOT NULL,
    danceability float4 NOT NULL,
    energy float4 NOT NULL,
    loudness float4 NOT NULL,
    speechiness float4 NOT NULL,
    acousticness float4 NOT NULL,
    liveness float4 NOT NULL,
    valence float4 NOT NULL,
    tempo float4 NOT NULL,
    instrumentalness float4 NOT NULL
);

CREATE FUNCTION float4_diff(x float4, y float4) RETURNS float8 AS
'SELECT (x - y)::float48' LANGUAGE sql IMMUTABLE;

CREATE TYPE float4range AS RANGE (
    subtype = float4,
    subtype_diff = float4_diff
);
CREATE TABLE danceability_range (
    danceability_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    danceability_type float4range NOT NULL
);
CREATE TABLE energy_range (
    energy_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    energy_range float4range
);
CREATE TABLE loudness_range (
    loudness_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    loudness_type float4range NOT NULL
);
CREATE TABLE speechiness_range (
    speechiness_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    speechiness_range float4range
);
CREATE TABLE acousticness_range (
    acousticness_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    acousticness_type float4range NOT NULL
);
CREATE TABLE liveness_range (
    liveness_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    liveness_range float4range
);
CREATE TABLE valence_range (
    valence_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    valence_type float4range NOT NULL
);
CREATE TABLE tempo_range (
    tempo_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tempo_range float4range
);
CREATE TABLE acousticness_range (
   acousticness_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   acousticness_range float4range
);
CREATE TABLE instrumentalness_range (
    instrumentalness_range_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    instrumentalness_range float4range
);
