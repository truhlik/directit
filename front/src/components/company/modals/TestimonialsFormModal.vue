<template>
	<div>
		<b-modal  ref="testimonialFormModal"
		          id="testimonial-form-modal"
							hide-footer
							centered
							@hide="modalHided">
		    <template v-slot:modal-title>
		      {{ $t('testimonial.title.evaluate')}} {{ model.name }}
		    </template>
			<div class="testimonials-form-modal">
				<b-row>
					<b-col sm="12"
					       class="text-center"
					       v-if="sent">
						<i class="pe-7s-check check-icon"></i>
						<div>
							<span class="info">Vaše hodnocení bylo uloženo. Nyní máte možnost jej smazat nebo upravit.</span>
						</div>
					</b-col>
					<b-col sm="12" class="mb-3 mt-3">
						<rate class="star-rate" :length="5" v-model="rating"/>
					</b-col>
					<b-col sm="12" class="mb-3">
						<b-form-group class="eval-text-group">
							<b-form-textarea id="id-eval-text"
							                 v-model="evaluateText"
							                 :placeholder="$t('testimonial.title.eval_text')">
							
							</b-form-textarea>
						</b-form-group>
					</b-col>
				</b-row>
				
				<b-row>
					<b-col sm="12" v-if="!sent" class="d-flex justify-content-center pt-4">
						<b-button variant="primary"
						          class="custom-md"
						          @click="sendTestimonial">Odeslat
						</b-button>
					</b-col>
					<b-col sm="12" v-else class="d-flex justify-content-between pt-4">
				<b-button class="mr-2 mb-2 btn-icon "
				          :key="sent"
				          variant="outline-danger"
									@click="deleteTestimonial">
                      <font-awesome-icon icon="trash-alt" />
                      Smazat hodnocení
                    </b-button>
				<b-button class="mr-2 mb-2 btn-icon btn-shadow custom-md"
				          :key="sent"
				          variant="primary"
									@click="updateTestimonial">
                      <font-awesome-icon icon="check" />
                       Uložit upravené hodnocení
                    </b-button>
					</b-col>
				</b-row>
			</div>
		</b-modal>
	</div>
</template>
<script>
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faCheck, faTrashAlt} from '@fortawesome/free-solid-svg-icons'

  library.add(faCheck, faTrashAlt);
	
	export default {
		name: 'testimonials-modal',
		data: () => ({
			model: {},
			testimonialId: null,
			rating: 0,
			evaluateText: '',
			sent: false
		}),
		methods: {
		  showModal (model) {
		    this.model = model;
		    this.$refs['testimonialFormModal'].show();
		  },
			hideModal() {
		    this.$refs['testimonialFormModal'].hide();
			},
			async deleteTestimonial(){
		    const url = "testimonials/" + this.testimonialId + '/';
		    await this.$axios.$delete(url).then(
		      response => {
		        this.$toast.success('Hodnocení ' + this.$t('form.actions.deleted'));
		        this.hideModal();
		      }
		    );
			},
			async updateTestimonial(){
		    const url = 'testimonials/' + this.testimonialId + '/';
		    const data = {
		      company: this.model.id,
			    rating: this.rating,
			    text: this.evaluateText
		    };
		    this.$axios.$patch(url, data).then(
		      response => {
		        this.$toast.success('Hodnocení ' + this.$t('form.actions.updated'));
		        this.hideModal();
		      }
		    )
			},
			async sendTestimonial(){
		    const data = {
		      company: this.model.id,
			    rating: this.rating,
			    text: this.evaluateText
		    };
		    await this.$axios.$post('testimonials/', data).then(
		      response => {
		        this.sent = true;
		        this.testimonialId = response.id;
		        this.$toast.success('Hodnocení ' + this.$t('messages.callback.sent'));
		      }
		    )
			},
			modalHided() {
				this.model = {};
				this.testimonialId = null;
				this.rating = 0;
				this.evaluateText = '';
				this.sent = false;
			}
		}
	}
</script>