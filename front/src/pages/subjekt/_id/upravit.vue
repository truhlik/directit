<template>
    <div class="company-update-wrap">
        <page-title :heading='company.name'
                    :subheading=subheadingCalc
                    :icon=icon
                    :model="company"
                    :profillButton="isClient"
                    v-if="company.name"
                    :pathLink="pathLink"
                    :pathName="$t('menu.ref_project_create')"
                    :pathIcon="pathIcon">
        </page-title>

        <CompanyForm :updateCompany="true"></CompanyForm>

        <div class="form-con">
        </div>
    </div>
</template>
<script>

    import {mapActions, mapState, mapGetters} from 'vuex'
    import CompanyForm from '~/components/company/CompanyForm'
    import PageTitle from "@/components/partials/PageTitle.vue";

  export default {
	  name: 'company-update',
		async fetch ({ store, params, redirect }) {
			if(params.id){
				await store.dispatch('companies/getCompanyDetail', {id: params.id});
			} else {
				redirect({name: 'subjekt-vytvorit___cs'});
			}
		},
		components: {
			CompanyForm,
			PageTitle
		},
		data: () => ({
			image: '',
			canUploadImage: false,
			subheading: $nuxt.$t('form.button.profile_edit'),
			icon: 'pe-7s-id icon-gradient bg-blue-icon',
            pathLink: 'subjekt-referencni-projekt',
            pathIcon: 'list',
		}),
		computed: {
			...mapState({
				company: state => state.companies.company
			}),
			...mapGetters({
					isClient: 'user/isClient',
					isSupplier: 'user/isSupplier',
					isConsultant: 'user/isConsultant',
			}),
			subheadingCalc(){
				if(this.isSupplier) return  $nuxt.$t('company.update')
				return $nuxt.$t('form.button.profile_edit')
			},
		},
	}
</script>