<template>
    <div>
        <page-title :heading=heading
                    :subheading=subheading
                    :icon=icon
                    v-if="heading">
        </page-title>
        <div class="analyzes-cards row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3 mb-2" v-for="(analysis, index) in analyzes.results" :key="index" :class="{highlighted: analysis.id == id}">
                <nuxt-link :to="localePath({name: `projekty-vytvorit`, query: { 'service-id': analysis.id, 'service-name': analysis.name }})" class="projectLink">
                <b-card border-variant="primary"
                        header-bg-variant="primary"
                        header-text-variant="white"
                        :header="analysis.name"
                        :footer="analysis.price + ''"
                        footer-tag="footer">
                    <b-card-text>
                        <b-row>
                            <b-col cols="2">
                                <i class="btn-icon-wrapper" :class="[analysis.icon_name]"> </i>
                            </b-col>
                            <b-col cols="10" class="description">
                                {{analysis.description}}
                            </b-col>
                        </b-row>
                    </b-card-text>
                    <!--<b-button href="#" variant="primary">Go somewhere</b-button>-->
                </b-card>
                </nuxt-link>
            </div>
        </div>
        <div class="d-flex justify-content-center mb-5 mt-5" v-if="analyzes">
            <b-button v-if="analyzes.pagination.next" class="btn-transition btn-hover-shine custom-lg"
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
        name: "analyzy-a-studie",
        components: {
            PageTitle
        },
        async fetch({store}) {
            await store.dispatch('services/getAnalyzes');
        },
        created() {
            this.id = this.$route?.query?.id
        },
        data: () => ({
            icon: 'pe-7s-graph2',
            heading: $nuxt.$t('menu.analyzes_studies'),
            subheading: $nuxt.$t('services.analyzes_studies.info_text'),
            id: null,
        }),
        computed: {
            ...mapState({
                analyzes: state => state.services.analyzes
            })
        },
        methods: {
            ...mapActions('services', {
                getAnalyzes: 'getAnalyzes',
            }),
            async loadMore() {
                const nextpage = this.analyzes.pagination.page + 1;
                const query = {...this.$route.query, ...{page: nextpage}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });

                const data = {
                    page: nextpage,
                };

                this.getAnalyzes(data);
            },
        }
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

    .analyzes-cards {
        //max-width: 900px;
    }
</style>