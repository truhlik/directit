<template>
    <div class="technology-box-component">
        <div class="row mt-4 d-flex align-items-stretch" id="technology-box-component-container">
            <div class="col-sm-6 col-lg-4 col-xl-3 h-auto category mb-3"
                 v-for="(category, index) in categories"
                 :id="'category-'+category.id"
                 :key="index">
                <!--for expanding :class="{'col-sm-12': selectedCategory==category.id, 'col-lg-12': selectedCategory==category.id, 'col-xl-12': selectedCategory==category.id, 'selected': selectedCategory==category.id}"-->
                <div class="card-shadow-primary profile-responsive card-border card">
                    <div class="dropdown-menu-header">
                        <div class="tab-pane active show">
                            <div class="dropdown-menu-header-inner bg-blue-icon">
                                <div class="menu-header-content btn-pane-right">
                                    <div>
                                        <h5 class="menu-header-title">{{category.name}}</h5>
                                        <h6 class="menu-header-subtitle">{{ category.subcategories.length }} {{ $t('technology.subcategories_count') }}</h6>
                                    </div>
                                </div>
                                <div class="mr-2" v-if="category.subcategories.length">
                                    <div class="rounded">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-content">
                        <div class="subcategories" v-if="category.subcategories.length" :class="{selected: selectedCategory==category.id}"><!--scroll-area-sm-->
                            <section class=""> <!--ps-container scrollbar-container ps ps&#45;&#45;theme_default ps&#45;&#45;active-y-->
                                <ul class="list-group list-group-flush"
                                    :class="{selected: selectedCategory==category.id}">
                                    <!--'list-group': selectedCategory!==category.id, 'list-group-flush': selectedCategory!==category.i-->
                                    <li class="list-group-item" v-for="(subcategory, subcategoryIndex) in category.subcategories"
                                        :key="subcategoryIndex">
                                        <div class="widget-content subcategory p-1 h-auto"
                                            @click="/*subcategory.products_count ? toggleSubcategory(subcategory.id, category.id) : null*/"
                                            :class="{'subcategory-has-products': !!subcategory.products_count}">
                                            <div class="widget-content-wrapper">
                                                <div class="widget-content-left center-elem mr-2">
                                                    <span class="subcategory-count badge badge-pill badge-primary subcategory-count-badge"
                                                        :class="{ invisible: !subcategory.products_count }">
                                                        <a href="#" v-b-modal="'product-list-modal-'+subcategory.id" class="product-list-modal-link text-white">
                                                            {{subcategory.products_count}}
                                                        </a>
                                                    </span>
                                                </div>
                                                <div class="widget-content-left">
                                                    <div class="widget-heading" v-if="!subcategory.products_count">
                                                        {{subcategory.name}}
                                                    </div>
                                                    <div class="widget-heading" v-if="subcategory.products_count">
                                                        <a href="#" v-b-modal="'product-list-modal-'+subcategory.id" class="product-list-modal-link">
                                                            {{subcategory.name}}
                                                        </a>
                                                    </div>
                                                </div>
                                                <!--<div class="widget-content-right widget-content-actions">
                                                    <button aria-haspopup="true" aria-expanded="true" type="button"
                                                            class="btn btn-primary mr-1 btn-icon btn-icon-only btn-sm dropdown-toggle"
                                                            :id="'toggle_subcategory_'+subcategory.id">
                                                        <i class="pe-7s-plus btn-icon-wrapper"></i>
                                                    </button>
                                                </div>-->
                                            </div>
                                        </div>
                                        <b-modal ok-only :title="subcategory.name" :id="'product-list-modal-'+subcategory.id">
                                            <ProductListModal :id="subcategory.id"></ProductListModal>
                                        </b-modal>
                                    </li>
                                </ul>
                                <!--<div class="ps__scrollbar-x-rail" style="left: 0px; bottom: 0px;">
                                    <div class="ps__scrollbar-x" tabindex="0" style="left: 0px; width: 0px;"></div>
                                </div>
                                <div class="ps__scrollbar-y-rail" style="top: 0px; height: 200px; right: 0px;">
                                    <div class="ps__scrollbar-y" tabindex="0" style="top: 0px; height: 130px;"></div>
                                </div>-->
                            </section>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--<ProductDetailModal ref="childProductDetailModal"></ProductDetailModal>-->
        <!--<pre>{{groupProducts}}</pre>-->


    </div>
</template>

<script>
    import {mapActions, mapMutations, mapState} from 'vuex';
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faPlus} from '@fortawesome/free-solid-svg-icons'
    import ProductListModal from "./ProductListModal";

    library.add(
        faPlus
    );

    export default {
        name: "BoxComponent",
        computed: {
            ...mapState({
                categories: state => state.technologies.categories,
                groupProducts: state => state.technologies.groupProducts,
            })
        },
        components: {
            ProductListModal
        },
        data: () => ({
            selectedCategory: null,
            expandedSubcategories: [],
        }),
        methods: {
            ...mapActions('technologies', {
                getCategories: 'getCategories',
                getCategoryProducts: 'getCategoryProducts',
            }),
            ...mapMutations({
                clearCategories: 'technologies/clearCategories',
                addSearchedItems: 'searchObject/addSearchedTag',
            }),
            toggleSubcategory(id, categoryId) {
                if (this.expandedSubcategories.includes(id)) {
                    //this.expandedSubcategory = null;
                    this.expandedSubcategories = this.expandedSubcategories.filter(item => item !== id)
                } else {
                    //console.log('toggleSubcategory', id)
                    this.selectedCategory = categoryId
                    this.expandedSubcategories.push(id)
                    if (!this.groupProducts[id]) {
                        this.getCategoryProducts(id)
                    }
                    //console.log('categoryId', categoryId)
                    //setTimeout(document.getElementById('category-' + categoryId)?.scrollIntoView(), 6000)
                }
            },
            showProductDetailModal(id) {
                console.log('showProductDetailModal', id)
                this.$refs.childProductDetailModal.showModal(id);
            },
        }
    }
</script>

<style scoped lang="scss">
    .subcategories {
        /*overflow-x: hidden;
        overflow-y: auto;*/
        max-height: 820px;
        overflow: hidden;
        transition: max-height 0.6s ease-in-out;

        &:hover {
            //max-height: 200vh;
            overflow-y: scroll;
        }

        &.selected {
            max-height: 200vh;

            /*> section {
                > ul {
                    display: flex;
                    flex-wrap: wrap;
                    > li {
                        flex: 1 0 250px;
                        border: none;
                        > ul {
                            border-bottom: 1px black solid;
                        }
                    }
                }
            }*/
        }
    }

    .subcategory {
        border: none
    }

    .subcategory.subcategory-has-products {
        cursor: pointer;

        &:hover {
            text-decoration: underline;
        }
    }

    .subcategory-count-badge {
        min-width: 3em;
    }

    .category {
        transition: all .6s ease;
    }

    .product-list-modal-link {
        color: initial;
        text-decoration: none;
        text-decoration-line: none;
        &:hover {
            color: initial;
            text-decoration: none;
            text-decoration-line: none;
        }
    }
</style>