<template>
	<div>
		<PageTitleColor :heading="heading + ' ' + company.name + ' (' + enumType[company.role] + ')'"
		                :icon=icon
		                :model="company"
		                v-if="heading"></PageTitleColor>
		
		<div class="custom-container card text-left">
			<div class="detail-wrap">
				<div class="info-sec">
					<b-row class="mb-3">
							<b-col sm="3" class="d-flex align-items-center justify-content-center">
								<div v-if="company.image" class="image-sec" :style="'background-image: url(' +  company.image + ')'"></div>
								<div v-else class="image-sec">
									<i class="pe-7s-user icon-gradient"></i>
								</div>
							</b-col>
						<b-col sm="6" class="pt-4">
							<div class="detail-info">
								<span class="icon-wrap"><font-awesome-icon icon="home" /></span>
								<span class="info-text"> {{ company.name }}</span>
							</div>
							<div class="detail-info">
								<span class="icon-wrap"><font-awesome-icon icon="map-marker-alt" /></span>
								<span class="info-text"> {{ company.address }}</span>
							</div>
							<div v-if="company.email" class="detail-info">
								<span class="icon-wrap"><font-awesome-icon icon="envelope" /></span>
								<span class="info-text"> {{ company.email }}</span>
							</div>
							<div v-if="company.phone" class="detail-info">
								<span class="icon-wrap"><font-awesome-icon icon="phone-alt" /></span>
								<span class="info-text"> {{ company.phone }}</span>
							</div>
						</b-col>
						<b-col sm="3" class="pt-4">
							<div v-if="company.role" class="detail-info">
								<span class="info-title">Typ:</span>
								<span class="info-text"> {{ enumType[company.role] }}</span>
							</div>
							<div v-if="company.reg_number" class="detail-info">
								<span class="info-title">{{ $t('form.ico')}}:</span>
								<span class="info-text"> {{ company.reg_number }}</span>
							</div>
							<div v-if="company.vat_number" class="detail-info">
								<span class="info-title">{{ $t('form.dic')}}:</span>
								<span class="info-text"> {{ company.vat_number }}</span>
							</div>
						</b-col>
						<b-col  sm="6"
										v-if="company.tags && (company.tags).length > 0">
							<h3>{{ $t('form.tags') }}</h3>
							<nuxt-link :to="getTagSearchLink(value.name)"
												 v-for="(value, index) in company.tags"
							        class="mb-2 mr-2 btn btn-primary"
											:key="value.name">{{ value.name }}<span class="badge badge-info badge-dot badge-dot-lg"> </span></nuxt-link>
							
						</b-col>
						<b-col sm="6" v-if="company.categories && (company.categories).length">
							<h3>{{ $t('form.categories') }}</h3>
							<nuxt-link :to="getTagSearchLink(value.name)"
											v-for="(value, index) in company.categories"
							        class="mb-2 mr-2 btn btn-primary"
											:key="value.name">{{ value.name }}<span class="badge badge-info badge-dot badge-dot-lg"> </span></nuxt-link>
							
						</b-col>
						<b-col sm="12" class="mt-4 detail-description">
								<p>{{ company.description }}</p>
						</b-col>
					</b-row>
					
					<MapDetailComponent v-if="company.gps_lat"
															:company="company"></MapDetailComponent>
					
					<b-row v-if="company.testimonials && (company.testimonials).length > 0">
						<b-col sm="12" class="mb-3 mt-3">
							<h2>{{ $t('testimonial.title.title') }}</h2>
						</b-col>
						<b-col sm="6"
	                  v-for="(value, index) in company.testimonials"
	                  :key="index">
	            <div  class="main-card mb-3 card">
	              <div class="card-header bg-blue-icon"><i class="header-icon lnr-user"> </i>{{ value.owner_name }}
	                <div class="btn-actions-pane-right actions-icon-btn">
									<rate class="rate"
									      :length="5"
									      v-model="value.rating"
												:readonly="true"/>
	                </div>
	              </div>
	              <div class="card-body"><p>With supporting text below as a natural lead-in to additional content.</p>
	                <p class="mb-0">Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled.</p></div>
	              <div class="d-block text-right card-footer">
<!--	                <button class="mr-2 btn btn-link btn-sm">Cancel</button>-->
<!--	                <button class="btn btn-success btn-lg">Save</button>-->
	              </div>
	            </div>
						</b-col>
					</b-row>
				</div>
			</div>
			
		</div>
	</div>
</template>

<script>
	import { mapState, mapGetters } from 'vuex'
	import PageTitleColor from "~/components/partials/PageTitleColor";
	import MapDetailComponent from "~/components/company/MapDetailComponent";
	import {library} from '@fortawesome/fontawesome-svg-core'
	import { faMapMarkerAlt, faPhoneAlt, faEnvelope, faUser, faHome } from '@fortawesome/free-solid-svg-icons'
	library.add(faMapMarkerAlt, faPhoneAlt, faEnvelope, faUser, faHome);
	
	export default {
	  name: 'company-detail',
		async fetch ({ store, params, redirect }) {
	    if(params.id && params.type){
	    	store.commit('companies/clearCompanies');
	      await store.dispatch('companies/getCompanyDetail', {id: params.id, companyType: params.type});
	    }else{
	      redirect('/');
	    }
		},
		components: {
			PageTitleColor,
			MapDetailComponent
		},
		data: () => ({
	    heading: $nuxt.$t('menu.profile'),
			icon: 'pe-7s-user',
		}),
		computed: {
	    ...mapState({
		    company: state => state.companies.company,
		    enumType: state => state.companies.enumType
	    }),
			...mapGetters({
				isSupplier: 'companies/isSupplier',
				isConsultant: 'companies/isConsultant',
			}),
		},
		methods: {
			getTagSearchLink(value) {
				if(this.isSupplier){
					return {name: 'subjekty-seznam-dodavatelu___cs', query: { search: value}}
				}else if(this.isConsultant) {
					return {name: 'subjekty-seznam-konzultantu___cs', query: { search: value}}
				}
	    	return '#'
			}
		}
	}
</script>