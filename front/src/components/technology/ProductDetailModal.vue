<template>
    <div class="product-detail-modal">
        <div v-if="loading" class="p-2 text-center">
            <b-spinner variant="primary" label="Spinning"></b-spinner>
        </div>
        <div class="w-100 d-flex justify-content-center" v-if="!loading">
            <div class="card-shadow-primary profile-responsive card-border mb-3 card w-100" v-if="product">
                <ul class="list-group list-group-flush">
                    <li class="bg-sunny-morning list-group-item" v-if="product.vendor">
                        <div class="widget-content p-0">
                            <div class="widget-content-wrapper">
                                <div class="widget-content-left mr-3"></div>
                                <div class="widget-content-left p-2">
                                    <!--<div class="widget-heading text-dark opacity-7">{{ $t('technology.vendor') }}:</div>
                                    <div class="widget-subheading opacity-10">{{product.vendor.name}}</div>-->
                                    <p class="vendor-title">
                                        <b>{{ $t('technology.vendor') }}:</b>
                                        {{product.vendor.name}}</p>
                                </div>
                                <div class="widget-content-right">
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="p-0 list-group-item">
                        <div class="card-body px-3 py-2" v-if="product.description"><p>{{product.description}}</p></div>
                    </li>
                    <li class="p-0 list-group-item">
                        <div class=""><!--grid-menu grid-menu-2col overflow-hidden-->
                            <div class="no-gutters row">
                                <div class="col-sm" v-if="product.suppliers.length"
                                     :class="{'col-12': product.categories.length==0 || product.suppliers.length+product.categories.length > 15}">
                                    <div class="card-body categories text-center">
                                        <div v-for="(supplier, supplierIndex) in product.suppliers">
                                            <nuxt-link :to="localePath({name: `subjekty-type-id`, params: { id: supplier.id, type: companyUrls.SUPPLIER }})"
                                                       class="mb-2 mr-2 btn btn-secondary w-auto p-1" :class="{'w-100': product.suppliers.length==1}"
                                                       :id="'supplier-' + supplier.id">
                                                {{supplier.name}}
                                                <span class="badge badge-secondary badge-dot badge-dot-lg"></span>
                                            </nuxt-link>
                                            <b-popover :target="'supplier-' + supplier.id"
                                                       placement="top"
                                                       triggers="hover" v-if="supplier.email || supplier.phone">
                                                <a :href="supplier.email" v-if="supplier.email">{{supplier.email}}</a>
                                                <a :href="'callto:' + supplier.phone">{{supplier.phone}}</a>
                                            </b-popover>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-sm" v-if="product.categories.length"
                                     :class="{'col-12': product.suppliers.length== 0 || product.suppliers.length+product.categories.length > 15}">
                                    <div class="card-body suppliers text-center">
                                        <nuxt-link :to="getCategorySearchLink(category.name)" class="mb-2 mr-2 btn btn-info w-auto p-1"
                                                   v-for="(category, categoryIndex) in product.categories" :id="'category-' + categoryIndex"
                                                   :key="'category-' + categoryIndex"
                                                   :class="{'w-100': product.categories.length==1}">
                                            {{category.name}}
                                            <span class="badge badge-info badge-dot badge-dot-lg"></span>
                                        </nuxt-link>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
                <b-spinner variant="primary" label="Spinning" v-if="!product"></b-spinner>
            </div>
        </div>
        <!--<pre class="d-block">{{product}}</pre>-->
        <!--</b-modal>-->
    </div>
</template>

<script>
    import ProjectToolTips from "~/components/features/include/ProjectToolTips";
    import {COMPANY_URLS} from "~/helpers/constants";

    export default {
        name: "product-detail-modal",
        components: {
            ProjectToolTips
        },
        props: {
            id: String | Number,
        },
        data: () => ({
            //id: null,
            product: null,
            companyUrls: COMPANY_URLS,
            loading: false,
        }),
        computed: {},
        methods: {
            /*closeModal() {
                this.$refs['productDetailModal'].hide();
            },
            showModal(id) {
                this.id = id;
                console.log('openModal', this.id)
                this.loadDetail()
                this.$refs['productDetailModal'].show();
            },*/
            async loadDetail() {
                const url = "products/" + this.id + '/';
                this.loading = true
                const response = await this.$axios.get(url)
                this.product = response.data
                this.loading = false
            },
            getCategorySearchLink(value) {
                return {name: 'subjekty-seznam-dodavatelu___cs', query: {search: value}}
            }
        },
        created: function () {
            if (!this.product) {
                this.loadDetail();
            }
        },
    }
</script>

<style lang="scss" scoped>
    .vendor-title {
        font-size: 20px;
    }
</style>