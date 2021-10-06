<template>
  <div>
    <div class="h-100 bg-royal bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="app-logo-inverse mx-auto mb-3"/>

          <div class="modal-dialog w-100 mx-auto">
            <div class="modal-content">
<!--              <img src="~/assets/img/logos/dark_wide.svg" class="logo">-->
              <div class="modal-body">
                <div class="divider"/>
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('auth.untilNextTime') }}</span>
                  </h4>
                  <h5>
                    <span>{{ $t('auth.thankYouForYourTime') }}</span>
                  </h5>
                </div>
              </div>
              <div class="modal-footer justify-content-center">
                <nuxt-link class="btn btn-primary btn-lg" :to="localePath({name:'auth-login'})">
                  {{ $t('auth.loginBack') }}
                </nuxt-link>
              </div>
            </div>
          </div>
          <div class="text-center text-white opacity-8 mt-3">
            {{ $t('common.copyright') }} &copy; {{ $t('common.endevel') }} {{ now }}
          </div>
        </b-col>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "logout",
    layout: 'userpage',
    auth: false,
    data() {
      return {
        now: new Date().getFullYear()
      }
    },
  }
</script>

<style scoped>
  .modal-body {
    padding: 0;
  }
</style>
