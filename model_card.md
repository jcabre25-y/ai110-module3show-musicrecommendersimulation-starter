# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

This recommender tries to suggest songs a user may like from a small music catalog. It looks at a user's preferred genre, mood, energy, and acoustic preference, then ranks songs that seem closest to that taste profile.

---

## 3. Data Used

The dataset contains 18 songs in `data/songs.csv`. Each song includes `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The data is useful for a classroom simulation, but it is small and does not represent all musical tastes equally. Some genres only appear once, and some moods, like `sad`, are missing completely.

---

## 4. Algorithm Summary

The system gives points when a song matches the user's favorite genre and favorite mood. It also gives similarity points when the song's energy is close to the user's target energy. A small bonus is added if the song's acousticness matches the user's acoustic preference. After every song gets a score, the recommender sorts the songs from highest to lowest and returns the top results.

---

## 5. Observed Behavior / Biases

The recommender works best when the dataset contains clear matches for the user's genre and mood. It struggles more when a mood is missing or when a genre has very few songs. One important limitation is that energy can still help weak matches rank fairly high, especially for unusual profiles. This means some users are better served than others, depending on how well their taste is represented in the dataset.

---

## 6. Evaluation Process

I tested the system with four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge-case profile called Sad But High Energy. I compared the top 5 results for each profile to what I would expect based on musical intuition. I also ran a small experiment where I made energy more important and genre less important. That experiment showed that the system became more sensitive to energy, but not more accurate overall.

---

## 7. Intended Use and Non-Intended Use

This system is meant for classroom learning and simple experimentation. It is good for showing how a recommender turns user preferences into ranked suggestions. It is not meant for real users, large catalogs, or high-stakes decisions. It should not be treated like a complete music app or a fair representation of all listener tastes.

---

## 8. Ideas for Improvement

- Add more songs so each genre and mood has better coverage.
- Use more features like valence and tempo in the final score.
- Add diversity rules so the top results are not too repetitive.

---

## 9. Personal Reflection

My biggest learning moment was realizing how much the weights matter. A small change, like making energy too important, changed the recommendations a lot and made some results worse. That helped me understand that recommender systems are not only about code, but also about careful design choices.

AI tools helped me move faster when I was brainstorming scoring rules, writing explanations, and checking how to structure my functions and documentation. I still had to double-check the AI suggestions against my dataset and my actual results, because a recommendation that sounds reasonable in theory can behave differently once it runs on real data. That was especially true when I tested edge-case profiles and saw that the output did not always match the intended mood.

One thing that surprised me is that even a simple algorithm can still feel like a real recommendation system when the inputs make sense. Exact genre matches, mood matches, and energy closeness were enough to create results that felt believable for profiles like Chill Lofi or High-Energy Pop. If I extended this project, I would add more songs, include more features like valence and tempo in the final score, and add some diversity rules so the top results do not feel too repetitive.
