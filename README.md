# Twitter-Downloader

download users all images and videos by twitter-id every 6 hours (login required, no twitter api required)
<br/>

#### based on [twitter_download](https://github.com/caolvchong-top/twitter_download)

## Environment Variables
| Environment Variable | Usage |
| --- | --- |
| `INTERVAL` | Try downloading tweets every `$INTERVAL` seconds |

## Volume Mapping
| Container Directory | Description                                                               |
| --- |---------------------------------------------------------------------------|
| `/download` | tweets will be downloaded here, organized by username                     |
| `/config/settings.json` | the settings.json file of [twitter_download](https://github.com/caolvchong-top/twitter_download) |

## Usage
```bash
docker run -d --name=twitter-downloader -v /path/to/config:/config -v /path/to/download:/download -e INTERVAL:43200 docker.io/0x2196f3/twitter-downloader
```
