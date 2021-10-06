<template>
    <div>
        <div  class="assistant-info"
              v-if="infoText && infoText.length">
            <span class="pe-7s-info text-primary icon"></span>
            <span>{{ infoText }}</span>
        </div>
        <div class="assistant-con">
            <form @submit.prevent="sendAssistant">
                <b-row>
                    <b-col sm="12" v-if="(assistantType === 'consierge')">
                        <b-form-group label-for="id_assistant_type"
                                      :label="$t('form.assistant_type')">
                            <b-form-select  id="id_assistant_type"
                                            v-model="assistant_type"
                                            :options="assistantTypes">

                            </b-form-select>
                        </b-form-group>
                    </b-col>
                    <b-col sm="12">
                        <b-form-group id="id-group-name"
                                      label-class="required"
                                      :label="$t('form.your_first_name')"
                                      label-for="id-name">
                            <b-form-input id="id-name"
                                          v-model="name"
                                          type="text"
                                          :placeholder="$t('form.your_first_name')"
                                          required
                                          :class="{ 'error' : objectError.name }"
                                          @input="validate('name')"/>
                            <span class="text-danger" v-for="(error, index) in objectError.name" :key="index">{{ error }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="6">
                        <b-form-group id="id-group-phone"
                                      label-class="required"
                                      :label="$t('form.your_phone')"
                                      label-for="id-phone"
                                      description="Telefon musí být ve formátu +420777000112">
                            <b-form-input id="id-phone"
                                          v-model="phone"
                                          type="text"
                                          :placeholder="$t('form.your_phone')"
                                          required
                                          :class="{ 'error' : objectError.phone }"
                                          @input="validate('phone')"/>
                            <span class="text-danger" v-for="(error, index) in objectError.phone" :key="index">{{ error }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="6" v-if="(assistantType === 'assistant')" class="time-widget">
                        <b-form-group id="id-group-time"
                                      :label="$t('form.time')"
                                      label-for="id-time"
                                      description="Čas musí být ve formátu hh:mm">
                            <date-picker id="id_time"
                                         v-model="time"
                                         :config="timeOptions"
                                         required
                                         :placeholder="$t('form.time')"
                                         :class="{ 'error' : objectError.time }"
                                         @input="validate('time')"></date-picker>
                            <span class="text-danger" v-for="(error, index) in objectError.time" :key="index">{{ error }}<br></span>
                        </b-form-group>
                    </b-col>

                    <b-col sm="12">
                        <CategoriesComponent accessoriesType="categories"
                                       modelType="assistants"
                                       :title="$t('form.categories')"></CategoriesComponent>
                    </b-col>

                    <b-col>
                        <b-form-group id="id-group-note"
                                      :label="$t('form.note')"
                                      label-for="id-note">
                            <b-form-textarea id="id-note"
                                             v-model="note"
                                             type="text"
                                             :placeholder="$t('form.note')"
                            />
                        </b-form-group>
                    </b-col>
                    <b-col sm="12" class="d-flex justify-content-center">
                        <b-button class="mr-2 mb-2 btn-hover-shine btn-transition custom-md"
                                  variant="primary"
                                  size="lg"
                                  type="submit">
                            {{ $t('form.button.send') }}
                        </b-button>

                    </b-col>
                </b-row>
            </form>
        </div>
        <b-modal  ref="assistantModal"
                  id="assistant-modal"
                  hide-header
                  hide-footer
                  centered
                  body-class="text-center"
                  @hide="modalHided">
            <i class="pe-7s-check check-icon"></i>
            <b-col sm="12"><span class="message">Děkujeme,<br> ozveme se vám.</span></b-col>
            <b-row class="mb-5">
                <b-col sm="12"><strong>{{ $t('form.first_name') }}: </strong>{{ assistant.name }}</b-col>
                <b-col sm="12"><strong>{{ $t('form.phone') }}: </strong>{{ assistant.phone }}</b-col>
                <b-col sm="12" v-if="assistant.time"><strong>{{ $t('form.time') }}: </strong>{{ assistant.time }}</b-col>
                <b-col sm="12" v-if="assistant.note"><strong>{{ $t('form.note') }}</strong><br>{{ assistant.note }}</b-col>
            </b-row>
            <b-row>
                <b-col>
                    <b-button class="mr-2 mb-2 btn-transition"
                              variant="outline-danger"
                              size="lg"
                              @click="deleteAssistant(assistant.id)">
                        Spletl jsem se. {{ $t('form.button.takeback') }}
                    </b-button>
                </b-col>
                <b-col>
                    <b-button class="mr-2 mb-2 btn-hover-shine btn-transition"
                              variant="primary"
                              size="lg"
                              @click="hideModal">
                        Vše v pořádku. {{ $t('form.button.close') }}
                    </b-button>
                </b-col>
            </b-row>
        </b-modal>
    </div>
</template>

<script>

    import {mapActions, mapMutations, mapState} from 'vuex'
    import CategoriesComponent from "~/components/features/CategoriesComponent";
    import { ASSISTANT_TYPE } from "~/helpers/constants";

    export default {
        name: 'AssistantForm',
        components: {
            CategoriesComponent
        },
        props: {
            closeParent: Function,
            infoText: {
                type: String,
                default: function() {
                    return $nuxt.$t('services.it_assistant.info_text');
                }
            },
            assistantType: {
                type: String,
                default: 'assistant'
            }
        },
        data(){
            return {
                timeOptions: {
                    format: 'HH:mm',
                    locale: 'cs',
                    showClose: true,
                    toolbarPlacement: 'bottom',
                    icons: {
                        time: 'pe-7s-alarm big-icon',
                        date: 'pe-7s-date big-icon',
                        up: 'pe-7s-angle-up big-icon',
                        down: 'pe-7s-angle-down big-icon',
                        previous: 'pe-7s-angle-left big-icon',
                        next: 'pe-7s-angle-right big-icon',
                        close: 'pe-7s-close big-icon'
                    }
                },
                assistantTypes: ASSISTANT_TYPE,
                objectValidator: {
                    name: {
                        name: 'name',
                        rules: ['required']
                    },
                    phone: {
                        name: 'phone',
                        rules: ['required']
                    },
                    time: {
                        name: 'time',
                        rules: ['required'],
                    }
                }
            }
        },
        computed: {
            ...mapState({
                assistant: state => state.user.assistant,
                objectError: state => state.errors.objectError,
                categories: state => state.categories.accessoriesCategories
            }),
            name: {
                set(name) {
                    this.addToAssistant({name});
                },
                get() {
                    return this.assistant.name;
                }
            },
            phone: {
                set(phone) {
                    this.addToAssistant({phone});
                },
                get() {
                    return this.assistant.phone;
                }
            },
            time: {
                set(time) {
                    this.addToAssistant({time});
                },
                get() {
                    return this.assistant.time;
                }
            },
            note: {
                set(note) {
                    this.addToAssistant({note});
                },
                get() {
                    return this.assistant.note || '';
                }
            },
            assistant_type: {
                set(assistant_type) {
                    this.addToAssistant({assistant_type});
                },
                get() {
                    return this.assistant.assistant_type || 'OTHER';
                }
            },
        },
        methods: {
            ...mapMutations('user',{
                addToAssistant: 'addToAssistant',
                setAssistant: 'setAssistant',
                clearAssistant: 'clearAssistant'
            }),
            ...mapMutations('categories',{
                clearAccessoriesCategories: 'clearAccessoriesCategories',
            }),
            ...mapActions('errors', {
                inputValidate: 'validate'
            }),
            ...mapActions('categories', {
                getCategoriesId: 'getCategoriesId'
            }),
            ...mapActions('user', {
                getMyAssistant: 'getMyAssistant',
            }),
            async sendAssistant(){
                const categories = await this.getCategoriesId();
                if(categories.length){
                    this.addToAssistant({categories});
                }

                let data = {...this.assistant};
                //data = this.checkForAssistant(data);

                console.log('sendAssistant', data);
                await this.$axios.$post(this.getUrl(), data).then(
                    response => {
                        this.setAssistant(response);
                        this.$refs['assistantModal'].show();
                        this.getMyAssistant();
                    },
                    error => {
                        this.$toast.error(this.$t('callback.messages.error'));
                    }
                );
            },
            deleteAssistant(){
                let url = this.getUrl();
                url = `${url}${this.assistant.id}/`;

                this.$axios.$delete(url).then(
                    response => {
                        this.$toast.success(this.$t('form.actions.deleted'));
                        this.clearAssistant();
                        this.$refs['assistantModal'].hide();
                        this.getMyAssistant();
                    }
                )
            },
            hideModal() {
                this.$refs['assistantModal'].hide();
            },
            modalHided() {
                this.clearAssistant();
                this.clearAccessoriesCategories();
                this.$emit("closeParent");
            },
            getUrl(){
                let url = 'assistant/';
                if(this.assistantType !== 'assistant'){
                    url = `${this.assistantType}/`;
                }
                return url;
            },
            checkForAssistant(data){
                delete data.assistant_type;
                return data;
            },
            checkForConsierge(data){
                delete data.time;
                return data;
            },
            validate(input) {
                const data = {
                    name: input,
                    objectData: this.assistant,
                    objectValidator: this.objectValidator
                };
                this.inputValidate(data);
            }
        }
    }
</script>
