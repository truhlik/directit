<template>
	<div>
		<div  class="callback-info"
					v-if="infoText">
			<span class="pe-7s-info text-primary icon"></span>
			<span>{{ infoText }}</span>
		</div>
		<div class="callback-con">
			<form @submit.prevent="sendCallback">
				<b-row>
					<b-col sm="12" v-if="(callbackType === 'consierge')">
						<b-form-group label-for="id_callback_type"
						              :label="$t('form.callback_type')">
							<b-form-select  id="id_callback_type"
															v-model="callback_type"
															:options="callbackTypes">

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
					<b-col sm="6" v-if="(callbackType === 'callback')" class="time-widget">
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
						<TagsComponent accessoriesType="tags"
						               modelType="callbacks"
						               :title="$t('form.tags')"></TagsComponent>
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
		<b-modal  ref="callbackModal"
		          id="callback-modal"
							hide-header
							hide-footer
							centered
		          body-class="text-center"
							@hide="modalHided">
			<i class="pe-7s-check check-icon"></i>
			<b-col sm="12"><span class="message">Děkujeme,<br> ozveme se vám.</span></b-col>
			<b-row class="mb-5">
				<b-col sm="12"><strong>{{ $t('form.first_name') }}: </strong>{{ callback.name }}</b-col>
				<b-col sm="12"><strong>{{ $t('form.phone') }}: </strong>{{ callback.phone }}</b-col>
				<b-col sm="12" v-if="callback.time"><strong>{{ $t('form.time') }}: </strong>{{ callback.time }}</b-col>
				<b-col sm="12" v-if="callback.note"><strong>{{ $t('form.note') }}</strong><br>{{ callback.note }}</b-col>
			</b-row>
			<b-row>
				<b-col>
					<b-button class="mr-2 mb-2 btn-transition"
					          variant="outline-danger"
					          size="lg"
										@click="deleteCallback(callback.id)">
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
  import TagsComponent from "~/components/features/TagsComponent";
  import { CALLBACK_TYPE } from "~/helpers/constants";

  export default {
	  name: 'CallbackForm',
		components: {
	    TagsComponent
		},
	  props: {
	    closeParent: Function,
		  infoText: {
	      type: String,
			  default: function() {
			    return $nuxt.$t('services.callback.info_text');
			  }
		  },
		  callbackType: {
	      type: String,
			  default: 'callback'
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
		    callbackTypes: CALLBACK_TYPE,
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
		    callback: state => state.user.callback,
	      objectError: state => state.errors.objectError,
		    tags: state => state.tags.accessoriesTags
	    }),
      name: {
        set(name) {
          this.addToCallback({name});
        },
        get() {
          return this.callback.name;
        }
      },
      phone: {
        set(phone) {
          this.addToCallback({phone});
        },
        get() {
          return this.callback.phone;
        }
      },
      time: {
        set(time) {
          this.addToCallback({time});
        },
        get() {
          return this.callback.time;
        }
      },
      note: {
        set(note) {
          this.addToCallback({note});
        },
        get() {
          return this.callback.note || '';
        }
      },
      callback_type: {
        set(callback_type) {
          this.addToCallback({callback_type});
        },
        get() {
          return this.callback.callback_type || 'OTHER';
        }
      },
		},
		methods: {
	    ...mapMutations('user',{
				addToCallback: 'addToCallback',
		    setCallback: 'setCallback',
		    clearCallback: 'clearCallback'
			}),
	    ...mapMutations('tags',{
				clearAccessoriesTags: 'clearAccessoriesTags',
			}),
      ...mapActions('errors', {
	      inputValidate: 'validate'
	    }),
      ...mapActions('tags', {
	      getTagsId: 'getTagsId'
	    }),
      ...mapActions('user', {
	      getMyCallbacks: 'getMyCallbacks',
	      getMyConsierges: 'getMyConsierges'
	    }),
			async sendCallback(){
	      const tags = await this.getTagsId();
	      if(tags.length){
	        this.addToCallback({tags: tags});
	      }

        let data = {...this.callback};
	      if( this.callbackType === 'callback'){
	        data = this.checkForCallback(data);
        }else {
	        data = this.checkForConsierge(data);
        }

	      await this.$axios.$post(this.getUrl(), data).then(
	        response => {
	          this.setCallback(response);
	          this.$refs['callbackModal'].show();
	          this.getMyCallbacks();
	          this.getMyConsierges();
	        },
		      error => {
	          this.$toast.error(this.$t('callback.messages.error'));
		      }
	      );
			},
		  deleteCallback(){
	      let url = this.getUrl();
		    url = `${url}${this.callback.id}/`;

		    this.$axios.$delete(url).then(
		      response => {
		        this.$toast.success(this.$t('form.actions.deleted'));
		        this.clearCallback();
		        this.$refs['callbackModal'].hide();
	          this.getMyCallbacks();
	          this.getMyConsierges();
		      }
		    )
		  },
			hideModal() {
	      this.$refs['callbackModal'].hide();
			},
			modalHided() {
	      this.clearCallback();
	      this.clearAccessoriesTags();
	      this.$emit("closeParent");
			},
      getUrl(){
	      let url = 'callbacks/';
	      if(this.callbackType !== 'callback'){
	        url = `${this.callbackType}/`;
        }
	      return url;
      },
      checkForCallback(data){
        delete data.callback_type;
	      return data;
      },
      checkForConsierge(data){
        delete data.time;
	      return data;
      },
	    validate(input) {
	      const data = {
	        name: input,
		      objectData: this.callback,
		      objectValidator: this.objectValidator
	      };
	      this.inputValidate(data);
	    }
		}
	}
</script>
