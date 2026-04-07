"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    """Print the top recommendations for a named user profile."""
    print(f"\n=== {profile_name} ===")
    print(f"Preferences: {user_prefs}\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.80,
            "target_tempo_bpm": 120,
            "target_valence": 0.80,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "focused",
            "target_energy": 0.40,
            "target_tempo_bpm": 80,
            "target_valence": 0.58,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.92,
            "target_tempo_bpm": 150,
            "target_valence": 0.45,
            "likes_acoustic": False,
        },
        "Edge Case: Sad But High Energy": {
            "favorite_genre": "ambient",
            "favorite_mood": "sad",
            "target_energy": 0.90,
            "target_tempo_bpm": 140,
            "target_valence": 0.20,
            "likes_acoustic": True,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
