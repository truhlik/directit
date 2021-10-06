<template>
  <div>
    <div class="bg-blue-icon bg-animation full-h pb-5 pt-5">
      <div class="d-flex justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="text-center">
	          <LogoWhite></LogoWhite>
          </div>

          <div class="modal-dialog w-100 mx-auto">
            <form class="modal-content" @submit.prevent="sendRegistration">
              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('account.registration_client') }}</span>
                  </h4>
                  <div class="registration-infotext d-block font-weight-normal mt-1 mb-2 grey--text">{{ $t('account.registration_client_infotext') }}</div>
                </div>

                <b-form-group id="id_group_company_name"
                              label-for="id_company_name"
                              :label="$t('form.company_name')">
                  <b-form-input id="id_email"
                                :class="{ 'error' : objectError.company_name }"
                                type="text"
                                v-model="new_user.company_name"
                                :placeholder="$t('form.company_name')"
                                @input="validate('company_name')">
                  </b-form-input>
                  <span class="text-danger" v-for="(error, index) in objectError.company_name" :key="index">{{ error }}<br></span>
                </b-form-group>

                <b-form-group id="id_group_email"
                              label-for="id_email"
                              :label="$t('form.email')">
                  <b-form-input id="id_email"
                                :class="{ 'error' : objectError.email }"
                                type="email"
                                v-model="new_user.email"
                                placeholder="E-mail"
                                @input="validate('email')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.email" :key="index">{{ error }}<br></span>
                </b-form-group>

                <b-form-group id="id_group_password1"
                              label-for="id_password1"
                              :label="$t('account.password')">
                  <b-form-input id="id_password1"
                                :class="{ 'error' : objectError.password1 }"
                                type="password"
                                v-model="new_user.password1"
                                v-bind:placeholder="$t('account.password')"
                                @input="validate('password1')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.password1" :key="index">{{ error }}<br></span>
                </b-form-group>

                <b-form-group id="id_group_password2"
                              label-for="id_password2"
                              :label="$t('account.password_again')">
                  <b-form-input id="id_password2"
                                :class="{ 'error' : objectError.password2 }"
                                type="password"
                                v-model="new_user.password2"
                                v-bind:placeholder="$t('account.password')"
                                @input="validate('password2')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.password2" :key="index">{{ error }}<br></span>
                </b-form-group>

                <b-form-group id="id_group_phone"
                              label-for="id_phone"
                              :label="$t('form.phone')">
                  <b-form-input id="id_phone"
                                :class="{ 'error' : objectError.phone }"
                                type="text"
                                v-model="new_user.phone"
                                :placeholder="$t('form.phone')"
                                @input="validate('phone')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.phone" :key="index">{{ error }}<br></span>
                </b-form-group>

                <b-form-group id="id_group_job"
                              label-for="id_job"
                              :label="$t('form.job')">
                  <b-form-input id="id_job"
                                :class="{ 'error' : objectError.job }"
                                type="text"
                                v-model="new_user.job"
                                :placeholder="$t('form.job')"
                                @input="validate('job')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.job" :key="index">{{ error }}<br></span>
                </b-form-group>

              </div>
              <div class="modal-footer clearfix">
	              <nuxt-link :to="localePath({name:'login'})" variant="primary" size="lg">{{ $t('account.login') }}</nuxt-link>
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
  import {getters} from "~/store/errors";
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
          },
          company_name: {
            name: 'company_name',
            rules: ['required'],
          },
          phone: {
            name: 'phone',
            rules: ['required'],
          },
          job: {
            name: 'job',
            rules: ['required'],
          },
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
		      password2: this.new_user.password2,
		      company_name: this.new_user.company_name,
		      phone: this.new_user.phone,
		      job: this.new_user.job,
	      };
		    await this.$axios.post('accounts/registration/client/', data).then(
		      response => {
		        this.$router.push('/');
		      },
          error => {

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

  .registration-infotext {
      color: $dark_brand;
      font-size: 14px;
  }
</style>
