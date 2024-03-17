from nicegui import ui
import json
from holidays import Holidays
from date import Date


ui.markdown('# **This is niceKalender**')

# f = open('databank.json')
# data = json.load(f)

holiday = Holidays()
new_holiday_start = None
new_holiday_end = None

@ui.refreshable
def info():
    ui.number(label='all holidays:', value=holiday.holidays_achieve["all"], 
            format='%.1f', on_change=lambda e: holiday.change_avai_holi(e.value))

    ui.label(f'available holidays: {holiday.holidays_achieve["available"]}')
    ui.label(f'used holidays: {holiday.holidays_achieve["used"]}')

info()
start_date = ui.input('Start date')
end_date = ui.input('End date')
used_date = ui.input('How many days?')
remarks = ui.input('Remarks')

ui.button('add new holidays:',on_click=lambda: new_holiday(used_date.value, start_date.value, end_date.value,remarks.value))

def new_holiday(day, start_date, end_date,remarks):
    holiday.new_holiday(int(day), start_date, end_date,remarks)
    ui.notify('New holiday added !!')
    info.refresh()
ui.run()