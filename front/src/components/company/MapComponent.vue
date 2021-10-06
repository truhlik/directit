<template>
	<div>
		<div id="map" class="companies_map" style="height:380px">
      <b-spinner class="map-spinner" variant="primary" label="Spinning"></b-spinner>
    </div>
	</div>
</template>

<script>
	import { mapState, mapActions } from 'vuex'
	import { COMPANY_URLS } from "~/helpers/constants";

  export default {
		mounted() {
	    if(this.$route.query.search){
	      this.searchInput = this.$route.query.search;
	    }
	    setTimeout(() => {
        Loader.load(null, null, () => {
          this.addToMap();

						const data = {
							companyType: this.companyType,
							page: this.$route.query.page ? this.$route.query.page : 1
						};

						if(this.$route.query.search){
							const dataAdd = {...data, ...{ searchedString: this.$route.query.search }
							};
							this.findCompanies(dataAdd)
						}

        });
      }, 1000)

		},
		props: ['companyType'],
	  data: () => ({
		  company_urls: COMPANY_URLS,
			getCompaniesMarkers: true // turn off / on map markers
	  }),
		computed: {
	    ...mapState({
		    markers: state => state.companies.mapMarkers,
	    })
		},
		methods: {
			addToMap(){
	        const center = SMap.Coords.fromWGS84(15.2295956, 49.8858261);
		      this.map = new SMap(JAK.gel("map"), center, 7);
		      this.layer = new SMap.Layer.Marker();
		      this.map.addDefaultLayer(SMap.DEF_BASE).enable();
		      //this.map.addDefaultControls();
					this.map.addLayer(this.layer);

					const compass = new SMap.Control.Compass({});
					this.map.addControl(compass, { left: "10px", top: "10px"});

					const zoom = new SMap.Control.Zoom();
					this.map.addControl(zoom, {right: "10px", top: "10px"});
					this.layer.enable();

					let allMarkers = [];
					let url;
					for(let index in this.markers){
					  const markerCoords = SMap.Coords.fromWGS84(this.markers[index].gps_lng, this.markers[index].gps_lat);
					  let options = {};

					  let card = new SMap.Card();
					  card.getHeader().innerHTML = `<span>${this.markers[index].name}</span>`;

					  let companyMarker = new SMap.Marker(markerCoords, this.markers[index].name, options);
					  companyMarker.decorate(SMap.Marker.Feature.Card, card);

					  allMarkers.push(companyMarker);
					}
					for(let i=0; i < allMarkers.length; i++){
					  this.layer.addMarker(allMarkers[i]);
					}
			},
			...mapActions('companies', {
				getAllCompaniesMarkers: 'getAllCompaniesMarkers',
				getLimitedCompanies: 'getLimitedCompanies',
				findCompanies: 'findCompanies'
			}),
		},
		watch: {
		  markers: function (newVal, oldVal) {
		    this.addToMap();
		  }
		}
	}
</script>
