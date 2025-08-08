class ExampleAgent:
    def __init__(self):
        pass

    def handle(self, text: str) -> str:
        # Placeholder logic - replace with real model calls later
        txt = text.strip().lower()
        if "help" in txt or "guide" in txt:
            return "I am NiruX — your spiritual defender. How can I help you today?"
        if "who are you" in txt:
            return "I am NiruX, designed to promote dharma and protect against harm."
        return "I hear you. (This is a placeholder reply — we'll add real AI soon.)"
