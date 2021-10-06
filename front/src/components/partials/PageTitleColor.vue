<template>
	<div class="app-inner-layout__header-boxed p-0">
		<div class="app-inner-layout__header page-title-icon-rounded text-white bg-blue-icon mb-4 colored-titlepage">
			<div class="app-page-title">
				<div class="page-title-wrapper">
					<div class="page-title-heading">
						<div class="page-title-icon"><i class="pe-7s-user icon-gradient bg-blue-icon"></i></div>
						<div>
							{{ heading }}
							<div v-if="subheading" class="page-title-subheading">{{ subheading }}</div>
						</div>
					</div>
					<div class="page-title-actions">
						
						<nuxt-link class="mr-3 btn btn-primary btn-transition"
						          :to="localePath({name:'subjekt-id-upravit', params: { id: model.id } })"
											v-if="(model.owners && model.owners[0] === user.id)">
							<font-awesome-icon icon="pen" /> {{ $t('form.button.update') }}
						</nuxt-link>
						
						<b-button type="button"
						          class="mr-3"
						          variant="primary"
											@click="showOrderModal">
							<font-awesome-icon icon="user" /> {{ $t('form.button.request')}}
						</b-button>
						<b-button type="button"
						          class="mr-3"
						          variant="primary"
											@click="showTestimonialForm">
							<font-awesome-icon icon="star" /> Přidat hodnocení
						</b-button>
						<TestimonialsFormModal ref="childTestimonialFormModal"></TestimonialsFormModal>
					</div>
				</div>
			</div>
		
		<OrderModal ref="childOrderModal"
								:company="model"></OrderModal>
		</div>
	</div>
</template>

<script>
	import { mapState } from 'vuex';
  import TestimonialsFormModal from "~/components/company/modals/TestimonialsFormModal";
  import OrderModal from "~/components/orders/OrderModal";
	import {library} from '@fortawesome/fontawesome-svg-core'
	import { faStar, faPen, faUser } from '@fortawesome/free-solid-svg-icons'
	library.add(faStar, faPen, faUser);
	
	export default {
		name: 'page-title-colored',
		props: {
		  heading: String,
			subheading: String,
			model: Object
		},
		components: {
		  TestimonialsFormModal,
			OrderModal
		},
		computed: {
		  ...mapState({
			  user: state => state.user.user
		  })
		},
		methods : {
		  showTestimonialForm() {
		    this.$refs['childTestimonialFormModal'].showModal(this.model);
		  },
			showOrderModal() {
				this.$refs.childOrderModal.showModal();
			}
		}
	}
</script>