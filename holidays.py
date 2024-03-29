import json
from date import Date
class Holidays:
    def __init__(self) -> None:
        with open('databank.json', 'r') as f:
            self.holidays_achieve = json.load(f)
        
    def new_holiday(self, new_holi, start, end, remarks):
        self.holidays_achieve["available"] = self.holidays_achieve["available"] - new_holi
        self.holidays_achieve["used"] = self.holidays_achieve["used"] + new_holi
        self.holidays_achieve["holiday times"] = self.holidays_achieve["holiday times"] + 1
        self.holidays_achieve["holidays"].append({"times": self.holidays_achieve["holiday times"], "start": start, "end": end, "remarks": remarks})
        self.achieve_json()


    def change_avai_holi(self, avai):
        self.holidays_achieve["available"] = avai
        self.achieve_json()

    def achieve_json(self) -> None:
        with open('databank.json', 'w') as json_file:
            json.dump(self.holidays_achieve, json_file)