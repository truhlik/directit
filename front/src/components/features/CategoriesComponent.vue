<template>
    <div class="accessories-wrap">
		<span v-if="helpText && !disabled" class="title-tags">{{ title }}
			<br>
			<small>{{ helpText }}</small>
		</span>
        <span v-else class="title-tags">{{ title }}</span>


        <!--		<span class="text-danger" v-for="(error, index) in objectError.categories" :key="index">{{ error }}<br></span>-->

        <span class="mb-2 mr-2 btn btn-info"
              v-if="propCategories.length && showCategoriesFromProp"
              v-for="(value, index) in propCategories"
        >
			{{ value.name }}
			<span class="badge badge-pill badge-light badge-delete"
                  v-if="canAdd && !disabled"
                  @click="deleteFromCategories(value)">✕ </span>
		</span>

        <span class="mb-2 mr-2 btn btn-info"
              v-if="accessoriesCategories.length"
              v-for="(value, index) in accessoriesCategories"
              :key="index">
			{{ value.name }}
			<span class="badge badge-pill badge-light badge-delete"
                  v-if="canAdd &&!disabled"
                  @click="deleteFromCategories(value)">✕ </span>
		</span>

        <b-button class="mb-2 mr-2 btn-icon btn-icon-only btn-shadow btn-dashed"
                  variant="outline-primary"
                  v-if="canAdd &&!disabled"
                  @click="showModal">
            <i class="pe-7s-plus btn-icon-wrapper" v-if="!singleOnly"> </i>
            <i class="pe-7s-tools btn-icon-wrapper" v-if="singleOnly"> </i>
        </b-button>


        <b-modal ref="AccessoriesModal"
                 id="accessories-modal"
                 :title="$t('form.categories')"
                 hide-footer scrollable >
            <div class="accessories-search-wrap">
                <b-form-group id="id-accessories-group">
                    <b-form-input id="id-tag-input"
                                  class="tag-input"
                                  type="text"
                                  v-model="accessoriesInput"
                                  @input="loadCategories"
                                  :placeholder="$t('form.search_in_input')"></b-form-input>
                </b-form-group>
            </div>
            <div class="accessories-categories-wrap row p-2 pr-1">
                <button class="mb-2 mr-2 btn btn-info col category"
                        v-for="(value, index) in categories"
                        :key="index"
                        @click="addToCategories(value)">
                    {{ value.name }}
                    <span class="badge badge-info badge-dot badge-dot-lg"> </span>
                </button>
            </div>

        </b-modal>
    </div>
</template>

<script>

    import {mapState, mapActions, mapMutations} from 'vuex'

    export default {
        name: 'company-accessories',
        props: {
            accessoriesType: {
                type: String,
                default: ''
            },
            modelWithCategories: {
                type: Object,
                default: () => {
                }
            },
            propCategories: {
                type: Array,
                default: () => []
            },
            modelType: {
                type: String,
                default: ''
            },
            title: {
                type: String,
                default: ''
            },
            senToApi: {
                type: Boolean,
                default: false
            },
            required: {
                type: Boolean,
                default: false
            },
            helpText: {
                type: String,
                default: ''
            },
            canAdd: {
                type: Boolean,
                default: true
            },
            singleOnly: {
                type: Boolean,
                default: false
            },
            disabled: {
                type: Boolean,
                default: false,
            },
        },
        data: () => ({
            accessoriesInput: '',
            showCategoriesFromProp: true,
            objectValidator: {
                categories: {
                    name: 'categories',
                    rules: ['required']
                },
            },
        }),
        created(){
            /*if(this.modelWithCategories?.categories?.length)
                this.addToCategories(this.modelWithCategories.categories[0]);*/
        },
        computed: {
            ...mapState({
                categories: state => state.categories.loadedCategories,
                accessoriesCategories: state => state.categories.accessoriesCategories,
                objectError: state => state.errors.objectError
            })
        },
        methods: {
            ...mapActions('errors', {
                inputValidate: 'validate'
            }),
            ...mapActions('categories', {
                addTagToCategories: 'addTagToCategories',
                deleteTagFromCategories: 'deleteTagFromCategories',
                getCategories: 'getCategories'
            }),
            ...mapMutations('categories', {
                addAccessoriesCategories: 'addAccessoriesCategories',
                setAccessoriesCategory: 'setAccessoriesCategory',
                deleteTagFromAccessCategories: 'deleteTagFromAccessCategories',
                deleteFromLoadedCategories: 'deleteFromLoadedCategories'
            }),
            validate() {
                const data = {
                    name: this.accessoriesType,
                    objectData: this.modelWithCategories,
                    objectValidator: this.objectValidator
                };
                this.inputValidate(data);
            },
            showModal() {
                const data = {
                    accessoriesType: this.accessoriesType
                };

                this.getCategories(data);
                this.$refs['AccessoriesModal'].show();
            },
            loadCategories(input) {
                const data = {
                    q: input,
                    accessoriesType: this.accessoriesType
                };
                this.getCategories(data);
            },
            setData(id) {
                return {
                    idModel: this.modelWithCategories.id,
                    modelType: this.modelType,
                    accessoriesType: this.accessoriesType,
                    dataSend: {
                        id: id
                    }
                };
            },
            addToCategories(category) {
                if (this.senToApi) {
                    const data = this.setData(category.id);
                    this.addTagToCategories(data);
                    this.showCategoriesFromProp = false;
                } else {
                    this.singleOnly ? this.setAccessoriesCategory(category) : this.addAccessoriesCategories(category);
                }
                this.$toast.success('Kategorie byla přidána');
                if(this.singleOnly) this.$bvModal.hide('accessories-modal');
                this.deleteFromLoadedCategories(category);
            },
            async deleteFromCategories(category) {
                if (this.senToApi) {
                    const data = this.setData(category.id);
                    await this.deleteTagFromCategories(data);
                    this.showCategoriesFromProp = false;
                } else {
                    this.deleteTagFromAccessCategories(category);
                    this.$toast.success('Kategorie byla odebrána');
                }
            }
        }
    }
</script>
