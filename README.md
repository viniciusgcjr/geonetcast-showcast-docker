# Dockerized geonetcast - Showcast

Show the satalite images from docker containers....

# Developers

* @marcellodesales - Computer Scientist
* @viniciusgcjr - Meteorologist

# Architecture

* agent: downloads the images from satalites
* webserver: serves the HTML page that renders the downloaded images

```
                              ┌─────────────┐
                              │ Showcast    │
                           ┌──┤             ├──┐
                           │  │ Images Agent│  │
          Download Images  │  └──────┬──────┘  │Download Images
                           │         │         │
                           └──────┐  │  ┌──────┘
                                  │  │  │
    ┌───────────┐               ┌─▼──▼──▼┐        ┌─────────────────┐
    │           │               │        │        │ Showcast        │
┌───┤ CHPC UTAH ├───────────────►   S3   ◄────────┤                 │
│   │           │               │        │        │ Frontend Server │
│   └───▲───────┘ Upload images └────────┘        └─────────────────┘
│       │         To the Cloud              Serves Images
└───────┘          Blob Store                Using Web Server
 Process
  Images
```

# Setup

```console
docker build -t marcellodesales/geonetcast-showcast-docker .
```

# Run

```

```
