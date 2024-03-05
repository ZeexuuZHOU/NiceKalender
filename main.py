from nicegui import ui
import json
from holidays import Holidays


ui.markdown('# **This is niceKalender**')

# f = open('databank.json')
# data = json.load(f)

holiday = Holidays()

ui.number(label='available holidays:', value=holiday.avai_holi, format='%.1f')
# result = ui.label()



ui.run()
ui.run()