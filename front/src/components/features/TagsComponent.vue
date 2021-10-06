<template>
	<div class="accessories-wrap">
		<span class="title-tags" v-bind:class="{ required: required }">{{ title }}</span>
		
		<span class="mb-2 mr-2 btn btn-info"
						v-if="propTags.length && showTagsFromProp"
						v-for="(value, index) in propTags"
						:key="index">
			{{ value.name }}<span class="badge badge-pill badge-light badge-delete"
														@click="deleteFromTags(value)">
				✕
			</span>
		</span>
		
		<span class="mb-2 mr-2 btn btn-info"
						v-if="accessoriesTags.length"
						v-for="(value, index) in accessoriesTags"
						:key="index">
			{{ value.name }}<span class="badge badge-pill badge-light badge-delete"
														@click="deleteFromTags(value)">
				✕
			</span>
		</span>
		
		<b-button class="mb-2 mr-2 btn-icon btn-icon-only btn-shadow btn-dashed"
		          variant="outline-primary"
							@click="showModal">
			<i class="pe-7s-plus btn-icon-wrapper"> </i>
		</b-button>
		
		
		<b-modal  ref="AccessoriesModal"
		          id="accessories-modal"
		          :title="$t('form.tags')"
							hide-footer>
			<div class="accessories-search-wrap">
				<b-form-group id="id-accessories-group">
					<b-form-input id="id-tag-input"
												class="tag-input"
												type="text"
					              v-model="accessoriesInput"
					              @input="loadTags"
												:placeholder="$t('form.search_in_input')"></b-form-input>
				</b-form-group>
			</div>
			<div class="accessories-tags-wrap">
				<button class="mb-2 mr-2 btn btn-info tag"
						     v-for="(value, index) in tags"
						     :key="value.name"
								@click="addToTags(value)">
					{{ value.name }}
					<span class="badge badge-info badge-dot badge-dot-lg"> </span>
				</button>
			</div>
			
		</b-modal>
		
	</div>
</template>

<script>
	
	import { mapState, mapActions, mapMutations } from 'vuex'
	
	export default {
		name: 'company-accessories',
		mounted(){
		  this.clearAccessoriesTags();
		},
		props: ['accessoriesType', 'modelWithTags','propTags' ,'modelType', 'title', 'senToApi', 'required'],
		data: () => ({
			accessoriesInput: '',
			showTagsFromProp: true
		}),
		computed: {
		  ...mapState({
			  tags: state => state.tags.loadedTags,
			  accessoriesTags: state => state.tags.accessoriesTags
		  })
		},
		methods: {
		  ...mapActions('tags', {
			  addTagToTags: 'addTagToTags',
			  deleteTagFromTags: 'deleteTagFromTags',
		    getTags: 'getTags'
		  }),
			...mapMutations('tags', {
			  clearAccessoriesTags: 'clearAccessoriesTags',
				addAccessoriesTags: 'addAccessoriesTags',
				deleteTagFromAccessories: 'deleteTagFromAccessories',
				deleteFromLoadedTags: 'deleteFromLoadedTags'
			}),
		  showModal(){
		    const data = {
		      accessoriesType: this.accessoriesType
		    };
		    
		    this.getTags(data);
		    this.$refs['AccessoriesModal'].show();
		  },
			loadTags(input){
			  const data = {
			    q: input,
				  accessoriesType: this.accessoriesType
			  };
			  this.getTags(data);
			},
			setData(id){
		    return {
		      idModel: this.modelWithTags.id,
			    modelType: this.modelType,
			    accessoriesType: this.accessoriesType,
			    dataSend: {
		        id: id
			    }
		    };
			},
			addToTags(tag){
		    if(this.senToApi){
		      const data = this.setData(tag.id);
		      this.addTagToTags(data);
					this.showTagsFromProp = false;
		    }else{
		      this.addAccessoriesTags(tag);
		      this.$toast.success('Tag byl přidán');
		    }
		    this.deleteFromLoadedTags(tag);
			},
			async deleteFromTags(tag){
		    if(this.senToApi){
			    const data = this.setData(tag.id);
			    await this.deleteTagFromTags(data);
					this.showTagsFromProp = false;
		    }else{
		      this.deleteTagFromAccessories(tag);
			    this.$toast.success('Tag byl odebrán');
		    }
			}
		}
	}
</script>