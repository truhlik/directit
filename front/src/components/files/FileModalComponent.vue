<template>
  <div>
<b-modal  class="text-left"
							ref="file-modal"
							hide-footer>
			<template v-slot:modal-title>
				{{ file.file | get-file-name }}
			</template>
	<b-row class="form-con">
					<b-col sm="12">
						<b-form-group id="id-group-name"
						              :label="$t('form.title')"
						              label-for="id-title">
							<b-form-input id="id-title"
							              v-model="title"
							              type="text"
							              :placeholder="$t('form.title')">

							</b-form-input>
						</b-form-group>
					</b-col>
					<b-col sm="12" class="mb-3">
						<b-form-group
										class="eval-text-group"
										:label="$t('form.description')"
										label-for="id-description">
							<b-form-textarea
											class=""
											id="id-description"
							        v-model="description"
							        :placeholder="$t('form.description')">

							</b-form-textarea>
						</b-form-group>
					</b-col>
				<b-col sm="6" class="text-center">
					<b-button class="mr-2 mb-2 btn-transition custom-md"
					          variant="outline-danger"
					          size="lg"
										@click="closeModal">
						{{ $t('form.button.close') }}
					</b-button>
				</b-col>
				<b-col sm="6" class="text-center">
					<b-button class="mr-2 mb-2 btn-hover-shine btn-transition custom-md"
					          variant="primary"
					          size="lg"
										@click="handlerUpdateFile">
						{{ $t('form.button.save') }}
					</b-button>
				</b-col>
	</b-row>
</b-modal>
  </div>
</template>

<script>
	import { mapActions, mapMutations, mapState } from 'vuex'
  import DelButton from '~/components/features/DelButton';

  export default {
    name: 'file-modal',
		components: {
			'DelButton': DelButton
		},
		props: {
    	updateFunction: {
    		type: Function
			}
		},
		computed: {
    	...mapState({
				file: state => state.files.file
			}),
      title: {
        set(title) {
          this.addToFile({title});
        },
        get() {
          return this.file.title;
        }
      },
      description: {
        set(description) {
          this.addToFile({description});
        },
        get() {
          return this.file.description;
        }
      },

		},
		methods: {
    	...mapActions({
				updateFile: 'files/updateFile'
			}),
	    ...mapMutations({
				 addToFile: 'files/addToFile'
			}),
    	openModal() {
	      this.$refs['file-modal'].show();
	    },
	    closeModal: function () {
	      this.$refs['file-modal'].hide();
	    },
			handlerUpdateFile(){
    		this.$emit('updateFunction', this.file)
			}
		}
  }
</script>