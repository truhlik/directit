<template>
  <div>
    <div class="h-100 bg-royal bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="app-logo-inverse mx-auto mb-3"/>

          <div class="modal-dialog w-100 mx-auto">
            <div class="modal-content">
              <div class="modal-body">
                <h1>{{ $t('common.redirecting') }}...</h1>
              </div>
            </div>
          </div>
          <div class="text-center text-white opacity-8 mt-3">
            Copyright &copy; Endevel {{ now }}
          </div>
        </b-col>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex';

  export default {
    name: 'Login',
    layout: 'userpage',
    async asyncData (context) {
      context.$auth.loginWith('social');
    },
    computed: {
      ...mapState({
        loggedIn: state => state.users.status,
      })
    },
    data() {
      return {
        now: new Date().getFullYear()
      }
    },
  }
</script>
