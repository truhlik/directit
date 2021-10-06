<template>
    <div>
        <div class="row mt-4">
            <div class="col-sm-6 col-lg-4 col-xl-3 h-auto"
                 v-for="(value, index) in companies"
                 :key="index">
                <company-widget :company="value"></company-widget>
            </div>
        </div>
        <div class="d-flex justify-content-center mb-5 mt-5">
            <b-button v-if="pagination.next" class="btn-transition btn-hover-shine custom-lg"
                      variant="primary"
                      @click="loadMore">
                {{ $t('company.loadMore') }}
            </b-button>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapMutations, mapState} from 'vuex';
    import TestimonialsFormModal from "~/components/company/modals/TestimonialsFormModal";
    import TestimonialsModal from "~/components/company/modals/TestimonialsModal";
    import OrderModal from "~/components/orders/OrderModal";
    import {COMPANY_URLS} from "~/helpers/constants";
    import CompanyWidget from "./CompanyWidget";

    export default {
        name: 'companies-list',
        computed: {
            ...mapState({
                companies: state => state.companies.companiesList,
                pagination: state => state.companies.companyPagination,
            })
        },
        components: {
            CompanyWidget,
            TestimonialsFormModal,
            TestimonialsModal,
            OrderModal
        },
        props: ['companyType'],
        data: () => ({
            selectedCompany: {},
            companyUrls: COMPANY_URLS
        }),
        methods: {
            ...mapActions('companies', {
                findCompanies: 'findCompanies',
                getAllCompaniesMarkers: 'getAllCompaniesMarkers',
            }),
            ...mapMutations({
                clearCompanies: 'companies/clearCompanies',
                addSearchedItems: 'searchObject/addSearchedTag',
            }),
            async loadMore() {
                const nextpage = this.pagination.page + 1;
                const query = {...this.$route.query, ...{page: nextpage}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });

                const data = {
                    //searchedString: this.searchInput,
                    companyType: this.companyType,
                    page: nextpage,
                    add: true,
                    searchedString: query?.search ? query.search : ''
                };

                this.findCompanies(data);
                // TODO načítání markerů do mapy (zatím zrušeno)
                // await this.getAllCompaniesMarkers(data);
            },
            async filterByTag(role, search) {
                this.addSearchedItems(search)
                // const query = {search};
                // this.$router.push({
                //   path: this.$route.path,
                //   query: query
                // });
                //
                // const data = {
                //   searchedString: search,
                //   companyType: this.companyType
                // };
                //
                // await this.clearCompanies();
                // await this.findCompanies(data);
            }
        }
    }
</script>
