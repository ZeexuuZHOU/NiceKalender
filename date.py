class Date():
    def __init__(self, date_str) -> None:
        self.year = int(date_str.split("-")[0])
        self.month = int(date_str.split("-")[1])
        self.day = int(date_str.split("-")[2])