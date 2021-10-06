<template>
  <div>
    <div class="h-100 bg-royal bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="app-logo-inverse mx-auto mb-3"/>
          <div class="modal-dialog w-100">;
            <form class="modal-content">
              <div class="modal-body">
                <div class="modal-title">
<!--                  <img src="~/assets/img/logos/dark_wide.svg">-->
                </div>
                <div class="divider"/>

                <RegisterForm :user="newUser" @validationChange="changeCompanyFormState"/>

                <div class="divider"/>

                <PasswordForm :user="newUser" @validationChange="changePasswordFormState"/>

                <div class="divider"/>

                <h6 class="mb-0">
                  {{ $t('auth.alreadyHave') }}
                  <nuxt-link :to="localePath({name:'auth-login'})" class="text-primary">
                    {{ $t('auth.signIn') }}
                  </nuxt-link>
                  |
                  <nuxt-link :to="localePath({name:'auth-forgot'})" class="text-primary">
                    {{ $t('auth.recoverPassword') }}
                  </nuxt-link>
                </h6>
              </div>
              <div class="modal-footer d-block text-center">
                <b-button
                  class="btn-wide btn-pill btn-shadow btn-hover-shine" size="lg"
                  :disabled="!isFormValid()"
                  @click="handleSubmit()"
                >
                  {{ $t('auth.createAccount') }}
                </b-button>
                <p class="mt-1 mb-0">
                  <small>
                    {{ $t('common.acceptingBySubmit') }}
                    <a href="https://rmotor.endevel.cz/terms/terms" target="_blank">
                      {{ $t('common.termsAndConditions') }}
                    </a>.
                  </small>
                </p>
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
  import {mapActions} from 'vuex';
  import PasswordForm from "~/components/auth/PasswordForm";
  import RegisterForm from "~/components/auth/RegisterForm";

  export default {
    name: 'register',
    components: { PasswordForm, RegisterForm },
    layout: 'userpage',
    auth: false,
    data() {
      return {
        newUser: {},
        now: new Date().getFullYear(),

        companyFormValid: null,
        passwordFormValid: null,
      }
    },
    methods: {
      ...mapActions({
        crateCompany: 'company/crateCompany',
      }),
      changeCompanyFormState(isValid) {
        this.companyFormValid = isValid;
      },
      changePasswordFormState(isValid) {
        this.passwordFormValid = isValid;
      },
      handleSubmit() {
        this.crateCompany(this.newUser).then(
          () => this.$router.push(this.localePath({name:'auth-register-success'}))
        ).catch(e => this.$toast.error(this.$t('common.serverError')))
      },
      isFormValid() {
        return this.companyFormValid && this.passwordFormValid;
      },
    },
  }
</script>

<style scoped lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Yellowtail&display=swap');

  :disabled {
    cursor: not-allowed;
  }

  .modal-title {
    text-align: center;

    img {
      max-width: 80%;
    }
  }
</style>

