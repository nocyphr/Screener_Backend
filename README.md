- [About](#about)
- [Structure](#structure)


# About
I will fill this in tomorrow :D i am quite tired today


# Structure
```
├── db
│   ├──data
│   │   └──... # persist db data through compose volume mapping
├── docker
│   ├── assets
│   │   ├── api_requirements.txt # pip install packages for fastAPI
│   │   ├── data.json # dummy data, will be replace by a test table in db later
│   │   └── db.env # expected to exist, not committed for obvious reasons
│   ├── docker.api.dockerfile
│   └── docker-compose.dev.yml
├── src
│    ├──api
│    │  └── api.py # just the barebones root api
├── README.md
└── dev.sh # start your dev version of everything quickly using `bash dev.sh`
```