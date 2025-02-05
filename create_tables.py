import json
import gray_code
from math import log2


def check_table_validity(table: list):
    word_length = int(log2(len(table)))

    if type(table) is not list:
        raise TypeError

    if not list:
        raise ValueError("Only nonempty lists are allowed")

    if len(table) != 2 ** word_length:
        raise ValueError("The table must have 2**n rows")

    for row in table:
        if type(row) is not list:
            raise TypeError("The table must be a list")

        if log2(len(row)) != int(log2(len(row))):
            raise ValueError("All rows must have 2**n elements")

        if len(row) != len(table[0]):
            raise ValueError("All rows must be equal in length")

        for element in row:
            element_has_state = all([i in ('0', '1') for i in element]) and element
            element_is_empty = all([i == '-' for i in element])

            if not (element_is_empty or element_has_state):
                raise ValueError(f"Unknown element {element}. Only (0, 1, -) are allowed")

            if element_has_state and not len(element) == word_length:
                raise ValueError(f"State {element} has invalid length")


def import_data(json_file: str) -> list:
    with open(json_file, "r") as f:
        table = json.load(f)

    check_table_validity(table)

    binary_length = int(log2(len(table)))
    states = gray_code.create_list(binary_length)
    new_table = {}

    for index, line in enumerate(table):
        new_table[states[index]] = line

    return new_table


def split_tables(ff_table: list, ff_type: str):
    binary_length = int(log2(len(ff_table)))
    all_splitted_tables = {}

    for i in range(binary_length):
        splitted_table = {}
        for row in ff_table:
            splitted_row = []

            for element in ff_table[row]:
                try:
                    splitted_row.append(element[i])
                except IndexError:
                    splitted_row.append("-")

            splitted_table[row] = splitted_row

        ff_name = f'{ff_type}{binary_length - i - 1}'
        all_splitted_tables[ff_name] = splitted_table

    return all_splitted_tables


def create_tables(json_file: str, ff_type: str) -> list:
    excit_table = import_data(json_file)
    all_tables = {}

    if ff_type not in ("D", "T", "RS", "JK"):
        raise ValueError("Not a valid flip flop! Must be D, T, RS or JK.")

    with open("flip_flops.json", "r") as f:
        flip_flop = json.load(f)[ff_type]

    for ff_index, ff_letter in enumerate(ff_type):
        ff_table = {}

        for row in excit_table:
            converted_table = []

            for element in excit_table[row]:
                converted_value = ""

                for index, element_value in enumerate(element):
                    if element_value not in "-":
                        converted_value += flip_flop[row[index] + element_value][ff_index]
                    else:
                        converted_value += "-"

                converted_table.append(converted_value)
            ff_table[row] = converted_table

        splitted_tables = split_tables(ff_table, ff_letter)
        for i in splitted_tables:
            all_tables[i] = splitted_tables[i]

    return all_tables
