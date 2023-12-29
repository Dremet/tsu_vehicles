import re
import requests
from bs4 import BeautifulSoup
from typing import List, Union


def get_workshop_data_by_id(id: int) -> (str, str, Union[str, int], int):
    """
    Retrieve useful information from steam workshop about a certain car by digging into the html content.

    Currently this information is retrieved:
    - url to car preview image
    - (current) steam name of maker
    - steam id of maker
    - number of subs (to the workshop item)

    Does return (None, None, None) if the id of a built-in car is provided.
    """

    url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={id}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    ### CHECK IF DEFAULT TRACK ###
    # if the workshop item does not exist (f.e. cause it is a built-in car, we will receive an error)
    workshop_item_does_not_exist = any(
        [
            "An error was encountered while processing your request"
            in list(section_text.strings)[0]
            for section_text in soup.find_all("p", "sectionText")
        ]
    )

    if workshop_item_does_not_exist:
        return None, None, None, None

    ### GET LINK TO IMAGE ###
    try:
        preview_image_url = soup.find("img", id="previewImage").get("src")
    except AttributeError:
        # this happens if there are multiple images
        preview_image_url = soup.find("img", id="previewImageMain").get("src")

    ### GET NAME OF MAKER ###
    maker_name = list(soup.find("div", "friendBlockContent").strings)[0].strip()
    maker_id = soup.find("a", "friendBlockLinkOverlay").get("href").split("/")[-1]

    ### CURRENT SUBSCRIBERS ###
    td_tags_in_stats_table = soup.find("table", "stats_table").find_all("td")

    assert (
        td_tags_in_stats_table[3].string == "Current Subscribers"
    ), "Stats table on steam must have changed!"

    current_subs = int(td_tags_in_stats_table[2].string)

    return preview_image_url, maker_name, maker_id, current_subs


def get_all_vehicle_ids_from_workshop() -> List[int]:
    page = 1
    stop = False
    all_ids = []

    while not stop:
        print(page)
        try:
            ids_batch = get_most_recent_vehicle_ids_from_workshop(page)
            page += 1
        except:
            stop = True

        if len(ids_batch) == 0:
            stop = True

        all_ids += ids_batch

    return all_ids


def get_most_recent_vehicle_ids_from_workshop(page: int = 1) -> List[int]:
    """
    Gets workshop ids from most recently added vehicles.
    """
    url = f"https://steamcommunity.com/workshop/browse/?appid=1478340&requiredtags%5B0%5D=Vehicle&actualsort=mostrecent&browsesort=mostrecent&p={page}"
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # clickable links to the cars
    # that link holds the id of the vehicles, see below
    link_items = soup.find_all("a", "item_link")

    ids = []

    for link in link_items:
        # this is how link.get("href") looks like:
        # https://steamcommunity.com/sharedfiles/filedetails/?id=3123303314&searchtext=
        id = re.search(r"id\=(.*?)&searchtext", link.get("href")).group(1)

        ids.append(int(id))

    return ids


if __name__ == "__main__":
    print(get_workshop_data_by_id(3124957840))
