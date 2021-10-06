
<template>
  <div>
    <div class="h-100 bg-blue-icon bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center flex-wrap">
        <b-col md="8" class="mx-auto app-login-box">
	        <div class="text-center">
	            <LogoWhite></LogoWhite>
	        </div>
          <div class="modal-dialog w-100 mx-auto">

            <form class="modal-content"
                  @submit.prevent="login"
                  v-if="!showForgetPassword">
              <div class="modal-body login-modal">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('account.welcome') }}</span>
                  </h4>
                </div>
                <b-form-group id="id_email_group"
                              label-for="id_email"
                              :label="$t('form.email')">
                  <b-form-input id="id_email"
                                :class="{ 'error' : objectError.email }"
                                type="email"
                                v-model="user.email"
                                required
                                placeholder="E-mail"
                                @input="validate('email')">
                  </b-form-input>
	                <span class="text-danger" v-for="(error, index) in objectError.email" :key="index">{{ error }}<br></span>
                </b-form-group>
                <b-form-group id="id_password_group"
                              label-for="id_password"
                              :label="$t('form.password')"
                              v-if="!showForgetPassword">
                  <b-form-input id="id_password"
                                type="password"
                                v-model="user.password"
                                required
                                v-bind:placeholder="$t('account.password')">
                  </b-form-input>
	                <span class="text-danger" v-for="(error, index) in objectError.password" :key="index">{{ error }}<br></span>
                </b-form-group>
              </div>
              <div class="modal-footer clearfix">
                  <b-link @click="loginForgetToggle" variant="primary" size="lg">{{ $t('account.forgot_password') }}</b-link>

                  <nuxt-link :to="localePath({name:'registrace-klient'})" variant="primary" size="lg">{{ $t('account.registration') }}</nuxt-link>

                  <b-button type="submit" variant="primary" size="lg">{{ $t('account.login') }}</b-button>
              </div>
            </form>


            <form class="modal-content"
                  @submit.prevent="sendForgotPassword"
                  :key="showForgetPassword"
                  v-else>
              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('account.your_email') }}</span>
                  </h4>
                </div>
                <b-form-group id="id_email_frg_group"
                              label-for="id_email">
                  <b-form-input id="id_email_frg"
                                :class="{ 'error' : objectError.email }"
                                type="email"
                                v-model="user.email"
                                required
                                placeholder="E-mail"
                                @input="validate('email')">
                  </b-form-input>
	                <span class="text-danger" v-for="(error, index) in objectError.email" :key="index">{{ error }}<br></span>
                </b-form-group>
              </div>
              <div class="modal-footer clearfix">
	                <b-link @click="loginForgetToggle" variant="primary" size="lg">{{ $t('account.login') }}</b-link>

                  <b-link to="/registration" variant="primary" size="lg">{{ $t('account.registration') }}</b-link>
	                <b-button @click="sendForgotPassword" variant="primary" size="lg">{{ $t('form.button.send') }}</b-button>
              </div>
            </form>

          </div>
          <div class="text-center text-white opacity-8 mt-3">
            &copy;{{ new Date().getFullYear() }} Endevel s. r. o.
          </div>
        </b-col>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'
  import LogoWhite from '~/components/LogoWhite'

  export default {
    layout: 'userpage',
	  components: {
      LogoWhite
	  },
    data() {
      return {
        user: {
          email: '',
	        password: ''
        },
        submitted: false,
	      showForgetPassword: false,
	      objectValidator: {
          email: {
            name: 'email',
            rules: ['email']
          }
	      }
      }
    },
    computed: {
      ...mapState({
        objectError: state => state.errors.objectError
      })
    },
    methods: {
      ...mapActions('errors', {
	      inputValidate: 'validate',
	      cleanErrorObject: 'cleanErrorObject'
	    }),
      async login(){
        this.$toast.show(this.$t('account.logging_in'));
        try {
	        await this.$auth.loginWith('local', {
	            data: this.user
	          });
	        this.$toast.success(this.$t('account.logged_in'));
        } catch(e){
        }
      },
	    sendForgotPassword(){
        const data = {
          email: this.user.email
        };
        this.$axios.$post('/accounts/password/reset/', data).then(
          response => {
            this.loginForgetToggle();
          }
        );

	    },
	    validate(input) {
	      const data = {
	        name: input,
		      objectData: this.user,
		      objectValidator: this.objectValidator
	      };
	      this.inputValidate(data);
	    },
	    loginForgetToggle(){
        this.showForgetPassword = !this.showForgetPassword;
        this.cleanErrorObject();
	    }
    }
  };
</script>

<style lang="scss">
  .modal-content{
    overflow: hidden;
  }
  .card{
    border-radius: 0;

    h5{
      margin: 0;
      text-align: center;
    }
  }
</style>
