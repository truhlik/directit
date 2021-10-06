<template>
  <div>
    <div class="h-100 bg-blue-icon bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box text-center">
<!--	        <LogoWhite></LogoWhite>-->
          <div class="modal-dialog w-100 mx-auto">
            <form class="modal-content" @submit.prevent="sendRegistration">
              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('account.registration') }}</span>
                  </h4>
                </div>
	              
                <b-form-group id="id_group_email" label-for="id_email">
                  <b-form-input id="id_email"
                                :class="{ 'error' : objectError.email }"
                                type="email"
                                v-model="new_user.email"
                                placeholder="E-mail"
                                @input="validate('email')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.email" :key="index">{{ error }}<br></span>
                </b-form-group>
	              
                <b-form-group id="id_group_password1" label-for="id_password1">
                  <b-form-input id="id_password1"
                                :class="{ 'error' : objectError.password1 }"
                                type="password"
                                v-model="new_user.password1"
                                v-bind:placeholder="$t('account.password')"
                                @input="validate('password1')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.password1" :key="index">{{ error }}<br></span>
                </b-form-group>
	              
                <b-form-group id="id_group_password2" label-for="id_password2">
                  <b-form-input id="id_password2"
                                :class="{ 'error' : objectError.password2 }"
                                type="password"
                                v-model="new_user.password2"
                                v-bind:placeholder="$t('account.password')"
                                @input="validate('password2')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.password2" :key="index">{{ error }}<br></span>
                </b-form-group>
	              
              </div>
              <div class="modal-footer clearfix">
	              <b-link to="/login" variant="primary" size="lg">{{ $t('account.login') }}</b-link>
	              <b-button type="submit" :disabled="!(Object.keys(objectError).length === 0)" variant="primary" size="lg">{{ $t('account.sign_in') }}</b-button>
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
  import {getters} from "../store/errors";
  import LogoWhite from '~/components/LogoWhite'

  export default {
    layout: 'userpage',
	  components: {
      LogoWhite
	  },
    data() {
      return {
        new_user: Object,
	      objectValidator: {
          email: {
            name: 'email',
            rules: ['email', 'required']
          },
          password1: {
            name: 'password1',
            rules: ['required', 'password']
          },
          password2: {
            name: 'password2',
            rules: ['required', 'sameAs'],
	          sameAs: 'password1'
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
	    async sendRegistration() {
	      let data = {
		      email: this.new_user.email,
		      password1: this.new_user.password1,
		      password2: this.new_user.password2
	      };
		    await this.$axios.post('accounts/registration/', data).then(
		      response => {
		        this.$router.push('/');
		      }
		    );
	    },
	    validate(input) {
	      const data = {
	        name: input,
		      objectData: this.new_user,
		      objectValidator: this.objectValidator
	      };
	      this.inputValidate(data);
	    },
      ...mapActions('errors', {
	      inputValidate: 'validate'
	    })
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