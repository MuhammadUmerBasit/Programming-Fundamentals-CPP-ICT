"""
Music Track & Audio Library Database Management System
======================================================
Python implementation replicating the C database program (thing.cpp).
Demonstrates structured records, file serialization, dynamic search,
and playlist filtering.

Author: Muhammad Umer Basit (Civil Engineering Student)
Reference: CS-114 Fundamentals of Programming
"""

import os
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Track:
    title: str
    artist: str
    genre: str
    year: int
    duration_min: float
    file_location: str


class MusicLibraryManager:
    def __init__(self, storage_file: str = "music_database.txt"):
        self.storage_file = storage_file
        self.tracks: List[Track] = []
        self.load_from_disk()

    def add_track(self, title: str, artist: str, genre: str, year: int,
                  duration_min: float, file_location: str):
        t = Track(
            title=title.strip(),
            artist=artist.strip(),
            genre=genre.strip(),
            year=year,
            duration_min=duration_min,
            file_location=file_location.strip()
        )
        self.tracks.append(t)
        self.save_to_disk()
        return t

    def search_by_artist(self, artist_query: str) -> List[Track]:
        q = artist_query.lower()
        return [t for t in self.tracks if q in t.artist.lower()]

    def search_by_genre(self, genre_query: str) -> List[Track]:
        q = genre_query.lower()
        return [t for t in self.tracks if q in t.genre.lower()]

    def save_to_disk(self):
        with open(self.storage_file, "w", encoding="utf-8") as f:
            for t in self.tracks:
                f.write(f"{t.title}|{t.artist}|{t.genre}|{t.year}|{t.duration_min}|{t.file_location}\n")

    def load_from_disk(self):
        if not os.path.exists(self.storage_file):
            return
        self.tracks = []
        with open(self.storage_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    t = Track(
                        title=parts[0],
                        artist=parts[1],
                        genre=parts[2],
                        year=int(parts[3]),
                        duration_min=float(parts[4]),
                        file_location=parts[5]
                    )
                    self.tracks.append(t)

    def display_library(self):
        print("=" * 85)
        print(f"{'Title':<25} {'Artist':<20} {'Genre':<15} {'Year':<6} {'Duration':<10}")
        print("=" * 85)
        for t in self.tracks:
            dur_str = f"{t.duration_min:.2f} min"
            print(f"{t.title[:23]:<25} {t.artist[:18]:<20} {t.genre[:13]:<15} {t.year:<6} {dur_str:<10}")
        print("=" * 85)


def run_demo():
    print("Testing Music Library Database Manager...")
    mgr = MusicLibraryManager("demo_library.txt")

    mgr.add_track("Clair de Lune", "Claude Debussy", "Classical", 1905, 5.02, "/audio/debussy.mp3")
    mgr.add_track("Canon in D", "Johann Pachelbel", "Baroque", 1680, 4.30, "/audio/pachelbel.mp3")
    mgr.add_track("Symphony No. 5", "Ludwig van Beethoven", "Classical", 1808, 7.15, "/audio/beethoven.mp3")

    mgr.display_library()
    if os.path.exists("demo_library.txt"):
        os.remove("demo_library.txt")


if __name__ == "__main__":
    run_demo()
