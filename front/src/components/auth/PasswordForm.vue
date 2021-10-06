<template>
  <b-row>
    <b-col md="6">
      <b-form-group label-for="password">
        <b-form-input
          id="password"
          type="password"
          v-model="user.password"
          required
          :placeholder="`${this.$t('auth.enterPassword')}...`"
          :state="getValidator().password.state"
          @change="checkValidity()"
        />
      </b-form-group>
    </b-col>
    <b-col md="6">
      <b-form-group label-for="passwordConfirmation">
        <b-form-input
          id="passwordConfirmation"
          type="password"
          v-model="user.password_confirmation"
          required
          :placeholder="`${this.$t('auth.repeatPassword')}...`"
          :state="getValidator().password_confirmation.state"
          @change="checkValidity()"
        />
      </b-form-group>
    </b-col>
  </b-row>
</template>

<script>
  import { validatePassword, validatePasswordConfirm } from "~/helpers/validators";

  export default {
    name: "RegisterForm",
    props: {
      user: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        isCompany: false,
      }
    },
    methods: {
      checkValidity() {
        const validator = this.getValidator();
        for (let key in validator)
          if(validator[key].valid === false) {
            this.$emit('validationChange', false);
            return;
          }

        this.$emit('validationChange', true);
      },
      getValidator() {
        return  {
          // password: validatePassword(this.user.password),
          // password_confirmation: validatePasswordConfirm(this.user.password_confirmation, this.user.password)
        };
      },
    }
  }
</script>

<style scoped>

</style>
