class SentenceInfo:
    def __init__(self, index, input, professional, casual, social_post, emoji, polite, **kwargs):
        self.index = index
        self.input = input
        self.professional = professional
        self.casual = casual
        self.social = social_post
        self.emoji = emoji
        self.polite = polite
        self.status = False

    def set_status(self, value):
        self.status = value
        return self