<template>
    <div class="accessories-wrap">
        <span class="title-products" v-bind:class="{ required: required }">{{ title }}</span>

        <span class="mb-2 mr-2 btn btn-info"
              v-if="propProducts.length && showProductsFromProp"
              v-for="(value, index) in propProducts"
              :key="index">
			{{ value.name }}
            <span v-if="!disabled" class="badge badge-pill badge-light badge-delete"
                                  @click="deleteFromProducts(value)">
				✕
			</span>
		</span>

        <span class="mb-2 mr-2 btn btn-info"
              v-if="accessoriesProducts.length"
              v-for="(value, index) in accessoriesProducts"
              :key="index">
			{{ value.name }}
            <span v-if="!disabled" class="badge badge-pill badge-light badge-delete"
                                  @click="deleteFromProducts(value)">
				✕
			</span>
		</span>

        <b-button v-if="!disabled" class="mb-2 mr-2 btn-icon btn-icon-only btn-shadow btn-dashed"
                  variant="outline-primary"
                  @click="showModal">
            <i class="pe-7s-plus btn-icon-wrapper"> </i>
        </b-button>


        <b-modal ref="AccessoriesModal"
                 id="accessories-modal"
                 :title="$t('form.products')"
                 hide-footer>
            <div class="accessories-search-wrap">
                <b-form-group id="id-accessories-group">
                    <b-form-input id="id-tag-input"
                                  class="tag-input"
                                  type="text"
                                  v-model="accessoriesInput"
                                  @input="loadProducts"
                                  :placeholder="$t('form.search_in_input')"></b-form-input>
                </b-form-group>
            </div>
            <div class="accessories-products-wrap">
                <button class="mb-2 mr-2 btn btn-info tag"
                        v-for="(value, index) in products"
                        :key="value.name"
                        @click="addToProducts(value)">
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
        mounted() {
            this.clearAccessoriesProducts();
        },
        props: {
            'accessoriesType': String,
            'modelWithProducts': Object,
            'propProducts': Array,
            'modelType': String,
            'title': String,
            'senToApi': Boolean,
            'required': Boolean,
            disabled: {
                type: Boolean,
                default: false,
            },
        },
        data: () => ({
            accessoriesInput: '',
            showProductsFromProp: true
        }),
        computed: {
            ...mapState({
                products: state => state.products.loadedProducts,
                accessoriesProducts: state => state.products.accessoriesProducts
            })
        },
        methods: {
            ...mapActions('products', {
                addProductToProducts: 'addProductToProducts',
                deleteProductFromProducts: 'deleteProductFromProducts',
                getProducts: 'getProducts'
            }),
            ...mapMutations('products', {
                clearAccessoriesProducts: 'clearAccessoriesProducts',
                addAccessoriesProducts: 'addAccessoriesProducts',
                deleteProductFromAccessories: 'deleteProductFromAccessories',
                deleteFromLoadedProducts: 'deleteFromLoadedProducts'
            }),
            showModal() {
                const data = {
                    accessoriesType: this.accessoriesType
                };

                this.getProducts(data);
                this.$refs['AccessoriesModal'].show();
            },
            loadProducts(input) {
                const data = {
                    q: input,
                    accessoriesType: this.accessoriesType
                };
                this.getProducts(data);
            },
            setData(id) {
                return {
                    idModel: this.modelWithProducts.id,
                    modelType: this.modelType,
                    accessoriesType: this.accessoriesType,
                    dataSend: {
                        id: id
                    }
                };
            },
            addToProducts(tag) {
                if (this.senToApi) {
                    const data = this.setData(tag.id);
                    this.addProductToProducts(data);
                    this.showProductsFromProp = false;
                } else {
                    this.addAccessoriesProducts(tag);
                    this.$toast.success('Produkt byl přidán');
                }
                this.deleteFromLoadedProducts(tag);
            },
            async deleteFromProducts(tag) {
                if (this.senToApi) {
                    const data = this.setData(tag.id);
                    await this.deleteProductFromProducts(data);
                    this.showProductsFromProp = false;
                } else {
                    this.deleteProductFromAccessories(tag);
                    this.$toast.success('Produkt byl odebrán');
                }
            }
        }
    }
</script>