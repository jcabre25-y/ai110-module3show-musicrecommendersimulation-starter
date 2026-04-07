# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does

---

## How The System Works

Real-world recommendation systems often combine many kinds of data, including user behavior, patterns from similar users, and features of the songs or videos themselves. At a large scale, platforms like Spotify and YouTube use hybrid systems that combine collaborative filtering with content-based signals to predict what a user may enjoy next. My version is much simpler and focuses on content-based matching. It compares a user's preferences to each song's attributes and gives higher scores to songs that match the user's favorite genre and mood and are close to the user's target energy. It will prioritize transparent, easy-to-explain recommendations over complex machine learning.

This simulation uses the following features:

- `Song`: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
- `UserProfile`: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

The recommender computes a score for each song using a weighted scoring rule. Songs get strong points for matching the user's genre, slightly smaller points for matching mood, and partial points when the song's energy is close to the user's target energy. Acoustic preference can add a small bonus. After each song is scored, the system ranks the songs from highest to lowest score and recommends the top results.

One example taste profile for this simulation is a listener who prefers lofi, likes focused or calm music, wants medium-low energy, and tends to like more acoustic or soft textures. A matching profile dictionary could look like this: `{"favorite_genre": "lofi", "favorite_mood": "focused", "target_energy": 0.40, "target_tempo_bpm": 80, "target_valence": 0.58, "likes_acoustic": true}`. This profile should be strong enough to separate something like intense rock from chill lofi because those categories differ across multiple features at once. Rock tracks in this dataset tend to have much higher energy and tempo and a more aggressive mood, while lofi tracks tend to be calmer, softer, and more acoustic. If the profile only used genre, it would be too narrow, but combining genre, mood, energy, tempo, and acoustic preference gives the recommender enough information to capture a clearer musical vibe.

The data flow of the system can be summarized as: Input (`UserProfile`) -> Process (loop through every song in the CSV and score each one) -> Output (sort by score and return the top `k` recommendations). Each song is judged individually against the same user preferences, then the final ranking compares all of those song scores to decide which songs should be recommended first.

```mermaid
flowchart TD
    A([Start]) --> B[User enters preferences<br/>genre, mood, target_energy, likes_acoustic]
    B --> C[Load songs from data/songs.csv]
    C --> D[Initialize empty results list]
    D --> E{More songs to score?}

    E -- Yes --> F[Get next song]
    F --> G[Compare song genre to favorite_genre]
    G --> H[Compare song mood to favorite_mood]
    H --> I[Calculate energy closeness<br/>1 - abs(song.energy - target_energy)]
    I --> J{Does acousticness match<br/>the user's preference?}
    J -- Yes --> K[Add acoustic bonus]
    J -- No --> L[Compute total score]
    K --> L
    L --> M[Store song, score, and explanation]
    M --> E

    E -- No --> N[Sort all songs by score<br/>highest to lowest]
    N --> O[Return top K recommendations]
    O --> P([End])
```

Finalized algorithm recipe:

- `+2.0` points for a genre match
- `+1.0` point for a mood match
- up to `+2.0` points for energy closeness using `2.0 * max(0, 1 - abs(song.energy - target_energy))`
- `+0.5` points if the song's acousticness matches the user's acoustic preference

This means the recommender rewards both exact matches and near matches. Genre gets the most weight because it is the broadest taste signal, mood refines the emotional feel, energy captures how calm or intense the song feels, and acousticness acts as a smaller supporting vibe feature.

This plan now includes an expanded dataset with 18 songs, a specific test user profile, and a weighted scoring rule that can be implemented directly in code. One likely bias in this system is that it may over-prioritize genre and miss songs from other genres that still match the user's mood or energy very well. It may also oversimplify musical taste by assuming that one profile can fully represent what a listener wants in every context.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

### CLI Verification

Running `python -m src.main` with the default `pop` / `happy` profile produces readable recommendations that show the song title, score, and explanation:

```text
Loaded songs: 18

Top recommendations:

1. Sunrise City by Neon Echo
   Score: 5.46
   Reasons: genre match (+2.0), mood match (+1.0), energy closeness (+1.96), acoustic preference match (+0.5)

2. Gym Hero by Max Pulse
   Score: 4.24
   Reasons: genre match (+2.0), energy closeness (+1.74), acoustic preference match (+0.5)

3. Rooftop Lights by Indigo Parade
   Score: 3.42
   Reasons: mood match (+1.0), energy closeness (+1.92), acoustic preference match (+0.5)

4. Pixel Arcade by Bit Runner
   Score: 2.48
   Reasons: energy closeness (+1.98), acoustic preference match (+0.5)

5. Night Drive Loop by Neon Echo
   Score: 2.40
   Reasons: energy closeness (+1.90), acoustic preference match (+0.5)
```

This output matches expectations for a user who likes energetic, upbeat pop. The strongest recommendation is `Sunrise City` because it matches both genre and mood and has energy close to the user's target.

Terminal screenshot:

![CLI recommendation output](./Screenshot%202026-04-06%20at%2011.58.08%E2%80%AFPM.png)

---

## Experiments You Tried

I stress-tested the recommender with four profiles:

- `High-Energy Pop`: favorite genre `pop`, favorite mood `happy`, target energy `0.80`, prefers less acoustic tracks
- `Chill Lofi`: favorite genre `lofi`, favorite mood `focused`, target energy `0.40`, prefers more acoustic tracks
- `Deep Intense Rock`: favorite genre `rock`, favorite mood `intense`, target energy `0.92`, prefers less acoustic tracks
- `Edge Case: Sad But High Energy`: favorite genre `ambient`, favorite mood `sad`, target energy `0.90`, prefers more acoustic tracks

The first three profiles behaved as expected. `Sunrise City` ranked first for the high-energy pop user, `Focus Flow` ranked first for the chill lofi user, and `Storm Runner` ranked first for the deep intense rock user. This suggests that the current weighted scoring rule works reasonably well when the profile lines up with songs that clearly exist in the dataset.

Compared to my own musical intuition, these results mostly feel right. For the `Chill Lofi` profile, `Focus Flow` ranking first makes sense because it matches the user's preferred genre and mood exactly, has the exact target energy of `0.40`, and also fits the user's acoustic preference. That combination makes it feel like the clearest example of the intended vibe. `Midnight Coding` and `Library Rain` also feel like reasonable follow-up recommendations because they are still lofi, lower-energy, and more acoustic.

Using the current weights in `recommender.py`, `Focus Flow` ranked first because it received the maximum possible score: `+2.0` for genre match, `+1.0` for mood match, `+2.0` for perfect energy closeness, and `+0.5` for matching the acoustic preference, for a total of `5.5`. This is a helpful example of how the scoring rule turns user preferences into a final ranking.

The edge-case profile exposed a weakness. Because the dataset does not contain a strong `sad` song and the algorithm only uses exact mood matching plus energy closeness, it still recommended songs that were high-energy even when their emotional tone was not especially sad. This shows that the current system can be "tricked" by conflicting preferences and may overweight energy when mood does not have a match.

One thing I watched for was whether the same song would dominate every profile. That did not happen in the first three tests, which suggests the current genre weight is not completely overpowering the rest of the system. However, because the dataset is still small, some songs can appear across multiple profiles when their energy values are close to many targets. That means the recommender still has limited variety and could become repetitive without a larger catalog or more features.

I also ran a small data experiment by halving the genre weight and doubling the energy weight. That changed genre from `+2.0` to `+1.0`, while energy changed from a maximum of `+2.0` to a maximum of `+4.0` using the same closeness formula. The math still worked correctly, but the ranking became much more sensitive to energy proximity.

This made the recommendations more different than more accurate. The top songs for the first three profiles stayed mostly reasonable, but songs with similar energy values started climbing higher even when they were weaker matches in genre or mood. The biggest change showed up in the edge-case profile: instead of favoring `Spacewalk Thoughts` for its ambient genre match, the system switched to mostly high-energy songs like `Storm Runner` and `Gym Hero`. That suggests the experiment reduced the model's ability to reflect a user's broader taste and made energy too dominant.

Evaluation screenshots:

High-Energy Pop and Chill Lofi:

![Evaluation output 1](./Screenshot%202026-04-07%20at%2012.09.44%E2%80%AFAM.png)

Deep Intense Rock:

![Evaluation output 2](./Screenshot%202026-04-07%20at%2012.09.56%E2%80%AFAM.png)

Edge Case: Sad But High Energy:

![Evaluation output 3](./Screenshot%202026-04-07%20at%2012.10.08%E2%80%AFAM.png)

Prompt used for a new "System Evaluation" chat:

```text
#codebase
I have a simple content-based music recommender that scores songs using genre match, mood match, energy closeness, and a small acousticness bonus.

Please suggest 4 to 6 adversarial or edge-case user profiles that could reveal weaknesses in my scoring logic. I want profiles that might create conflicting signals, such as very high energy but a sad mood, or a genre preference that does not exist strongly in the dataset.

For each profile, explain:
- why it is a useful test
- what kind of incorrect or surprising recommendation behavior it might expose
- what this could teach me about bias or oversimplification in my system
```

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
