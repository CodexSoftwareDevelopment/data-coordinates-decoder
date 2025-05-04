import requests
import re
from bs4 import BeautifulSoup

def fetch_coord_str(doc_url):
    response = requests.get(doc_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        coord_str = text.lstrip("Coding assessment input dataPublished using Google DocsReport abuseLearn moreCoding assessment input dataUpdated automatically every 5 minutesThe table below contains the input data needed to solve the coding assessment exercise.x-coordinateCharactery-coordinate")
        return coord_str
    else:
        raise Exception(f"Failed to fetch document text. Status code: {response.status_code}")

def extract_coords(coord_str):
    pattern = r"(\d{1,2})(.)(\d)"
    matches = re.findall(pattern, coord_str)

    parsed_coords = {}
    for x_str, char, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        parsed_coords[(x, y)] = char

    return parsed_coords

def print_grid(parsed_coords):
    coords = parsed_coords.keys()

    max_x = max(x for x, y in coords)
    max_y = max(y for x, y in coords)

    for y in range(max_y +1):
        row = ""
        for x in range(max_x +1):
            row += parsed_coords.get((x, y), " ")
        print(row)

def main():
    url = "https://docs.google.com/document/d/e/2PACX-1vSCJGXDu491Y3rRgJPVhtdsY5ivkbQ5FJMDvPyanh2F7HNk2cea9AZIHa1j-RShETAsCxKqqbZ_Vz7J/pub"
    coord_str = fetch_coord_str(url)
    parsed_coords = extract_coords(coord_str)
    print_grid(parsed_coords)

main()