<template>
  <div>
    <div class="h-100 bg-royal bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="app-logo-inverse mx-auto mb-3"/>
          <div class="modal-dialog w-100">
            <form class="modal-content">
<!--              <img src="~/assets/img/logos/dark_wide.svg" class="logo">-->
              <div class="modal-body">
                <div class="divider"/>

                <p class="text-center font-size-xlg">
                  {{ $t('auth.registrationSuccess') }}
                </p>

              </div>
              <div class="modal-footer d-block text-center">
                <nuxt-link :to="localePath({name:'auth-login'})"
                  class="btn btn-secondary btn-lg btn-wide btn-pill btn-shadow btn-hover-shine"
                >
                  {{ $t('auth.signIn') }}
                </nuxt-link>
              </div>
            </form>
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
    name: 'registerSuccess',
    layout: 'userpage',
    auth: false,
    data() {
      return {
        now: new Date().getFullYear(),
      }
    }
  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Yellowtail&display=swap');

  .modal-body {
    padding: 0;
  }
</style>

