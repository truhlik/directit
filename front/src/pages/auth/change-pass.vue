<template>
  <div>
    <PageTitle :heading=title :subheading=subheading :icon=icon />
    <b-card :title="title" class="main-card mb-4">
      <b-row>
        <b-col md="6">
          <b-form-group label-for="oldPassword">
            <b-form-input
              id="oldPassword"
              type="password"
              v-model="old_password"
              required
              :placeholder="`${this.$t('auth.enterPassword')}...`"
            />
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col md="6">
          <b-form-group label-for="password">
            <b-form-input
              id="password"
              type="password"
              v-model="password"
              required
              :placeholder="`${this.$t('auth.enterPassword')}...`"
              :state="validator.password.state"
              @change="setValidator()"
            />
        </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group label-for="passwordConfirmation">
            <b-form-input
              id="passwordConfirmation"
              type="password"
              v-model="password_confirmation"
              required
              :placeholder="`${this.$t('auth.repeatPassword')}...`"
              :state="validator.password_confirmation.state"
              @change="setValidator()"
            />
          </b-form-group>
        </b-col>
      </b-row>

<!--      <PasswordForm :user="{password: password, password_confirmation: password_confirmation}"/>-->
      <b-row>
        <b-col>
          <b-button
            color="primary" class="btn-wide btn-pill btn-shadow btn-hover-shine" size="lg"
            @click="changePassword(password, password_confirmation)"
          >
<!--            TODO disalbed on formValid-->
            {{ $t('auth.changePassword') }}
          </b-button>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
  import PasswordForm from "~/components/auth/PasswordForm";
  import PageTitle from "~/components/partials/PageTitle";
  import { validatePassword, validatePasswordConfirm } from "~/helpers/validators";

  export default {
    name: 'passwordChange',
    components: {PageTitle, PasswordForm},
    data() {
      return {
        title: this.$t('passwordChange.title'),
        subheading: this.$t('passwordChange.subtitle'),
        icon: 'pe-7s-key icon-gradient bg-malibu-beach',

        formValid: false,
        old_password: undefined,
        password: undefined,
        password_confirmation: undefined,

        validator: {
          password: {},
          password_confirmation: {}
        }
      }
    },
    methods: {
      changePassword(){
        // TODO
      },
      checkValidity() {
        for (let key in this.validator)
          if(this.validator[key].valid === false) {
            this.formValid = false;
            return;
          }

        this.formValid = true;
      },
      setValidator() {
        this.validator = {
          // password: validatePassword(this.password),
          // password_confirmation: validatePasswordConfirm(this.password_confirmation, this.password)
        };
      },
    },
    mounted() {
      this.setValidator();
    }
  }
</script>

<style scoped>
  :disabled {
    cursor: not-allowed;
  }
</style>

