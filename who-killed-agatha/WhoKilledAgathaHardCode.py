class WhoKilledAgatha:
    def __init__(self, agata_hate_array = []):
        self.agata_hate_array = agata_hate_array
        pass

    def agata_hates_who(self):
        # **'Agatha hates everybody except the butler'
        # agatha hates herself (second index 1 which means agatha hates herself)
        # agata doesn't hate butler (third index 0 which means agatha doesn't hate butler)
        # agata hates charles (fourth/last index 1 which means agatha hates charles)
        self.agata_hate_array.push('Agatha', 1, 0, 1)

