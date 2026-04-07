# Reflection

## Profile Comparisons

High-Energy Pop vs. Chill Lofi:

The High-Energy Pop profile pushed upbeat and polished songs like `Sunrise City` and `Gym Hero` to the top because those songs are energetic and closer to a bright pop sound. The Chill Lofi profile shifted toward `Focus Flow`, `Midnight Coding`, and `Library Rain` because those songs are calmer, more acoustic, and much closer to a study or background vibe. This difference makes sense because the profiles are testing opposite energy levels and very different moods.

High-Energy Pop vs. Deep Intense Rock:

Both profiles like high-energy music, so some songs with strong energy scores can appear in both lists. The main difference is that the pop profile prefers cheerful songs, while the rock profile prefers intense songs, so `Sunrise City` wins for pop and `Storm Runner` wins for rock. `Gym Hero` shows up in both types of results because it has high energy and an intense feel, even though it is still tagged as pop.

High-Energy Pop vs. Edge Case: Sad But High Energy:

The High-Energy Pop profile gets results that feel upbeat and fun, but the edge-case profile gets stranger results because the system cannot find many songs that are both sad and high-energy. That means songs start ranking mostly because they are energetic, not because they match the emotional tone well. This helps show why `Gym Hero` can keep appearing for people who want "Happy Pop" or other energetic music: its high energy makes it score well even when other features are only partial matches.

Chill Lofi vs. Deep Intense Rock:

These two profiles produce very different outputs because one wants calm, focused, acoustic songs and the other wants loud, intense, high-energy songs. `Focus Flow` and `Midnight Coding` make sense for Chill Lofi, while `Storm Runner` and `Iron Horizon` fit Deep Intense Rock much better. This comparison shows that the recommender can separate very different vibes when the dataset has clear examples of both.

Chill Lofi vs. Edge Case: Sad But High Energy:

The Chill Lofi profile gets coherent study-style recommendations because the dataset has multiple lofi and calm songs. The edge-case profile is much less stable because its mood is missing from the dataset and its energy target conflicts with the kind of songs the ambient genre usually suggests. This makes the edge-case list feel less emotionally accurate, even though the math is still working as designed.

Deep Intense Rock vs. Edge Case: Sad But High Energy:

These two profiles can overlap on energy, which is why some intense songs rise in both lists. The difference is that the rock profile has a clear genre and mood match available in the catalog, while the edge-case profile does not. Because of that, the rock profile feels more valid and the edge-case profile exposes a weakness in the recommender.
