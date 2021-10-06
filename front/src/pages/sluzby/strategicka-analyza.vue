<template>
	<div>
		<page-title :heading=heading
		            :subheading=subheading
		            :icon=icon
		            v-if="heading">
		</page-title>
            <div class="main-card mb-3 card analysis-services">
                <div class="grid-menu grid-menu-3col">
                  <div class="no-gutters row">
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 1 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-network btn-icon-wrapper"> </i>
	                      Architektura IT - Kde jsme dnes a kde chceme být zítra
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 2 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-cloud-check btn-icon-wrapper"> </i>
	                      Cloud vs. On-Premise – Analýza alternativ pro vybraný systém
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 3 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-cog btn-icon-wrapper"> </i>
	                       Možnosti Automatizace - Zhodnocení které funkce pro automatizaci uvažovat
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 4 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-license btn-icon-wrapper"> </i>
	                      Licenční Audit a Optimalizace - Změny licenčních modelů, expirace, upgrade, crossgrade a další
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 5 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-link btn-icon-wrapper"> </i>
	                      Analýza - Síťová infrastruktury a konektivita
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 6 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-graduation-hat btn-icon-wrapper"> </i>
	                      Školení specifických kompetencí - IT pracovníci či uživatelé
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 7 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-credit btn-icon-wrapper"> </i>
	                      Finanční IT Audit - Vybraná oblast a záměr
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 8 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-door-lock btn-icon-wrapper"> </i>
	                      IT Security - Bezpečnost sítě
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 9 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-laptop-phone btn-icon-wrapper"> </i>
	                       IT Security - Bezpečnost dat na koncových stanicích
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 10 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-exit-up btn-icon-wrapper"> </i>
	                      IT Security – Backup a disaster recovery
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 11 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-laptop btn-icon-wrapper"> </i>
	                      IT Security – Legislativa a nařízení
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 12 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-graph btn-icon-wrapper"> </i>
	                      Analýza - Identity Management v organizaci
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 13 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-layers btn-icon-wrapper"> </i>
	                      Business Continuity Management – Postupy a identifikace slabých míst
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 14 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-graph1 btn-icon-wrapper"> </i>
	                      Procesní analýza - Interní SLA, Issue tracking system
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 15 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-headphones btn-icon-wrapper"> </i>
	                      Intranet a Interní Komunikace - Interní marketing a informovanost
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 16 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-graph2 btn-icon-wrapper"> </i>
	                       Externí SLA analýza - Zajištění dostupnosti externích služeb
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 17 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="lnr-database btn-icon-wrapper"> </i>
	                      Databáze - Výkon, uložení dat, konsolidace serverů, licenční politika, backup
                      </nuxt-link>
                    </div>
                    <div class="col-sm-6 col-xl-4">
                      <nuxt-link :to="localePath({name: 'projekty-vytvorit', query:{ project_id: 18 }})" class="btn-icon-vertical btn-square btn-transition btn btn-outline-primary"><i class="pe-7s-notebook btn-icon-wrapper"> </i>
	                      Katalogu Služeb IT v Organizaci - ITIL
                      </nuxt-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
	
	</div>
</template>

<script>
  import PageTitle from "~/components/partials/PageTitle";

  export default {
    name: 'strategy-analysis',
    components: {
      PageTitle
    },
    data: () => ({
      icon: 'pe-7s-graph',
      heading: $nuxt.$t('menu.analysis'),
	    subheading: $nuxt.$t('services.analysis.info_text')
    })
  }
</script>