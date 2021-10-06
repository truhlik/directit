<template>
    <div class="ict-services" v-if="services">
        <div class="services-cards row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3 mb-2" v-for="(service, index) in services.results" :key="index" :class="{highlighted: service.id == highlightId}">
                <nuxt-link :to="localePath({name: `projekty-vytvorit`, query: { 'service-id': service.id, 'service-name': service.name }})" class="projectLink">
                    <b-card border-variant="primary"
                            header-bg-variant="primary"
                            header-text-variant="white"
                            :header="service.name"
                            :footer="service.price + ''"
                            footer-tag="footer">
                        <b-card-text>
                            <b-row>
                                <b-col cols="2">
                                    <i class="btn-icon-wrapper" :class="[service.icon_name]"> </i>
                                </b-col>
                                <b-col cols="10" class="description">
                                    {{service.description}}
                                </b-col>
                            </b-row>
                        </b-card-text>
                        <!--<b-button href="#" variant="primary">Go somewhere</b-button>-->
                    </b-card>
                </nuxt-link>
            </div>
        </div>
        <div class="d-flex justify-content-center mb-5 mt-5" v-if="services && services.pagination">
            <b-button v-if="services.pagination.next" class="btn-transition btn-hover-shine custom-lg"
                      variant="primary"
                      @click="loadMore">
                {{ $t('company.loadMore') }}
            </b-button>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "IctServices",
        created() {
            (async () => {
                await this.$store.dispatch('services/getServices');
            })()
        },
        computed: {
            ...mapState({
                services: state => state.services.services
            })
        },
        props: {
            highlightId: String | Number,
        },
        methods: {
            ...mapActions('services', {
                getServices: 'getServices',
            }),
            async loadMore() {
                const nextpage = this.services.pagination.page + 1;
                const query = {...this.$route.query, ...{page: nextpage}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });

                const data = {
                    page: nextpage,
                };

                this.getServices(data);
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
            //max-width: calc(100% - 60px);
            color: #000;
        }
    }

    .btn-icon-wrapper {
        font-size: 30px;
    }

    .services-cards {
        //max-width: 900px;
    }

    .highlighted {
        font-weight: bold;
        animation: highlight .6s ease-in-out;
    }
</style>