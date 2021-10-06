<template>
  <div>
    <div class="h-100 bg-plum-plate bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">

          <div class="modal-dialog w-100 mx-auto">
            <form class="modal-content" @submit.prevent="handleSubmit">
              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <span>{{ $t('account.add_new_password') }}</span>
                  </h4>
                </div>
                <b-form-group id="group_new_password"
                              label-for="id_new_password">
                  <b-form-input id="id_new_password"
                                type="password"
                                v-model="user.new_password1"
                                required
                                v-bind:placeholder="$t('account.password')"
                                @input="validate('new_password1')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.new_password1" :key="index">{{ error }}<br></span>
                </b-form-group>
                <b-form-group id="group_password_confirm"
                              label-for="id_password_confirm">
                  <b-form-input id="id_password_confirm"
                                type="password"
                                v-model="user.new_password2"
                                required
                                v-bind:placeholder="$t('account.password_again')"
                                @input="validate('new_password2')">
                  </b-form-input>
		              <span class="text-danger" v-for="(error, index) in objectError.new_password2" :key="index">{{ error }}<br></span>
                </b-form-group>
              </div>
              <div class="modal-footer clearfix">
                <div class="float-right">
	                <b-button @click="sendNewPassword" variant="primary" size="lg">{{ $t('form.button.send')}}</b-button>
                </div>
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

  export default {
    name: 'passwordChange',
    layout: 'userpage',
	  middleware ({ route, redirect }) {
      if(!route.query.hasOwnProperty('uid') || !route.query.hasOwnProperty('token'))
        redirect('/');
	  },
    data () {
      return {
        user: {
	        new_password1: '',
	        new_password2: '',
        },
	      uid: this.$route.query.uid,
	      token: this.$route.query.token,
	      objectValidator: {
          new_password1: {
            name: 'new_password1',
            rules: ['required', 'password']
          },
          new_password2: {
            name: 'new_password2',
            rules: ['required', 'sameAs'],
	          sameAs: 'new_password1'
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
	    sendNewPassword(){
	      const url = 'accounts/password/reset/confirm/';
	      const data = {
	        new_password1: this.user.new_password1,
		      new_password2: this.user.new_password2,
	        uid: this.uid,
		      token: this.token
	      };
	      this.$axios.$post(url, data).then(
	        response => {
	          this.$router.push('/');
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