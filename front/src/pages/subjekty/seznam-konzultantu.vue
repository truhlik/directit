<template>
	<div>
		<page-title :heading=heading
								:subheading=subheading
								:icon=icon
								v-if="heading"
								:orderButton="true"
								type="CONSULTANT"/>
		<SearcherComponent
						companyType="consultants"
						:searchMapMarkers="false"
		/>
		<!--		<MapComponent companyType="consultants"></MapComponent>-->
		<BoxComponent companyType="consultants"/>
	</div>
</template>

<script>
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
			heading: $nuxt.$t('menu.list_consultants'),
			subheading: $nuxt.$t('help_text.consultants_list'),
			icon: 'pe-7s-search icon-gradient bg-blue-icon',
			companyType: 'consultants',
		}),
	}
</script>