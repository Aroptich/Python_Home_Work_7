import data_provider as dp
import Data_base as db


def UI_view() -> tuple[str]:
    first_name = dp.input_first_name()
    last_name = dp.input_last_name()
    phone_number = dp.input_number_phone()
    db.record_data_txt(first_name, last_name, phone_number)
    return first_name, last_name, phone_number
