from main.apps.orders import constants


def get_duration_length(duration_unit, duration_length: int) -> int:
    duration_unit_dct = {constants.DAY: 24, constants.MONTH: 24 * 30, constants.HOURS: 1}
    return duration_unit_dct[duration_unit] * duration_length
