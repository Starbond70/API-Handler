import random

def generate_fortune(apod, sentiment, chaos, trends):
    vibe = f"\U0001F30C Cosmic Vibe: \"{apod['title']}\""
    mood = f"\U0001F4F0 Global Mood: {sentiment}"
    chaos_lvl = f"\U0001F525 Chaos Index: {chaos}"
    tech = f"\U0001F4C8 Today's Hot Tech: {', '.join(trends)}"

    message = random.choice([
        f"Today feels {sentiment}. Let the {['description']} guide your focus. Embrace {trends[0]} and avoid noisy distractions.",
        f"A day of {chaos} energy. Align your thoughts with the stars, and maybe… commit some {trends[1]} code."
    ])

    return "\n".join([vibe, tech, chaos_lvl, mood, "\n\U0001F52E Fortune:", message])