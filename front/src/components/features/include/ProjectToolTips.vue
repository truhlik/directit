<template>
    <div>
        <!-- TOOLTIP 1 -->
        <div v-if="num == 1">
            <p>Definice a analýza variant řešení z hlediska IT a businessu. Posouzení daného záměru v rámci celkového kontextu, IT architektury, vhodné
                technologie a designu. Analýzy se dělí podle rozsahu a komplexity od jednoduchých výchozích analýz přes studie proveditelnosti po komplexní
                strategické analýzy.</p>
        </div>
        <!-- TOOLTIP 2 -->
        <!--<div v-if="num == 2">
          <p>Zhodnocení vnitřního i vnějšího prostředí, architektura, technologie a design. Možnosti integrace a
            implementace.</p>
          <span>Příklady:</span>
          <ul class="list-alpha">
            <li>Konkrétní rešerše trhu – technologie a dodavatelé</li>
            <li>Připomínkování Vašich představ a koncepce</li>
            <li>TCO Cloud vs. On-premise řešení</li>
            <li>Standardní řešení vs. řešení na míru</li>
            <li>Propojení několika systémů, lepší sdílení a využití dat</li>
          </ul>
          <span>
          Standardní Výstupy:
        </span>
          <ul>
            <li class="text-primary text-bold">Strategická analýza</li>
          </ul>
        </div>-->
        <!-- TOOLTIP 2, previously 3 -->
        <div v-if="num == 2">
            <p>V rámci studie trhu provádíme komplexní a nezávislou analýzu toho jaké technologie a jaké subjekty se na trhu nabízí pro pokrytí daných ICT
                potřeb. Předmětem posouzení jsou klíčové ukazatele ve smyslu cena - kvalita - čas.</p>
        </div>
        <!-- TOOLTIP 3 -->
        <!--<div v-if="num == 4">
          <p>Vypracování poptávky a sběr dat o podmínkách dodání od Vámi vybraného počtu potenciálních dodavatelů. Celé na
            základě Vámi zadaných kritérií za cílem získání těch nejlepších podmínek.</p>
          <span>Příklady:</span>
          <ul class="list-alpha">
            <li>Příprava Výběrového/poptávkového řízení</li>
            <li>Úspora na stávajícím řešení/technologii</li>
            <li>Studie indikativních nabídek</li>
            <li>Srovnání garance a podmínek dodavatelů</li>
          </ul>
          <span>
          Standardní Výstupy:
        </span>
          <ul>
            <li class="text-primary text-bold">Příprava Výběrového Řízení</li>
            <li class="text-primary text-bold">Příprava Poptávkového Řízení</li>
          </ul>
        </div>-->
        <!-- TOOLTIP 3, previously 5 -->
        <div v-if="num == 3">
            <p>Ve fázi selekce dodavatelů se specializujeme na přípravy VŘ, zpracování dokumentace, komunikace s dodavateli a nezávislé posuzovaní nabídek.</p>

        </div>
        <!-- TOOLTIP 4, previously 6 -->
        <div v-if="num == 4">
            <p>Realizace prostřednictvím Direct IT zahrnuje přímé využívaní našich expertů pro konkrétní definované účely konzultace, implementace a podpory ICT
                technologií.</p>

        </div>
        <div v-if="services && services.length">
            <p>Související služby:</p>
            <ul>
                <li class="text-primary text-bold" v-for="service in services">
                    <nuxt-link target="_blank" :to="localePath({name: serviceCategoryLink[service.category], query: { id: service.id }})">{{service.name}}</nuxt-link>
<!--                    <a :href="'#'+localePath({name: serviceCategoryLink[service.category], query: { id: service.id }})" target="_blank">{{service.name}}</a>-->
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            num: {
                type: Number,
                default: 0
            },
            services: {
                type: Array,
                default: null
            }
        },
        data: () => ({
            serviceCategoryLink: {
                ANALYZE: `sluzby-analyzy-a-studie`,
                SERVICE: `sluzby-ict-sluzby`,
                CONSULTANT: `sluzby-konzultanti-a-specialiste`,
            },
        }),
    }
</script>