<template>
	<div>
    <page-title :heading=heading
                :subheading=subheading
                :icon=icon
                v-if="heading"
				:orderButton="true"
				type="SUPPLIER">
    </page-title>
		<SearcherComponent
						companyType="suppliers"
		></SearcherComponent>
		<MapComponent companyType="suppliers"></MapComponent>
		<BoxComponent companyType="suppliers"></BoxComponent>
	</div>
</template>

<script>
	import { mapState } from 'vuex'
	import MapComponent from "~/components/company/MapComponent";
	import BoxComponent from "~/components/company/BoxComponent";
	import SearcherComponent from "~/components/company/SearcherComponent";
	import PageTitle from "~/components/partials/PageTitle.vue";
	
	export default {
		name: 'map-component',
		components: {
		  MapComponent,
			BoxComponent,
			SearcherComponent,
			PageTitle
		},
		data: () => ({
			f2: {gradient: ["#3ac47d"]},
			f3: {gradient: ["#16aaff"]},
			heading: $nuxt.$t('menu.list_suppliers'),
			subheading: $nuxt.$t('help_text.suppliers_list'),
			icon: 'pe-7s-search bg-blue-icon icon-gradient',
			companyType: 'suppliers',
		}),
    watchQuery(newQuery, oldQuery) {
			this.search = newQuery?.search;
    }
	}
</script>