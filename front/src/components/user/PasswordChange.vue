<template>
	<div>
		<div class="change-pswd-con form-con">
			<h2 class="text-center">{{ $t('account.change_your_password') }}</h2>
			<b-row>
				<b-col sm="12" class="d-flex justify-content-center">
					<b-form-group id="group_new_password"
					              label-for="id_new_password">
						<b-form-input id="id_new_password"
						              type="password"
						              v-model="user.new_password1"
						              required
						              v-bind:placeholder="$t('account.password')"
						              @input="validate('new_password1')">
						</b-form-input>
						<span class="text-danger" v-for="(error, index) in objectError.new_password1"
						      :key="index">{{ error }}<br></span>
					</b-form-group>
				
				</b-col>
				<b-col sm="12" class="d-flex justify-content-center">
					<b-form-group id="group_password_confirm"
					              label-for="id_password_confirm">
						<b-form-input id="id_password_confirm"
						              type="password"
						              v-model="user.new_password2"
						              required
						              v-bind:placeholder="$t('account.password_again')"
						              @input="validate('new_password2')">
						</b-form-input>
						<span class="text-danger" v-for="(error, index) in objectError.new_password2"
						      :key="index">{{ error }}<br></span>
					</b-form-group>
				
				</b-col>
				<b-col sm="12" class="d-flex justify-content-center">
						<b-button @click="sendNewPassword" variant="primary" size="lg">{{ $t('form.button.change')}}</b-button>
				</b-col>
			</b-row>
		</div>
	</div>
</template>

<script>
  import {mapActions, mapState} from 'vuex'
  import PasswordChange from "~/components/user/PasswordChange";

  export default {
		name: 'user-edit',
    components: {PasswordChange},
    data () {
      return {
        user: {
          new_password1: '',
          new_password2: '',
        },
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
	      const url = 'accounts/password/change/';
	      const data = {
	        new_password1: this.user.new_password1,
		      new_password2: this.user.new_password2
	      };
	      this.$axios.$post(url, data).then(
	        response => {
	          this.user = {}
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
	}
</script>