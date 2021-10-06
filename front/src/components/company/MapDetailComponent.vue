<template>
	<div>
		<div id="map" class="companies_map" style="height:300px">
      <b-spinner class="map-spinner" variant="primary" label="Spinning"></b-spinner>
    </div>
	</div>
</template>

<script>
	export default {
	  name: 'map-detail-component',
		props: ['company'],
		mounted() {
	    setTimeout(() => {
        Loader.load(null, null, () => {
          this.addToMap();
        });
      }, 1000)
		},
		methods: {
			addToMap(){
	        let companyCoord = SMap.Coords.fromWGS84(this.company.gps_lng, this.company.gps_lat);
		      let map = new SMap(JAK.gel("map"), companyCoord, 15);
		      let layer = new SMap.Layer.Marker();

		      map.addDefaultLayer(SMap.DEF_BASE).enable();
					map.addLayer(layer);


					const compass = new SMap.Control.Compass({});
					map.addControl(compass, { left: "10px", top: "10px"});

					const zoom = new SMap.Control.Zoom();
					map.addControl(zoom, {right: "10px", top: "10px"});
					layer.enable();

					let options = {};
					let companyMarker = new SMap.Marker(companyCoord, this.company.name, options);
					layer.addMarker(companyMarker);

					let card = new SMap.Card();
					card.getHeader().innerHTML = this.company.name;
					card.getBody().innerHTML = this.company.address;
					companyMarker.decorate(SMap.Marker.Feature.Card, card);

			},
		}
	}
</script>
