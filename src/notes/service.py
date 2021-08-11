from src.notes.models import Notes


class CountNotes:
    """ Count all objects notes in database """
    def __init__(self):
        self.count = Notes.objects.count()
