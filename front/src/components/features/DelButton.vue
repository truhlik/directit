<template>
	<div>
		<button type="button"
		        class="btn-shadow d-inline-flex align-items-center btn btn-danger"
		        v-b-modal.deleteModal>
			{{ $t('form.button.delete') }}
		</button>
		<b-modal  ref="deleteModal"
		          id="deleteModal"
		          hide-footer
							centered>
			<template v-slot:modal-title>
				<h4 class="text-center">Smazat <strong>{{ model.name }}</strong> ?</h4>
    </template>
			
        <div class="w-100 d-flex justify-content-center">
          <b-button
            variant="danger"
            size="lg"
            @click="deleteObject()"
          >
            Smazat
          </b-button>
          <b-button
	          class="ml-5"
            variant="success"
            size="lg"
            @click="closeModal"
          >
            Ne, ponechat
          </b-button>
        </div>
		</b-modal>
	</div>
</template>

<script>
	export default {
		name: 'del-button',
		props: {
		  model: Object,
			modelName: String,
			routerBack: {
		  	type: Boolean,
				default: true
			}
		},
		methods:{
		  showModal() {
		    this.$refs['deleteModal'].show();
		  },
			closeModal() {
		    this.$refs['deleteModal'].hide();
			},
			async deleteObject(){
		    const url = `${this.modelName}/${this.model.id}/`;
		    this.$axios.$delete(url).then(
		      response => {
		        this.$toast.success(this.$t('form.actions.deleted'));
		        if(this.routerBack){
		        	this.$router.back();
						}else{
		        	console.log($nuxt.$route.name)
		        	this.$router.push($nuxt.$route.path)
						}
		      }
		    );
			}
		}
	}
</script>