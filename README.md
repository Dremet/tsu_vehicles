# TSU Vehicles

This project revolves around extracting data from JSON files and web scraping the Steam Workshop to gather information on TSU vehicles. The collected data is then stored in an SQLite database, which will be utilized by a dedicated website.

## What is TSU?

TSU stands for Turbo Sliders Unlimited, a driving game with a strong emphasis on online multiplayer, user-created content, and moddability. It serves as a spiritual successor to classic top-down racing games, now in 3D with modern online features. Whether for casual fun or serious competition, TSU offers a versatile racing experience. For more details, refer to the [Steam game description](https://store.steampowered.com/app/1478340/Turbo_Sliders_Unlimited/).


## Purpose of this Project

The uniqueness of TSU lies in its moddability, with the community creating numerous cars and tracks. However, managing an overview of all available cars can be challenging. Currently, the [Steam Workshop page for TSU vehicles](https://steamcommunity.com/workshop/browse/?appid=1478340&requiredtags%5B0%5D=Vehicle&actualsort=mostrecent&browsesort=mostrecent&p=1) serves as the primary source, but it lacks user-friendliness and detailed information.

This project aims to create a database for an optimized TSU vehicle website (not part of this repository). The website could:

1. Recommend specific cars to beginners for various categories (e.g., GT, Formula, Rally, Fun).
2. Display physics values set in the vehicle editor.
3. Showcase historical changes to vehicles.
4. Present typical/average values for all vehicle parameters.
5. Provide information on creating custom cars.
6. Offer enhanced filters (e.g., categories like GT).
7. And more.
These are just initial ideas.


## How it Works

The project relies on two data sources:
1. [Steam Workshop](https://steamcommunity.com/workshop/browse/?appid=1478340&requiredtags%5B0%5D=Vehicle&actualsort=mostrecent&browsesort=mostrecent&p=1): Web scraping extracts information about vehicle/workshop IDs, preview images, subscriber count, etc.
2. Vehicle JSON files: Future updates to the game will allow exporting vehicle settings as JSON files from the in-game vehicle editor. Examples provided by the supportive game developer can be found in [/vehicles](/vehicles).

## Database

For simplicity and low complexity, an SQLite database is used. It requires minimal setup and stores data in a  file.

## Contribution

Feel free to contact me on Discord (dremet / André Petersen) if you want to share thoughts or contribute to the code.