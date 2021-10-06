<template>
  <div id="user-edit-wrap">
    <PageTitle
      :heading=heading
      :icon=icon
      v-if="heading"
      :image="company.image"
    >

    </PageTitle>
    <div class="custom-container card pt-5">
      <b-card
        v-if="!isClient"
        :title="isSupplier ? $t('account.completation_tips_title_supplier') : $t('account.completation_tips_title_consultant')"
        style="box-shadow: none"
        class="mb-2 d-flex flex-wrap justify-content-center text-center"
      >
        <b-card-text class="d-flex flex-wrap justify-content-center align-items-stretch">
          <b-nav
            pills
            fill
            justified
          >
            <b-nav-item
              v-if="isSupplier"
              :to="{ name: 'subjekt-vytvorit___cs' }"
            >
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip1')}}
            </b-nav-item>
            <b-nav-item
              v-if="isSupplier"
              :to="{ name: 'subjekt-vytvorit___cs' }"
            >
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip2')}}
            </b-nav-item>
            <b-nav-item
              v-if="isSupplier"
              :to="{ name: 'subjekt-vytvorit___cs' }"
            >
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip3')}}
            </b-nav-item>
            <b-nav-item :to="{ name: 'subjekt-vytvorit___cs' }">
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip4')}}
            </b-nav-item>
            <b-nav-item :to="{ name: 'subjekt-vytvorit___cs' }">
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip5')}}
            </b-nav-item>
            <b-nav-item
              v-if="isSupplier"
              :to="{ name: 'subjekt-vytvorit___cs' }"
            >
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip6')}}
            </b-nav-item><!-- 
            <b-nav-item v-if="isConsultant"
              :to="{ name: 'subjekt-vytvorit___cs' }">
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip7')}}
            </b-nav-item> -->
            <b-nav-item
              v-if="isConsultant"
              :to="{ name: 'subjekt-referencni-projekt___cs' }"
            >
              <font-awesome-icon icon="lightbulb" />
              {{$t('account.completation_tips.tip8')}}
            </b-nav-item>
          </b-nav>
        </b-card-text>
      </b-card>
      <b-row>
        <b-col
          md="6"
          class="d-flex align-items-center mb-5"
          id="AccountInfoForm"
        >
          <AccountInfoForm :user="user"></AccountInfoForm>
        </b-col>
        <b-col
          md="6"
          class="d-flex align-items-center mb-5"
        >
          <PasswordChange></PasswordChange>
        </b-col>
        <b-col
          sm="12"
          class="text-center"
          v-if="!isClient"
        >
          Pro doplnění všech vašich kompetencí a expertizy klikněte <nuxt-link :to="{ name: 'subjekt-id-upravit___cs', params: {id: company.id} }">zde</nuxt-link>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import AccountInfoForm from "~/components/user/AccountInfoForm";
import PasswordChange from "~/components/user/PasswordChange";
import PageTitle from "~/components/partials/PageTitle";
import { faLightbulb } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
library.add(faLightbulb);

export default {
  name: "user-edit",
  async fetch({ store }) {
    // await store.dispatch('user/getUser');
    // await store.dispatch('user/getOwnCompany');
  },
  components: {
    PasswordChange,
    AccountInfoForm,
    PageTitle,
  },
  data: () => ({}),
  computed: {
    ...mapState({
      user: (state) => state.user.user,
      company: (state) => state.companies.company,
    }),
    ...mapGetters({
      isClient: "user/isClient",
      isSupplier: "user/isSupplier",
      isConsultant: "user/isConsultant",
    }),
    heading() {
      if (this.isConsultant) return $nuxt.$t("menu.consultant_profile");
      if (this.isSupplier) return $nuxt.$t("menu.company_profile");
      return $nuxt.$t("menu.user_profile");
    },
    icon() {
      if (this.isSupplier) "pe-7s-home icon-gradient bg-blue-icon";
      return "pe-7s-user icon-gradient bg-blue-icon";
    },
  },
};
</script>

<style lang="scss">
.nav-pills {
  .nav-item {
    .nav-link {
      transition: all ease-in-out 0.3s;
      height: 100%;
      a:hover {
        background-color: $cyan;
        color: $white !important;
      }

      svg {
        width: 58px;
        display: inline-block;
        font-size: 22px;
      }
    }
  }
}
</style>