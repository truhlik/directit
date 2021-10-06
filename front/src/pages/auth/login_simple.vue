<template>
  <div>
    <div class="h-100 bg-plum-plate bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">

          <div class="modal-dialog w-100 mx-auto">
            <form class="modal-content" @submit.prevent="handleSubmit">

              <div class="card text-white card-body bg-danger" v-if="alert.message">
                <h5 class="text-white card-title">{{ alert.message }}</h5>
              </div>

              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <div>Vítejte zpět,</div>
                    <span>prosím, přihlašte se ke svému účtu níže.</span>
                  </h4>
                </div>
                <b-form-group id="exampleInputGroup1"
                              label-for="exampleInput1">
                  <b-form-input id="exampleInput1"
                                type="email"
                                v-model="email"
                                required
                                placeholder="Váš email...">
                  </b-form-input>
                </b-form-group>
                <b-form-invalid-feedback id="inputLiveFeedback">
                  Email musí být vyplněný
                </b-form-invalid-feedback>
                <b-form-group id="exampleInputGroup2"
                              label-for="exampleInput2">
                  <b-form-input id="exampleInput2"
                                type="password"
                                v-model="password"
                                required
                                placeholder="Vaše heslo...">
                  </b-form-input>
                </b-form-group>
              </div>
              <div class="modal-footer clearfix">
                <div class="float-right">
                  <b-button :type="'submit'" variant="primary" :disabled="status.loggingIn" size="lg">Přihlásit se</b-button>
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
    data() {
      return {
        email: '',
        password: '',
        submitted: false
      }
    },
    computed: {
      ...mapState({
        // alert: state => state.alert,
        // status: state => state.users.status
      })
    },
    methods: {
      // ...mapActions('users/login'),
      handleSubmit(e) {
        this.submitted = true;
        const {email, password} = this;
        // if (email && password) {
        //   this.login({email, password})
        // }
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
