<template>
  <div>
    <page-title
      :heading=heading
      :subheading=subheading
      :icon=icon
      v-if="heading"
      :orderButton="false"
    />
    <SearcherComponent :mine-only="true"></SearcherComponent>
    <BoxComponent :mine-only="true" />
  </div>
</template>

<script>
import PageTitle from "~/components/partials/PageTitle.vue";
import SearcherComponent from '~/components/referential-projects/SearcherComponent';
import BoxComponent from '~/components/referential-projects/BoxComponent';

export default {
  components: { PageTitle, SearcherComponent, BoxComponent },
  name: "moje-referencni-projekty",
  data: () => ({
    f2: { gradient: ["#a8c470"] },
    f3: { gradient: ["#387eff"] },
    heading: $nuxt.$t("menu.reference_projects"),
    subheading: $nuxt.$t("help_text.reference_projects"),
    icon: "pe-7s-search icon-gradient bg-blue-icon",
  }),
};
</script>

<style lang="scss"></style>