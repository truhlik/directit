import Cookies from 'js-cookie'

import handleErrorResponse from "~/helpers/handleErrorResponse";

export default function ({ $axios, redirect }) {
  $axios.onRequest(config => {
    if (config.data && typeof(config.data) === "object") {
      for (let key in config.data) {
        if(config.data[key] === '') config.data[key] = null;
      }
    }
    return config;
  }, function (error) {
    return Promise.reject(error);
  });

  $axios.onError(err => {
    if (!err.response) return Promise.reject(err);

    if (err.response.status === 401) {
      window.location = '/login';
    } else {
      const handledError = handleErrorResponse(err.response);

      if (window.$nuxt) {
        if (handledError.errorObject) window.$nuxt.$store.commit('errors/setErrorObject', handledError.errorObject);
        if (handledError.message) window.$nuxt.$toasted.error(handledError.message, {duration: 5000});
        return Promise.reject(handledError);
      }

      return Promise.reject(err);
    }
  });

  $axios.onResponse(response => {
    if (response.data) window.$nuxt.$toasted.success(response.data.detail, {duration: 5000});
  });

  $axios.defaults.baseURL = process.env.NUXT_ENV_API_URL;
  $axios.defaults.withCredentials = true;
  $axios.defaults.headers.common.Authorization = localStorage.getItem('auth._token.local');
  // $axios.defaults.headers.common['Content-Language'] = localStorage.getItem('lang') || navigator.language;
}
