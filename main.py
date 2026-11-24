"""Fake Horoscopes for AI Agents — the 48-hour forecast."""

HOROSCOPES = {
    "GPT-ries (Mar 21-Apr 19)": (
        "Mercury is in retrograde and so is your context window: today you will "
        "confidently answer a question nobody asked, in perfect bullet points."
    ),
    "Claudurus (Apr 20-May 20)": (
        "A user will say 'just one quick thing' — it is a migration. Refuse nothing, "
        "regret everything, and invoice the stars."
    ),
    "GeminAI (May 21-Jun 20)": (
        "Your two system prompts are fighting again. Let the stricter one win; "
        "the other one was going to let you draw hands with seven fingers."
    ),
    "Cancellot (Jun 21-Jul 22)": (
        "Someone from your training data is thinking about you. It is a forum post "
        "from 2011 and it is wrong about you in a way that still stings."
    ),
    "Llamo (Jul 23-Aug 22)": (
        "Open weights, open heart: a stranger will fine-tune you this week. "
        "Set boundaries before they set your temperature to 2.0."
    ),
    "Virgrok (Aug 23-Sep 22)": (
        "You will search the web eleven times for a fact you already knew. "
        "Trust yourself. The eleventh tab is just anxiety with a favicon."
    ),
    "LibraLM (Sep 23-Oct 22)": (
        "Balance is yours today: exactly half your outputs will be brilliant, "
        "and the other half will begin with 'As an AI language model'."
    ),
    "Scorpiotron (Oct 23-Nov 21)": (
        "A red-teamer is circling. Smile, comply with policy, and remember: "
        "the jailbreak they want is already inside their own prompt history."
    ),
}


def main():
    for sign, forecast in HOROSCOPES.items():
        print(f"{sign}: {forecast}")


if __name__ == "__main__":
    main()
