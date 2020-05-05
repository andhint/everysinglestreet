# everysinglestreet
This summer I'm making it my goal to ride every street in the city of Buffalo. This repo will contains the code for tracking and visualizing my progress. I've been tracking all my rides using Strava and exporting the raw GPX files. This code produces a html file of "slippy" map with the GPS paths of my rides which allows me to see which areas of the city I've completed and which I to do. The current version of this map can be found [here](https://andhint.github.io/everysinglestreet/map.html).

## Project Organization
```
├── README.md  
├── requirement.txt          <- requirements for reproducing environment       
├── data
│   ├── geo                  <- Spatial files (ex Buffalo municipal boundary geojson)
│   └── rides                <- GPX files of rides (Exported from Strava)
├── src
│   ├── everysinglestreet.py <- main script to read GPX files and produce progress map
│   └── everysinglestreet    <- Python package with classes/functions
└── docs                     <- output directory for html map. Set up to be source for github project pages

```
Roughly based off of [Cookie Cutter Data Science structure](https://drivendata.github.io/cookiecutter-data-science/)

## Environment/Requirements
Created in Python 3, requirements are recorded in [requirements.txt](https://github.com/andhint/everysinglestreet/blob/master/requirements.txt)

To reproduce (recommended within a virtual env): `pip install -r requirements.txt`

