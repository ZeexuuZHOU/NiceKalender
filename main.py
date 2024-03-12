from nicegui import ui
import json
from holidays import Holidays


ui.markdown('# **This is niceKalender**')

# f = open('databank.json')
# data = json.load(f)

holiday = Holidays()

ui.number(label='available holidays:', value=holiday.holidays_achieve["available"], 
          format='%.1f', on_change=lambda e: holiday.change_avai_holi(e.value))
ui.label(f'used holidays: {holiday.holidays_achieve["used"]}')

ui.run()