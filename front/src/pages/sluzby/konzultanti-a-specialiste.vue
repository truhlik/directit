<template>
    <div>
        <page-title :heading=heading
                    :subheading=subheading
                    :icon=icon
                    v-if="heading">
        </page-title>
        <div class="consultants-cards row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3 mb-2" v-for="(consultant, index) in consultants.results" :key="index" :class="{highlighted: consultant.id == id}">
                <nuxt-link :to="localePath({name: `projekty-vytvorit`, query: { 'service-id': consultant.id, 'service-name': consultant.name }})" class="projectLink">
                <b-card border-variant="primary"
                        header-bg-variant="primary"
                        header-text-variant="white"
                        :header="consultant.name"
                        :footer="consultant.price ? consultant.price : null"
                        footer-tag="footer">
                    <b-card-text>
                        <b-row>
                            <b-col md="2">
                                <i class="btn-icon-wrapper" :class="[consultant.icon_name]"></i>
                            </b-col>
                            <b-col md="10" cols="10" class="description">
                                {{consultant.description}}
                            </b-col>
                        </b-row>
                    </b-card-text>
                    <!--<b-button href="#" variant="primary">Go somewhere</b-button>-->
                </b-card>
                </nuxt-link>
            </div>
        </div>
        <div class="d-flex justify-content-center mb-5 mt-5" v-if="consultants">
            <b-button v-if="consultants.pagination.next" class="btn-transition btn-hover-shine custom-lg"
                      variant="primary"
                      @click="loadMore">
                {{ $t('company.loadMore') }}
            </b-button>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import PageTitle from "~/components/partials/PageTitle";

    export default {
        name: "konzultanti-a-specialiste",
        components: {
            PageTitle
        },
        async fetch({store}) {
            await store.dispatch('services/getConsultants');
        },
        created() {
            this.id = this.$route?.query?.id
        },
        data: () => ({
            icon: 'pe-7s-users',
            heading: $nuxt.$t('menu.consultants_specialists'),
            subheading: $nuxt.$t('services.consultants_specialists.info_text'),
            id: null,
        }),
        computed: {
            ...mapState({
                consultants: state => state.services.consultants
            })
        },
        methods: {
            ...mapActions('services', {
                getConsultants: 'getConsultants',
            }),
            async loadMore() {
                const nextpage = this.consultants.pagination.page + 1;
                const query = {...this.$route.query, ...{page: nextpage}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });

                const data = {
                    page: nextpage,
                };

                this.getConsultants(data);
            },
        },
    }
</script>

<style scoped lang="scss">
    .projectLink, .projectLink:hover {
        text-decoration: none;

        &:hover .card-header {
            text-decoration: underline;
        }

        .description {
            text-decoration: none;
            color: #000;
        }
    }

    .btn-icon-wrapper {
        font-size: 30px;
    }

    .highlighted {
        font-weight: bold;
        animation: highlight .6s ease-in-out;
    }
</style>