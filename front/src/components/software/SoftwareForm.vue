<template>
	<div class="custom-container card">
		<div class="form-con mt-5">
			<form @submit.prevent="softwareCreateUpdate">
				<b-row>
					<b-col sm="6">
						<b-form-group label-for="id_name"
						              :label="$t('form.name')"
													label-class="required">
							<b-form-input id="id_name"
								            :class="{ 'error' : objectError.name }"
														:required="true"
							              v-model="name"
							              type="text"
							              :placeholder="$t('form.name')"
														@input="validate('name')">
							</b-form-input>
							<span class="text-danger" v-for="(error, index) in objectError.name" :key="index">{{ error }}<br></span>
						</b-form-group>
					
					</b-col>
					<b-col sm="6">
						<b-form-group label-for="id_licence_till"
						              :label="$t('form.licence_till')">
							<date-picker  id="id_licence_till"
							              v-model="licence_till"
														:config="tillOptions"
														:placeholder="$t('form.licence_till')"></date-picker>
						</b-form-group>
					
					</b-col>
					<b-col sm="4">
						<b-form-group label-for="id_licence_count"
						              :label="$t('form.licence_count')">
							<b-form-input id="id_licence_count"
														:required="true"
							              v-model="licence_count"
							              type="number">
							</b-form-input>
						</b-form-group>
					
					</b-col>
					<b-col sm="4">
						<b-form-group label-for="id_licence_unit"
						              :label="$t('form.licence_unit')">
							<b-form-select  id="id_licence_unit"
															v-model="licence_unit"
															:options="licence_metric">
							
							</b-form-select>
						</b-form-group>
					</b-col>
					<b-col sm="4" class="mb-3">
						<b-form-group label-for="id_licence_type"
						              :label="$t('form.licence_type')">
							<b-form-select  id="id_licence_type"
															v-model="licence_type"
															:options="licence_types">
							
							</b-form-select>
						</b-form-group>
					</b-col>
					<b-col sm="6">
						<b-form-group label-for="id_service_contact"
						              :label="$t('form.service_contact')">
							<b-form-input id="id_service_contact"
								            :class="{ 'error' : objectError.service_contact }"
							              v-model="service_contact"
							              type="text"
							              :placeholder="$t('form.service_contact')"
														@input="validate('name')">
							</b-form-input>
							<span class="text-danger" v-for="(error, index) in objectError.service_contact" :key="index">{{ error }}<br></span>
						</b-form-group>
					</b-col>
					<b-col sm="6"></b-col>
					<b-col sm="3">
						<b-form-group label-for="id_find_alternative"
						              :label="$t('form.find_alternative')">
							<b-form-checkbox  id="id_find_alternative"
																v-model="find_alternative"
																switch
																size="lg"></b-form-checkbox>
						</b-form-group>
					</b-col>
					<b-col sm="3">
						<b-form-group label-for="id_watch_expiration"
						              :label="$t('form.watch_expiration')">
							<b-form-checkbox  id="id_watch_expiration"
																v-model="watch_expiration"
																switch
																size="lg"></b-form-checkbox>
						</b-form-group>
					</b-col>
					<b-col sm="3">
						<b-form-group label-for="id_need_extension"
						              :label="$t('form.need_extension')">
							<b-form-checkbox  id="id_need_extension"
																v-model="need_extension"
																switch
																size="lg"></b-form-checkbox>
						</b-form-group>
					</b-col>
					<b-col sm="3">
						<b-form-group label-for="id_need_customization"
						              :label="$t('form.need_customization')">
							<b-form-checkbox  id="id_need_customization"
																v-model="need_customization"
																switch
																size="lg"></b-form-checkbox>
						</b-form-group>
					</b-col>
					<b-col sm="6" class="mb-3">
						<b-form-group label-for="id_need_upgrade"
						              :label="$t('form.need_upgrade')">
							<b-form-checkbox  id="id_need_upgrade"
																v-model="need_upgrade"
																switch
																size="lg"></b-form-checkbox>
						</b-form-group>
					</b-col>
					
					<b-col v-if="update" sm="12">
					<CategoriesComponent accessoriesType="categories"
															:modelWithCategories="software"
					                    :propCategories="software.categories"
															modelType="software"
															:senToApi="true"
					                    :helpText="helpText"
															:title="$t('form.categories')"></CategoriesComponent>
					
						
					</b-col>
					<b-col v-else sm="12">
					<CategoriesComponent accessoriesType="categories"
															:title="$t('form.categories')"
															:modelWithCategories="software"
					                    :helpText="helpText"
															:required="true"></CategoriesComponent>
					
						
					</b-col>
					<b-col class="d-flex justify-content-center mt-4 mb-5">
						<b-button class="btn-transition btn-hover-shine custom-lg"
						          variant="primary"
											type="submit">{{ $t('form.button.save') }}
						</b-button>
					</b-col>
				</b-row>
			</form>
		</div>
	</div>
</template>

<script>
	import { mapActions, mapState, mapMutations } from 'vuex'
	import CategoriesComponent from "~/components/features/CategoriesComponent"
	import { LICENCE_TYPE, LICENCE_METRIC } from "~/helpers/constants";

  export default {
		name: 'software-form',
		props: ['update'],
		components: {
		  CategoriesComponent
		},
		data: () => ({
			helpText: $nuxt.$t('help_text.software_category'),
			tillOptions: {
			  format: 'YYYY-MM-DD',
				locale: 'cs',
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
			licence_types: LICENCE_TYPE,
			licence_metric: LICENCE_METRIC,
			objectValidator: {
				name: {
					name: 'name',
					rules: ['required']
				},
			},
		}),
		computed: {
		  ...mapState({
			  software: state => state.software.software,
        objectError: state => state.errors.objectError,
			  selectCategories: state => state.categories.accessoriesCategories
		  }),
			name: {
			  set(name){
			    this.addToSoftware({ name });
			  },
				get(){
			    return this.software.name || '';
				}
			},
			licence_count: {
			  set(licence_count){
			    this.addToSoftware({ licence_count });
			  },
				get(){
			    return this.software.licence_count || 0;
				}
			},
			licence_till: {
			  set(licence_till){
			    this.addToSoftware({ licence_till });
			  },
				get(){
			    return this.software.licence_till || '';
				}
			},
			service_contact: {
			  set(service_contact){
			    this.addToSoftware({ service_contact });
			  },
				get(){
			    return this.software.service_contact || '';
				}
			},
			find_alternative: {
			  set(find_alternative){
			    this.addToSoftware({ find_alternative });
			  },
				get(){
			    return this.software.find_alternative || false;
				}
			},
			licence_type: {
			  set(licence_type){
			    this.addToSoftware({ licence_type });
			  },
				get(){
			    return this.software.licence_type || '';
				}
			},
			licence_unit: {
			  set(licence_unit){
			    this.addToSoftware({ licence_unit });
			  },
				get(){
			    return this.software.licence_unit || '';
				}
			},
			watch_expiration: {
			  set(watch_expiration){
			    this.addToSoftware({ watch_expiration });
			  },
				get(){
			    return this.software.watch_expiration || false;
				}
			},
			need_extension: {
			  set(need_extension){
			    this.addToSoftware({ need_extension });
			  },
				get(){
			    return this.software.need_extension || false;
				}
			},
			need_customization: {
			  set(need_customization){
			    this.addToSoftware({ need_customization });
			  },
				get(){
			    return this.software.need_customization || false;
				}
			},
			need_upgrade: {
			  set(need_upgrade){
			    this.addToSoftware({ need_upgrade });
			  },
				get(){
			    return this.software.need_upgrade || false;
				}
			},
		},
		methods: {
      ...mapActions('errors', {
	      inputValidate: 'validate'
	    }),
		  ...mapActions('categories', {
		      getCategoriesId: 'getCategoriesId'
		  }),
			...mapActions('software', {
			  createAPISoftware: 'createSoftware',
				updateAPISoftware: 'updateSoftware'
			}),
		  ...mapMutations('software', {
		    addToSoftware: 'addToSoftware'
		  }),
	    validate(input) {
	      const data = {
	        name: input,
		      objectData: this.software,
		      objectValidator: this.objectValidator
	      };
	      this.inputValidate(data);
	    },
			async softwareCreateUpdate() {
	      let categoriesID = await this.getCategoriesId(this.selectCategories);
	      
	      if(categoriesID.length === 0) {
	        categoriesID = await this.getCategoriesId(this.software.categories);
	      }
       
	      this.addToSoftware({categories: categoriesID});
	      
	      if(this.update){
	        this.updateAPISoftware(this.software);
	      }else{
	        this.createAPISoftware(this.software);
	      }
		    
			}
		}
	}
</script>