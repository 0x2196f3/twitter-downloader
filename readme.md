# Twitter-Downloader

download users all images and videos by twitter-id every 12 hours (NO TWITTER API NEEDS)
<br/>

#### based on [twmd](https://github.com/mmpx12/twitter-media-downloader)

## Environment Variables
| Environment Variable | Usage |
| --- | --- |
| `INTERVAL` | Try downloading tweets every `$INTERVAL` seconds |

## Volume Mapping
| Container Directory | Description                                                               |
| --- |---------------------------------------------------------------------------|
| `/downloads` | tweets will be downloaded here, organized by username                     |
| `/config/users.txt` | list of users to watch, one username per line, no `@` or other characters |
| `/config/twmd_cookies.json` | Your Twitter account cookies                                              |

## Usage
```bash
docker run -d --name=twitter-downloader -v /path/to/config:/config -v /path/to/downloads:/downloads -e INTERVAL:43200 twitter-downloader
```

## How to Get twmd_cookies.json
- goto [twitter-media-downloader](https://github.com/mmpx12/twitter-media-downloader/releases/)
- select the latest binary file that suite your architecture
- run twitter-media-downloader and login
```bash
./twitter-media-downloader twmd -u Spraytrains -a -L
```
- twmd_cookies.json will show in the same directory as the binary file