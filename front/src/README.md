# directit-front

> Nuxt.js part of the Direct IT project

## Build Setup

``` bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

## Vytvoření .env souboru v rootu front projektu
NUXT_ENV_API_URL='http://localhost:8000/api/v1/'
NUXT_ENV_SENTRY_DSN=''

# in case of Error: listen EACCES: permission denied 127.0.0.1:54531 run this in PowerShell
net stop winnat
net start winnat