<template>
	<div>
    <page-title :heading=heading
                :subheading="subheading"
                :icon=icon
                v-if="heading"
                :pathUrl="pathUrl"
                :pathName="$t('menu.add_software')"
                :pathIcon="pathIcon">
    </page-title>
	    <b-card class="main-card mb-4">
        <b-table :hover="true"
                 :striped="true"
                 :items="items"
                 :fields="fields"
                 :current-page="softwarePagination.page">
	        <template v-slot:cell(watch_expiration)="data">
		       {{ data.item.watch_expiration ? 'Ano' : 'Ne' }}
	        </template>
	        <template v-slot:cell(find_alternative)="data">
		       {{ data.item.find_alternative ? 'Ano' : 'Ne' }}
	        </template>
	        <template v-slot:cell(need_customization)="data">
		       {{ data.item.need_customization ? 'Ano' : 'Ne' }}
	        </template>
	        <template v-slot:cell(need_extension)="data">
		       {{ data.item.need_extension ? 'Ano' : 'Ne' }}
	        </template>
	        <template v-slot:cell(need_upgrade)="data">
		       {{ data.item.need_upgrade ? 'Ano' : 'Ne' }}
	        </template>
	        <template v-slot:cell(detail)="row">
		        <nuxt-link :to="localePath({ name: 'technologie-id-upravit', params: { id: row.item.id} })">
		        <b-button size="sm" class="mr-2"
		        variant="primary">
		          {{ $t('form.button.update')}}
		        </b-button>
			        </nuxt-link>
	        </template>
        </b-table>
      <b-row>
        <b-col md="6" class="my-1">
          <b-pagination-nav :total-rows="softwarePagination.count"
                            :value="softwarePagination.page"
                            :per-page="softwarePagination.page_size"
                            :number-of-pages="softwarePagination.num_pages"
                            :link-gen="pageGen"
                            use-router
                            class="my-0" />
        </b-col>
      </b-row>
    </b-card>
        <page-disclaimer :text="$t('disclaimer.technology_info')"></page-disclaimer>
	</div>
</template>

<script>
	import { mapState } from 'vuex'
	import PageTitle from "~/components/partials/PageTitle";
    import PageDisclaimer from "~/components/partials/PageDisclaimer";
	
	export default {
	  name: 'software-list',
		async fetch({ store, query }){
	    await store.dispatch('software/getSoftwareList', {page: query.page ? query.page : 1});
		},
		components: {
            PageDisclaimer,
			PageTitle,
		},
		data: () => ({
	    heading: $nuxt.$t('menu.software_list'),
			subheading: $nuxt.$t('subheadings.software_list'),
			icon: 'pe-7s-news-paper',
			pathUrl: '/technologie/vytvorit/',
			pathIcon: 'plus',
						fields: [
			  {
          key: 'name',
				  label: 'Název'
				},
			  {
          key: 'licence_count',
				  label: 'Počet licencí / Zařízení'
				},
			  {
          key: 'licence_till',
				  label: 'Licence do'
				},
				{
				  key: 'watch_expiration',
					label: 'Sledovat expiraci'
				},
			  {
          key: 'find_alternative',
				  label: 'Zajímá mě alternativa'
				},
			  {
          key: 'need_customization',
				  label: 'Potřeba customizace'
				},
			  {
          key: 'need_extension',
				  label: 'Potřeba rozšíření'
				},
			  {
          key: 'need_upgrade',
				  label: 'Potřeba aktualizace / nahrazení'
				},
				{
				  key: 'detail',
					label: ''
				}
			],
		}),
		computed: {
		  ...mapState({
			  softwarePagination: state => state.software.softwarePagination,
			  items: state => state.software.softwareList,
		  })
		},
		methods: {
      pageGen(pageNum) {
        return pageNum === 1 ? '?' : `?page=${pageNum}`
      }
		},
    watchQuery: ['page']
		
	}
</script>