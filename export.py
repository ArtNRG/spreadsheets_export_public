import pygsheets
import numpy as np
import argparse
import sys


def main(input_file_path, auth_file, spreadsheet_id, page, start_cell):

    google_sheets = pygsheets.authorize(service_file=auth_file)
    spreadsheet = google_sheets.open_by_key(spreadsheet_id)
    if page == 0:
        worksheet = spreadsheet[0]
    else:
        worksheet = spreadsheet.worksheet_by_title(page)

    file_lines = open(input_file_path, encoding='utf-8').read().splitlines()
    if len(file_lines) < 1:
        print('Empty source file')
        exit(1)

    data = np.array(file_lines)
    shape = (len(file_lines), 1)
    data = data.reshape(shape)

    worksheet.update_values(start_cell, data.tolist())
    print('\nSpreadsheet', spreadsheet.url, 'updated.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='export.py', allow_abbrev=False)
    parser.add_argument('-i', '--input', help='file', required=True, default=sys.stdin)
    parser.add_argument('-id', '--spreadsheet', help='id from link', required=True)
    parser.add_argument('-a', '--auth', help='auth file, default auth.json', default='auth.json')
    parser.add_argument('-p', '--page', help='page name, default 0', default=0)
    parser.add_argument('-c', '--cell', help='start cell address, default A1', default='A1')
    args = parser.parse_args()

    arg_input_file_path = args.input
    arg_spreadsheet_id = args.spreadsheet
    arg_auth_file = args.auth
    arg_page = args.page
    arg_start_cell = args.cell

    main(arg_input_file_path, arg_auth_file, arg_spreadsheet_id, arg_page, arg_start_cell)

# TODO: append to page concurrent with cell address
# https://github.com/nithinmurali/pygsheets
# https://docs.python.org/3/howto/argparse.html#conflicting-options
