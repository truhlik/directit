<template>
    <div class="product-list-modal">
        <div v-if="!groupProducts[id]" class="p-2 text-center"><!--expandedSubcategories.includes(subcategory.id) &&-->
            <b-spinner variant="primary" label="Spinning"></b-spinner>
        </div>
        <div v-if="groupProducts[id]"
             class="box-tags"><!--expandedSubcategories.includes(subcategory.id) &&-->
            <span class="mr-2 d-inline-flex" v-for="(product, productIndex) in groupProducts[id]" :key="productIndex">
                <!--<a href="#" @click="showProductDetailModal(product.id)">{{product.name}}</a>-->


                <b-button href="#" v-b-modal="'product-modal-'+product.id" class="btn-light mb-1">
                    {{product.name}}
                    <span class="badge badge-dark badge-dot badge-dot-lg"></span>
                </b-button>

                <b-modal ok-only :title="product.name" :id="'product-modal-'+product.id">
                    <ProductDetailModal :id="product.id"></ProductDetailModal>
                </b-modal>
            </span>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapMutations, mapState} from 'vuex';
    import ProductDetailModal from "~/components/technology/ProductDetailModal";

    export default {
        name: "ProductListModal",
        props: {
            id: Number | String,
        },
        components: {
            ProductDetailModal,
        },
        computed: {
            ...mapState({
                groupProducts: state => state.technologies.groupProducts,
            }),
        },
        created() {
            if (!this.groupProducts[this.id]) {
                this.getCategoryProducts(this.id)
            }
        },
        methods: {
            ...mapActions('technologies', {
                getCategoryProducts: 'getCategoryProducts',
            }),
        },
    }
</script>

<style scoped>

</style>
