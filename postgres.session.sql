-- CREATE TABLE songs (
--     id int,
--     title varchar,
--     length float,
--     release_date date
-- );

-- CREATE TABLE playlists (
--     id int,
--     title varchar,
--     length float,
--     FOREIGN KEY (created_by) REFERENCES users (id) ON DELETE CASCADE,
--     date_added timestamp
-- );

-- CREATE TABLE albums (
--     id int,
--     title varchar,
--     length float,
--     release_date date
-- );

-- CREATE TABLE artists (
--     id int,
--     name varchar,
--     albums_released int
-- );

-- CREATE TABLE users (
--     id int,
--     name varchar,
--     playlists_created int
-- );

-- CREATE TABLE playlist_songs (
--     id int,
--     FOREIGN KEY (song_id) REFERENCES songs (id),
--     FOREIGN KEY (playlist_id) REFERENCES playlists (id),
--     order int
-- );

-- CREATE TABLE album_songs (
--     id int,
--     FOREIGN KEY (song_id) REFERENCES songs (id),
--     FOREIGN KEY (album_id)REFERENCES albums (id),
--     order int
-- );

-- CREATE TABLE album_artists (
--     id int,
--     FOREIGN KEY (artist_id) REFERENCES artists (id),
--     FOREIGN KEY (album_id) REFERENCES albums (id)
-- );

-- CREATE TABLE song_artists (
--     id int,
--     FOREIGN KEY (artist_id) REFERENCES artists (id),
--     FOREIGN KEY (song_id) REFERENCES songs (id)
-- );

DROP TABLE "albums";
DROP TABLE "artists";
DROP TABLE "songs";
DROP TABLE "users";