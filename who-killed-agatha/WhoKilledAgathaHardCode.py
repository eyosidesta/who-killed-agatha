class WhoKilledAgatha:
    def __init__(self, agatha_hate_array = [], butler_hate_array = [], charles_hate_array = []):
        self.agatha_hate_array = agatha_hate_array
        self.butler_hate_array = butler_hate_array
        self.charles_hate_array = charles_hate_array

    def agatha_hates_who(self):
        # **'Agatha hates everybody except the butler'
        # agatha hates herself (second index 1 which means agatha hates herself)
        # agata doesn't hate butler (third index 0 which means agatha doesn't hate butler)
        # agata hates charles (fourth/last index 1 which means agatha hates charles)
        self.agatha_hate_array.push('Agatha', 1, 0, 1)
        return self.agata_hate_array
    
    def butler_hates_who(self):
        # ** 'The butler hates everyone not richer than Aunt Agatha.
        # butler hates agatha (second index 1 which means butler hates agatha)
        # butler doesn't hate himself (third index 0 which means butler doesn't hate himself)
        # ** 'The butler hates everyone whom Agatha hates'
        # butler hates charles (fourth/last index 1 which means butler hates charles)
        self.butler_hate_array.push('Butler', 1, 0, 1)
        return self.butler_hate_array
    

    def charles_hates_who(self):
        # **'Agatha hates everybody except the butler'
        # agatha hates herself (second index 1 which means agatha hates herself)
        # agata doesn't hate butler (third index 0 which means agatha doesn't hate butler)
        # agata hates charles (fourth/last index 1 which means agatha hates charles)
        self.charles_hate_array.push('Charles', 1, 0, 1)
        return self.charles_hate_array
    
