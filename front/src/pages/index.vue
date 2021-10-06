<template>
    <div class="content main-content">
        <div class="row dashboard-row">
            <div class="col-sm-12 col-md-6 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg bg-info"></div>
                            <i class="lnr-laptop-phone text-info"></i></div>
                        <div class="widget-numbers">
							<span>
								<ICountUp
                                        :startVal="startVal"
                                        :endVal="myProjects.length"
                                        :decimals="decimals"
                                        :duration="duration"
                                        :options="options"
                                />
							</span>
                        </div>
                        <div class="widget-subheading fsize-1 pt-2 opacity-10 text-info font-weight-bold">
                            Projekty
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 col-md-6 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg bg-info"></div>
                            <i class="lnr-graduation-hat text-info"></i>
                        </div>
                        <div class="widget-numbers"><span>
                            <ICountUp
                                    :startVal="startVal"
                                    :endVal="myAssistant.pagination.count"
                                    :decimals="decimals"
                                    :duration="duration"
                                    :options="options"
                            />
                        </span>
                        </div>
                        <div class="widget-subheading fsize-1 pt-2 opacity-10 text-info font-weight-bold">
                            {{$t('services.it_assistant.title')}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 col-md-12 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg bg-info"></div>
                            <i class="lnr-diamond text-info"></i></div>
                        <div class="widget-numbers text-dark">
	                      <span>
                                <ICountUp
                                        :startVal="startVal"
                                        :endVal="mySoftware.pagination.count"
                                        :decimals="decimals"
                                        :duration="duration"
                                        :options="options"
                                />

                        </span>
                        </div>
                        <div class="widget-subheading fsize-1 pt-2 opacity-10 text-info font-weight-bold">
                            {{$t('services.monitored_technologies.title')}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 col-md-5 col-xl-4">
                <div class="main-card mb-3 card">
                    <div class="card-body"><h5 class="card-title">Projekty</h5>
                        <div
                                class="vertical-time-simple vertical-without-time vertical-timeline vertical-timeline--animate vertical-timeline--one-column">

                            <div v-for="(project, index_project) in myProjects" :key="index_project" class="vertical-timeline-element">
                                <div><span class="vertical-timeline-element-icon bounce-in"></span>
                                    <div class="vertical-timeline-element-content bounce-in"><h4 class="timeline-title">{{ project.name }}</h4></div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <!--<div class="col-sm-12 col-md-5 col-xl-4">
                <div class="main-card mb-3 card">
                    <div class="card-body"><h5 class="card-title">Expert Callback</h5>
                        <div
                                class="vertical-time-simple vertical-without-time vertical-timeline vertical-timeline&#45;&#45;animate vertical-timeline&#45;&#45;one-column">

                            <div v-for="(callback, index_callback) in myCallbacks.results" :key="callback.id" class="vertical-timeline-element">
                                <div><span class="vertical-timeline-element-icon bounce-in"></span>
                                    <div class="vertical-timeline-element-content bounce-in"><h4 class="timeline-title">{{ callback.name }}</h4></div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 col-md-5 col-xl-4">
                <div class="main-card mb-3 card">
                    <div class="card-body"><h5 class="card-title">IT Consierge</h5>
                        <div
                                class="vertical-time-simple vertical-without-time vertical-timeline vertical-timeline&#45;&#45;animate vertical-timeline&#45;&#45;one-column">

                            <div v-for="(consierge, index_consierge) in myConsierges.results" :key="consierge.id" class="vertical-timeline-element">
                                <div><span class="vertical-timeline-element-icon bounce-in"></span>
                                    <div class="vertical-timeline-element-content bounce-in"><h4 class="timeline-title">{{ consierge.name }}</h4></div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>-->
            <div class="col-sm-12 col-md-5 col-xl-4">
                <div class="main-card mb-3 card">
                    <div class="card-body"><h5 class="card-title">{{$t('services.it_assistant.title')}}</h5>
                        <div
                                class="vertical-time-simple vertical-without-time vertical-timeline vertical-timeline--animate vertical-timeline--one-column">

                            <div v-for="(assistant, index_assistant) in myAssistant.results" :key="assistant.id" class="vertical-timeline-element">
                                <div><span class="vertical-timeline-element-icon bounce-in"></span>
                                    <div class="vertical-timeline-element-content bounce-in"><h4 class="timeline-title">{{ assistant.name }}</h4></div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 col-md-5 col-xl-4">
                <div class="main-card mb-3 card">
                    <div class="card-body"><h5 class="card-title">{{$t('services.monitored_technologies.title')}}</h5>
                        <div
                                class="vertical-time-simple vertical-without-time vertical-timeline vertical-timeline--animate vertical-timeline--one-column">

                            <div v-for="(software, index_software) in mySoftware.results" :key="software.id" class="vertical-timeline-element">
                                <div><span class="vertical-timeline-element-icon bounce-in"></span>
                                    <div class="vertical-timeline-element-content bounce-in"><h4 class="timeline-title">{{ software.name }}</h4></div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-6">
                <div class="card mb-5">
                    <div class="card widget-content bg-blue-icon pointer" @click="subjects_database = !subjects_database">
                        <div class="widget-content-wrapper text-white">
                            <div class="widget-content-left">
                                <div class="widget-heading">Moje IT</div>
                            </div>
                            <div class="widget-content-right">
                                <div class="widget-numbers text-white"><span><font-awesome-icon class="ml-1" icon="laptop"/></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <transition name="slideDown">
                        <div class="row" v-if="subjects_database">
                            <div class="col-sm-12">
                                <div class="card no-shadow rm-border bg-transparent widget-chart text-left">
                                    V sekci Moje IT můžete jednoduše řídit a kontrolovat technologie a zařízení, které jsou ve
                                    vašem IT využívány a současně plánovat nové projekty a poptávat zdroje.
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="card no-shadow rm-border bg-transparent widget-chart text-left pb-0">
                                    <div class="icon-wrapper rounded-circle">
                                        <div class="icon-wrapper-bg opacity-10 bg-primary"></div>
                                        <i class="lnr-keyboard text-light opacity-8"></i></div>
                                    <div class="widget-chart-content">
                                        <strong>1. Zadat Technologii</strong>
                                        <div class="widget-subheading">Vám umožňuje si jednoduše zmapovat technologie, které jsou
                                            využívány pro vytvoření uceleného přehledu a nastavení aktivit, jako upozornění
                                            expirace, zájem o vyhledání alternativ, potřebu customizace a mnoho dalšího.<br>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-start it-btns">
                                    <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-3"
                                               :to="localePath({name: 'technologie-vytvorit'})">
                                        Zadat technologii
                                    </nuxt-link>
                                </div>
                                <div class="divider m-0 d-md-none d-sm-block"></div>
                            </div>
                            <div class="col-sm-12">
                                <div class="card no-shadow rm-border bg-transparent widget-chart text-left pb-0">
                                    <div class="icon-wrapper rounded-circle">
                                        <div class="icon-wrapper-bg opacity-10 bg-primary"></div>
                                        <i class="lnr-file-add text-light opacity-8"></i></div>
                                    <div class="widget-chart-content">
                                        <strong>2. Vytvořit Projekt</strong>
                                        <div class="widget-subheading"> je nástroj plánování IT projektů a poptávky, jež jsou aktuální
                                            v krátkodobém, střednědobém i dlouhodobém horizontu.<br>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-start it-btns">
                                    <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-3"
                                               :to="localePath({name: 'projekty-vytvorit'})">
                                        Vytvořit projekt
                                    </nuxt-link>
                                </div>
                                <div class="divider m-0 d-md-none d-sm-block"></div>
                            </div>

                        </div>
                    </transition>

                </div>
            </div>
            <div class="col-lg-6">
                <div class="card">
                    <div class="card widget-content bg-blue-icon pointer" @click="subjects_database = !subjects_database">
                        <div class="widget-content-wrapper text-white">
                            <div class="widget-content-left">
                                <div class="widget-heading">Subjekty & Technologie</div>
                            </div>
                            <div class="widget-content-right">
                                <div class="widget-numbers text-white"><span><font-awesome-icon class="ml-1" icon="database"/></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <transition name="slideDown">
                        <div class="col-sm-12" v-if="subjects_database">
                            <div class="card no-shadow rm-border bg-transparent widget-chart text-left">
                                V sekci Databáze subjektů je možné identifikovat, lokalizovat a následně alokovat IT
                                dodavatele či nezávislé IT konzultanty, experty a lektory. Filtrace je možná jak geograficky,
                                tak podle vybrané expertizy.
                                Výběr můžete provést sami či na základě zadaných požadavků delegovat celou věc na team
                                Direct IT a my pro Vás potřebnou expertizu zajistíme.
                            </div>
                            <div class="justify-content-center d-flex">
                                <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-3"
                                           :to="localePath({name: 'subjekty-seznam-dodavatelu'})">
                                    <font-awesome-icon class="ml-1" icon="user-tie"/>
                                    Seznam Dodavatelů
                                </nuxt-link>
                                <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-3"
                                           :to="localePath({name: 'subjekty-seznam-konzultantu'})">
                                    <font-awesome-icon class="ml-1" icon="user-tie"/>
                                    Seznam Konzultantů
                                </nuxt-link>
                                <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-3"
                                           :to="localePath({name: 'subjekty-seznam-technologii'})">
                                    <font-awesome-icon class="ml-1" icon="user-tie"/>
                                    Katalog
                                </nuxt-link>
                            </div>
                        </div>

                    </transition>

                </div>
            </div>
        </div>

        <div class="row">

            <div class="col-sm-12 col-md-6 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content dashboard">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg"></div>
                            <i class="pe-7s-graph2 text-primary"></i>
                        </div>
                        <div class="widget-numbers">
								<span>
									{{$t('menu.analyzes_studies')}}
								</span>
                        </div>
                        <div class="widget-subheading pt-2">
                            {{$t('services.analyzes_studies.info_text')}}
                        </div>
                    </div>
                    <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-1"
                               :to="localePath({name: 'sluzby-analyzy-a-studie'})">
                        {{$t('menu.analyzes_studies')}}
                    </nuxt-link>
                </div>
            </div>
            <div class="col-sm-12 col-md-6 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content dashboard">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg"></div>
                            <i class="pe-7s-server btn-icon-wrapper text-primary"></i>
                        </div>
                        <div class="widget-numbers">
							<span>
									{{$t('menu.ict_services')}}
							</span>
                        </div>
                        <div class="widget-subheading pt-2">
                            {{$t('services.ict_services.info_text')}}
                        </div>
                    </div>
                    <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-1"
                               :to="localePath({name: 'sluzby-ict-sluzby'})">
                        {{$t('menu.ict_services')}}
                    </nuxt-link>
                </div>
            </div>
            <div class="col-sm-12 col-md-6 col-xl-4">
                <div class="card mb-3 widget-chart">
                    <div class="widget-chart-content dashboard">
                        <div class="icon-wrapper rounded">
                            <div class="icon-wrapper-bg"></div>
                            <i class="pe-7s-users btn-icon-wrapper text-primary"></i>
                        </div>
                        <div class="widget-numbers">
							<span>
									{{$t('menu.consultants_specialists')}}
							</span>
                        </div>
                        <div class="widget-subheading pt-2">
                            {{$t('services.consultants_specialists.info_text')}}
                        </div>
                    </div>
                    <nuxt-link class="btn btn-transition btn-hover-shine btn-outline-primary m-1 mb-1"
                               :to="localePath({name: 'sluzby-konzultanti-a-specialiste'})">
                        {{$t('menu.consultants_specialists')}}
                    </nuxt-link>
                </div>
            </div>
        </div>
        <page-disclaimer :text="$t('disclaimer.security_info')"></page-disclaimer>

        <CallbackModal ref="childCallbackModal"
                       :modalName="modalName"
                       :infoText="modalInfoText"
                       :callbackType="callbackType"></CallbackModal>
    </div>
</template>

<script>
    import VuePerfectScrollbar from 'vue-perfect-scrollbar'
    import ICountUp from 'vue-countup-v2';
    import CallbackModal from "~/components/user/modals/CallbackModal"
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {
        faDatabase,
        faLaptop,
        faUser,
        faUserTie,
        faServer,
        faUsers,
    } from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

    import {mapActions, mapState} from 'vuex'
    import PageDisclaimer from "../components/partials/PageDisclaimer";

    library.add(
        faUser,
        faLaptop,
        faDatabase,
        faUserTie,
        faServer,
        faUsers,
    );

    export default {
        name: 'homepage',
        components: {
            PageDisclaimer,
            VuePerfectScrollbar,
            ICountUp,
            FontAwesomeIcon,
            CallbackModal
        },
        async fetch({store, redirect}) {
            if (!store.getters['user/isClient']) {
                redirect({name: 'uzivatel-upravit___cs'})
            }

            await store.dispatch('projects/getMyProjects', {})

        },
        created() {
            //this.getMyConsierges();
            //this.getMyCallbacks();
            this.getMyAssistant();
            this.getMySoftware();
        },
        data: () => ({
            callbacks: [],
            consierges: [],
            startVal: 0,
            decimals: 0,
            duration: 5.5,
            options: {
                useEasing: true,
                useGrouping: true,
                separator: ',',
                decimal: '.',
                prefix: '',
                suffix: ''
            },
            modalName: '',
            modalInfoText: '',
            callbackType: '',
            subjects_database: false,
        }),
        computed: {
            ...mapState({
                //myCallbacks: state => state.user.myCallbacks,
                //myConsierges: state => state.user.myConsierges,
                myProjects: state => state.projects.projectList,
                myAssistant: state => state.user.myAssistant,
                mySoftware: state => state.user.mySoftware,
            })
        },
        methods: {
            ...mapActions({
                //getMyCallbacks: 'user/getMyCallbacks',
                //getMyConsierges: 'user/getMyConsierges',
                getMyAssistant: 'user/getMyAssistant',
                getMySoftware: 'user/getMySoftware',
            }),
            // async fillConsierges(){
            //   this.$axios.$get('consierge/').then(
            //     response => {
            //       this.consierges = response.results ? response.results : [];
            //     }
            //   );
            // },
            openCallback() {
                this.modalName = 'Expert Callback';
                this.modalInfoText = this.$t('services.callback.info_text');
                this.callbackType = 'callback';
                this.$refs['childCallbackModal'].openModal();
            },
            openConsierge() {
                this.modalName = 'IT Consierge';
                this.modalInfoText = this.$t('services.it_consierge.info_text');
                this.callbackType = 'consierge';
                this.$refs['childCallbackModal'].openModal();
            }
        }
    }
</script>
