class WhoKilledAgatha:
    def __init__(self, agatha_hate_array = [], butler_hate_array = [], charles_hate_array = [], agatha_rich_array = [], butler_rich_aray = [], charles_rich_array = []):
        self.agatha_hate_array = agatha_hate_array
        self.butler_hate_array = butler_hate_array
        self.charles_hate_array = charles_hate_array
        self.agatha_rich_array = agatha_rich_array
        self.butler_rich_array = butler_rich_aray
        self.charles_rich_array = charles_rich_array

    def agatha_hates_who(self):
        # **'Agatha hates everybody except the butler'
        # agatha hates herself (second index 1 which means agatha hates herself)
        # agata doesn't hate butler (third index 0 which means agatha doesn't hate butler)
        # agata hates charles (fourth/last index 1 which means agatha hates charles)
        self.agatha_hate_array.append('Agatha')        
        self.agatha_hate_array.append(1)
        self.agatha_hate_array.append(0)
        self.agatha_hate_array.append(1)

        return self.agatha_hate_array
    
    def butler_hates_who(self):
        # ** 'The butler hates everyone not richer than Aunt Agatha.
        # butler hates agatha (second index 1 which means butler hates agatha)
        # butler doesn't hate himself (third index 0 which means butler doesn't hate himself)
        # ** 'The butler hates everyone whom Agatha hates'
        # butler hates charles (fourth/last index 1 which means butler hates charles)
        self.butler_hate_array.append('Butler')
        self.butler_hate_array.append(1)
        self.butler_hate_array.append(0)
        self.butler_hate_array.append(1)
        return self.butler_hate_array
    

    def charles_hates_who(self):
        # **'Charles hates no one that Agatha hates'
        # charles doesn't hate agatha (second index 1 which means charles doesn't hate agatha)
        # charles either hates or doesn't hate butler (i't not defined) (third index 0.5 which means it's unknown)
        # charles doesn't hate himself (fourth/last index 1 which means charles doesn't hate himself)
        self.charles_hate_array.append('Charles')
        self.charles_hate_array.append(0)
        self.charles_hate_array.append(0.5)
        self.charles_hate_array.append(0)
        return self.charles_hate_array
    
    def agatha_richer_than_who(self):
        self.agatha_rich_array.append('Agatha')
        self.agatha_rich_array.append(0)
        self.agatha_rich_array.append(0)
        self.agatha_rich_array.append(0.5)
        return self.agatha_rich_array
    
    def butler_richer_than_who(self):
        # ** 'butler hates everyone not richer than Aunt Agatha'
        self.butler_richer_than_who.append('Butler')
        self.butler_richer_than_who.append(1)
        self.butler_richer_than_who.append(0)
        self.butler_richer_than_who.append(0.5)
        return self.butler_rich_array
    

    def charles_richer_than_who(self):
        self.charles_hate_array.append('Charles')
        self.charles_hate_array.append(0.5)
        self.charles_hate_array.append(0.5)
        self.charles_hate_array.append(0)
        return self.charles_rich_array
    
    def check_who_hates_agatha(self):
        if self.agatha_hate_array[1] == 1:
            self.hates_agatha.append('Agatha')
        if self.butler_hate_array[1] == 1:
            self.hates_agatha.append('Butler')
        if self.charles_hate_array[1] == 1:
            self.hates_agatha.append('Charles')

        return self.hates_agatha
    
    def check_not_richer_than_agatha(self):
        if self.agatha_rich_array[1] == 0:
            self.not_richer_than_agatha.append('Agatha')
        if self.butler_hate_array[1] == 0:
            self.not_richer_than_agatha.append('Buttler')
        if self.charles_hate_array[1] == 0:
            self.not_richer_than_agatha.append('Charles')

        return self.not_richer_than_agatha
    
    def get_the_killer(self):
        pass


find_killer = WhoKilledAgatha()
find_killer.agatha_hates_who()
print("the value is: ", find_killer.agatha_hate_array)