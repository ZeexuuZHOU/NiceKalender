class Holidays:
    def __init__(self) -> None:
        self.avai_holi = 30
        self.used_holi = 0
        
    def new_holiday(self, new_holi):
        self.avai_holi = self.avai_holi - new_holi
        self.used_holi = self.used_holi + new_holi

    def change_avai_holi(self, avai):
        self.avai_holi = avai
