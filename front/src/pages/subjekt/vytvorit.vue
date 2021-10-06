<template>
	<div id="company-create-wrap">
    <page-title :heading=heading
                :icon=icon
                v-if="heading">
    </page-title>
		<CompanyForm></CompanyForm>
		<div class="form-con">
		</div>
	</div>
</template>

<script>
	
	import { mapActions, mapMutations, mapState } from 'vuex'
	import CompanyForm from '~/components/company/CompanyForm'
	import PageTitle from "~/components/partials/PageTitle.vue";
	
  export default {
    name: 'create-company',
		async fetch ({ store, params, redirect }) {
	    await store.dispatch('user/getOwnCompany');
		},
	  components: {
      CompanyForm,
		  PageTitle
	  },
	  data: () => ({
			heading: $nuxt.$t('menu.createCompany'),
			icon: 'pe-7s-add-user icon-gradient bg-blue-icon'
	  }),
	  computed: {
      ...mapState({
	      company: state => state.companies.company
      })
	  },
	  methods: {
      ...mapMutations('companies', {
	      clearCompany: 'clearCompany'
      }),
		  ...mapActions('companies', {
        createCompany: 'createCompany'
		  })
	  }
  }
</script>