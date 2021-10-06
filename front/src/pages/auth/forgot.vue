<template>
  <div>
    <div class="h-100 bg-royal bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="6" class="mx-auto app-login-box">
          <div class="app-logo-inverse mx-auto mb-3"/>
          <div class="modal-dialog w-100">
            <div class="modal-content">
<!--              <img src="~/assets/img/logos/dark_wide.svg" class="logo">-->
              <div class="modal-header">
                <div class="h5 modal-title">
                  Forgot your Password?
                  <h6 class="mt-1 mb-0 opacity-8">
                    <span>Use the form below to recover it.</span>
                  </h6>
                </div>
              </div>
              <div class="modal-body">
                <div>
                  <Form>
                    <b-row form>
                      <b-col md="12">
                        <b-form-group>
                          <label for="email">Email</label>
                          <b-form-input type="email" name="email" id="email"
                                        placeholder="Email here..."/>
                        </b-form-group>
                      </b-col>
                    </b-row>
                  </Form>
                </div>
                <div class="divider"/>
                <h6 class="mb-0">
                  <nuxt-link :to="localePath({name:'auth-login'})" class="text-primary">
                    Sign in existing account
                  </nuxt-link>
                </h6>
              </div>
              <div class="modal-footer clearfix">
                <div class="float-right">
                  <b-button variant="primary" size="lg">Recover Password</b-button>
                </div>
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
  export default {
    name: 'Forgot',
    layout: 'userpage',
    auth: false,
    data() {
      return {
        now: new Date().getFullYear()
      }
    }
  }
</script>
