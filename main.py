"""
Script to generate CSV files from a Tribler tags database.
The generated CSV files can be used for plotting purposes.
"""
import sqlite3

DB_PATH = 'data/tags.db'

con = sqlite3.connect(DB_PATH)

with open("data/tag_frequencies.csv", "w") as out_file:
    out_file.write("tag count\n")
    cur = con.cursor()
    rows = cur.execute("SELECT Tag.name, COUNT(TorrentTag.tag) AS count "
                       "FROM TorrentTagOp, TorrentTag, Tag "
                       "WHERE TorrentTagOp.torrent_tag = TorrentTag.id AND TorrentTag.tag = Tag.id "
                       "GROUP BY TorrentTag.tag "
                       "ORDER BY count DESC;")

    for row in rows:
        out_file.write("%s %d\n" % row)

with open("data/user_to_tag_frequencies.csv", "w") as out_file:
    out_file.write("user_id,tag_count\n")
    cur = con.cursor()
    rows = cur.execute("SELECT TorrentTagOp.peer, COUNT(TorrentTag.tag) AS count "
                       "FROM TorrentTagOp, TorrentTag, Tag "
                       "WHERE TorrentTagOp.torrent_tag = TorrentTag.id AND TorrentTag.tag = Tag.id "
                       "GROUP BY TorrentTagOp.peer ORDER BY count DESC;")

    for row in rows:
        out_file.write("%s,%d\n" % row)


with open("data/torrent_to_tag_frequencies.csv", "w") as out_file:
    out_file.write("infohash,tag_count\n")
    cur = con.cursor()
    rows = cur.execute("SELECT HEX(Torrent.infohash), COUNT(TorrentTag.tag) AS count "
                       "FROM TorrentTagOp, TorrentTag, Torrent "
                       "WHERE TorrentTagOp.torrent_tag = TorrentTag.id AND TorrentTag.torrent = Torrent.id "
                       "GROUP BY TorrentTag.torrent ORDER BY count DESC;")

    for row in rows:
        out_file.write("%s,%d\n" % row)

con.close()
