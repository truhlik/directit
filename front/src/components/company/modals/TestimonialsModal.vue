<template>
	<div>
		<b-modal  ref="testimonialModal"
		          id="testimonial-modal"
							hide-footer
							centered
							@hide="hideModal">
	    <template v-slot:modal-title>
	      Hodnocení: {{ company.name }}
	    </template>
			<div class="testimonials-modal">
				<div class="testimonial-wrap"
						v-for="(value, index) in company.testimonials"
						:key="index">
					<div class="top-wrap">
						<span class="name">
							{{ value.owner_name }}
						</span>
						<rate class="rate"
						      :length="5"
						      v-model="value.rating"
									:disabled="true"/>
					</div>
					<div class="text">
						<p>{{ value.text }}</p>
					</div>
				</div>
			</div>
		</b-modal>
	</div>
</template>
<script>
	export default {
		name: 'testimonials-modal',
		props: ['company'],
		methods: {
		  showModal () {
		    this.$refs['testimonialModal'].show();
		  },
			hideModal() {
		    this.$refs['testimonialModal'].hide();
			},
		}
	}
</script>