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
                                        <span>{{ $t('account.registration_consultant') }}</span>
                                    </h4>
                                </div>
                                
                                <ares-box :ares-data="aresData" :loading-ares="loadingAres"></ares-box>

                                <b-form-group id="id_reg_number_label"
                                              label-for="id_reg_number"
                                              :label="$t('form.reg_number')">
                                    <b-form-input id="id_reg_number"
                                                  :class="{ 'error' : objectError.reg_number }"
                                                  type="text"
                                                  v-model="new_user.reg_number"
                                                  :placeholder="$t('form.reg_number')"
                                                  @input="debounceRegNumberInput();">
                                    </b-form-input>
                                    <span class="text-danger" v-for="(error, index) in objectError.reg_number" :key="index">{{ error }}<br></span>
                                </b-form-group>

                                <b-form-group id="id_full_name_label"
                                              label-for="id_full_name"
                                              :label="$t('form.full_name')">
                                    <b-form-input id="id_full_name"
                                                  :class="{ 'error' : objectError.full_name }"
                                                  type="text"
                                                  v-model="new_user.full_name"
                                                  :placeholder="$t('form.full_name')"
                                                  @input="validate('full_name')">
                                    </b-form-input>
                                    <span class="text-danger" v-for="(error, index) in objectError.username" :key="index">{{ error }}<br></span>
                                </b-form-group>

                                <!--<b-form-group id="id_username_label"
                                              label-for="id_username"
                                              :label="$t('form.username')">
                                  <b-form-input id="id_username"
                                                :class="{ 'error' : objectError.username }"
                                                type="text"
                                                v-model="new_user.username"
                                                :placeholder="$t('form.username')"
                                                @input="validate('username')">
                                  </b-form-input>
                                  <span class="text-danger" v-for="(error, index) in objectError.username" :key="index">{{ error }}<br></span>
                                </b-form-group>-->

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

                                <b-form-group id="id_group_phone"
                                              label-for="id_phone"
                                              :label="$t('form.phone')">
                                    <b-form-input id="id_phone"
                                                  :class="{ 'error' : objectError.phone }"
                                                  type="tel"
                                                  v-model="new_user.phone"
                                                  :placeholder="$t('form.phone')"
                                                  @input="validate('phone')">
                                    </b-form-input>
                                    <span class="text-danger" v-for="(error, index) in objectError.phone" :key="index">{{ error }}<br></span>
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


                            </div>
                            <div class="modal-footer clearfix">
                                <nuxt-link :to="localePath({name:'login'})" variant="primary" size="lg">{{ $t('account.login') }}</nuxt-link>
                                <b-button type="submit" :disabled="!(Object.keys(objectError).length === 0)" variant="primary" size="lg">{{
                                    $t('account.sign_in') }}
                                </b-button>
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
    import debounce from 'debounce'
    import AresBox from "../../components/company/AresBox";

    export default {
        layout: 'userpage',
        components: {
            AresBox,
            LogoWhite,
        },
        data() {
            return {
                new_user: {},
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
                    reg_number: {
                        name: 'reg_number',
                        rules: [],
                    },
                    phone: {
                        name: 'phone',
                        rules: ['required'],
                    },
                    username: {
                        name: 'username',
                        rules: ['required'],
                    },
                    full_name: {
                        name: 'full_name',
                        rules: ['required'],
                    },
                },
                aresData: null,
                loadingAres: false,
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
                    full_name: this.new_user.full_name.trim(),
                    email: this.new_user.email.trim(),
                    password1: this.new_user.password1,
                    password2: this.new_user.password2,
                    phone: this.new_user.phone.trim(),
                    reg_number: this.new_user?.reg_number?.trim(),
                    username: this.new_user.username,
                };
                await this.$axios.post('accounts/registration/consultant/', data).then(
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
            }),
            debounceRegNumberInput:
                debounce(async function (e) {
                    //console.log({e}, this.new_user.reg_number)
                    if(!this.new_user?.reg_number?.trim()) return;
                    this.loadingAres = true;
                    try {
                        const response = await this.$axios.get('ares/company/', {
                            params: {
                                reg_number: this.new_user.reg_number.trim(),
                            }
                        });
                        this.aresData = response.data;
                        this.loadingAres = false;
                        //console.log(this.new_user?.full_name?.length, this.new_user.full_name, response.data.name)
                        if (!this.new_user?.full_name?.length) this.new_user.full_name = response.data.name
                        this.validate('reg_number')
                    } catch (e) {
                        console.log({e})
                        this.loadingAres = false;
                    }
                }, 500),
        },
        watch: {
            new_user: {
                handler: async function (newVal, oldVal) {
                    //console.log({newVal, oldVal}, oldVal.reg_number === newVal.reg_number)
                },
                deep: true
            },
        },
    }
</script>

<style lang="scss">
    .modal-content {
        overflow: hidden;
    }
</style>
