require('dotenv').config();

let modulesOptions = [
    '@nuxtjs/auth',
    '@nuxtjs/axios',
    '@nuxtjs/sentry',
    '@nuxtjs/svg',
    '@nuxtjs/toast',
    'bootstrap-vue/nuxt',
    'nuxt-i18n',
    '@nuxtjs/style-resources',
  ];

if(process.env.HOTJAR_ID) {
  modulesOptions.push(
    ['@netsells/nuxt-hotjar', {
        id: process.env.HOTJAR_ID,
        sv: 6,
    }]
  )
}

export default {
  mode: 'spa',
  /*
  ** Headers of the page
  */
  head: {
    title: 'Direct IT admin',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
    'assets/base.scss',
    'assets/variables.scss',
    "~layouts/global.css",
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    { src: '~plugins/api.js' },
    { src: '~plugins/vuelidate.js' },
    { src: '~plugins/vue-rate.js' },
    { src: '~plugins/date-picker.js' },
    { src: '~plugins/fontawesome.js' },
    { src: '~plugins/mapy_cz.js' },
    { src: '~plugins/filters.js' },
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/style-resources',
  ],
  /*
  ** Nuxt.js modules
  */
  modules: modulesOptions,
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    credentials: true
  },
  /*
  ** Build configuration
  */

  styleResources: {
    scss: [
        'assets/variables.scss'
    ]
  },

  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  },

  env: {
    NUXT_ENV_API_URL: process.env.NUXT_ENV_API_URL,
    NUXT_ENV_SENTRY_DSN: process.env.NUXT_ENV_SENTRY_DSN
  },
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: process.env.NUXT_ENV_API_URL + `accounts/login/`, method: 'POST', propertyName: 'key' },
          logout: { url: process.env.NUXT_ENV_API_URL + `accounts/logout/`, method: 'POST'},
          user: false
        },
        tokenRequired: true,
        tokenType: 'Token'
      },
    },
    redirect: {
      login: '/login',
      logout: '/login',
      callback: '/login',
      home: '/'
    }
  },
  /*
  ** Toasted options
  */
  toast: {
    duration: 2000,
    position: 'top-left'
  },
  /*
  ** i18n
   */
  i18n: {
    locales: [
      {
        title: 'Česky',
        code: 'cs',
        iso: 'cs-CZ',
        file: 'cs-CZ.js'
      }
    ],
    langDir: 'locales/',
    lazy: true,
    defaultLocale: 'cs'
  },

  /*
  ** Sentry
   */
 sentry: {
    dsn: process.env.NUXT_ENV_SENTRY_DSN || '',
  },

  router: {
    mode: "hash"
  },

  server: {
    port: 54531 // default: 3000
  }

}
